// function showDropdown(cellId) {
//     var dropdown = document.getElementById(cellId + '-dropdown');
//     var display = dropdown.style.display;
  
//     if (display === 'block') {
//       dropdown.style.display = 'none';
//     } else {
//       dropdown.style.display = 'block';
//     }
// }


const services = ["Boat Cleaning & Detailing",
  "Gel-coat restoration",
  "Interior cleaning and upholstery care",
  "Teak cleaning and restoration",
  "Bottom painting",
  "Engine maintenance and servicing"];

$(document).ready(function(){
  const servicesContainer = document.getElementById("servicesContainer");

  services.forEach(service => {
    const serviceDiv = document.createElement("div");
    serviceDiv.textContent = service;

    serviceDiv.classList.add("service-item");
    servicesContainer.appendChild(serviceDiv);
    console.log(service);
  });
});

