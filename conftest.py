import os

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # ou firefox/webkit, se quiser
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


# ========== Evidência em sucesso e falha ==========

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Executa o teste e pega o resultado
    outcome = yield
    rep = outcome.get_result()

    # Pegue o page do teste (se existir)
    page = item.funcargs.get("page", None)

    if rep.when == "call" and page is not None:
        # Certifique-se que o atributo extra existe para o relatório
        rep.extra = getattr(rep, "extra", [])

        screenshots_dir = os.path.join("evidencias")
        os.makedirs(screenshots_dir, exist_ok=True)

        file_name = f"{item.name}_{rep.outcome}.png"
        file_path = os.path.join(screenshots_dir, file_name)

        # Tira a screenshot
        page.screenshot(path=file_path, full_page=True)

        # Adiciona a screenshot ao relatório html do pytest-html
        if pytest_html:
            rep.extra.append(pytest_html.extras.image(file_path))
