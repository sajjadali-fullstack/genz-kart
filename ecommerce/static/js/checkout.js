$(document).ready(function () {
    $('.payWithRazorpay').click(function (e) {
        e.preventDefault();



        let fname = $("[name='fname']").val();
        let lname = $("[name='lname']").val();
        let email = $("[name='email']").val();
        let phone = $("[name='phone']").val();
        let address = $("[name='address']").val();
        let city = $("[name='city']").val();
        let state = $("[name='state']").val();
        let country = $("[name='country']").val();
        let pincode = $("[name='pincode']").val();
        let token = $("[name='csrfmiddlewaretoken']").val();

        if (fname == "" || lname == "" || email == "" || phone == "" || address == "" || city == "" || state == "" || country == "" || pincode == "") {

            swal("Alert!", "All fields are required!", "error");
            return false;
        }
        else {

            $.ajax({
                method: "GET",
                url: "/proceed-to-pay/",
                success: function (response) {
                    // For Checking Purpose
                    // console.log(response);


                    let options = {
                        "key": "rzp_test_TMykbynEGhodDP", // Enter the Key ID generated from the Dashboard
                        // "amount": response.total_price * 100, // Amount is in currency subunits.
                        "amount": 1 * 100, 
                        "currency": "INR",
                        "name": "GenZKart | Sajjad Ali", //your business name
                        "description": "Complete your GenZKart order securely.",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responses) {
                            // Store the payment_id in my database
                            alert(responses.razorpay_payment_id);
                            data = {
                                "fname": fname,
                                "lname": lname,
                                "email": email,
                                "phone": phone,
                                "address": address,
                                "city": city,
                                "state": state,
                                "country": country,
                                "pincode": pincode,
                                "payment_mode": "Paid by Razorpay",
                                "payment_id": response.razorpay_payment_id,
                                csrfmiddlewaretoken: token
                            }



                            // To get the order details
                            $.ajax({
                                method: "POST",
                                url: "/placeorder/",
                                data: data,
                                dataType: "dataType",
                                success: function (responsec) {
                                    swal("Congratulations!", responsec.status, "success").then((value) => {
                                        window.location.href = "/my-orders/";
                                    });;
                                    swal(responsec.status);

                                }

                            });











                        },
                        "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                            "name": fname + " " + lname, //your customer's name
                            "email": email,
                            "contact": phone  //Provide the customer's phone number for better conversion rates 
                        },
                        "notes": {
                            "address": address + ", " + city + ", " + state + ", " + country + " - " + pincode
                        },
                        "theme": {
                            "color": "#3399cc"
                            // "color": "#198754"
                        }
                    };
                    var rzp1 = new Razorpay(options);

                    rzp1.open();


                }
            })
        }

    });
});    