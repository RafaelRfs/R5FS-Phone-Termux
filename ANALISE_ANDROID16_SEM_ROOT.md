# Análise de compatibilidade (Android 16 + Termux sem root)

## Resumo executivo

Este repositório foi projetado para um cenário antigo (Android 6 + Termux com root/`su`) e depende fortemente de:

- `su -c` e escrita direta em caminhos internos do app (`/data/data/com.termux/...`);
- Python 2 (`python2`, `raw_input`, `urllib2`, `xrange`, `Queue`);
- versões antigas/fixas de ferramentas (ex.: Metasploit 4.14.28);
- pacotes que mudaram de nome ou foram removidos nos repositórios atuais do Termux.

No estado atual, a instalação "como está" **não é compatível** com Android 16 sem root. Parte dos scripts ainda possui sintaxe válida de shell, mas o fluxo de instalação e execução principal falha por dependências e premissas desatualizadas.

---

## O que ainda funciona (parcialmente)

1. **Sintaxe dos scripts `.sh`**
   - Todos os scripts shell da raiz passaram em validação sintática via `bash -n`.

2. **Parte dos arquivos Python compila em Python 3**
   - Alguns scripts compilam com `py_compile` em Python 3 (`adminFinder2.py`, `bruteforceForm.py`, `client.py`, `downloader.py`, `network.py`, `network-nmap.py`, `server.py`, `ShowDb.py`, `ShowDbLocal.py`).
   - Isso indica que há código que pode ser migrado com esforço moderado, apesar de ainda quebrar em runtime por APIs Python 2 e dependências ausentes.

---

## O que não funciona mais (ou está quebrado no cenário atual)

### 1) Fluxo de instalação exige root e comandos obsoletos

- `Setup.sh` usa `su -c`, `tsu` e move arquivos para `/data/data/com.termux/files/usr/bin`, padrão incompatível com ambiente não-root moderno.
- `aptInstallPhoneHacker.sh`, `aptInstallBin.sh`, `aptInstallMetasploit.sh`, `aptInstallSudoNgrok.sh`, `initPstServer.sh` também dependem de `su -c`.

### 2) Dependência direta de Python 2

- Wrappers executáveis chamam `python2` explicitamente (`Client`, `Server`, `network`, `mit`).
- Scripts usam construções Python 2 (`raw_input`, `urllib2`, `Queue`, `xrange`, sintaxe `except Exception,e`, `print` sem parênteses).
- No ambiente atual, `python2` não está disponível por padrão e vários scripts quebram com Python 3 sem adaptação.

### 3) Evidência prática de falha em runtime

- `python3 network.py 127 1` falha em `xrange`.
- `python3 adminFinder2.py --help` falha por `urllib2`.
- `python3 server.py` falha sem `scapy` instalado e ainda contém `raw_input`, incompatível com Python 3.

### 4) Lista de pacotes desatualizada

- `aptInstallApps.sh` solicita pacotes legados como `python`, `python-dev`, `python2`, `python2-dev`, além de combinações que mudaram ao longo do tempo no Termux.
- Scripts de Metasploit fixam versão muito antiga (`4.14.28`) e cadeia de gems rigidamente pinada, com alta chance de incompatibilidade hoje.

### 5) Funcionalidades que dependem de root deixaram de ser viáveis

- Leitura de chaves Wi-Fi (`/data/misc/wifi/*.conf`) exige root (`wifi.sh` / `showifi`).
- Cópias/escritas em áreas internas do Termux via `su -c` não são válidas no modelo atual sem root.

---

## Classificação por status (Android 16 sem root)

- **Funciona**
  - Validação sintática dos `.sh`.

- **Funciona com ajustes mínimos**
  - Scripts Python já quase em Python 3, mas que precisam apenas corrigir APIs antigas e dependências.

- **Não funciona sem refatoração**
  - Instalador principal (`Setup.sh` + cadeia `aptInstall*.sh`).
  - Wrappers que chamam `python2`.
  - Tooling legado de Metasploit/Gems fixos.

- **Não funciona sem root (por design)**
  - Leitura de arquivos privados de Wi-Fi e operações em paths privilegiados via `su`.

---

## Plano de modernização recomendado

1. **Remover raiz do problema (root)**
   - Eliminar `su -c` e `tsu`.
   - Substituir cópia para `/data/data/com.termux/files/usr/bin` por instalação em `$PREFIX/bin` com permissões do usuário atual.

2. **Migrar 100% para Python 3**
   - Trocar `raw_input` → `input`, `urllib2` → `urllib.request`/`requests`, `Queue` → `queue`, `xrange` → `range`, sintaxe antiga de `except` e `print`.
   - Revisar operações de `socket` para `bytes`/`str` em Python 3.

3. **Atualizar instalação de dependências**
   - Revisar `aptInstallApps.sh` para pacotes válidos atuais do Termux.
   - Trocar `pip` legado por `python -m pip`.

4. **Reescrever wrappers de comandos**
   - `Client`, `Server`, `network`, `mit`, etc. para chamar `python3` e paths robustos.

5. **Separar features impossíveis sem root**
   - Marcar explicitamente (ou remover) módulos que dependem de acesso privilegiado (ex.: chaves Wi-Fi).

6. **Documentar nova matriz de suporte**
   - Ex.: "Suportado: Android 12+ sem root (Termux atual), Python 3.11+, sem leitura de dados privados do sistema".

---

## Conclusão

O projeto preserva valor histórico e parte da base pode ser reaproveitada, mas o instalador e vários fluxos críticos estão acoplados ao ecossistema antigo (Android 6 + root + Python 2). Para Android 16 sem root, o caminho viável é uma **modernização estruturada** (instalação, wrappers, Python 3 e escopo funcional sem privilégios).
