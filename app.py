from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/support', methods=['POST'])
def support_ticket():
    data = request.json
    user_email = data.get('email', '')
    
    if user_email:
        return jsonify({"message": f"Support request received for {user_email}. Our team will contact you shortly."}), 200
    else:
        return jsonify({"error": "Invalid email address"}), 400

if __name__ == '__main__':
    app.run(debug=True)
