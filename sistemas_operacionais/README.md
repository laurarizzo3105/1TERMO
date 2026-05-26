# 🖥️ Sistemas Operacionais: Fundamentos e Linux

Este documento organiza os tópicos centrais sobre a gestão de hardware, software e as diferenças entre ecossistemas abertos e fechados.

---

## 📚 1. Conceitos Básicos
*O que é e para que serve um S.O.?*

- **Função do S.O.:** Ponte entre o hardware e o usuário (Gerenciamento de memória, processos e arquivos).
- **Kernel (Núcleo):** A parte do sistema que fala diretamente com o processador e memória.
- **Interface de Usuário:** Diferença entre **GUI** (Interface Gráfica) e **CLI** (Linha de Comando/Terminal).

---

## 🔐 2. Sistemas Operacionais: Abertos vs. Fechados
*Entendendo os modelos de licenciamento e desenvolvimento.*

- **Sistemas Fechados (Proprietários):**
  - Exemplos: Windows, macOS, iOS.
  - O código-fonte não é acessível ao público; restrições de modificação e redistribuição.
- **Sistemas Abertos (Open Source):**
  - Exemplos: Linux, Android (AOSP), FreeBSD.
  - Liberdade para estudar, modificar e distribuir o código.

---

## 🐧 3. O Ecossistema Linux e Distribuições
*Por que existem tantas versões de Linux?*

- **O que é o Linux:** Tecnicamente, Linux é apenas o **Kernel**. O sistema completo é chamado de GNU/Linux.
- **Distribuições (Distros):** São variações do sistema que combinam o Kernel com diferentes interfaces e ferramentas.
  - **Debian:** Uma das mais antigas e estáveis. Focada em software livre e robustez.
  - **Ubuntu:** Baseada no Debian, focada em facilidade de uso.
  - **CentOS/Fedora:** Focadas em ambientes corporativos e servidores.

---

## 🍥 4. Foco em Debian
*Explorando a base de muitos sistemas modernos.*

- **Estabilidade:** Versões *Stable*, *Testing* e *Unstable* (Sid).
- **Gerenciamento de Pacotes:** 
  - O uso do `apt` (Advanced Package Tool).
  - Comandos essenciais: `apt update`, `apt install`, `apt upgrade`.
- **Arquitetura:** Como o Debian organiza diretórios (`/etc` para configs, `/home` para usuários, `/bin` para executáveis).

---

## 🛠️ 5. Laboratório Prático: Primeiros Passos no Terminal
1. **Navegação:** `pwd`, `ls`, `cd`.
2. **Manipulação:** `mkdir`, `touch`, `cp`, `mv`.
3. **Permissões:** Entendendo o `sudo` (SuperUser Do) e o `chmod`.
4. **Informações do Sistema:** `top`, `df -h`, `uname -a`.

---
*Notas de Aula - Disciplina de Sistemas Operacionais*
