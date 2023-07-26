import os

from flask import Flask, render_template, jsonify



app = Flask(__name__)



services_list = ["Boat Cleaning & Detailing",
  "Gel-coat restoration",
  "Interior cleaning and upholstery care",
  "Teak cleaning and restoration",
  "Bottom painting",
  "Engine maintenance and servicing"]

# service_dic = {
#     "Boat Cleaning & Detailing": ["details", 1, "image"],
#     "Gel-coat restoration": ["details", 2, "image"],
#   "Interior cleaning and upholstery care": ["details", 3, "image"],
#   "Teak cleaning and restoration": ["details", 4, "image"],
#   "Bottom painting": ["details", 5, "image"],
#   "Engine maintenance and servicing": ["details", 6, "image"]
# }
service_dic = {
  "Boat Cleaning & Detailing": [
    "Our professional boat cleaning and detailing services ensure that your boat looks its best at all times. From hull to deck, we pay attention to every detail to provide a thorough and comprehensive cleaning. Expect your boat to shine like new after our services.",
    150,
    "boat_cleaning.jpg"
  ],
  "Gel-coat restoration": [
    "Our gel-coat restoration service brings back the original shine and luster of your boat's gel-coat. We use top-quality products and techniques to repair and revive the surface, leaving it looking brand new. Expect a smooth and glossy gel-coat after our restoration process.",
    200,
    "gel_coat_restoration.jpg"
  ],
  "Interior cleaning and upholstery care": [
    "Our interior cleaning and upholstery care services ensure that the inside of your boat remains clean and comfortable. We pay attention to every corner and surface, providing a deep and thorough cleaning. Expect a fresh and welcoming interior after our service.",
    100,
    "interior_cleaning.jpg"
  ],
  "Teak cleaning and restoration": [
    "Our specialized teak cleaning and restoration services keep your boat's teak surfaces in top condition. We use gentle yet effective cleaning methods to remove dirt and stains, and our restoration techniques breathe new life into weathered teak. Expect beautiful and well-maintained teak after our service.",
    120,
    "teak_restoration.jpg"
  ],
  "Bottom painting": [
    "Our expert bottom painting services protect your boat's hull from the elements and marine growth. We use high-quality marine-grade paints to ensure long-lasting and effective protection. Expect a smooth and protected hull after our bottom painting service.",
    180,
    "bottom_painting.jpg"
  ],
  "Engine maintenance and servicing": [
    "Our comprehensive engine maintenance and servicing keep your boat's engine running smoothly and efficiently. We perform routine checks, tune-ups, and repairs to ensure optimal performance. Expect a reliable and well-maintained engine after our servicing.",
    250,
    "engine_maintenance.jpg"
  ]
}

# there might be two service partners
# partners = {
#     "Yard": ["Glass-Tech"],
#     "Safety": ["D-Dey"],
#     "Decking": ["All Water Customs"],
#     "Broker": [],
#     "Security": [],
#     "Service": [],
#     "Fuel":[]
# }

# Name of the company : [what type of partner, "image url", "company url"]
partners = {
    "Glass-Tech": ["Yard", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/LOGO.png?raw=true", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"],
    "D-Dey": ["Safety", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/LOGO.png?raw=true", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"],
    "All Water Customs": ["Decking", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/LOGO.png?raw=true","https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"],
    "Miami Maritime Group": ["Broker", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/LOGO.png?raw=true", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"],
    "Locmarine ": ["Security", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/LOGO.png?raw=true", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"],
    "VooDoo Marine": ["Service", "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/26228258_1418779181560853_4220528378819641344_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=105&_nc_ohc=ya-zqwspi00AX_GP8R8&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBg3rDrXVAUFUdWcVjBWSqG8i7o6UF-4HYEWtuRYhMSvg&oe=64C2CEF9&_nc_sid=8b3546", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"],
    "Elite Marine": ["Service", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/LOGO.png?raw=true", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"],
    "DC Fuel Services ": ["Fuel", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/LOGO.png?raw=true", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjgiMjkwKqAAxWil4kEHb8cAeEQPAgJ"]

}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():


    return render_template('services.html', services=services_list, service_dic=service_dic, partners=partners)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html', services=services_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# if __name__ == '__main__':
#     app.run(debug=True)