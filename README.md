# MLI-Knot Keyboard

**MLI-Knot Keyboard** is a small local Windows desktop app that simulates controlled keyboard typing into a field manually selected by the user.

It was created for legitimate situations where a form or desktop field does not accept paste input, but still accepts normal keyboard typing. The user remains in control: open the target app or website manually, click the destination field, start the countdown, and the app types the provided text character by character.

> Current public release: **v0.1.0**

---

## Download for Windows

For normal use, you do **not** need to install Python or build anything.

1. Open the repository **Releases** page.
2. Download the latest Windows release asset, usually named something like:
   - `MLI-Knot-keyboard-windows.zip`; or
   - `MLI-Knot-keyboard.exe`.
3. If you downloaded the `.zip`, extract it.
4. Run `MLI-Knot-keyboard.exe`.

Release page:

```text
https://github.com/proftectiagocosta-hash/MLI-Knot-keyboard/releases
```

Because this executable is generated with PyInstaller and is not digitally signed yet, Windows may show a security warning on first run. This is common for new unsigned executables. Only run files downloaded from the official repository release page.

---

## What the app does

- Provides a simple Tkinter interface.
- Lets the user type or paste text into a multiline text box.
- Waits for a configurable countdown before typing starts.
- Gives the user time to click the target field manually.
- Types the text character by character.
- Supports accented Unicode characters on Windows, such as `ç`, `á`, `ã`, `é`, `ê`, `ó`, `õ`, `ú`.
- Includes a Portuguese/English interface toggle.
- Includes a quick test button.
- Includes visible status logs.
- Includes safe cancellation options.

---

## How to use

1. Open `MLI-Knot-keyboard.exe`.
2. Paste or type the text into the app.
3. Set the initial delay.
4. Set the interval between characters.
5. Click **Start typing** / **Iniciar digitação**.
6. During the countdown, click the target field where the text should be typed.
7. Wait for the typing to finish.

Recommended first test:

```text
abc123 ação maçã órgão útil você não
```

Test it first in Notepad before using it in another app or website.

---

## How to cancel

You can stop the process safely by:

- clicking the **Cancel** / **Cancelar** button;
- pressing `ESC` while the app window is focused;
- moving the mouse quickly to the upper-left corner of the screen to trigger PyAutoGUI failsafe.

Important: after you click the destination field, the app window may lose focus. In that case, the most reliable emergency stop is the PyAutoGUI failsafe: move the mouse to the upper-left corner of the screen.

---

## Responsible use

This tool is intended for legitimate personal, educational, accessibility, testing, and productivity workflows.

Use it only in systems and fields where you have permission to enter data.

Do **not** use this project for:

- spam;
- abuse;
- captcha bypass;
- login bypass;
- fraud;
- anti-fraud evasion;
- security control evasion;
- unauthorized automation.

MLI-Knot Keyboard:

- is not a keylogger;
- does not capture global keyboard input;
- does not capture passwords;
- does not run hidden in the background;
- does not send data to the internet;
- does not scrape browsers;
- does not bypass captcha, login, authentication, anti-fraud, or security controls;
- only types into the field manually selected by the user.

---

## Limitations

- The target field must be focused manually by the user.
- Some remote desktops, virtual machines, elevated windows, protected applications, or highly restricted web fields may block synthetic keyboard events.
- The app does not verify what text was received by the destination field.
- Non-Windows Unicode behavior depends on PyAutoGUI, keyboard layout, and the desktop environment.

---

## For developers

Use this section only if you want to run or build the project from source.

### Requirements

- Python 3.9 or newer.
- Tkinter available in your Python installation.
- Permission to control keyboard input on the local desktop.

### Clone the repository

```bash
git clone https://github.com/proftectiagocosta-hash/MLI-Knot-keyboard.git
cd MLI-Knot-keyboard
```

### Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install runtime dependencies

```bash
pip install -r requirements.txt
```

### Run from Python

```bash
python main.py
```

---

## Build the Windows executable

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

Build folders and generated executables are intentionally ignored by Git.

