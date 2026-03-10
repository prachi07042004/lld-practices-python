'''
  DIP (Dependency Inversion Principle) - states that high level modules(business logic) should not directly depend on low level modules(specific implementations).Both should depend on abstractions(interfaces)
  High level - what your app does (notificaton service)
  Low Level - (db, email, etc.)
  Abstraction - Interface/Contract between them
'''
class EmailService:
  def send_email(self, message):
    print(f"Sending message: {message}")
    