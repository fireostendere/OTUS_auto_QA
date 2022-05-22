def test_logo(app):
    app.open_admin_page()
    assert len(app.driver.find_elements_by_css_selector("img")) == 1


def test_input_username(app):
    app.open_admin_page()
    assert len(app.driver.find_elements_by_id("input-username")) == 1


def test_input_password(app):
    app.open_admin_page()
    assert len(app.driver.find_elements_by_id("input-password")) == 1


def test_forgotten(app):
    app.open_admin_page()
    assert len(app.driver.find_elements_by_link_text("Forgotten Password")) == 1


def test_login_button(app):
    app.open_admin_page()
    assert len(app.driver.find_elements_by_css_selector(".btn")) == 1
