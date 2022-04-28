/**
 * @todo maybe the custom autocomplete logic could be extract to be reusable
 */
// publicWidget.registry.productsSearchBar = publicWidget.Widget.extend({
//     selector: '.o_wsale_products_searchbar_form',
//     xmlDependencies: ['/website_sale/static/src/xml/website_sale_utils.xml'],
//     events: {
//         'input .search-query': '_onInput',
//         'focusout': '_onFocusOut',
//         'keydown .search-query': '_onKeydown',
//     },
//     autocompleteMinWidth: 300,

//     /**
//      * @constructor
//      */
//     init: function () {
//         this._super.apply(this, arguments);

//         this._dp = new concurrency.DropPrevious();

//         this._onInput = _.debounce(this._onInput, 400);
//         this._onFocusOut = _.debounce(this._onFocusOut, 100);
//     },
//     /**
//      * @override
//      */
//     start: function () {
//         this.$input = this.$('.search-query');

//         this.order = this.$('.o_wsale_search_order_by').val();
//         this.limit = parseInt(this.$input.data('limit'));
//         this.displayDescription = !!this.$input.data('displayDescription');
//         this.displayPrice = !!this.$input.data('displayPrice');
//         this.displayImage = !!this.$input.data('displayImage');

//         if (this.limit) {
//             this.$input.attr('autocomplete', 'off');
//         }

//         return this._super.apply(this, arguments);
//     },

//     //--------------------------------------------------------------------------
//     // Private
//     //--------------------------------------------------------------------------

//     /**
//      * @private
//      */
//     _fetch: function () {
//         return this._rpc({
//             route: '/shop/products/autocomplete',
//             params: {
//                 'term': this.$input.val(),
//                 'options': {
//                     'order': this.order,
//                     'limit': this.limit,
//                     'display_description': this.displayDescription,
//                     'display_price': this.displayPrice,
//                     'max_nb_chars': Math.round(Math.max(this.autocompleteMinWidth, parseInt(this.$el.width())) * 0.22),
//                 },
//             },
//         });
//     },
//     /**
//      * @private
//      */
//     _render: function (res) {
//         var $prevMenu = this.$menu;
//         this.$el.toggleClass('dropdown show', !!res);
//         if (res) {
//             var products = res['products'];
//             this.$menu = $(qweb.render('website_sale.productsSearchBar.autocomplete', {
//                 products: products,
//                 hasMoreProducts: products.length < res['products_count'],
//                 currency: res['currency'],
//                 widget: this,
//             }));
//             this.$menu.css('min-width', this.autocompleteMinWidth);
//             this.$menu.css('margin', 0);
//             this.$el.append(this.$menu);
//         }
//         if ($prevMenu) {
//             $prevMenu.remove();
//         }
//     },

//     //--------------------------------------------------------------------------
//     // Handlers
//     //--------------------------------------------------------------------------

//     /**
//      * @private
//      */
//     _onInput: function () {
//         if (!this.limit) {
//             return;
//         }
//         this._dp.add(this._fetch()).then(this._render.bind(this));
//     },
//     /**
//      * @private
//      */
//     _onFocusOut: function () {
//         if (!this.$el.has(document.activeElement).length) {
//             this._render();
//         }
//     },
//     /**
//      * @private
//      */
//     _onKeydown: function (ev) {
//         switch (ev.which) {
//             case $.ui.keyCode.ESCAPE:
//                 this._render();
//                 break;
//             case $.ui.keyCode.UP:
//             case $.ui.keyCode.DOWN:
//                 ev.preventDefault();
//                 if (this.$menu) {
//                     let $element = ev.which === $.ui.keyCode.UP ? this.$menu.children().last() : this.$menu.children().first();
//                     $element.focus();
//                 }
//                 break;
//         }
//     },
// });


