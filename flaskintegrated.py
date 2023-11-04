from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_python_file():
    data = request.get_json()
    code = data.get('code', '')

    with open('temp_file.py', 'w') as f:
        f.write(code)

    try:
        output = subprocess.check_output(['python', 'temp_file.py'], stderr=subprocess.STDOUT, text=True)
        return jsonify({'output': output.strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output.strip()}), 500

if __name__ == '__main__':
    app.run(debug=True)
