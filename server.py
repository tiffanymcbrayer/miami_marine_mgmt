from __future__ import print_function
import os

from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
from flask_mail import Mail, Message


import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




app = Flask(__name__)


services_list = ["Boat Cleaning & Detailing",
  "Gel-coat restoration",
  "Interior cleaning and upholstery care",
  "Teak cleaning and restoration",
  "Bottom painting",
  "Engine maintenance and servicing"]


service_dic = {
  "Boat Cleaning & Detailing": [
    "Our professional boat cleaning and detailing services ensure that your boat looks its best at all times. From hull to deck, we pay attention to every detail to provide a thorough and comprehensive cleaning. Expect your boat to shine like new after our services.",
    "boat_cleaning.jpg"
  ],
  "Gel-coat restoration": [
    "Our gel-coat restoration service brings back the original shine and luster of your boat's gel-coat. We use top-quality products and techniques to repair and revive the surface, leaving it looking brand new. Expect a smooth and glossy gel-coat after our restoration process.",
    "gel_coat_restoration.jpg"
  ],
  "Interior cleaning and upholstery care": [
    "Our interior cleaning and upholstery care services ensure that the inside of your boat remains clean and comfortable. We pay attention to every corner and surface, providing a deep and thorough cleaning. Expect a fresh and welcoming interior after our service.",
    "interior_cleaning.jpg"
  ],
  "Teak cleaning and restoration": [
    "Our specialized teak cleaning and restoration services keep your boat's teak surfaces in top condition. We use gentle yet effective cleaning methods to remove dirt and stains, and our restoration techniques breathe new life into weathered teak. Expect beautiful and well-maintained teak after our service.",
    "teak_restoration.jpg"
  ],
  "Bottom painting": [
    "Our expert bottom painting services protect your boat's hull from the elements and marine growth. We use high-quality marine-grade paints to ensure long-lasting and effective protection. Expect a smooth and protected hull after our bottom painting service.",
    "bottom_painting.jpg"
  ],
  "Engine maintenance and servicing": [
    "Our comprehensive engine maintenance and servicing keep your boat's engine running smoothly and efficiently. We perform routine checks, tune-ups, and repairs to ensure optimal performance. Expect a reliable and well-maintained engine after our servicing.",
    "engine_maintenance.jpg"
  ]
}





# Name of the company : [what type of partner, "image url", "company url"]
partners = {
    "Glass-Tech": ["Yard", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/glass-tech.png?raw=true", 
                   "https://www.glass-tech.com/"],
    "D-Dey": ["Safety", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/D-DEY.png?raw=true", 
              "https://d-dey.myshopify.com/"],
    "All Water Customs": ["Decking", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/All_water_customs.png?raw=true",
                          "https://allwatercustoms.com/"],
    "Miami Maritime Group": ["Broker", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/Miami_Maritime_Group.png?raw=true", 
                             "https://www.miamimaritimegroup.com/"],
    "Locmarine ": ["Security", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/locmarine.png?raw=true", 
                   "https://www.locmarine.com/"],
    "VooDoo Marine": ["Service", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/Voodoo_marine.png?raw=true",
                       "https://www.instagram.com/voodoomarine/?hl=en"],
    "Elite Marine": ["Service", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/Elite_Marine.png?raw=true", 
                     "https://www.instagram.com/elitemarineservices/"],
    "DC Fuel Services ": ["Fuel", "https://github.com/tiffanymcbrayer/miami_marine_mgmt/blob/main/partner_images/dc_fuel_services.png?raw=true", 
                          "https://www.dcfuelsvc.com/"]

}

people = {
    "David Costa": {"photo": "https://writingcenter.fas.harvard.edu/sites/hwpi.harvard.edu/files/styles/os_files_xxlarge/public/writingcenter/files/person-icon.png?m=1614398157&itok=Bvj8bd7F",
                   "title": "Title", 
                   "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                   "instagram": ""},
    "Mark Lopez": {"photo": "https://writingcenter.fas.harvard.edu/sites/hwpi.harvard.edu/files/styles/os_files_xxlarge/public/writingcenter/files/person-icon.png?m=1614398157&itok=Bvj8bd7F",
                   "title": "Title", 
                  "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                   "instagram": ""},
    "Person 3": {"photo": "https://writingcenter.fas.harvard.edu/sites/hwpi.harvard.edu/files/styles/os_files_xxlarge/public/writingcenter/files/person-icon.png?m=1614398157&itok=Bvj8bd7F",
                   "title": "Title", 
                  "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                   "instagram": ""},
    "Person 4": {"photo": "https://writingcenter.fas.harvard.edu/sites/hwpi.harvard.edu/files/styles/os_files_xxlarge/public/writingcenter/files/person-icon.png?m=1614398157&itok=Bvj8bd7F",
                   "title": "Title", 
                   "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                   "instagram": ""}
}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/services')
def services():

    return render_template('services.html', services=services_list, service_dic=service_dic, partners=partners)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', people=people)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            # Access the form data sent from the JavaScript code
            form_data = request.json
            name = form_data.get('name')
            email = form_data.get('email')
            phone = form_data.get('phone')
            service_type = form_data.get('serviceType')
            message = form_data.get('message')

            subject = 'Service Inquiry - Website Form'
            body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nService Type: {service_type}\nMessage: {message}"
            

            send_email(body, 'tiffanymcbrayer@miamimarinemgmt.com', 'tiffanymcbrayer@miamimarinemgmt.com', subject)

            # Process the form data as needed
            # For example, you can save it to a database or perform any other actions

            # Return a response to the client (JavaScript) if needed
            # In this example, we'll simply return a success message
            response_data = {'message': 'Form data received successfully'}
            return jsonify(response_data), 200

        except Exception as e:
            # Handle any errors that may occur during form data processing
            error_message = str(e)
            return jsonify({'error': error_message}), 500

    else:
        # This is a GET request, render the contact.html page with the services_list
        return render_template('contact.html', services=services_list)




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def send_email(body, to_email, from_email, subject):
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send']

    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)

        # Create the email message
        message = MIMEText(body)
        message['to'] = to_email
        message['from'] = from_email
        message['subject'] = subject

        # Encoded message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        encoded_message = {'raw': raw_message}

        # Send the email
        service.users().messages().send(userId='me', body=encoded_message).execute()
        print("Email sent successfully!")

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

    