odoo.define('bista_website_sale.website_sale', function (require) {
    'use strict';
    require('website_sale.website_sale');
    
    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var qweb = core.qweb;

    var VariantMixin = require('sale.VariantMixin');

    require("web.zoomodoo");


    publicWidget.registry.WebsiteSale.include({
        events: _.extend({}, publicWidget.registry.WebsiteSale.prototype.events, {
            'change .custom_js_quantity[data-product-id]': '_onChangeCartQuantity',
            'click a.quick_add_to_cart': '_onClickQuickAdd',
        }),
        init: function () {
            this._super.apply(this, arguments);
            this.qucikAddToCart = _.debounce(this.qucikAddToCart.bind(this), 300);
        },
        _onClickQuickAdd : function (ev) {
            ev.preventDefault();
            this.qucikAddToCart(ev);
        },
        qucikAddToCart: function (ev) {
            ev.preventDefault();
            this.$currentTarget = $(ev.currentTarget);
            $(ev.currentTarget).addClass('d-none qk_adding_cart');
            this._onClickAdd(ev).then(()=> {
                if ($('.qk_adding_cart').length) {
                    var $js_product = $('.qk_adding_cart').closest('.js_product');
                    var find_vs_btn = $js_product.find('.css_quantity');
                    find_vs_btn.find('input.custom_js_quantity').val(1);
                    find_vs_btn.removeClass('d-none');
                    $js_product.find('.quick_add_to_cart').removeClass('qk_adding_cart');
                    // find_vs_btn.closest('.qk_adding_cart').removeClass("qk_adding_cart");
                }
            });
        },

    _onChangeCartQuantity: function (ev) {
        var $input = $(ev.currentTarget);
        if ($input.data('update_change')) {
            return;
        }
        var value = parseInt($input.val() || 0, 10);
        if (isNaN(value)) {
            value = 1;
        }

        var on_hand_qty = parseInt($input.data('max') || 1, 10)
        if (value > on_hand_qty) {
            value = on_hand_qty
            $input.val(value)
          }
        
        var $dom = $input.closest('tr');
        // var default_price = parseFloat($dom.find('.text-danger > span.oe_currency_value').text());
        var $dom_optional = $dom.nextUntil(':not(.optional_product.info)');
        var line_id = parseInt($input.data('line-id'), 10);
        var productIDs = [parseInt($input.data('product-id'), 10)];
        this._changeCartQuantity($input, value, $dom_optional, line_id, productIDs);
    },
    _onClickSubmit: function (ev, forceSubmit) {
        let recaptcha = $("#g-recaptcha-response").val();
        if (recaptcha === "") {
            ev.preventDefault();
            document.getElementById('err').innerHTML="Please check Captcha";
            return false;
        }

        return this._super(ev, forceSubmit);
    }
    });

    publicWidget.registry.WebsiteSaleLayout.include({
        init: function () {
            this._super.apply(this, arguments);
            var $grid = $('#products_grid');
            var isList = $(".o_wsale_apply_list.active").length;

            isList ? $grid.find('.p-0.text-center').addClass('w-25') : $grid.find('.p-0.text-center').removeClass('w-25');
            isList ? $grid.find('.o_wsale_product_grid_wrapper').removeAttr("style") : $grid.find('.o_wsale_product_grid_wrapper').attr("style", "height: 330px;");
        },
        _onApplyShopLayoutChange: function (ev) {
            const wysiwyg = this.options.wysiwyg;
            if (wysiwyg) {
                wysiwyg.odooEditor.observerUnactive('_onApplyShopLayoutChange');
            }
            var switchToList = $(ev.currentTarget).find('.o_wsale_apply_list input').is(':checked');
            if (!this.editableMode) {
                this._rpc({
                    route: '/shop/save_shop_layout_mode',
                    params: {
                        'layout_mode': switchToList ? 'list' : 'grid',
                    },
                });
            }
            var $grid = this.$('#products_grid');
            // Disable transition on all list elements, then switch to the new
            // layout then reenable all transitions after having forced a redraw
            // TODO should probably be improved to allow disabling transitions
            // altogether with a class/option.
            $grid.find('*').css('transition', 'none');
            $grid.toggleClass('o_wsale_layout_list', switchToList);
            switchToList ? $grid.find('.p-0.text-center').addClass('w-25') : $grid.find('.p-0.text-center').removeClass('w-25');
            switchToList ? $grid.find('.o_wsale_product_grid_wrapper').removeAttr("style") : $grid.find('.o_wsale_product_grid_wrapper').attr("style", "height: 330px;");
            void $grid[0].offsetWidth;
            $grid.find('*').css('transition', '');
            if (wysiwyg) {
                wysiwyg.odooEditor.observerActive('_onApplyShopLayoutChange');
            }
        },
    });

});