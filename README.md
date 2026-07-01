# MLI-Knot Keyboard

## English

MLI-Knot Keyboard is a small local Python/Tkinter app that simulates controlled human typing into a field manually selected by the user.

It is useful when a legitimate form or desktop field does not accept paste input. The user opens the target application or website manually, clicks the desired field, and then starts the app countdown. After the countdown, the app types the provided text character by character.

## Responsible Use

This tool is intended for legitimate personal, educational, accessibility, testing, and productivity workflows. Use it only in systems and fields where you have permission to enter data.

Do not use this project for spam, abuse, captcha bypass, login bypass, fraud, anti-fraud evasion, security control evasion, or any unauthorized automation.

## Features

- Simple Tkinter interface.
- Multiline text box for typing or pasting text.
- Initial delay before typing starts.
- Configurable interval between characters.
- Visible countdown and status log.
- Portuguese and English UI toggle.
- Quick test button using `abc123`.
- Safe cancellation with the Cancel button.
- `ESC` cancellation while the app window is focused.
- `pyautogui.FAILSAFE = True`, allowing abort by moving the mouse to the upper-left screen corner.
- Windows Unicode typing support for accented characters through `SendInput`.

## Safety Notes

MLI-Knot Keyboard:

- is not a keylogger;
- does not capture global keyboard input;
- does not capture passwords;
- does not run hidden in the background;
- does not send data to the internet;
- does not scrape browsers;
- does not bypass captcha, login, authentication, anti-fraud, or security controls;
- only types into the field manually selected by the user.

## Install from Python

Requirements:

- Python 3.9 or newer;
- Tkinter available in your Python installation;
- permission to control keyboard input on your local desktop.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install runtime dependencies:

```bash
pip install -r requirements.txt
```

## Run from Python

```bash
python main.py
```

## Build the Windows `.exe`

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Build manually with PyInstaller:

```bash
pyinstaller --noconfirm --clean --onefile --windowed --name MLI-Knot-keyboard main.py
```

Or run the helper script on Windows:

```bat
build_exe.bat
```

The final executable is generated at:

```text
dist/MLI-Knot-keyboard.exe
```

## Downloading the `.exe`

When GitHub Actions is enabled, the Windows build workflow uploads the executable as an artifact. Open the repository on GitHub, go to **Actions**, select a successful **Build Windows executable** run, and download the `MLI-Knot-keyboard-windows` artifact.

When the author publishes a release manually, the executable can also be downloaded from **GitHub Releases**.

## Publishing a Manual GitHub Release

1. Build the executable locally or download it from a successful Actions artifact.
2. Go to the GitHub repository page.
3. Open **Releases**.
4. Click **Draft a new release**.
5. Create a tag such as `v1.0.0`.
6. Attach `dist/MLI-Knot-keyboard.exe`.
7. Add release notes and publish.

## How to Cancel

You can cancel safely by:

- clicking the `Cancel` button;
- pressing `ESC` while the app window is focused;
- moving the mouse to the upper-left corner of the screen to trigger PyAutoGUI failsafe.

The app checks for cancellation before each character and during waits between characters.

## Windows Accents and Special Characters

On Windows, normal printable ASCII characters use PyAutoGUI. Accented and non-ASCII characters use Windows `SendInput` Unicode events through `ctypes`.

The app logs the Windows `INPUT` structure size before typing. On 64-bit Windows, the expected value is:

```text
Tamanho ctypes INPUT: 40
```

Test text for Notepad:

```text
abc123 ação maçã órgão útil você não
```

## Limitations

- The target field must be focused manually by the user.
- Some remote desktops, virtual machines, elevated windows, or protected applications may block synthetic keyboard events.
- Non-Windows Unicode behavior depends on PyAutoGUI, keyboard layout, and the desktop environment.
- The app does not verify what text was received by the destination field.

## Credits and Attribution

MLI-Knot-keyboard was created by Tiago Fernandes da Costa (@proftec.tiagocosta). If you use, redistribute, modify, or reference this project, please preserve proper credit to the original author.

See `NOTICE` and `CITATION.cff` for attribution metadata.

## License

Licensed under the Apache License, Version 2.0. See `LICENSE`.

---

## Português

MLI-Knot Keyboard é um pequeno app local em Python/Tkinter que simula digitação humana controlada em um campo selecionado manualmente pelo usuário.

Ele é útil quando um formulário ou campo legítimo não aceita colar texto. O usuário abre o aplicativo ou site manualmente, clica no campo desejado e inicia a contagem regressiva. Depois da contagem, o app digita o texto informado caractere por caractere.

## Uso Responsável

