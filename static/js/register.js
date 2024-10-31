function validation() {
    var firstname = document.forms["Formfill"]["firstname"].value;
    var lastname = document.forms["Formfill"]["lastname"].value;
    var age = document.forms["Formfill"]["age"].value;
    var email = document.forms["Formfill"]["email"].value;
    var phone = document.forms["Formfill"]["phone"].value;
    var pincode = document.forms["Formfill"]["pincode"].value;

    if (firstname == "" || lastname == "" || age == "" || email == "" || phone == "") {
        alert("All fields must be filled out");
        return false;
    }

    // Validate email format
    var emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!email.match(emailPattern)) {
        alert("Please enter a valid email address");
        return false;
    }

    // Validate phone number format
    var phonePattern = /^\d{10}$/;
    if (!phone.match(phonePattern)) {
        alert("Please enter a valid phone number (10 digits)");
        return false;
    }

    // If all validations pass, display "Thank you" message

    // Prevent form submission since we're handling it here
}
