from selene import browser, have, command


class GitHubHomePage:

    def open(self):
        browser.open("https://github.com")
       # browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
      #      have.size_greater_than_or_equal(3)
       # )
       # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def sign_in_desktop(self):
        browser.element('[class*=sign-in]').click()

    def sign_in_mobile(self):
        browser.element('.HeaderMenu-toggle-bar').click()
        browser.element('[class*=sign-in]').click()
