# MLI-Knot-keyboard

Ferramenta local simples, em Python, para simular digitação humana em um campo já selecionado pelo usuário.

## Objetivo

Alguns sites ou sistemas não aceitam copiar e colar em determinados campos. Com esta ferramenta, o usuário abre o site manualmente, clica no campo desejado e executa a automação para digitar o texto informado como se fosse pelo teclado.

A versão atual usa uma interface gráfica em Tkinter para evitar problemas de codificação do terminal com caracteres acentuados.

## Árvore de arquivos

```text
MLI-Knot-keyboard/
|-- README.md
|-- requirements.txt
|-- main.py
|-- ui.py
|-- keyboard_simulator.py
`-- config.py
```

## Instalação

Requisitos:

- Python 3.9 ou superior
- Tkinter disponível na instalação do Python
- Ambiente local com permissão para controlar teclado

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Uso rápido

1. Execute `python main.py`.
2. Digite ou cole o texto na caixa multilinha.
3. Configure o atraso inicial, em segundos.
4. Configure o intervalo entre caracteres, em segundos.
5. Clique em `Iniciar digitação`.
6. Confirme o início na janela de confirmação.
7. Durante a contagem regressiva, clique no campo de destino.
8. Aguarde a digitação automática terminar.

A janela mostra a instrução: “Após clicar em iniciar, selecione o campo de destino antes da contagem terminar”.

## Como cancelar

Você pode cancelar com segurança de três formas:

- Clique no botão `Cancelar`.
- Pressione `ESC` enquanto a janela do app estiver em foco.
- Mova o mouse para o canto superior esquerdo da tela para acionar o `pyautogui.FAILSAFE`.

O programa verifica o sinal de cancelamento antes de cada caractere e também durante a espera entre caracteres.

## Acentos e caracteres especiais

A entrada principal agora é feita em uma caixa de texto Tkinter, não pelo terminal. Isso evita os problemas comuns do PowerShell com caracteres como `ç`, `á`, `ã`, `é`, `ê`, `í`, `ó`, `õ` e `ú`.

No Windows, a digitação usa eventos Unicode do sistema para preservar caracteres acentuados caractere por caractere. Em outros sistemas, a ferramenta usa o método de escrita do PyAutoGUI, que pode depender do layout de teclado e do suporte do ambiente gráfico.

## Observações de segurança

Esta ferramenta:

- não cria keylogger;
- não captura teclas digitadas pelo usuário;
- não captura senhas;
- não roda escondida em segundo plano;
- não acessa navegador por scraping;
- não tenta burlar captcha, login, autenticação, bloqueios de segurança ou mecanismos antiabuso;
- não envia dados para a internet;
- exige confirmação manual antes da digitação iniciar;
- apenas digita no campo que o usuário selecionou manualmente.

Use apenas em campos e sistemas nos quais você tem permissão para inserir dados.
