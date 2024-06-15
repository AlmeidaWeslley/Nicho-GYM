Cenario 01:
    Desde que o usuario acesse a pagina home
    Quando o usuario clicar no nome "NICHO-GYM" no cabeçalho
    Então ele é redirecionado para o a pagina home

Cenario 02:
    Desde o usuario acesse a pagina home
    Quando o usuario clicar no icone do github
    Então o usuario será redirecionado para o repositorio do codigo

Cenario 03:
    Desde o usuario acesse a pagina home
    Quando o usuario clicar no botão de cadastro
    Então o usuario será redirecionado para a pagina de cadastro

Cenario 04:
    Desde que o usuario acesse a home page
    Quando o usuario clicar no botão "login"
    Então o usuario é redirecionado para a pagina de login

Cenario 05:
    Desde o usuario acessar a pagina de cadastro
    Quando o usuario clicar no botão de voltar
    Então o usuario é redirecionado para a pagina home

Cenario 06:
    Desde o usuario acessar a pagina de login
    Quando o usuario clicar no botão de voltar
    Então o usuario é redirecionado para a pagina home

Cenario 07:
    Desde que o usuario acesse a pagina de login
    Quando o usuario preencher o campo de responsavel com "teste"
    E o usuario preencher o campo de senha com "Senha12345"
    Então o usuario é redirecionado para a pagina de dashboard

Cenario 08:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Alunos"
    Então o usuario será redirecionado para a pagina de alunos cadastrados

Cenario 09:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Personais"
    Então o usuario será redirecionado para a pagina de personais cadastrados

Cenario 10:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Avaliação"
    Então o usuario será redirecionado para a pagina de avaliações cadastradas

Cenario 11:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "logout"
    Então o usuario será redirecionado para a pagina home

Cenario 12:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Alunos"
    E quando o usuario ser redirecionado para a pagina de alunos cadastrados
    E quando o usuario clicar no botão de voltar
    Então o usuario será redirecionado para a pagina de dashboard

Cenario 13:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Personais"
    E quando o usuario ser redirecionado para a pagina de personais cadastrados
    E quando o usuario clicar no botão de voltar
    Então o usuario será redirecionado para a pagina de dashboard

Cenario 14:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Avaliação"
    E quando o usuario ser redirecionado para a pagina de avaliações cadastradas
    E quando o usuario clicar no botão de voltar
    Então o usuario será redirecionado para a pagina de dashboard

Cenario 15:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Alunos"
    E quando o usuario ser redirecionado para a pagina de alunos cadastradas
    E quando o usuario clicar no botão verde de adicionar novo aluno
    Então o usuario será redirecionado para a pagina de cadastro de alunos

Cenario 16:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Personais"
    E quando o usuario ser redirecionado para a pagina de personais cadastradas
    E quando o usuario clicar no botão verde de adicionar novo personal
    Então o usuario será redirecionado para a pagina de cadastro de personal

Cenario 17:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Avaliação"
    E quando o usuario ser redirecionado para a pagina de avaliações cadastradas
    E quando o usuario clicar no botão verde de adicionar nova avaliação
    Então o usuario será redirecionado para a pagina de cadastro de avaliação

Cenario 18:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Avaliação"
    E quando o usuario ser redirecionado para a pagina de avaliações cadastradas
    E quando o usuario clicar no botão verde de adicionar nova avaliação
    E quando o usuario clicar no botão de voltar
    Então o usuario será redirecionado para a tela de avaliações cadastradas

Cenario 19:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Alunos"
    E quando o usuario ser redirecionado para a pagina de alunos cadastradas
    E quando o usuario clicar no botão de voltar
    Então o usuario será redirecionado para a tela de alunos cadastradas

Cenario 20:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Personais"
    E quando o usuario ser redirecionado para a pagina de personais cadastradas
    E quando o usuario clicar no botão de voltar
    Então o usuario será redirecionado para a tela de personais cadastradas

Cenario 21:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Alunos"
    E quando o usuario ser redirecionado para a pagina de alunos cadastradas
    E quando o usuario preencher o campo 'Nome do aluno' com "Weslley"
    E quando o usuario preencher o campo 'Sobrenome' com "Almeida"
    E quando o usuario preencher o campo 'E-mail' com "weslley@gmail.com"
    E quando o usuario preencher o campo 'Data de Nascimento' com "14062024"
    E quando o usuario preencher o campo 'Valor de Pagamento' com "600"
    E quando o usuario preencher o campo 'Data do proximo Pagamento' com "14072024"
    E quando o usuario preencher o campo 'Telefone' com "11111111111"
    E quando o usuario clicar no botão 'cadastrar aluno'
    Então o usuario será redirecionado para a tela de alunos cadastrados

Cenario 22:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Personais"
    E quando o usuario ser redirecionado para a pagina de personais cadastradas
    E quando o usuario preencher o campo 'Nome do personal' com "Carlos"
    E quando o usuario preencher o campo 'Sobrenome' com "Gustavo"
    E quando o usuario preencher o campo 'E-mail' com "carlos@gmail.com"
    E quando o usuario preencher o campo 'Telefone' com "11111111111"
    E quando o usuario clicar no botão 'cadastrar personal'
    Então o usuario será redirecionado para a tela de personais cadastrados

Cenario 23:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Avaliação"
    E quando o usuario ser redirecionado para a pagina de avaliações cadastradas
    E quando o usuario preencher o campo 'Peso' com "80"
    E quando o usuario preencher o campo 'Dobra tripical' com "10"
    E quando o usuario preencher o campo 'Dobra abdominal' com "50"
    E quando o usuario preencher o campo 'Dobra subescapular' com "20"
    E quando o usuario preencher o campo 'Dobra suprailiaca' com "20"
    E quando o usuario clicar no botão 'finalizar avaliacao'
    Então o usuario será redirecionado para a tela de personais cadastrados

Cenario 24:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Personais"
    E quando o usuario ser redirecionado para a pagina de personais cadastradas
    E quando o usuario clicar no botão de lixeiro
    Então o usuario deletará um personal

Cenario 25:
    Desde que o usuario acesse a pagina de dashboard 
    Quando o usuario clicar no nome "Alunos"
    E quando o usuario ser redirecionado para a pagina de alunos cadastradas
    E quando o usuario clicar no botão de lixeiro
    Então o usuario deletará um aluno