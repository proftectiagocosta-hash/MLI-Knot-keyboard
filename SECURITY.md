# Security Policy / Política de Segurança

[English](#english) | [Português](#português)

---

## English

### Supported versions

Security fixes are evaluated for the latest public release and the current `main` branch.

| Version | Supported |
|---|---|
| Latest public release | Yes |
| Current `main` branch | Yes |
| Older releases | Best effort |
| Unofficial builds or modified copies | No |

### Official distribution

Download MLI-Knot Keyboard only from the official GitHub repository and its Releases page:

- repository: `proftectiagocosta-hash/MLI-Knot-keyboard`;
- release assets published by the repository maintainer.

The Windows executable may be unsigned. Windows can therefore display a reputation or security warning. A warning alone does not prove that a file is malicious, but users should not bypass warnings for files obtained from mirrors, third-party websites, messaging attachments, or unknown sources.

Before running a release asset:

1. confirm that it came from the official repository;
2. confirm that the release and file names match the published release notes;
3. scan the downloaded file with the security tools available on the system;
4. test new builds in a controlled environment when possible.

### Security model

MLI-Knot Keyboard is designed as a local desktop utility. Its documented behavior is to type user-provided text into a field manually selected by the user.

The official project is not intended to:

- capture global keyboard input;
- record passwords or clipboard history;
- run invisibly in the background;
- transmit typed content over the network;
- bypass authentication, captcha, anti-fraud, access-control, or security mechanisms;
- automate systems without the user's permission.

A report is security-relevant when observed behavior contradicts these boundaries or creates a realistic risk of unauthorized input, data exposure, persistence, code execution, artifact tampering, or unsafe distribution.

### Responsible use boundary

Use the application only on systems and input fields where you are authorized to enter data.

Reports requesting features or techniques for spam, credential entry, captcha bypass, login bypass, fraud, anti-fraud evasion, security-control evasion, or unauthorized automation are outside the supported security scope.

### Reporting a vulnerability

Do not publish sensitive technical details, proof-of-concept payloads, personal data, credentials, or exploitable step-by-step instructions in a public issue.

Use GitHub private vulnerability reporting when it is available for this repository. When it is unavailable, contact the maintainer through a private channel listed on the maintainer's GitHub profile.

Include only the information needed to investigate safely:

- affected version or commit;
- operating-system version;
- whether the official executable or source version was used;
- expected behavior;
- observed behavior;
- minimal reproduction steps;
- impact assessment;
- logs or screenshots with personal and sensitive data removed;
- whether the issue can cause unintended typing, data exposure, persistence, remote communication, or artifact substitution.

Do not attach real passwords, tokens, private documents, confidential text, or recordings containing sensitive information.

### Response process

After receiving a valid report, the maintainer will attempt to:

1. acknowledge the report;
2. reproduce and classify the issue;
3. identify affected versions and artifacts;
4. prepare a correction or mitigation when appropriate;
5. update documentation, releases, or distribution guidance;
6. disclose the issue publicly only after the relevant risk has been reduced.

No fixed response or remediation deadline is guaranteed. This project is independently maintained.

### Release and artifact concerns

Report suspected release tampering, unexpected executable behavior, mismatched release assets, or unofficial copies that claim to be official.

The maintainer cannot guarantee the safety or integrity of:

- binaries rebuilt by third parties;
- modified source copies;
- mirrors and repackaged downloads;
- files distributed outside the official repository;
- versions with removed safety controls.

### Security limitations

Synthetic keyboard input depends on the operating system, keyboard layout, focused application, permissions, remote-desktop environment, and security software. Some protected applications may block the input, while other applications may interpret it differently than expected.

The application cannot verify that the destination field received the intended text. Users should test with non-sensitive content and keep the cancellation mechanisms available.

---

## Português

### Versões suportadas

Correções de segurança são avaliadas para a versão pública mais recente e para o estado atual da branch `main`.

| Versão | Suporte |
|---|---|
| Versão pública mais recente | Sim |
| Branch `main` atual | Sim |
| Versões anteriores | Melhor esforço |
| Builds não oficiais ou cópias modificadas | Não |

### Distribuição oficial

Baixe o MLI-Knot Keyboard somente pelo repositório oficial no GitHub e pela página de Releases:

- repositório: `proftectiagocosta-hash/MLI-Knot-keyboard`;
- arquivos de release publicados pelo mantenedor do repositório.

O executável do Windows pode não possuir assinatura digital. Por isso, o Windows pode exibir um alerta de reputação ou segurança. O alerta, isoladamente, não comprova que o arquivo seja malicioso, mas o usuário não deve ignorar avisos para arquivos obtidos em espelhos, sites de terceiros, anexos de mensagens ou fontes desconhecidas.

Antes de executar um arquivo de release:

1. confirme que ele veio do repositório oficial;
2. confirme que o nome da release e do arquivo corresponde às notas publicadas;
3. examine o arquivo com as ferramentas de segurança disponíveis no sistema;
4. teste builds novos em ambiente controlado quando possível.

### Modelo de segurança

O MLI-Knot Keyboard foi projetado como uma ferramenta desktop local. Seu comportamento documentado é digitar um texto fornecido pelo usuário em um campo selecionado manualmente pelo próprio usuário.

O projeto oficial não pretende:

- capturar globalmente a entrada do teclado;
- registrar senhas ou histórico da área de transferência;
- executar oculto em segundo plano;
- transmitir pela rede o conteúdo digitado;
- contornar autenticação, captcha, antifraude, controle de acesso ou mecanismos de segurança;
- automatizar sistemas sem autorização do usuário.

Um relato é relevante para segurança quando o comportamento observado contradiz esses limites ou cria risco realista de entrada não autorizada, exposição de dados, persistência, execução de código, adulteração de artefatos ou distribuição insegura.

### Limite de uso responsável

Utilize o aplicativo somente em sistemas e campos nos quais você esteja autorizado a inserir dados.

Solicitações de recursos ou técnicas voltadas a spam, entrada de credenciais, bypass de captcha, bypass de login, fraude, evasão antifraude, evasão de controles de segurança ou automação não autorizada estão fora do escopo de segurança suportado.

### Como relatar uma vulnerabilidade

Não publique em issue pública detalhes técnicos sensíveis, provas de conceito exploráveis, dados pessoais, credenciais ou instruções passo a passo que facilitem abuso.

Utilize o relato privado de vulnerabilidade do GitHub quando o recurso estiver disponível neste repositório. Caso não esteja disponível, contate o mantenedor por um canal privado indicado no perfil do mantenedor no GitHub.

Inclua apenas as informações necessárias para uma investigação segura:

- versão ou commit afetado;
- versão do sistema operacional;
- indicação de uso do executável oficial ou da versão em código-fonte;
- comportamento esperado;
- comportamento observado;
- passos mínimos para reprodução;
- avaliação de impacto;
- logs ou capturas com dados pessoais e sensíveis removidos;
- indicação de possível digitação involuntária, exposição de dados, persistência, comunicação remota ou substituição de artefato.

Não anexe senhas reais, tokens, documentos privados, textos confidenciais ou gravações que contenham informações sensíveis.

### Processo de resposta

Após receber um relato válido, o mantenedor tentará:

1. confirmar o recebimento;
2. reproduzir e classificar o problema;
3. identificar versões e artefatos afetados;
4. preparar correção ou mitigação quando aplicável;
5. atualizar documentação, releases ou orientações de distribuição;
6. divulgar publicamente o problema somente depois que o risco relevante tiver sido reduzido.

Não há garantia de prazo fixo para resposta ou correção. Este projeto possui manutenção independente.

### Releases e artefatos

Relate suspeitas de adulteração de release, comportamento inesperado do executável, divergência entre arquivos publicados ou cópias não oficiais que se apresentem como oficiais.

O mantenedor não pode garantir segurança ou integridade de:

- binários recompilados por terceiros;
- cópias modificadas do código-fonte;
- espelhos e downloads reempacotados;
- arquivos distribuídos fora do repositório oficial;
- versões com mecanismos de segurança removidos.

### Limitações de segurança

A entrada sintética de teclado depende do sistema operacional, layout do teclado, aplicativo em foco, permissões, ambiente de acesso remoto e software de segurança. Alguns aplicativos protegidos podem bloquear a entrada, enquanto outros podem interpretá-la de forma diferente da esperada.

O aplicativo não consegue confirmar se o campo de destino recebeu o texto pretendido. Teste primeiro com conteúdo não sensível e mantenha disponíveis os mecanismos de cancelamento.
