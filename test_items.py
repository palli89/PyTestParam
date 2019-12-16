import time

def test_site_language(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"), "Кнопка, ты где?"
    time.sleep(5)