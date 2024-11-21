import psutil
import time
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure the email alerts
def send_email_alert(subject, body):
    sender_email = "aniket.ag1408@gmail.com"  # Update with your email
    receiver_email = "ganiket957@gmail.com"  # Update with receiver's email
    password = "cuqb vmau yhfs lxqp"  # Use your app password if 2FA is enabled

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Alert sent via email!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Configure Slack alerts
def send_slack_alert(message):
    slack_webhook_url = "https://hooks.slack.com/services/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"  # Your Slack webhook URL
    slack_data = {
        "text": message
    }
    try:
        response = requests.post(slack_webhook_url, json=slack_data)
        if response.status_code == 200:
            print("Alert sent to Slack!")
        else:
            print(f"Failed to send Slack alert. Response code: {response.status_code}")
    except Exception as e:
        print(f"Error sending Slack alert: {e}")

# Monitor system resources
def monitor_system(thresholds):
    while True:
        # Monitor CPU usage
        cpu = psutil.cpu_percent(interval=1)  # 1 second interval
        # Monitor memory usage
        memory = psutil.virtual_memory().percent
        # Monitor disk usage
        disk = psutil.disk_usage('/').percent
        
        alert_message = f"CPU Usage: {cpu}%\n"  # Always include CPU usage in the alert message

        # Check if any resource exceeds the threshold
        if cpu > thresholds['cpu']:
            alert_message += f"Warning: CPU usage is {cpu}% (Threshold: {thresholds['cpu']}%)\n"
        if memory > thresholds['memory']:
            alert_message += f"Warning: Memory usage is {memory}% (Threshold: {thresholds['memory']}%)\n"
        if disk > thresholds['disk']:
            alert_message += f"Warning: Disk usage is {disk}% (Threshold: {thresholds['disk']}%)\n"

        # Send alert if any resource exceeds the threshold
        if alert_message:
            send_email_alert("System Health Alert", alert_message)
            send_slack_alert(alert_message)

        time.sleep(60)  # Run every minute (60 seconds)

if __name__ == "__main__":
    thresholds = {
        'cpu': 80,       # CPU usage threshold (%)
        'memory': 80,    # Memory usage threshold (%)
        'disk': 85       # Disk usage threshold (%)
    }

    print("Starting system health monitoring...")
    monitor_system(thresholds)
