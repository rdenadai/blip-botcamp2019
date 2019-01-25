# **BLiP BotCamp2019**

Chatbot criado durante o BotCamp2019 da empresa Take usando o aplicativo **BLiP**.

[BLiP Botcamp: Chatbots: da teoria à mão na massa](https://botcamp.blip.ai/)

## Equipe

 - Eduardo Mercio
 - Rodolfo De Nadai
 - Romualdo Junior


## Como usar

 - Crie uma conta no [BLiP](https://blip.ai)
 - Dentro da conta, crie um bot e realize a importação do arquivo [sampabot.json](https://github.com/rdenadai/blip-botcamp2019/blob/master/bot/sampabot.json)
 - Para se conectar as api's será necessário executar o código em python deste repositório, para isso faça:
   - Realizar o git clone do repositório

   ```bash
   $> git clone https://github.com/rdenadai/blip-botcamp2019.git
   ```

   - Feito isso, verifique se você tem python instalado no seu sistema operacional. Se for linux, provavelmente você possui, como usamos uma versão mais nova da linguagem sugiro instalar usando o [pyenv](https://github.com/pyenv/pyenv).
   No caso de Windows ou Mac, favor consultar respectivamente em [python.org](https://www.python.org/)

   - Caso queria você pode criar seu próprio endpoint... fique a vontade! ;)

   - Tendo o python instalado é só executar os comandos:

   ```bash
   $> pip install virtualenv
   $> virtualenv venv
   $> source venv/bin/activate
   $> pip install -r requirements.txt
   $> gunicorn application:app --reload -b 0.0.0.0:8080 -w 4 -k uvicorn.workers.UvicornWorker
   ```

   - Seu serviço estará sendo executado no computar na porta 8080.

   - Minha sugestão é subir no [heroku](https://heroku.com)

   - Pronto, você pode testar o chatbot.
