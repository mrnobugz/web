from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """
    This is the main route for the homepage.
    It renders the index.html template.
    """
    # You can pass dynamic data to your template from here.
    # For example, we can define the team members' info in a list of dictionaries.
    team_members = [
        {
            "name": "Elibarick Maleko",
            "title": "Bachelor of Information Technology (BIT)",
            "photo_url": "https://placehold.co/100x100/e0e7ff/3730a3?text=Photo"
        },
        {
            "name": "Delphinus Rubangilana Egidius",
            "title": "Bachelor of Science in Computer Science",
            "photo_url": "https://placehold.co/100x100/e0e7ff/3730a3?text=Photo"
        }
    ]
    # The 'team_members' variable is passed to the template
    return render_template('index.html', team_members=team_members)

if __name__ == '__main__':
    # This will run the app in debug mode for development
    # For production, you would use a proper WSGI server like Gunicorn
    app.run(debug=True)