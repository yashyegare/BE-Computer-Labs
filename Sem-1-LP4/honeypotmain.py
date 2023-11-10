# Import necessary modules
from flask import Flask, request

# Initialize the Flask app
app = Flask(__name__)

# Route for handling form submissions to '/contact'
@app.route('/contact', methods=['POST'])
def contact():
    # Check if the 'honeypot' field is filled
    if request.form['honeypot'] != '':
        # If the honeypot field is filled, assume it's a bot and return a message
        return "Bot detected!"
    else:
        # If the honeypot field is empty, proceed as normal and acknowledge the submission
        return "Thanks for your submission!"

# Main form route, where the form for user interaction is displayed
@app.route('/')
def index():
    return '''
        <form action="/contact" method="post">
            <input type="text" name="name" placeholder="Your Name"><br>
            <input type="email" name="email" placeholder="Your Email"><br>
            <input type="text" name="message" placeholder="Your Message"><br>

            <!-- Honeypot field, hidden from users -->
            <input type="text" name="honeypot" style="display:none">
            <input type="submit" value="Submit">
        </form>
    '''

# Run the app if this is the main module
if __name__ == '__main__':
    app.run(debug=True)