Esta ferramenta é destinada a fluxos legítimos pessoais, educacionais, de acessibilidade, teste e produtividade. Use apenas em sistemas e campos nos quais você tem permissão para inserir dados.

Não use este projeto para spam, abuso, burlar captcha, burlar login, fraude, evasão antifraude, evasão de controles de segurança ou qualquer automação não autorizada.

## Recursos

- Interface simples em Tkinter.
- Caixa multilinha para digitar ou colar texto.
- Atraso inicial antes da digitação.
- Intervalo configurável entre caracteres.
- Contagem e log de status visíveis.
- Alternância de idioma entre Português e Inglês.
- Botão de teste rápido usando `abc123`.
- Cancelamento seguro pelo botão Cancelar.
- Cancelamento por `ESC` enquanto a janela do app estiver em foco.
- `pyautogui.FAILSAFE = True`, permitindo abortar ao mover o mouse para o canto superior esquerdo da tela.
- Suporte a Unicode no Windows para caracteres acentuados via `SendInput`.

## Segurança

MLI-Knot Keyboard:

- não é keylogger;
- não captura teclado global;
- não captura senhas;
- não roda escondido em segundo plano;
- não envia dados para a internet;
- não acessa navegador por scraping;
- não burla captcha, login, autenticação, antifraude ou controles de segurança;
- apenas digita no campo selecionado manualmente pelo usuário.

## Instalação via Python

Requisitos:

- Python 3.9 ou superior;
- Tkinter disponível na instalação do Python;
- permissão para controlar entrada de teclado no desktop local.

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências de execução:

```bash
pip install -r requirements.txt
```

## Execução via Python

```bash
python main.py
```

## Gerar o `.exe` para Windows

Instale as dependências de desenvolvimento:

```bash
pip install -r requirements-dev.txt
```

Gere manualmente com PyInstaller:

```bash
pyinstaller --noconfirm --clean --onefile --windowed --name MLI-Knot-keyboard main.py
```

Ou execute o script auxiliar no Windows:

```bat
build_exe.bat
```

O executável final fica em:

```text
dist/MLI-Knot-keyboard.exe
```

## Baixar o `.exe`

Quando o GitHub Actions estiver habilitado, o workflow de Windows publica o executável como artifact. Abra o repositório no GitHub, entre em **Actions**, selecione uma execução bem-sucedida de **Build Windows executable** e baixe o artifact `MLI-Knot-keyboard-windows`.

Quando o autor publicar uma release manualmente, o executável também poderá ser baixado em **GitHub Releases**.

## Publicar uma Release Manual no GitHub

1. Gere o executável localmente ou baixe o artifact de uma execução bem-sucedida do Actions.
2. Abra a página do repositório no GitHub.
3. Entre em **Releases**.
4. Clique em **Draft a new release**.
5. Crie uma tag, por exemplo `v1.0.0`.
6. Anexe `dist/MLI-Knot-keyboard.exe`.
7. Adicione notas da versão e publique.

## Como Cancelar

Você pode cancelar com segurança de três formas:

- clicar no botão `Cancelar`;
- pressionar `ESC` enquanto a janela do app estiver em foco;
- mover o mouse para o canto superior esquerdo da tela para acionar o failsafe do PyAutoGUI.

O app verifica o cancelamento antes de cada caractere e durante as pausas entre caracteres.

## Acentos e Caracteres Especiais no Windows

No Windows, caracteres ASCII imprimíveis usam PyAutoGUI. Caracteres acentuados e não ASCII usam eventos Unicode do Windows via `SendInput` com `ctypes`.

Antes de digitar, o app registra o tamanho da estrutura `INPUT`. Em Windows 64-bit, o valor esperado é:

```text
Tamanho ctypes INPUT: 40
```

Texto de teste no Bloco de Notas:

```text
abc123 ação maçã órgão útil você não
```

## Limitações

- O campo de destino precisa ser focado manualmente pelo usuário.
- Alguns desktops remotos, máquinas virtuais, janelas elevadas ou aplicativos protegidos podem bloquear eventos sintéticos de teclado.
- Em sistemas não Windows, o comportamento Unicode depende do PyAutoGUI, do layout de teclado e do ambiente gráfico.
- O app não verifica qual texto foi recebido pelo campo de destino.

## Créditos e Atribuição

MLI-Knot-keyboard foi criado por Tiago Fernandes da Costa (@proftec.tiagocosta). Se você usar, redistribuir, modificar ou referenciar este projeto, preserve o crédito adequado ao autor original.

Veja `NOTICE` e `CITATION.cff` para metadados de atribuição.

## Licença

Licenciado sob a Apache License, Version 2.0. Veja `LICENSE`.
