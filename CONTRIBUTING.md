# Contributing / Contribuindo

[English](#english) | [Português](#português)

Thank you for considering a contribution to MLI-Knot Keyboard.

Obrigado por considerar uma contribuição para o MLI-Knot Keyboard.

---

## English

### Project boundary

MLI-Knot Keyboard is a small local Windows desktop application that types user-provided text into a field manually selected by the user.

Contributions must preserve the project's documented boundaries:

- local and visible operation;
- explicit user control;
- safe cancellation;
- no hidden background behavior;
- no credential capture;
- no network transmission of typed content;
- no captcha, login, anti-fraud, access-control, or security-control bypass;
- no unauthorized automation, spam, abuse, or fraud support.

Proposals that weaken these boundaries may be rejected even when technically possible.

### Choose the correct report type

#### Bug report

Use a bug report when the current application behaves differently from its documented behavior.

Include:

- application version or commit;
- Windows version;
- whether you used the official release executable or ran from source;
- source of the downloaded executable, when applicable;
- keyboard layout and interface language;
- exact steps to reproduce;
- expected behavior;
- observed behavior;
- whether the problem also occurs in Notepad;
- sanitized logs, screenshots, or sample text when useful.

Before reporting a typing problem, test with non-sensitive text in Notepad. This helps distinguish an application issue from restrictions imposed by a browser, remote desktop, virtual machine, elevated window, or protected field.

#### Feature request

Use a feature request for a new capability or an intentional behavior change.

Explain:

- the user problem;
- the proposed behavior;
- why it fits the local, visible, user-controlled security model;
- possible safety or accessibility effects;
- how the feature could be tested.

Do not request features intended for spam, bulk account actions, credential entry, captcha bypass, login bypass, fraud, anti-fraud evasion, security-control evasion, or automation without authorization.

#### Security report

Do not publish vulnerability details, credentials, personal data, or exploitable instructions in a public issue.

Follow [`SECURITY.md`](SECURITY.md) for responsible private reporting.

### Protect private and sensitive information

Never include real passwords, tokens, API keys, confidential text, private documents, customer information, personal conversations, or data copied from a protected destination field.

When demonstrating a problem:

- use fictional or synthetic text;
- remove names, email addresses, account identifiers, paths, and notifications;
- sanitize screenshots and logs;
- avoid recordings that expose other applications or private desktop content;
- verify filenames and metadata before attaching files.

### Development setup

Use the setup documented in `README.md`.

Typical source workflow:

```bash
python -m venv .venv
pip install -r requirements.txt
python main.py
```

Development and packaging dependencies may be installed from `requirements-dev.txt` when needed.

Do not commit virtual environments, generated executables, build directories, temporary files, caches, or local editor configuration unless the repository explicitly tracks them.

### Branches and commits

Create a focused branch from the current `main` branch.

Recommended branch examples:

```text
fix/unicode-typing
fix/cancel-behavior
docs/windows-build
feature/accessibility-status
```

Keep commits intentional and readable. Each commit should represent one coherent change and should not mix unrelated formatting, refactoring, documentation, dependency, and functional work.

### Pull request scope

Prefer small pull requests with one clear purpose.

A pull request should explain:

- what changed;
- why the change is needed;
- user-visible effects;
- safety implications;
- files or subsystems affected;
- tests performed;
- known limitations or untested environments.

Avoid unrelated cleanup. Do not silently expand the scope after review has started.

### Required validation

Run the checks relevant to the change. At minimum, confirm that the application still opens and that the changed behavior works as described.

For changes affecting typing or cancellation, test where applicable:

1. ordinary ASCII text in Notepad;
2. accented Unicode text such as `ação, maçã, órgão, útil`;
3. initial countdown behavior;
4. character interval behavior;
5. Cancel button;
6. `ESC` while the application window is focused;
7. PyAutoGUI upper-left-corner failsafe;
8. Portuguese and English interface modes;
9. empty-input and invalid-setting behavior;
10. application recovery after cancellation or an error.

Never perform tests with real credentials or confidential content.

If a test could not be performed, state that limitation in the pull request instead of presenting it as completed.

### Generated files and releases

Do not commit:

- `dist/` or `build/` directories;
- generated `.exe` or `.zip` files;
- PyInstaller temporary output;
- local logs or crash dumps containing private information;
- unofficial release artifacts.

Release assets are published separately through the repository's official Releases process after review and testing.

### Dependencies and workflows

Changes to dependencies, packaging, permissions, or GitHub Actions require a clear justification.

For dependency changes, describe:

- why the dependency is needed;
- whether it is runtime or development-only;
- its effect on package size and build behavior;
- relevant licensing or security considerations;
- how the change was validated.

Avoid granting workflow permissions beyond the minimum needed.

### Documentation and language

Keep documentation accurate and consistent with actual behavior. Do not claim that a feature, test, release, signature, security guarantee, or platform support exists unless it has been confirmed.

This repository supports Portuguese and English documentation and interface text. When changing user-visible wording, keep both languages aligned when the corresponding translation exists.

### License and attribution

By submitting a contribution, you agree that your contribution may be distributed under the repository's Apache License 2.0.

Preserve existing copyright, license, notice, and attribution information. Do not add third-party code, media, or text unless its license permits inclusion and the required attribution is documented.

### Review expectations

Submission does not guarantee acceptance, inclusion in a release, or a fixed review deadline.

A contribution may be revised or declined because of scope, maintainability, safety, licensing, compatibility, testing, or project-direction concerns.

---

## Português

### Limite do projeto

O MLI-Knot Keyboard é um pequeno aplicativo desktop local para Windows que digita um texto fornecido pelo usuário em um campo selecionado manualmente pelo próprio usuário.

As contribuições devem preservar os limites documentados do projeto:

- operação local e visível;
- controle explícito do usuário;
- cancelamento seguro;
- ausência de execução oculta em segundo plano;
- ausência de captura de credenciais;
- ausência de transmissão pela rede do conteúdo digitado;
- ausência de bypass de captcha, login, antifraude, controle de acesso ou mecanismos de segurança;
- ausência de automação não autorizada, spam, abuso ou suporte a fraude.

Propostas que enfraqueçam esses limites podem ser rejeitadas mesmo quando forem tecnicamente possíveis.

### Escolha o tipo correto de relato

#### Relato de bug

Utilize um relato de bug quando o aplicativo atual se comportar de forma diferente do que está documentado.

Inclua:

- versão do aplicativo ou commit;
- versão do Windows;
- indicação de uso do executável oficial ou execução pelo código-fonte;
- origem do executável baixado, quando aplicável;
- layout do teclado e idioma da interface;
- passos exatos para reprodução;
- comportamento esperado;
- comportamento observado;
- indicação se o problema também ocorre no Bloco de Notas;
- logs, capturas ou texto de exemplo sanitizados quando forem úteis.

Antes de relatar um problema de digitação, teste com texto não sensível no Bloco de Notas. Isso ajuda a separar um problema do aplicativo de restrições impostas por navegador, acesso remoto, máquina virtual, janela elevada ou campo protegido.

#### Solicitação de recurso

Utilize uma solicitação de recurso para uma nova capacidade ou mudança intencional de comportamento.

Explique:

- o problema do usuário;
- o comportamento proposto;
- por que ele respeita o modelo de segurança local, visível e controlado pelo usuário;
- possíveis efeitos sobre segurança ou acessibilidade;
- como a funcionalidade poderia ser testada.

Não solicite recursos destinados a spam, ações em massa sobre contas, inserção de credenciais, bypass de captcha, bypass de login, fraude, evasão antifraude, evasão de controles de segurança ou automação sem autorização.

#### Relato de segurança

Não publique em issue pública detalhes de vulnerabilidade, credenciais, dados pessoais ou instruções exploráveis.

Siga o arquivo [`SECURITY.md`](SECURITY.md) para realizar um relato privado e responsável.

### Proteja informações privadas e sensíveis

Nunca inclua senhas reais, tokens, chaves de API, textos confidenciais, documentos privados, informações de clientes, conversas pessoais ou dados copiados de um campo protegido.

Ao demonstrar um problema:

- use texto fictício ou sintético;
- remova nomes, e-mails, identificadores de conta, caminhos e notificações;
- sanitize capturas e logs;
- evite gravações que exponham outros aplicativos ou conteúdo privado da área de trabalho;
- verifique nomes de arquivos e metadados antes de anexar arquivos.

### Ambiente de desenvolvimento

Utilize a configuração documentada no `README.md`.

Fluxo típico pelo código-fonte:

```bash
python -m venv .venv
pip install -r requirements.txt
python main.py
```

Dependências de desenvolvimento e empacotamento podem ser instaladas pelo `requirements-dev.txt` quando necessário.

Não faça commit de ambientes virtuais, executáveis gerados, diretórios de build, arquivos temporários, caches ou configurações locais do editor, exceto quando o repositório os rastrear explicitamente.

### Branches e commits

Crie uma branch focada a partir do estado atual da `main`.

Exemplos recomendados:

```text
fix/unicode-typing
fix/cancel-behavior
docs/windows-build
feature/accessibility-status
```

Mantenha os commits intencionais e legíveis. Cada commit deve representar uma mudança coerente e não deve misturar formatação, refatoração, documentação, dependências e alterações funcionais sem relação entre si.

### Escopo do Pull Request

Prefira Pull Requests pequenos e com um único propósito claro.

O Pull Request deve explicar:

- o que mudou;
- por que a mudança é necessária;
- efeitos visíveis para o usuário;
- implicações de segurança;
- arquivos ou subsistemas afetados;
- testes realizados;
- limitações conhecidas ou ambientes não testados.

Evite limpezas não relacionadas. Não amplie silenciosamente o escopo depois que a revisão tiver começado.

### Validação necessária

Execute as verificações relevantes para a mudança. No mínimo, confirme que o aplicativo continua abrindo e que o comportamento alterado funciona conforme descrito.

Para mudanças relacionadas à digitação ou cancelamento, teste quando aplicável:

1. texto ASCII comum no Bloco de Notas;
2. texto Unicode acentuado, como `ação, maçã, órgão, útil`;
3. comportamento da contagem regressiva inicial;
4. intervalo entre caracteres;
5. botão Cancelar;
6. tecla `ESC` enquanto a janela do aplicativo estiver em foco;
7. failsafe do PyAutoGUI no canto superior esquerdo;
8. modos de interface em português e inglês;
9. comportamento com entrada vazia e configuração inválida;
10. recuperação do aplicativo após cancelamento ou erro.

Nunca execute testes com credenciais reais ou conteúdo confidencial.

Quando um teste não puder ser executado, declare essa limitação no Pull Request em vez de apresentá-lo como concluído.

### Arquivos gerados e releases

Não faça commit de:

- diretórios `dist/` ou `build/`;
- arquivos `.exe` ou `.zip` gerados;
- saídas temporárias do PyInstaller;
- logs locais ou dumps de falha com informações privadas;
- artefatos de release não oficiais.

Os arquivos de release são publicados separadamente pelo processo oficial de Releases do repositório depois de revisão e testes.

### Dependências e workflows

Mudanças em dependências, empacotamento, permissões ou GitHub Actions exigem justificativa clara.

Para alterações de dependências, descreva:

- por que a dependência é necessária;
- se ela é de execução ou apenas de desenvolvimento;
- efeito no tamanho do pacote e no comportamento do build;
- considerações relevantes de licença ou segurança;
- como a alteração foi validada.

Evite conceder aos workflows permissões além do mínimo necessário.

### Documentação e idioma

Mantenha a documentação correta e consistente com o comportamento real. Não afirme que uma funcionalidade, teste, release, assinatura, garantia de segurança ou suporte de plataforma existe sem confirmação.

Este repositório oferece documentação e textos de interface em português e inglês. Ao alterar textos visíveis ao usuário, mantenha os dois idiomas alinhados quando existir tradução correspondente.

### Licença e atribuição

Ao enviar uma contribuição, você concorda que ela poderá ser distribuída sob a licença Apache 2.0 do repositório.

Preserve informações existentes de direitos autorais, licença, aviso e atribuição. Não adicione código, mídia ou texto de terceiros sem que a licença permita a inclusão e sem documentar a atribuição necessária.

### Expectativas de revisão

O envio não garante aceitação, inclusão em release ou prazo fixo de revisão.

Uma contribuição pode ser revisada ou recusada por questões de escopo, manutenção, segurança, licença, compatibilidade, testes ou direção do projeto.
