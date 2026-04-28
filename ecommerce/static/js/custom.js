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

})