# 🌐 Curso: Arquitetura de IoT (Internet das Coisas)

Este documento contém o planejamento pedagógico e técnico para as aulas de arquitetura de sistemas conectados.

---

## 📖 1. Conteúdo Programático
- **Fundamentos de IoT:** Sensores, atuadores e o ciclo de vida do dado.
- **Camadas de Arquitetura:**
  - *Percepção:* Sensores e hardware (Arduino).
  - *Rede:* Protocolos de comunicação (MQTT, HTTP, Serial).
  - *Aplicação:* Processamento e dashboards (Python).
- **Edge Computing:** Processamento local vs. nuvem.

---

## 🛠️ 2. Hardware: Ecossistema Arduino
O foco será a interface com o mundo físico através de microcontroladores.
- **Pinagem (GPIO):** Entradas e saídas digitais e analógicas.
- **Protocolos de Comunicação:** I2C, SPI e UART (Serial).
- **Componentes:** Leitura de sensores (LDR, DHT11) e controle de carga (Relés/LEDs).

---

## 💻 3. Desenvolvimento em C++ (Firmware)
A programação de baixo nível para o Arduino foca em eficiência e controle direto de hardware.
- **Estrutura Base:** `void setup()` e `void loop()`.
- **Lógica de Controle:**
  - Manipulação de interrupções.
  - Temporização sem travamento (`millis()` em vez de `delay()`).
  - Bibliotecas de sensores (`.h` e `.cpp`).

---

## 🐍 4. Programação em Python (Integração e Dados)
O Python atuará como o cérebro da camada superior (Gateway ou Servidor).
- **Comunicação Serial:** Uso da biblioteca `PySerial` para ler dados do Arduino.
- **Protocolos IoT:**
  - Envio de dados para a nuvem via **MQTT** (Paho-MQTT).
  - Criação de APIs simples com Flask/FastAPI para controle remoto.
- **Tratamento de Dados:** Armazenamento em arquivos `.csv` ou bancos de dados (SQLite).

---

## 🚀 5. Exercício Prático Proposto
**Projeto: Monitoramento e Alerta Remoto**
1. **Arduino (C++):** Lê um sensor de temperatura e envia o valor pela porta Serial.
2. **Python:** Monitora a porta Serial em tempo real. Se a temperatura ultrapassar um limite, o Python envia um alerta (e-mail ou log) e comanda o Arduino a ligar um cooler.

---
*Documento gerado para fins educacionais.*
