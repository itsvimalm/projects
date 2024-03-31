from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Simple username and password for authentication
USERNAME = "admin"
PASSWORD = "password"

# Serve the login page
@app.route('/')
def login():
    return render_template('login.html')

# Handle login authentication
@app.route('/login', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('traffic_data'))  # Redirect to traffic data page if login successful
    else:
        return render_template('login.html', error="Invalid username or password")

# Serve the traffic data page
@app.route('/traffic_data')
def traffic_data():
    return render_template('traffic_data.html')

# Handle POST request from traffic data page
@app.route('/control_signal', methods=['POST'])
def control_signal():
    # Receive data from traffic data page
    selected_data = request.json

    # Send data to ESP8266 (example)
    # Here you would replace this with your actual code to send data to ESP8266
    print("Selected data received from traffic data page:", selected_data)

    # Dummy response for demonstration
    response = {'message': 'Data received and processed successfully'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
