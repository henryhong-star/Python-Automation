from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utility.utilities import BaseClass


class TestAccount(BaseClass):

    def test_account_registration(self):

        self.driver.find_element_by_link_text("Sign in").click()

        self.driver.find_element_by_css_selector("#email_create").send_keys("qs67sbeyoqj@temporary-mail.net")

        self.driver.find_element_by_css_selector("#SubmitCreate").click()

        self.driver.find_element_by_css_selector("#id_gender1").click()

        self.driver.find_element_by_css_selector("#customer_firstname").send_keys("Judith")

        self.driver.find_element_by_css_selector("#customer_lastname").send_keys("Meagher")

        self.driver.find_element_by_css_selector("#passwd").send_keys("123456789")

        #driver.execute_script("window.scrollTo(0, 800)")

        drop_down_day = Select(self.driver.find_element(By.ID, "days"))

        drop_down_day.select_by_value('25')

        drop_down_month = Select(self.driver.find_element(By.ID, "months"))

        drop_down_month.select_by_value('8')

        drop_down_year = Select(self.driver.find_element(By.ID, "years"))

        drop_down_year.select_by_value('2018')

        self.driver.find_element_by_css_selector("#newsletter").click()

        self.driver.find_element_by_css_selector("#optin").click()

        self.driver.find_element_by_xpath("//input[@name='company']").send_keys("Cale Systems")

        self.driver.find_element_by_css_selector("#address1").send_keys("3187  Charter Street")

        self.driver.find_element_by_css_selector("#city").send_keys("Montrose")

        drop_down_state = Select(self.driver.find_element(By.ID, "id_state"))

        drop_down_state.select_by_value("32")

        self.driver.find_element_by_css_selector("#postcode").send_keys("85281")

        drop_down_country = Select(self.driver.find_element(By.ID,"id_country"))

        drop_down_country.select_by_value("21")

        self.driver.find_element_by_css_selector("#phone").send_keys("480-784-1580")

        self.driver.find_element_by_css_selector("#phone_mobile").send_keys("602-317-5856")

        self.driver.find_element_by_css_selector("#alias").send_keys("home")

        self.driver.find_element_by_css_selector("#submitAccount").click()

        account_confirm = self.driver.find_element_by_xpath("//p[@class='info-account']").text

        assert account_confirm == "Welcome to your account. Here you can manage all of your personal information and orders."

        self.driver.find_element_by_css_selector("a[title='Home']").click()