import time
from playwright.sync_api import Locator, Page, TimeoutError as PlaywrightTimeoutError

class Utils:

    @staticmethod
    def wait_for_element(get_locator_function, attempts=5, interval=1):
        """
        Tenta encontrar um locator repetidamente até atingir o número de tentativas.

        :param get_locator_function: função que retorna um Locator do Playwright (ex: lambda: page.locator('...'))
        :param attempts: número máximo de tentativas
        :param interval: tempo (em segundos) entre cada tentativa
        :return: Locator pronto para interação
        :raises: Exception se o elemento não for encontrado após todas as tentativas
        """
        for i in range(attempts):
            try:
                locator = get_locator_function()
                locator.wait_for(state="visible", timeout=2000)
                return locator
            except PlaywrightTimeoutError:
                time.sleep(interval)
        raise Exception(f"[Utils] Elemento não encontrado após {attempts} tentativas.")

    @staticmethod
    def wait_for_text(page: Page, text: str, timeout: int = 10):
        """
        Espera até que um texto esteja visível na página.

        :param page: Instância do Playwright Page
        :param text: Texto a ser encontrado
        :param timeout: Tempo máximo de espera em segundos
        :return: True se o texto for encontrado, False caso contrário
        """
        locator = page.locator(f"//*[contains(text(), '{text}')]")
        try:
            locator.wait_for(state="visible", timeout=timeout * 1000)
            return True
        except PlaywrightTimeoutError:
            print(f"[Utils] Texto '{text}' não encontrado após {timeout} segundos.")
            return False