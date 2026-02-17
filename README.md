# 📝 Gerenciador de Tarefas Simples (CLI)

Este é um projeto em **Python** que implementa um sistema básico de lista de tarefas (To-Do List) operando via linha de comando. É uma ferramenta prática para organizar atividades rápidas durante o dia.

---

## 🚀 Funcionalidades

O script oferece um menu interativo com as seguintes opções:

1.  **Adicionar Tarefa:** Insere uma nova string à lista de afazeres.
2.  **Remover Tarefa:** Exibe a lista numerada e permite excluir um item específico pelo seu índice.
3.  **Listar Tarefas:** Exibe todas as tarefas pendentes de forma organizada.
4.  **Sair:** Encerra a execução do loop e do programa.



---

## 🛠️ Tecnologias e Conceitos Utilizados

Para construir este projeto, foram aplicados conceitos fundamentais de programação:

* **Estruturas de Repetição:** Uso do `while True` para manter o menu ativo.
* **Estruturas Condicionais:** `if/elif/else` para processar a escolha do usuário.
* **Manipulação de Listas:** Métodos como `.append()` para adicionar e `.pop()` para remover elementos.
* **Funções Integradas:** `input()`, `print()` e `enumerate()` para indexação.

---

## 📖 Como Usar

### Pré-requisitos
* Possuir o **Python 3.x** instalado.

### Execução
1.  Abra o seu terminal ou prompt de comando.
2.  Navegue até a pasta onde está o arquivo (ex: `main.py`).
3.  Execute o comando:
    ```bash
    python main.py
    ```

---

## 📋 Regras de Negócio

O código possui verificações simples para evitar erros de execução:
* **Validação de Lista Vazia:** Se você tentar listar ou remover tarefas sem ter adicionado nenhuma, o programa exibirá um aviso amigável.
* **Tratamento de Índice:** Ao remover uma tarefa, o programa verifica se o número digitado está dentro do intervalo real da lista, evitando o erro de "Index Out of Range".

---

## 💡 Sugestões de Evolução
 considerando implementar futuras atualizações:
* **Persistência de Dados:** Salvar a lista em um arquivo `.txt` ou `.json` para não perder os dados ao fechar.
* **Status de Conclusão:** Marcar tarefas como "Feito" ou "Pendente".
* **Interface Gráfica:** Transformar o menu de texto em uma janela usando bibliotecas como `Tkinter` ou `PyQt`.
