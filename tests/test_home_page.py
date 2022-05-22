def test_logo(app):
    app.open_main_page()
    assert len(app.driver.find_elements_by_css_selector("#logo .img-responsive")) == 1


def test_basket(app):
    app.open_main_page()
    assert len(app.driver.find_elements_by_id("cart-total")) == 1


def test_slide_show(app):
    app.open_main_page()
    assert len(app.driver.find_elements_by_css_selector(".swiper-slide-active > a > .img-responsive")) == 1


def test_swiper_carouse(app):
    app.open_main_page()
    assert len(app.driver.find_elements_by_css_selector("#carousel0 > .swiper-wrapper")) == 1


def test_product(app):
    app.open_main_page()
    assert len(app.driver.find_elements_by_css_selector(".product-layout:nth-child(1) .img-responsive")) == 1
