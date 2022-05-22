
def test_logo(app):
    app.open_catalog_page()
    assert len(app.driver.find_elements_by_css_selector("#logo .img-responsive")) == 1


def test_home_btn(app):
    app.open_catalog_page()
    assert len(app.driver.find_elements_by_css_selector(".fa-home")) == 1


def test_add_btn(app):
    app.open_catalog_page()
    assert len(app.driver.find_elements_by_css_selector(".product-layout:nth-child(1) .hidden-xs")) == 1


def test_like_btn(app):
    app.open_catalog_page()
    assert len(app.driver.find_elements_by_css_selector(".product-layout:nth-child(1) .fa-heart")) == 1


def test_product_img(app):
    app.open_catalog_page()
    assert len(app.driver.find_elements_by_css_selector(".product-layout:nth-child(1) .img-responsive")) == 1
