def test_logo(app):
    app.open_product_page()
    assert len(app.driver.find_elements_by_css_selector(".img-responsive")) == 1


def test_home_btn(app):
    app.open_product_page()
    assert len(app.driver.find_elements_by_css_selector(".fa-home")) == 1


def test_like_btn(app):
    app.open_product_page()
    assert len(app.driver.find_elements_by_css_selector(".btn > .fa-heart")) == 1


def test_add_to_card(app):
    app.open_product_page()
    assert len(app.driver.find_elements_by_id("button-cart")) == 1


def test_tab_reviews(app):
    app.open_product_page()
    assert len(app.driver.find_elements_by_css_selector(".nav-tabs > li:nth-child(2) > a")) == 1
