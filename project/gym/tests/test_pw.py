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

    expect(page).to_have_url(re.compile("http://127.0.0.1:8000/"))


def test_icone_github(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.locator('//*[@id="footer-container-github"]/a').click()

    expect(page).to_have_url(re.compile("https://github.com/welly555/Nicho-GYM"))


def test_redirecionar_cadastro(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Cadastre-se").click()

    expect(page).to_have_url(re.compile("cadastro/"))


def test_button_voltar_cadastro(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Cadastre-se").click()

    page.locator('//*[@id="button-voltar"]').click()

    expect(page).to_have_url(re.compile("http://127.0.0.1:8000/"))


def test_redirecionar_login(page: Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Login").click()

    expect(page).to_have_url(re.compile("login/"))

def test_button_voltar_login(page:Page):
    page.goto("http://127.0.0.1:8000/")

    page.get_by_role("link", name="Login").click()

    page.locator('//*[@id="button-voltar"]').click()

    expect(page).to_have_url(re.compile("http://127.0.0.1:8000/"))


def test_realizar_login(page: Page):
    page.goto("http://127.0.0.1:8000/login/")

    page.locator('//*[@id="id_Responsavel"]').fill("teste")

    page.locator('//*[@id="id_Senha"]').fill("Senha12345")

    page.get_by_role("button", name="login").click()

    expect(page).to_have_url(re.compile("dashboard/"))


def test_acessar_alunos_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.get_by_role("link", name="Alunos").click()

    expect(page).to_have_url(re.compile("dashboard_aluno"))


def test_acessar_personais_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.locator('//*[@id="header-id-personal"]').click()

    expect(page).to_have_url(re.compile("dashboard_personal/"))


def test_acessar_avaliacoes_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.get_by_role("link", name="Avaliação").click()

    expect(page).to_have_url(re.compile("dashboard_avaliacao/"))


def test_fazer_logout(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    page.get_by_role("button", name="logout").click()

    expect(page).to_have_url(re.compile("login/"))

def test_alunos_cadastrados_button_voltar(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("link", name="Alunos").click()

    page.locator('//*[@id="button_voltar"]').click()

    expect(page).to_have_url(re.compile("dashboard/"))


def test_personais_cadastrados_button_voltar(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.locator('//*[@id="header-id-personal"]').click()

    page.locator('//*[@id="button_voltar"]').click()

    expect(page).to_have_url(re.compile("dashboard/"))


def test_avaliacao_cadastrados_button_voltar(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("link", name="Avaliação").click()

    page.locator('//*[@id="button_voltar"]').click()

    expect(page).to_have_url(re.compile("dashboard/"))


def test_acessar_tela_cadastro_aluno(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("link", name="Alunos").click()

    page.locator('//*[@id="adicionar"]').click()

    expect(page).to_have_url(re.compile("aluno/"))


def test_voltar_tela_cadastro_aluno(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("link", name="Alunos").click()
    page.locator('//*[@id="adicionar"]').click()

    page.locator('//*[@id="button-voltar"]').click()

    expect(page).to_have_url(re.compile("dashboard_aluno"))


def test_acessar_tela_cadastro_personal(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.locator('//*[@id="header-id-personal"]').click()

    page.locator('//*[@id="adicionar"]').click()

    expect(page).to_have_url(re.compile("personal/"))


def test_voltar_tela_cadastro_personal(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.locator('//*[@id="header-id-personal"]').click()
    page.locator('//*[@id="adicionar"]').click()

    page.locator('//*[@id="button-voltar"]').click()

    expect(page).to_have_url(re.compile("dashboard_personal"))


def test_cadastrar_aluno(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("link", name="Alunos").click()
    page.locator('//*[@id="adicionar"]').click()

    page.locator('//*[@id="id_Nome"]').fill("Weslley")
    page.locator('//*[@id="id_sobrenome"]').fill("Almeida")
    page.locator('//*[@id="id_E_mail"]').fill("weslley@gmail.com")
    page.locator('//*[@id="id_Data_Nascimento"]').fill("14062024")
    page.locator('//*[@id="id_Valor_pagamento"]').fill("600")
    page.locator('//*[@id="id_Data_pagamento"]').fill("14072024")
    page.locator('//*[@id="id_telefone"]').fill("11111111111")

    page.get_by_role("button", name="cadastra aluno").click()

    expect(page).to_have_url(re.compile("aluno"))


def test_cadastrar_personal(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.locator('//*[@id="header-id-personal"]').click()

    page.locator('//*[@id="adicionar"]').click()

    page.locator('//*[@id="id_nome"]').fill("Carlos")
    page.locator('//*[@id="id_sobrenome"]').fill("Gustavo")
    page.locator('//*[@id="id_E_mail"]').fill("carlos@gmail.com")
    page.locator('//*[@id="id_telefone"]').fill("11111111111")

    page.get_by_role("button", name="cadastrar personal").click()


def test_cadastrar_avaliacao(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    # Adcionar um aluno
    page.locator('//*[@id="id_Nome"]').fill("Weslley")
    page.locator('//*[@id="id_sobrenome"]').fill("Almeida")
    page.locator('//*[@id="id_E_mail"]').fill("weslley@gmail.com")
    page.locator('//*[@id="id_Data_Nascimento"]').fill("14062024")
    page.locator('//*[@id="id_Valor_pagamento"]').fill("600")
    page.locator('//*[@id="id_Data_pagamento"]').fill("14072024")
    page.locator('//*[@id="id_telefone"]').fill("11111111111")

    page.get_by_role("link", name="Avaliação").click()

    page.locator('//*[@id="adicionar"]').click()

    page.locator('//*[@id="id_peso"]').fill("80")
    page.locator('//*[@id="id_altura"]').fill("1,80")
    page.locator('//*[@id="id_Dobra_tripical"]').fill("10")
    page.locator('//*[@id="id_Dobra_abdominal"]').fill("50")
    page.locator('//*[@id="id_Dobra_subescapular"]').fill("20")
    page.locator('//*[@id="id_Dobra_suprailiaca"]').fill("30")

    page.get_by_role("button", name="finalizar avaliacao").click()


def test_deletar_alunos_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("link", name="Alunos").click()

    page.locator('//*[@id="deletar"]').click()

    expect(page).to_have_url(re.compile("dashboard_aluno"))


def test_deletar_personais_cadastrados(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()
    page.locator('//*[@id="header-id-personal"]').click()

    page.locator('//*[@id="deletar"]').click()

    expect(page).to_have_url(re.compile("dashboard_personal/"))


def test_acessar_tela_cadastro_avaliacao(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    # Cadastrar um aluno
    page.locator('//*[@id="id_Nome"]').fill("Weslley")
    page.locator('//*[@id="id_sobrenome"]').fill("Almeida")
    page.locator('//*[@id="id_E_mail"]').fill("weslley@gmail.com")
    page.locator('//*[@id="id_Data_Nascimento"]').fill("14062024")
    page.locator('//*[@id="id_Valor_pagamento"]').fill("600")
    page.locator('//*[@id="id_Data_pagamento"]').fill("14072024")
    page.locator('//*[@id="id_telefone"]').fill("11111111111")

    page.get_by_role("link", name="Avaliação").click()

    page.locator('//*[@id="adicionar"]').click()

    expect(page).to_have_url(re.compile("avaliacao/"))


def test_voltar_tela_cadastro_avalaicao(page: Page):
    #Login para ser redirecionado para a dashboard
    page.goto("http://127.0.0.1:8000/login/")
    page.locator('//*[@id="id_Responsavel"]').fill("teste")
    page.locator('//*[@id="id_Senha"]').fill("Senha12345")
    page.get_by_role("button", name="login").click()

    # Adcionar um aluno
    page.locator('//*[@id="id_Nome"]').fill("Weslley")
    page.locator('//*[@id="id_sobrenome"]').fill("Almeida")
    page.locator('//*[@id="id_E_mail"]').fill("weslley@gmail.com")
    page.locator('//*[@id="id_Data_Nascimento"]').fill("14062024")
    page.locator('//*[@id="id_Valor_pagamento"]').fill("600")
    page.locator('//*[@id="id_Data_pagamento"]').fill("14072024")
    page.locator('//*[@id="id_telefone"]').fill("11111111111")

    page.get_by_role("link", name="Avaliação").click()
    page.locator('//*[@id="adicionar"]').click()

    page.locator('//*[@id="button-voltar"]').click()

    expect(page).to_have_url(re.compile("dashboard_avalaicao"))
