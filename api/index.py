# from flask import Flask, request, jsonify, render_template
# import re

# app = Flask(__name__)

# def increment_mac(mac, count=7):
#     mac_int = int(mac.replace(":", ""), 16)
#     mac_list = []
#     for i in range(1, count + 1):
#         next_mac_int = mac_int + i
#         next_mac = ':'.join(f'{(next_mac_int >> ele) & 0xff:02x}' for ele in range(40, -1, -8)).upper()
#         mac_list.append(next_mac)
#     return mac_list

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate():
#     data = request.json
#     mac = data.get('mac', '').replace('-', ':').replace('.', ':').upper()
    
#     if len(mac) == 12:
#         mac = ':'.join(mac[i:i+2] for i in range(0, 12, 2))
    
#     if re.match("[0-9A-F]{2}([:])[0-9A-F]{2}(\\1[0-9A-F]{2}){4}$", mac):
#         generated_macs = increment_mac(mac)
#         return jsonify({ 'macs': generated_macs })
#     else:
#         return jsonify({ 'error': 'Invalid MAC address format.' }), 400

# if __name__ == '__main__':
#     app.run(debug=True)
    
from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__, template_folder="../templates")

def increment_mac(mac, count=7):
    mac_int = int(mac.replace(":", ""), 16)
    mac_list = []
    for i in range(1, count + 1):
        next_mac_int = mac_int + i
        next_mac = ':'.join(f'{(next_mac_int >> ele) & 0xff:02x}' for ele in range(40, -1, -8)).upper()
        mac_list.append(next_mac)
    return mac_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST']) 
def generate():
    data = request.json
    mac = data.get('mac', '').replace('-', ':').replace('.', ':').upper()

    if len(mac) == 12:
        mac = ':'.join(mac[i:i+2] for i in range(0, 12, 2))

    if re.match("[0-9A-F]{2}([:])[0-9A-F]{2}(\\1[0-9A-F]{2}){4}$", mac):
        generated_macs = increment_mac(mac)
        return jsonify({'macs': [mac] + generated_macs}) 
    else:
        return jsonify({'error': 'Invalid MAC address format.'}), 400 

app = app