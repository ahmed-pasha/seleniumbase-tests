from seleniumbase import BaseCase
import time

class InternetHerokuappTests(BaseCase):

    def test_login(self):
        self.open("https://the-internet.herokuapp.com/login")
        time.sleep(1)  # Adding delay
        self.type("#username", "tomsmith")
        time.sleep(1)  # Adding delay
        self.type("#password", "SuperSecretPassword!")
        time.sleep(1)  # Adding delay
        self.click("button[type='submit']")
        time.sleep(1)  # Adding delay
        self.assert_text("You logged into a secure area!", "#flash")

    def test_add_remove_elements(self):
        self.test_login()  # Ensure login is done first
        self.open("https://the-internet.herokuapp.com/add_remove_elements/")
        time.sleep(1)  # Adding delay
        self.click("button[onclick='addElement()']")
        time.sleep(1)  # Adding delay
        self.assert_element_present(".added-manually")
        time.sleep(1)  # Adding delay
        self.click(".added-manually")
        time.sleep(1)  # Adding delay
        self.assert_element_not_present(".added-manually")

    def test_checkboxes(self):
        self.test_login()  
        self.open("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(1)  # Adding delay
        self.assert_false(self.is_checked("#checkboxes input:nth-child(1)"))
        time.sleep(1)  # Adding delay
        self.click("#checkboxes input:nth-child(1)")
        time.sleep(1)  # Adding delay
        self.assert_true(self.is_checked("#checkboxes input:nth-child(1)"))
        time.sleep(1)  # Adding delay
        self.assert_true(self.is_checked("#checkboxes input:nth-child(3)"))
        time.sleep(1)  # Adding delay
        self.click("#checkboxes input:nth-child(3)")
        time.sleep(1)  # Adding delay
        self.assert_false(self.is_checked("#checkboxes input:nth-child(3)"))

    def test_context_menu(self):
        self.test_login()  
        self.open("https://the-internet.herokuapp.com/context_menu")
        time.sleep(1)  # Adding delay
        self.context_click("#hot-spot")
        time.sleep(1)  
        self.assert_alert_text("You selected a context menu")
        self.accept_alert()

    def test_file_upload(self):
        self.test_login() 
        self.open("https://the-internet.herokuapp.com/upload")
        time.sleep(1) 
        self.choose_file("#file-upload", "sample.txt")
        time.sleep(1) 
        self.click("#file-submit")
        time.sleep(1) 
        self.assert_text("File Uploaded!", "h3")

