$(document).ready(function(){
  // Parse to make correct data types 
  let serviceList = JSON.parse(services);
  let serviceDictionary = JSON.parse(service_dic);


  // Create service container to then add service items to
  const servicesContainer = document.getElementById("servicesContainer");
  serviceList.forEach(service => {
    const serviceDiv = document.createElement("div");
    serviceDiv.textContent = service;

    serviceDiv.classList.add("service-item");
    
    // Create the "plus" icon element and add it to the service div
    const iconElement = document.createElement("i");
    iconElement.classList.add("expand-icon", "fas", "fa-plus");
    serviceDiv.appendChild(iconElement);

    servicesContainer.appendChild(serviceDiv);
  });
 

  // Add click event listener to the services container
  // If the div of a service is clicked -> than a detailed view will expand below
  servicesContainer.addEventListener("click", function(event) {
    if (event.target.classList.contains("service-item")) {
      toggleServiceDetails(event.target, serviceDictionary);
    }
  });
});


// Function to toggle the service detailed div 
function toggleServiceDetails(serviceDiv, serviceDictionary) {
  const serviceDetailsDiv = serviceDiv.nextElementSibling;
  const iconElement = document.createElement("i");
  iconElement.classList.add("expand-icon", "fas");
  if (serviceDetailsDiv && serviceDetailsDiv.classList.contains("service-details")) {
    // If service details div exists, remove it and change the icon to "plus" icon
    serviceDetailsDiv.remove();
    iconElement.classList.add("fa-plus");
    iconElement.classList.remove("fa-minus");
  } else {
    // Otherwise, create and insert it and change the icon to "minus" icon
    const serviceName = serviceDiv.textContent;
    const serviceDetails = serviceDictionary[serviceName];

    const newServiceDetailsDiv = generateServiceDetailsHTML(serviceDetails);
    serviceDiv.insertAdjacentElement("afterend", newServiceDetailsDiv);

    iconElement.classList.add("fa-minus");
    iconElement.classList.remove("fa-plus");
  }
  // Check if the icon already exists and remove it before inserting the new icon
  const existingIcon = serviceDiv.querySelector(".expand-icon");
  if (existingIcon) {
    existingIcon.remove();
  }
  serviceDiv.appendChild(iconElement);
}

// Function to create the service detail view html code that is added in the toggleServiceDetails function
function generateServiceDetailsHTML(serviceDetails) {
  const [details, price, imageSrc] = serviceDetails;

  const newServiceDetailsDiv = document.createElement("div");

  
  // Create a paragraph for detailed explanation
  const detailsParagraph = document.createElement("p");
  detailsParagraph.textContent = details;
  newServiceDetailsDiv.appendChild(detailsParagraph);

  // // Create an image element for the small image
  // const imageElement = document.createElement("img");
  // imageElement.src = imageSrc;
  // imageElement.classList.add("service-image");
  // newServiceDetailsDiv.appendChild(imageElement);

  newServiceDetailsDiv.classList.add("service-details");

  return newServiceDetailsDiv;
}