---

## GitHub Actions build

The repository includes a Windows workflow that can build the executable automatically.

To use it:

1. Open the repository on GitHub.
2. Go to **Actions**.
3. Select the Windows build workflow.
4. Click **Run workflow**.
5. Wait for a successful run.
6. Download the generated artifact from the run page.

Artifacts are temporary. For public distribution, publish the tested executable or ZIP file in **GitHub Releases**.

---

## Release procedure for maintainers

Recommended manual release flow:

1. Update the source code locally.
2. Test the app with Python.
3. Build the `.exe` locally or with GitHub Actions.
4. Test the generated `.exe` on Windows.
5. Commit and push all source/documentation changes.
6. Create a GitHub Release, for example `v0.1.0`, `v0.2.0`, etc.
7. Attach the tested Windows artifact, usually `MLI-Knot-keyboard-windows.zip` or `MLI-Knot-keyboard.exe`.
8. Add release notes.
9. Publish the release.

---

## Credits and attribution

MLI-Knot-keyboard was created by **Tiago Fernandes da Costa** (**@proftec.tiagocosta**).

If you use, redistribute, modify, or reference this project, please preserve proper credit to the original author.

See `NOTICE` and `CITATION.cff` for attribution metadata.

---

## License

Licensed under the **Apache License, Version 2.0**. See `LICENSE`.

---

# Português

**MLI-Knot Keyboard** é um pequeno app desktop local para Windows que simula digitação controlada em um campo selecionado manualmente pelo usuário.

Ele foi criado para situações legítimas em que um formulário ou campo não aceita colar texto, mas aceita digitação normal pelo teclado. O usuário continua no controle: abre o app ou site de destino manualmente, clica no campo desejado, inicia a contagem regressiva e o app digita o texto caractere por caractere.

> Versão pública atual: **v0.1.0**

---

## Baixar para Windows

Para uso normal, você **não precisa** instalar Python nem gerar executável.

1. Abra a página **Releases** do repositório.
2. Baixe o arquivo mais recente para Windows, normalmente com nome parecido com:
   - `MLI-Knot-keyboard-windows.zip`; ou
   - `MLI-Knot-keyboard.exe`.
3. Se baixou o `.zip`, extraia o arquivo.
4. Execute `MLI-Knot-keyboard.exe`.

Página de releases:

```text
https://github.com/proftectiagocosta-hash/MLI-Knot-keyboard/releases
```

Como o executável é gerado com PyInstaller e ainda não possui assinatura digital, o Windows pode exibir um aviso de segurança na primeira execução. Isso é comum em executáveis novos e não assinados. Execute apenas arquivos baixados da página oficial de releases do repositório.

---

## O que o app faz

- Oferece uma interface simples em Tkinter.
- Permite digitar ou colar texto em uma caixa multilinha.
- Aguarda uma contagem regressiva configurável antes de iniciar.
- Dá tempo para o usuário clicar manualmente no campo de destino.
- Digita o texto caractere por caractere.
- Suporta caracteres Unicode acentuados no Windows, como `ç`, `á`, `ã`, `é`, `ê`, `ó`, `õ`, `ú`.
- Possui alternância de interface entre Português e Inglês.
- Possui botão de teste rápido.
- Exibe logs de status.
- Possui opções seguras de cancelamento.

---

## Como usar

1. Abra `MLI-Knot-keyboard.exe`.
2. Cole ou digite o texto no app.
3. Configure o atraso inicial.
4. Configure o intervalo entre caracteres.
5. Clique em **Iniciar digitação** / **Start typing**.
6. Durante a contagem regressiva, clique no campo onde o texto deve ser digitado.
7. Aguarde a digitação terminar.

Texto recomendado para primeiro teste:

```text
abc123 ação maçã órgão útil você não
```

Teste primeiro no Bloco de Notas antes de usar em outro aplicativo ou site.

---

## Como cancelar

Você pode parar o processo com segurança de três formas:

