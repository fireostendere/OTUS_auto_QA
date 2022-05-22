class App:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.base_url = base_url

    def open_main_page(self):
        self.driver.get(self.base_url)

    def open_catalog_page(self):
        self.driver.get(self.base_url + "/smartphone")

    def open_product_page(self):
        self.driver.get(self.base_url + "/mp3-players/ipod-classic")

    def open_admin_page(self):
        self.driver.get(self.base_url + "/admin/")

    def open_user_reg_page(self):
        self.driver.get(self.base_url + "/index.php?route=account/register")
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

