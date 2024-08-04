from seleniumbase import BaseCase

class AdditionalTheInternetTests(BaseCase):

    def test_form_authentication(self):
        self.open("https://the-internet.herokuapp.com/login")
        self.type("#username", "tomsmith")
        self.type("#password", "SuperSecretPassword!")
        self.click("button[type='submit']")
        self.assert_text("Secure Area", "h2")
        self.assert_element(".flash.success")

    def test_file_upload(self):
        self.open("https://the-internet.herokuapp.com/upload")
        self.choose_file("#file-upload", "C:\\Users\\pasha\\Desktop\\file.txt")
        self.click("#file-submit")
        self.assert_text("File Uploaded!", "h3")
        self.assert_element("#uploaded-files")

    def test_javascript_alerts(self):
        self.open("https://the-internet.herokuapp.com/javascript_alerts")
        
        self.click("button[onclick='jsAlert()']")
        self.wait_for_alert(timeout=20)
        self.accept_alert()
        self.assert_text("You successfully clicked an alert", "#result")

        self.click("button[onclick='jsConfirm()']")
        self.wait_for_alert(timeout=20)
        self.dismiss_alert()
        self.assert_text("You clicked: Cancel", "#result")

        self.click("button[onclick='jsPrompt()']")
        self.wait_for_alert(timeout=20)
        self.send_keys_to_alert("SeleniumBase")
        self.accept_alert()
        self.assert_text("You entered: SeleniumBase", "#result")

    def test_basic_auth(self):
        self.open("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        self.assert_text("Congratulations! You must have the proper credentials.", "p")

    def test_dynamic_controls(self):
        self.open("https://the-internet.herokuapp.com/dynamic_controls")
        self.click("#checkbox-example button")
        self.assert_text("It's gone!", "#message")

        # This step will fail intentionally
        self.assert_element("#checkbox")  # This element should not exist

        self.click("#checkbox-example button")
        self.assert_element("#checkbox")

        self.click("#input-example button")
        self.assert_element("#input-example input:enabled")

        self.click("#input-example button")
        self.assert_element("#input-example input:disabled")

if __name__ == "__main__":
    from pytest import main
    main(["-v", "tests.py"])
