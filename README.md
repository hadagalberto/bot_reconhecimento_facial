Bot para Reconhecimento Facial
===================


Esse bot para Telegram foi desenvolvido na linguagem Python. Seu funcionamento se dá da seguinte forma:
- Um usuário do Telegram começa o Bot. 
- Envia uma foto para o bot. 
- O Bot faz a chamada da API da Microsoft.
- Retorna uma outra foto com os rostos já marcados.

Foi desenvolvido para fins de estudo da linguagem. 

-------------

**Requisitos**

- Python na versão 3 (Se estiver no Ubuntu 16.04 ou menor siga os passos desse link: https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get para instalar o python3)
- Um PC ou servidor rodando Windows ou Linux ou Heroku.
- Um cérebro
-------------

**Como usar**
-------------


Siga os passos a seguir e você será capaz de rodar esse bot em instantes e sem nenhum problema!

**Passos a seguir:**

- Faça um clone desse repositório:
- `git clone https://github.com/hadagalberto/bot_reconhecimento_facial.git bot`
- Entre na pasta:
- `cd bot`
- Renomeie o arquivo chaves_sample.py para chaves.py
- Preencha os dados das chaves (Role a página abaixo para ver como conseguir essas chaves)
- Instale as libs nessessárias:
- `pip install requirements.txt`
- Rode o Bot:
- `python bot.py`
- Faça um teste enviando alguma foto com rostos para o bot!

--------
**Conseguindo as chaves nessessárias**
--------
- **Chave de Bot no Telegram:**
- Inicie um chat com o @BotFather
- Dê o comando '/newbot' e siga os passos até finalizar, gerando assim uma chave de acesso

- **Chave Microsoft Cognition Services**
- Entre nesse link: https://azure.microsoft.com/pt-br/try/cognitive-services/?api=face-api
- Clique em: "Obter chave de API" na frente de "API de Detecção Facial"
- Faça login em sua conta e terá criado a chave

**Lembrando que esse bot ainda está em fase de desenvolvimento, poderão ocorrer bugs inesperados**
