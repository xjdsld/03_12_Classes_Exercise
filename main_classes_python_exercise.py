class Mail_Method:
  def mail(self, address):
    raise NotImplementedError('!')

class Email(Mail_Method):
  def mail(self, address):
    print(f"You're sending an e-mail message to {address}")

class Post(Mail_Method):
  def mail(self, address):
    print(f"You're sending a letter to {address}")

class Pigeon(Mail_Method):
  def mail(self, address):
    print(f"You're sending a letter with a pigeon to {address}")


def process_mail(method:Mail_Method, address):
    method.mail(address)

address = 'generalmailbox@gmail.com'

process_mail(Email(), address)
process_mail(Post(), address)
process_mail(Pigeon(), address)
