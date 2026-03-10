from notification_channel import NotificationChannel

class EmailService(NotificationChannel):

  def send(self, message):
    print(f"Sending message: {message}")