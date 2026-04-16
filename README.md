# Documentação do Projeto EduDjango

## Visão Geral do Projeto
EduDjango é uma aplicação web desenvolvida para facilitar a gestão de cursos e avaliações em instituições de ensino. O projeto visa proporcionar uma interface intuitiva para administradores e alunos, permitindo o gerenciamento eficiente de informações acadêmicas.

## Estrutura do Projeto
- **edu_django/**: Pacote principal da aplicação.
  - **models.py**: Contém as definições dos modelos de dados.
  - **views.py**: Classe e funções responsáveis pela lógica de apresentação.
  - **forms.py**: Formulários utilizados nas interações do usuário.
  - **urls.py**: Roteamento das URLs da aplicação.
- **templates/**: Contém os templates HTML para renderização das páginas.
- **static/**: Arquivos estáticos como CSS e JavaScript.

## Instruções de Instalação
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/jorgearaujoengquim/EduDjango.git
   cd EduDjango
   ```
2. **Crie um ambiente virtual**:
   ```bash
   python -m venv env
   source env/bin/activate  # No Windows use `env\Scripts\activate`
   ```
3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure o banco de dados**:
   Edite o arquivo `settings.py` para ajustar as configurações do banco de dados conforme necessário.

5. **Aplique as migrações**:
   ```bash
   python manage.py migrate
   ```

## Modelos de Dados
### Curso
- **Nome**: nome do curso (String)
- **Descrição**: descrição do curso (Texto)

### Avaliacao
- **Curso**: referência ao modelo Curso (Chave Estrangeira)
- **Nota**: nota atribuída ao aluno (Decimal)
- **Data da Avaliação**: data em que a avaliação foi realizada (Data)

## Explicação das Views
As views são responsáveis pela lógica de cada página da aplicação. Utilizam-se classes para organizar a funcionalidade em vez de funções simples, tornando o código mais legível e escalável.

## Formulários
Os formulários são definidos no arquivo `forms.py`. Eles utilizam a biblioteca Django Forms para validação e manipulação dos dados enviados pelo usuário.

## Roteamento de URL
As URLs são gerenciadas no arquivo `urls.py`, onde cada endpoint está associado a uma view correspondente, facilitando a navegação pela aplicação.

## Como Executar o Projeto
Para iniciar o servidor de desenvolvimento, use:
```bash
python manage.py runserver
```
O aplicativo estará acessível em `http://127.0.0.1:8000/`.

## Funcionalidades
- Gestão de cursos e avaliações.
- Avaliações em tempo real e gestão de notas.
- Interface amigável para usuários e administradores.

## Notas de Desenvolvimento
- O projeto está em constante desenvolvimento. Contribuições são bem-vindas!
- Para relatar problemas ou sugerir melhorias, utilize a seção de issues do GitHub.

---