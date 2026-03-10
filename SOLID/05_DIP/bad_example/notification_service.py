'''
  -Tighly coupled
  -Hard to modify (No flexibility)
  -Difficult to test
'''

from email_service import EmailService
from sms_service import SmsService

class NotificationService:
  def __init__(self):
    self.email_service = EmailService()
    self.sms_service = SmsService()

  def notifyByEmail(self, message):
    self.email_service.send_email(message)

  def notifyBySMS(self, message):
    self.sms_service.send_sms(message)

ns = NotificationService()
ns.notifyByEmail("HEllO")
ns.notifyBySMS("Good Evening")