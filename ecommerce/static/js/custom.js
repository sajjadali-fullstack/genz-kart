$(document).ready(function () {

    // Increment
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        let inc_val = $(this).closest('.product_data').find('.qty-input').val();  // Fetching Value 1
        let value = parseInt(inc_val, 10);  // Adding 1 to Value 1
        value = isNaN(value) ? 0 : value;  // Checking if value is NaN or not
        if (value < 20) { // Increment only if value is less than 20
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }

    });

    // Decrement
    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        let dec_val = $(this).closest('.product_data').find('.qty-input').val();  // Fetching Value 1
        let value = parseInt(dec_val, 10);  // Adding 1 to Value 1
        value = isNaN(value) ? 0 : value;  // Checking if value is NaN or not
        if (value > 1) { // Increment only if value is less than 20
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }

    });


    $('.addToCartBtn').click(function (e) {
        e.preventDefault();

        let product_id = $(this).closest('.product_data').find('.prod_id').val();
        let product_qty = $(this).closest('.product_data').find('.qty-input').val();
        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-cart/",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token

            },

            success: function (response) {
                console.log(response);

                if (response.error) {
                    alertify.error(response.error);
                }
                else if (response.status) {
                    alertify.success(response.status);
                }
            }

        });




    });
    $('.changeQuantity').click(function (e) {
        e.preventDefault();

        let product_id = $(this).closest('.product_data').find('.prod_id').val();
        let product_qty = $(this).closest('.product_data').find('.qty-input').val();
        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/update-cart/",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token

            },

            success: function (response) {
                console.log(response);

                if (response.error) {
                    alertify.error(response.error);
                }
                else if (response.status) {
                    alertify.success(response.status);
                }
            }

        });

    });

    // Delete Cart Item
    // $('.delete-cart-item').click(function (e) {
    //     e.preventDefault();
    //     // Fetch:- product id,
    //     let product_id = $(this).closest('.product_data').find('.prod_id').val();
    //     let token = $('input[name=csrfmiddlewaretoken]').val();

    //     $.ajax({
    //         method: "POST",
    //         url: "delete-cart-item",
    //         data: {
    //             'product_id': product_id,
    //             csrfmiddlewaretoken: token
    //         },
    //         success: function (response) {
    //             alertify.sucess(response.status);
    //             $('.cartdata').load(location.href + ' .cartdata');

    //         }

    //     });



    // });

    $(document).ready(function () {
        // Event Delegation use kiya hai taaki dynamic reload (.load) ke baad bhi button kaam kare
        $(document).on('click', '.delete-cart-item', function (e) {
            e.preventDefault();

            let $this = $(this); // Current button ka reference
            let product_id = $this.closest('.product_data').find('.prod_id').val();
            let token = $('input[name=csrfmiddlewaretoken]').val();

            $.ajax({
                method: "POST",
                url: "/delete-cart-item/", // URL ke aage aur peeche slash (/) zaroor lagayein
                data: {
                    'product_id': product_id,
                    csrfmiddlewaretoken: token
                },
                success: function (response) {
                    // Sahi spelling 'success' ke sath Alertify notification
                    alertify.success(response.status);

                    // Sirf cart data wale part ko refresh karne ke liye
                    $('.cartdata').load(location.href + ' .cartdata');
                },
                error: function (xhr, status, error) {
                    console.log("Error details:", error);
                    alertify.error("Something went wrong! Please try again.");
                }
            });
        });
    });



});