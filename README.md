# 🧠 Classificação de Tipos de Vidro com MLP

Projeto desenvolvido na disciplina **Tópicos Avançados de Inteligência Artificial**.

## 📌 Objetivo

Construir um modelo de Machine Learning capaz de classificar diferentes tipos de vidro com base em suas propriedades químicas, utilizando uma rede neural do tipo MLP (Multilayer Perceptron).

---

## 📊 Dataset

- Nome: Glass Identification  
- Tipo de problema: Classificação multiclasse  
- Variável alvo (target): `Type`  
- Features: composição química (Na, Mg, Al, Si, Ca, etc)

O modelo recebe valores numéricos e prevê o tipo de vidro.

---

## ⚙️ Pipeline do Projeto

### 1. Pré-processamento
- Remoção de duplicatas (1 linha removida)  
- Verificação de valores ausentes (não encontrados)  
- Tratamento de outliers com Z-score (|Z| > 2)  
- Padronização com StandardScaler (média = 0, desvio = 1)  

---

### 2. Seleção de Variáveis
Métodos utilizados:
- Correlação de Pearson  
- Mutual Information  
- Random Forest  

Features finais:
Mg, Al, RI, K, Ca, Na  

---

### 3. Modelo MLP
- Camadas ocultas: (16, 8)  
- Função de ativação: ReLU  
- Learning rate: 0.001  

---

### 4. MLOps (Weights & Biases)

Utilizado para:
- Versionamento de dados  
- Registro de métricas por época  
- Armazenamento de hiperparâmetros  
- Salvamento do modelo  

Link:
https://wandb.ai/uchoastudies-ufrn/glass-ml-project  

---

## 📈 Resultados

- Acurácia: **0.62**  
- F1-score: **0.57**  

### Observações:
- Bom desempenho em classes maiores  
- Baixo desempenho em classes raras  
- Evidência de desbalanceamento  

---

## 📊 Interpretação

A matriz de confusão mostrou que o modelo:
- Acerta classes mais frequentes  
- Erra classes menores  
- Está enviesado  

---

## 📁 Estrutura

glass-ml-project/  
│  
├── data/  
├── models/  
├── src/  
├── notebooks/  
├── requirements.txt  
└── README.md  

---

## 🚀 Como Executar

1. Criar ambiente:
python -m venv .venv  

2. Ativar:
.venv\Scripts\activate  

3. Instalar:
pip install -r requirements.txt  

4. Rodar:
notebooks/analysis.ipynb  

---

## ⚠️ Limitações

- Dataset desbalanceado  
- Baixa performance em classes raras  

---

## 🔮 Trabalhos Futuros

- Balanceamento de dados  
- Testar outros modelos  
- Melhor ajuste de hiperparâmetros  

---

## 👤 Autor

Gabriel Samir Costa Uchôa Monteiro Oliveira