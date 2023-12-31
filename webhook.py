from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    event = request.headers.get('X-GitHub-Event')
    if event == 'push':
        try:
            branch = data['ref'].split('/')[-1]
            if branch == 'main':
                playbook_path = "/opt/webhook/playbook_prod.yml"
            
                subprocess.run(["ansible-playbook", playbook_path])
                print("Ansible playbook executed successfully for the main branch")
            elif branch == 'download_ota':
                playbook_path = "/opt/webhook/playbook_download_ota.yml"
            
                subprocess.run(["ansible-playbook", playbook_path])
                print("Ansible playbook executed successfully for the download ota branch")
        except Exception as e:
            print("Error executing Ansible playbook:", e)

    return "Webhook received successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
