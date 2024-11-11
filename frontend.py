from flask import Flask, jsonify, request, render_template_string
import whois
import lookup  # Assuming lookup.py is in the same directory or in the Python path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <h1>Welcome to the Domain Lookup Service!</h1>
        <form action="/lookup" method="get">
            <label for="domain">Enter domain:</label>
            <input type="text" id="domain" name="domain">
            <input type="submit" value="Check">
        </form>
    ''')

@app.route('/whois', methods=['GET'])
def whois_lookup():
    domain = request.args.get('domain')
    if not domain:
        return jsonify({"error": "No domain provided"}), 400
    
    try:
        domain_info = whois.whois(domain)
        return jsonify(domain_info.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/lookup', methods=['GET'])
def lookup_domain():
    domain = request.args.get('domain')
    if not domain:
        return jsonify({"error": "No domain provided"}), 400
    
    # Use the lookup function from lookup.py
    status = lookup.check_online_status(domain)
    
    return jsonify({"domain": domain, "status": status})

@app.route('/form')
def form():
    """
    Renders a form with two input fields and two submit buttons.

    The first form allows the user to enter a domain and submit it to the '/lookup' endpoint.
    The second form allows the user to enter another input and submit it to the '/another_feature' endpoint.

    Returns:
        str: HTML content for the forms.
    """
    """
    Renders HTML forms for domain lookup and another feature.

    This function returns a string containing two HTML forms:
    1. A form for domain lookup with a text input for the domain and a submit button.
    2. A form for another feature with a text input for another input and a submit button.

    Usage:
    - Include this function in a Flask application.
    - Ensure `render_template_string` is imported from `flask`.
    - Map the form actions (`/lookup` and `/another_feature`) to appropriate view functions in the Flask app.

    Example:
        app = Flask(__name__)

        @app.route('/')
        def index():
            return form()

        @app.route('/lookup')
        def lookup():
            # Handle domain lookup
            pass

        @app.route('/another_feature')
        def another_feature():
            # Handle another feature
            pass

        if __name__ == '__main__':
            app.run(debug=True)
    """
    return render_template_string('''
        <form action="/lookup" method="get">
            <label for="domain">Enter domain:</label>
            <input type="text" id="domain" name="domain">
            <input type="submit" value="Check">
        </form>
        <form action="/another_feature" method="get">
            <label for="another_input">Another feature input:</label>
            <input type="text" id="another_input" name="another_input">
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/scrape_homepage', methods=['GET'])
def scrape_homepage():
    input_value = request.args.get('another_input')
    if not input_value:
        return jsonify({"error": "No input provided"}), 400
    
    # Use scrape_homepage function from lookup.py
    result = lookup.scrape_homepage(input_value)
    
    return jsonify({"input": input_value, "result": result})

if __name__ == '__main__':
    app.run(debug=True)
    @app.route('/webcheck', methods=['GET'])
    def webcheck():
        domain = request.args.get('domain')
        if not domain:
            return jsonify({"error": "No domain provided"}), 400
        
        # Use the lookup function from lookup.py to check online status
        online_status = lookup.check_online_status(domain)
        
        return jsonify({"domain": domain, "online_status": online_status})
    