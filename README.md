# 🖥️ System Health Monitor

A Python-based system resource monitoring tool that tracks **CPU**, **Memory**, and **Disk** usage in real-time and sends alerts via **Email** and **Slack** when usage exceeds predefined thresholds.

## 🚀 Features

- 📊 Real-time monitoring of:
  - **CPU Usage**
  - **Memory Usage**
  - **Disk Usage**
- 🔔 Alert Notifications:
  - Sends alerts to your **Email** (via SMTP)
  - Sends alerts to a **Slack channel** (via Webhook)
- ⏱️ Checks system health every **60 seconds**
- 🛠️ Customizable resource thresholds

---

## 📦 Requirements

Install the required dependencies using pip:

```bash
pip install psutil requests
```

---

## ⚙️ Configuration

### 1. Email Alerts

- Replace the following values in `send_email_alert()`:
  ```python
  sender_email = "your_email@gmail.com"
  receiver_email = "recipient_email@gmail.com"
  password = "your_app_password"
  ```
- If using Gmail, enable **App Passwords** from your Google Account → Security → App Passwords (especially if 2FA is enabled).

### 2. Slack Alerts

- Set up a Slack **Incoming Webhook**:
  - Go to: https://api.slack.com/messaging/webhooks
  - Create a webhook and copy the URL
- Replace the webhook URL in `send_slack_alert()`:
  ```python
  slack_webhook_url = "https://hooks.slack.com/services/XXX/YYY/ZZZ"
  ```

---

## 🧪 Usage

Run the script with:

```bash
python system_monitor.py
```

You will see:

```
Starting system health monitoring...
```

The script checks your system every minute and alerts when resource usage exceeds defined limits.

---

## 📈 Threshold Configuration

Edit these values in the `__main__` section to set your custom thresholds:

```python
thresholds = {
    'cpu': 80,       # Alert if CPU usage > 80%
    'memory': 80,    # Alert if memory usage > 80%
    'disk': 85       # Alert if disk usage > 85%
}
```

---

## 📬 Alert Message Example

```
CPU Usage: 92.5%
Warning: CPU usage is 92.5% (Threshold: 80%)
Warning: Memory usage is 85.2% (Threshold: 80%)
```

---

## 🔐 Security Notes

- Avoid hardcoding credentials in production.
- Use environment variables or `.env` files for storing sensitive data.
- Never share your actual email passwords or Slack webhook URLs in public repositories.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.
