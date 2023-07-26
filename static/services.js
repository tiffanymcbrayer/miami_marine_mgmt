$(document).ready(function(){
  // Parse to make correct data types 
  let serviceList = JSON.parse(services);
  let serviceDictionary = JSON.parse(service_dic);
  let partnerDictionary = JSON.parse(partners);
  
  generateCarousel(partnerDictionary);

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

  // Create a paragraph for price
  const priceParagraph = document.createElement("p");
  priceParagraph.textContent = `Price: $${price}`;
  newServiceDetailsDiv.appendChild(priceParagraph);

  // // Create an image element for the small image
  // const imageElement = document.createElement("img");
  // imageElement.src = imageSrc;
  // imageElement.classList.add("service-image");
  // newServiceDetailsDiv.appendChild(imageElement);

  newServiceDetailsDiv.classList.add("service-details");

  return newServiceDetailsDiv;
}


function generateCarousel(partnerDictionary) {
  const carouselContainer = document.getElementById("carouselContainer");
  const partnerKeys = Object.keys(partnerDictionary);

  const partnersPerCarouselItem = 3;
  const numCarouselItems = Math.ceil(partnerKeys.length / partnersPerCarouselItem);

  const carouselInner = document.createElement("div");
  carouselInner.classList.add("carousel-inner");

  for (let i = 0; i < numCarouselItems; i++) {
    const carouselItem = document.createElement("div");
    carouselItem.classList.add("carousel-item");
    if (i === 0) {
      carouselItem.classList.add("active");
    }

    const indexes = partnerKeys.slice(i * partnersPerCarouselItem, (i + 1) * partnersPerCarouselItem);
   
    const partnerRow = makeCard(partnerDictionary, indexes);
    carouselItem.appendChild(partnerRow);

    carouselInner.appendChild(carouselItem);
  }
  carouselContainer.appendChild(carouselInner);
}

function makeCard(partnerDictionary, indexes) {
  const partnerRow = document.createElement("div");
  partnerRow.classList.add("row", "mb-4");

  for (const index of indexes) {
    const partnerData = partnerDictionary[index];
    console.log("partnerData:", partnerData);

    const partnerColumn = document.createElement("div");
    partnerColumn.classList.add("col-md-4"); // Each partner will take 4 columns

    const partnerCard = document.createElement("div");
    partnerCard.classList.add("partner-card");

    const imageContainer = document.createElement("div");
    imageContainer.classList.add("partner-img-container");

    const imageElement = document.createElement("img");
    imageElement.src = partnerData[1]; // Set the image URL from partnerData at the given index
    imageElement.alt = partnerData[0];
    imageElement.classList.add("partner-card-img-top");


    const partnerWebsiteLink = document.createElement("a"); // Create the anchor tag for the partner's website
    partnerWebsiteLink.href = partnerData[2]; // Set the website URL from partnerData at the given index
    partnerWebsiteLink.target = "_blank"; // Open link in a new tab
    partnerWebsiteLink.appendChild(imageElement); // Add the image inside the anchor tag

    imageContainer.appendChild(partnerWebsiteLink); // Add the anchor tag inside the container
    partnerCard.appendChild(imageContainer); // Add container inside the card




    // imageContainer.appendChild(imageElement);
    // partnerCard.appendChild(imageContainer);

    const cardBody = document.createElement("div");
    cardBody.classList.add("card-body");

    const cardTitle = document.createElement("div");
    cardTitle.classList.add("card-title");
    cardTitle.textContent = partnerData[0];

    cardBody.appendChild(cardTitle);
    partnerCard.appendChild(cardBody);

    partnerColumn.appendChild(partnerCard);
    partnerRow.appendChild(partnerColumn);
  }

  return partnerRow;
}



  

// Function if i want to go back to grid!!
function generateGrid(partnerDictionary) {
  const partnersGrid = document.getElementById("partnersGrid");
  const partnerKeys = Object.keys(partnerDictionary);

  for (let i = 0; i < partnerKeys.length; i++) {
    const partnerKey = partnerKeys[i];
    const partnerData = partnerDictionary[partnerKey];

    const partnerColumn = document.createElement("div");
    partnerColumn.classList.add("col-md-4", "mb-4");

    const partnerCard = document.createElement("div");
    partnerCard.classList.add("partner-card"); // Changed class name

    const imageContainer = document.createElement("div");
    imageContainer.classList.add("partner-img-container"); // Added new container for circular cropping

    const imageElement = document.createElement("img");
    imageElement.src = partnerData[1]; // Set the image URL
    imageElement.alt = partnerData[0];
    imageElement.classList.add("partner-card-img-top"); // Changed class name

    imageContainer.appendChild(imageElement); // Add image inside the container
    partnerCard.appendChild(imageContainer); // Add container inside the card

    const cardBody = document.createElement("div");
    cardBody.classList.add("card-body");

    const cardTitle = document.createElement("div");
    cardTitle.classList.add("card-title");
    cardTitle.textContent = partnerData[0];

    cardBody.appendChild(cardTitle);
    partnerCard.appendChild(cardBody);
    partnerColumn.appendChild(partnerCard);
    partnersGrid.appendChild(partnerColumn);
  }
}