- clicar no botão **Cancelar** / **Cancel**;
- pressionar `ESC` enquanto a janela do app estiver em foco;
- mover rapidamente o mouse para o canto superior esquerdo da tela para acionar o failsafe do PyAutoGUI.

Importante: depois que você clicar no campo de destino, a janela do app pode perder o foco. Nesse caso, a parada de emergência mais confiável é o failsafe do PyAutoGUI: mover o mouse para o canto superior esquerdo da tela.

---

## Uso responsável

Esta ferramenta é destinada a fluxos legítimos pessoais, educacionais, de acessibilidade, teste e produtividade.

Use apenas em sistemas e campos nos quais você tem permissão para inserir dados.

Não use este projeto para:

- spam;
- abuso;
- burlar captcha;
- burlar login;
- fraude;
- evasão antifraude;
- evasão de controles de segurança;
- automação não autorizada.

MLI-Knot Keyboard:

- não é keylogger;
- não captura teclado global;
- não captura senhas;
- não roda escondido em segundo plano;
- não envia dados para a internet;
- não acessa navegador por scraping;
- não burla captcha, login, autenticação, antifraude ou controles de segurança;
- apenas digita no campo selecionado manualmente pelo usuário.

---

## Limitações

- O campo de destino precisa ser focado manualmente pelo usuário.
- Alguns desktops remotos, máquinas virtuais, janelas elevadas, aplicativos protegidos ou campos web muito restritos podem bloquear eventos sintéticos de teclado.
- O app não verifica qual texto foi recebido pelo campo de destino.
- Em sistemas não Windows, o comportamento Unicode depende do PyAutoGUI, do layout de teclado e do ambiente gráfico.

---

## Para desenvolvedores

Use esta seção apenas se quiser rodar ou gerar o projeto a partir do código-fonte.

### Requisitos

- Python 3.9 ou superior.
- Tkinter disponível na instalação do Python.
- Permissão para controlar entrada de teclado no desktop local.

### Clonar o repositório

```bash
git clone https://github.com/proftectiagocosta-hash/MLI-Knot-keyboard.git
cd MLI-Knot-keyboard
```

### Criar e ativar ambiente virtual

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar dependências de execução

```bash
pip install -r requirements.txt
```

### Rodar via Python

```bash
python main.py
```

---

## Gerar o executável para Windows

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

O executável final é gerado em:

```text
dist/MLI-Knot-keyboard.exe
```

As pastas de build e os executáveis gerados são ignorados intencionalmente pelo Git.

---

## Build pelo GitHub Actions

O repositório possui um workflow Windows que pode gerar o executável automaticamente.

Para usar:

1. Abra o repositório no GitHub.
2. Entre em **Actions**.
3. Selecione o workflow de build Windows.
4. Clique em **Run workflow**.
5. Aguarde uma execução bem-sucedida.
6. Baixe o artifact gerado na página da execução.

Artifacts são temporários. Para distribuição pública, publique o executável ou ZIP testado em **GitHub Releases**.

---

## Procedimento de release para mantenedores

Fluxo manual recomendado:

1. Atualize o código-fonte localmente.
2. Teste o app via Python.
3. Gere o `.exe` localmente ou pelo GitHub Actions.
4. Teste o `.exe` gerado no Windows.
5. Faça commit e push das alterações de código/documentação.
6. Crie uma GitHub Release, por exemplo `v0.1.0`, `v0.2.0`, etc.
7. Anexe o artifact testado para Windows, normalmente `MLI-Knot-keyboard-windows.zip` ou `MLI-Knot-keyboard.exe`.
8. Adicione as notas da versão.
9. Publique a release.

---

## Créditos e atribuição

MLI-Knot-keyboard foi criado por **Tiago Fernandes da Costa** (**@proftec.tiagocosta**).

Se você usar, redistribuir, modificar ou referenciar este projeto, preserve o crédito adequado ao autor original.

Veja `NOTICE` e `CITATION.cff` para metadados de atribuição.

---

## Licença

Licenciado sob a **Apache License, Version 2.0**. Veja `LICENSE`.
