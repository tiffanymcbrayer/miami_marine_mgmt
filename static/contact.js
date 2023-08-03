$(document).ready(function() {
    // Parse services to make an array
    let serviceList = JSON.parse(services);
    serviceList.unshift(""); // empty string for the first option to be blank on the dropdown

    const serviceTypeSelect = document.getElementById("serviceType");

    serviceList.forEach(service => {
        const serviceOption = document.createElement("option");
        serviceOption.textContent = service;
        serviceTypeSelect.appendChild(serviceOption);
    });

    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const phoneInput = document.getElementById("phone");
    const serviceTypeInput = document.getElementById("serviceType");
    const messageInput = document.getElementById("message");

    const contactButton = document.getElementById("contactButton");
    contactButton.addEventListener("click", function() {
        // Access the values entered by the user
        const name = nameInput.value;
        const email = emailInput.value;
        const phone = phoneInput.value;
        const serviceType = serviceTypeInput.value;
        const message = messageInput.value;

        // Clear any existing error messages
        clearErrorMessages();

        // Validation checks
        let hasErrors = false;

        if (!name) {
            setError('name', 'Please enter your name.');
            hasErrors = true;
        }

        if (!email && !phone) {
            setError('email', 'Please enter either your email or phone number.');
            setError('phone', 'Please enter either your email or phone number.');
            hasErrors = true;
        } else {
            if (email && !email.includes('@')) {
                setError('email', 'Please enter a valid email address.');
                hasErrors = true;
            }

            if (phone && (!/^\d*$/.test(phone) || phone.length < 10)) {
                console.log("HERE");
                setError('phone', 'Please enter a valid phone number.');
                hasErrors = true;
            }
        }

        if (hasErrors) {
            return;
        }

        // Prepare the data to send to the server
        const formData = {
            name: name,
            email: email,
            phone: phone,
            serviceType: serviceType,
            message: message
        };

        // Make an HTTP POST request to the server
        fetch('/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle the response from the server (if needed)
            console.log('Server response:', data);
            // Display a success message (optional)
            showSuccessMessage();
            // Clear the input fields (optional)
            clearInputFields();
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
            // Optionally, you can display an error message to the user here
        });
    });

    function setError(inputId, errorMessage) {
        const input = document.getElementById(inputId);
        input.classList.add('error');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = errorMessage;
        input.parentNode.appendChild(errorDiv);
    }

    function clearErrorMessages() {
        const errorMessages = document.getElementsByClassName('error-message');
        while (errorMessages.length > 0) {
            errorMessages[0].parentNode.removeChild(errorMessages[0]);
        }
        const inputs = document.querySelectorAll('.error');
        inputs.forEach(input => input.classList.remove('error'));
    }

    function showSuccessMessage() {
        // Optionally, you can create a success message div and display it on the page
        // For example:
        //alert('You have sent a request form!');
        swal("Request Sent!", "Thanks for reaching out! We will get back to you shortly.", "success");
        // const successDiv = document.createElement('div');
        // successDiv.className = 'success-message';
        // successDiv.textContent = 'You have sent a request form!';
        // document.getElementById('form-container').appendChild(successDiv);
    }

    function clearInputFields() {
        // Clear the input fields
        nameInput.value = '';
        emailInput.value = '';
        phoneInput.value = '';
        serviceTypeInput.value = '';
        messageInput.value = '';
    }
});
