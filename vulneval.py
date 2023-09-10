from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

# Vulnerability 1: Insecure use of eval
@app.route('/calculate')
def calculate():
    expression = request.args.get('expression')
    result = eval(expression)
    return jsonify({'success': True, 'result': result})

# Vulnerability 2: Arbitrary code execution using exec
@app.route('/run_code')
def run_code():
    code = request.args.get('code')
    exec(code)
    return jsonify({'success': True, 'message': 'Code executed!'})

# Vulnerability 3: OS command injection
@app.route('/rename_file')
def rename_file():
    old_name = request.args.get('old_name')
    new_name = request.args.get('new_name')
    os.system(f'mv {old_name} {new_name}')
    return jsonify({'success': True, 'message': 'File renamed!'})

if __name__ == '__main__':
    app.run(debug=True)
