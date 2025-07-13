# 🤖 Discord Bot Tradutor

Um bot simples para Discord feito em Python, que traduz mensagens automaticamente usando a API do Google Translate.

![Python](https://img.shields.io/badge/Feito%20com-Python%203.11-blue?style=flat&logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-2.5.2-blueviolet)
![Googletrans](https://img.shields.io/badge/googletrans-4.0.2-green)

---

## 📦 Requisitos

- Python 3.11 ou 3.12 (⚠️ Python 3.13 pode causar problemas!)
- Ambiente virtual (recomendado)
- Token de bot do Discord (obtenha em: https://discord.com/developers/applications)

### Pacotes usados:
- discord.py==2.5.2
- googletrans==4.0.2

---

## 🛠️ Como instalar

1. Clone ou copie este projeto:
   git clone https://github.com/hiroyats05/Discord-Bot.git
   cd Discord-Bot

2. Crie um ambiente virtual:
   python -m venv venv

3. Ative o ambiente virtual:
   .\venv\Scripts\activate        (no PowerShell do Windows)

4. Instale os pacotes necessários:
   pip install -r requirements.txt

---

## ⚙️ Configuração do Bot

Abra o arquivo `bot.py` e substitua a linha:

    bot.run('INSIRA O TOKEN DO SEU BOT')

por:

    bot.run('SEU_TOKEN_DO_SEU_BOT')

---

## 💬 Comando Disponível

.traduzir "idioma" "mensagem"

Exemplo:

.traduzir en Olá, tudo bem?

Resposta esperada:

Tradução (en): Hello, how are you?

---

## 🌍 Idiomas Suportados (exemplos)

| Código | Idioma     |
|--------|------------|
| pt     | Português  |
| en     | Inglês     |
| es     | Espanhol   |
| fr     | Francês    |
| de     | Alemão     |
| ja     | Japonês    |

⚠️ Use os códigos ISO dos idiomas no comando.

## 👨‍💻 Autor

Criado por: Hiroshi Yatabe  
GitHub: https://github.com/hiroyats05   
Finalidade: Aprendizado com bots do Discord e tradução automática.

---

## 📝 Licença

Este projeto é livre para uso educacional e pessoal.
