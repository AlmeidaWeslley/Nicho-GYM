import re
from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_nome_cabecalho(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="NICHO-GYM").click()


def test_icone_github(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.locator('//*[@id="footer-container-github"]/a').click()


def test_redirecionar_cadastro(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Cadastre-se").click()


def test_button_voltar_cadastro(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Cadastre-se").click()

    page.locator('//*[@id="button-voltar"]').click()


def test_redirecionar_login(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Login").click()

def test_button_voltar_login(page:Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Login").click()

    page.locator('//*[@id="button-voltar"]').click()


def test_realizar_login(page: Page):
    page.goto("http://127.0.0.1:8000/login/")

    page.locator('//*[@id="id_Responsavel"]').fill("teste")

    page.locator('//*[@id="id_Senha"]').fill("Senha12345")

    page.get_by_role("button", name="login").click


def test_acessar_alunos_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.get_by_role("link", name="Alunos").click()


def test_acessar_personais_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.locator('//*[@id="header-id-personal"]').click()


def test_acessar_avaliacoes_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.get_by_role("link", name="Avaliação").click()


def test_fazer_logout(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.get_by_role("button", name="logout").click()