from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Utility.utilities import BaseClass


class TestPurchases(BaseClass):

    def test_popular_items_purchase(self):

        #self.driver.execute_script("window.scrollTo(0, 800)")                                                           # For Firefox Browser Only

        action = ActionChains(self.driver)

        items = self.driver.find_elements_by_xpath("//ul[@id='homefeatured']/li/div")

        for item in items:

            action.move_to_element(item).perform()
            self.driver.find_element_by_link_text("Add to cart").click()
            #self.verify_element_presence("span[title='Continue shopping']")                                            # For Firefox Browser Only
            self.driver.find_element_by_css_selector("span[title='Continue shopping']").click()                         # For Chrome and Edge Only

        #self.driver.execute_script("window.scrollTo(0, 0)")                                                            # For Firefox Browser Only

        #self.verify_element_presence("a[title='View my shopping cart']")                                               # For Firefox Browser Only

        action.move_to_element(self.driver.find_element_by_css_selector("a[title='View my shopping cart']")).perform()

        self.driver.find_element_by_css_selector("#button_order_cart").click()

        self.driver.find_element_by_link_text("Proceed to checkout").click()

        self.driver.find_element_by_css_selector("#email").send_keys("p10r0famdy@temporary-mail.net")

        self.driver.find_element_by_css_selector("#passwd").send_keys("123456789")

        self.driver.find_element_by_css_selector("#SubmitLogin").click()

        self.driver.find_element_by_css_selector("textarea[name='message']").send_keys("This is a gift")

        self.driver.find_element_by_css_selector("button[name='processAddress']").click()

        self.driver.find_element_by_css_selector("#cgv").click()

        self.driver.find_element_by_link_text("(Read the Terms of Service)").click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.find_element_by_css_selector("a[title='Close']").click()

        self.driver.find_element_by_css_selector("button[name='processCarrier']").click()

        self.driver.find_element_by_css_selector("a[title='Pay by bank wire']").click()

        self.driver.find_element_by_css_selector("#cart_navigation button").click()

        print(self.driver.find_element_by_css_selector(".box p strong").text)

        purchase_complete = self.driver.find_element_by_css_selector(".box p strong").text

        assert purchase_complete == "Your order on My Store is complete."









