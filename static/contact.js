$(document).ready(function(){


    // Parse services to make array
    let serviceList = JSON.parse(services);
    serviceList.unshift(""); // empty string for first option to be blank on drop down


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

        // Do something with the data, e.g., send it to the server or perform validation
        console.log("Name:", name);
        console.log("Email:", email);
        console.log("Phone:", phone);
        console.log("Service Type:", serviceType);
        console.log("Message:", message);

        // Clear the input fields (optional)
        nameInput.value = "";
        emailInput.value = "";
        phoneInput.value = "";
        serviceTypeInput.value = "";
        messageInput.value = "";
    });

});




