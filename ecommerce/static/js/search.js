$(document).ready(function () {

    $("#searchproducts").autocomplete({

        source: function (request, response) {

            $.ajax({

                url: "/search-products/",

                data: {
                    search: request.term
                },

                success: function (data) {

                    response(
                        $.map(data, function (item) {

                            return {
                                label: item.name,
                                value: item.name,
                                id: item.id,
                                category_slug: item.category_slug,
                                product_slug: item.product_slug
                            };

                        })
                    );

                }

            });

        },

        minLength: 2

    });

});



// Produch Show

$(document).ready(function () {

    $("#searchproducts").autocomplete({

        source: function (request, response) {

            $.ajax({

                url: "/search-products/",

                data: {
                    search: request.term
                },

                success: function (data) {

                    response(
                        $.map(data, function (item) {

                            return {
                                label: item.name,
                                value: item.name,
                                id: item.id,
                                category_slug: item.category_slug,
                                product_slug: item.product_slug
                            };

                        })
                    );

                }

            });

        },

        minLength: 2,

        select: function (event, ui) {

            window.location.href =
        "/collections/" +
        ui.item.category_slug +
        "/" +
        ui.item.product_slug;

        }

    });

});