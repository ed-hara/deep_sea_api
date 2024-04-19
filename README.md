PUC-Rio: DESENVOLVIMENTO FULL STACK BASICO

SPRINT 1

Este projeto tem o intuito de apresentar o MVP para sistema de demanda da minha empresa, onde cadastramos os navios atendidos, inserindo suas características, prospects de chegada, atracação e saida, serviços a serem realizados na estadia e emails de contato. A idéia é desenvolver o sistema para adequação na rotina interna da empresa que envolve check list operacional e automação de emails para clientes.


## Para executar a aplicação, segue um breve passo a passo

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), evitando instalar libs diretamente no sistema operacional, que pode criar conflitos de versões.

```
No arquivo requirements.txt, estão listadas as bibliotecas necessárias para rodar a aplicação. Após instalação (python3 -m venv nome_do_ambiente_virtual) e ativação da máquina virtual (source nome_do_ambiente_virtual/bin/activate) para linux e (nome_do_ambiente_virtual\Scripts\Activate) para windows, deve-se utilizar o seguinte comando para instalar as bibliotecas: 

(env)$ pip install -r requirements.txt
```

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
