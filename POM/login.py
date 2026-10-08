from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):  # In constructor, we need to define all the locators of that page, not actions.
        self.page = page
        self.login_link=self.page.locator("#login2")
        self.user_input=self.page.locator("#loginusername")
        self.password_input=self.page.locator("#loginpassword")
        self.login_button=self.page.locator("button[onclick='logIn()']")

    # Need to create different Action methods for the corresponding actions of each element on the page.

    # def click_login_link(self):
    #     self.login_link.click()
    #
    # def click_user_input(self,username):
    #     self.user_input.fill("") # Before filling the username in this input box, it will clear the input box first
    #     self.user_input.fill(username)
    #
    # def click_password_input(self,password):
    #     self.password_input.fill("")
    #     self.password_input.fill(password)
    #
    # def click_login_button(self):
    #     self.login_button.click()

    # Instead of creating multiple Action methods,for multiple elements, we can combine  all the actions into one single method.


    def perform_login(self,username,password):
        self.login_link.click()
        self.user_input.fill("")
        self.user_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
