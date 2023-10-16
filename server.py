import os

from flask import Flask, request, render_template, jsonify, send_from_directory, url_for


import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




app = Flask(__name__)


services_list = ["Boat Cleaning & Detailing",
  "Corrosion Detail & Treatment",
  "Captain Services",
  "Ceramic Coating for Glass and Engines",
  "Service and Repairs"]


service_dic = {
  "Boat Cleaning & Detailing": [
    "Our professional boat cleaning and detailing services ensure that your boat looks its best at all times. From hull to deck, we pay attention to every detail to provide a thorough and comprehensive cleaning. Expect your boat to shine like new after our services."
    ],
  "Corrosion Detail & Treatment": [
    "An in-depth and thorough removal of any existing corrosion in your bilge, motors, and electronics. Followed by a chemical treatment to reduce additional corrosion in these areas. Your bilge, engines, and electronics will look cleaner than ever while having a layer of protection against humidity and saltwater."
  ],
  "Captain Services": [
    "Boat transport to and from service centers by USCG licensed captains. Only available for service centers within Miami-Dade. You can trust that our captains will safely deliver your boat, so you don't have to take time out of your schedule to do so."
  ],
  "Ceramic Coating for Glass and Engines": [
    "Ceramic coating is a great way to protect and properly seal your motors or glass windows. With that being said, the ceramic coating makes it easier to clean, such as fish blood, heavy stains, or even dirt. It is a once a year job and is a great way to keep your motors shining all year long."
  ],
  "Service and Repairs": [
    ""
  ]
}







people = {
    "david_costa": {"name":  "David Costa",
                   "photo": "https://writingcenter.fas.harvard.edu/sites/hwpi.harvard.edu/files/styles/os_files_xxlarge/public/writingcenter/files/person-icon.png?m=1614398157&itok=Bvj8bd7F",
                   "short_info":"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                   "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                   "instagram": "https://www.instagram.com/dcost22/"},
    "mark_lopez": {"name":  "Mark Lopez",
                  "photo": "https://writingcenter.fas.harvard.edu/sites/hwpi.harvard.edu/files/styles/os_files_xxlarge/public/writingcenter/files/person-icon.png?m=1614398157&itok=Bvj8bd7F",
                  "short_info":"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                  "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                   "instagram": "https://www.instagram.com/markk_lopezzzz/"},
    "christopher_tavera": {"name": "Christopher Tavera",
                "photo": "https://writingcenter.fas.harvard.edu/sites/hwpi.harvard.edu/files/styles/os_files_xxlarge/public/writingcenter/files/person-icon.png?m=1614398157&itok=Bvj8bd7F",
                  "short_info":"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                  "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                  "instagram": "https://www.instagram.com/miamiskindiver/"},
}


@app.route('/')
def home():
  #return render_template('home.html')
  return render_template('home-parallax.html')



@app.route('/services')
def services():
  return render_template('services.html',services=services_list, service_dic=service_dic)

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
        services_list_other = services_list + ["Other"]
        return render_template('contact.html', services=services_list_other)




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

    


