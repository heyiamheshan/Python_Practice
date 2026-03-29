class phone :
    def call(self):
        print("Calling...")
class smartphone(phone):
    def browse(self):
        print("Browsing the internet...")

my_phone=smartphone()
my_phone.call()  # Inherited method from phone class