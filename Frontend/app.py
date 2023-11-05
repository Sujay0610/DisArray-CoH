from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('vanilla.html')

@app.route('/execute', methods=['POST'])
def execute():
    try:
        path = 'Frontend\scripts'


        script_path = os.path.join(path, 'new2flask.py')
        print(script_path)
        
        # Check if the script file exists
        if not os.path.exists(script_path):
            return {'output': 'Error: Script file not found.'}

        # Execute the Python script
        result = subprocess.check_output(['python', script_path], stderr=subprocess.STDOUT, text=True)
        return {'output': result}
    except subprocess.CalledProcessError as e:
        return {'output': e.output}

if __name__ == '__main__':
    app.run(debug=True)
