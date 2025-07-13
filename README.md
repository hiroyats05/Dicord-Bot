DISCORD BOT - TRADUTOR DE MENSAGENS
Este é um bot simples para Discord feito em Python. Ele traduz mensagens usando a API do Google Translate
(através da biblioteca `googletrans`) quando o usuário envia um comando no canal.

🔧 REQUISITOS
- Python 3.11 ou 3.12 (Python 3.13 pode causar problemas)
- Ambiente virtual (recomendado)
- Token de bot do Discord (obtido em https://discord.com/developers/applications)

Pacotes Python usados:
- discord.py==2.5.2
- googletrans==4.0.2

🚀 COMO INSTALAR
1. Clone ou copie este projeto para seu computador.

2. No terminal (PowerShell), navegue até a pasta do projeto e crie um ambiente virtual:
   python -m venv venv

3. Ative o ambiente virtual:
   .\venv\Scripts\activate

4. Instale os pacotes necessários:
   pip install -r requirements.txt

5. Edite o arquivo `bot.py` e substitua:
   bot.run('INSIRA SEU TOKEN AQUI')
   pelo seu token real do bot.

💬 COMANDO DISPONÍVEL
.traduzir <idioma> <mensagem>

Exemplo:
.traduzir en Olá, tudo bem?

Resposta esperada:
Tradução (en): Hello, how are you?

Idiomas devem ser informados usando códigos ISO, por exemplo:
- pt (português)
- en (inglês)
- es (espanhol)
- fr (francês)
- de (alemão)
- ja (japonês)

Criado por: Hiroshi Yatabe / github.com/hiroyats05
Data: Julho de 2025
Projeto para aprendizado e testes com Discord Bots e tradução automática.
