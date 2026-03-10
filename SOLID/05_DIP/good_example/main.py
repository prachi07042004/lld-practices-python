from notification_service import NotificationService
from email_service import EmailService
from sms_service import SMSService

sms_service = SMSService()
ns = NotificationService(sms_service)
ns.notify("Heyy")

