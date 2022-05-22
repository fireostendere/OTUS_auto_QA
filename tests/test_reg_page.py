
def test_logo(app):
    app.open_user_reg_page()
    assert len(app.driver.find_elements_by_css_selector(".img-responsive")) == 1


def test_input_first_name(app):
    app.open_user_reg_page()
    assert len(app.driver.find_elements_by_id("input-firstname")) == 1


def test_input_last_name(app):
    app.open_user_reg_page()
    assert len(app.driver.find_elements_by_id("input-lastname")) == 1


def test_input_password(app):
    app.open_user_reg_page()
    assert len(app.driver.find_elements_by_id("input-password")) == 1


def test_subscribe_radio_btn(app):
    app.open_user_reg_page()
    assert len(app.driver.find_elements_by_css_selector(".radio-inline:nth-child(2) > input")) == 1
