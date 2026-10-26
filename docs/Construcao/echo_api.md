# Consumo de API com EchoAPI (VS Code)

> Objetivo: testar e consumir a API REST de **Produtos** (Django REST Framework) diretamente pelo VS Code, usando a extensão **EchoAPI**, sem sair do editor.

## 1. O que é o EchoAPI

O **EchoAPI for VS Code** é um cliente HTTP (semelhante ao Postman/Insomnia) que roda como extensão do VS Code. Com ele é possível:

* montar e enviar requisições `GET`, `POST`, `PUT`, `PATCH` e `DELETE`;
* organizar as requisições em **coleções** e pastas;
* usar **ambientes** com variáveis (`{{base_url}}`, `{{produto_id}}`);
* escrever **scripts de pré e pós-requisição** (sintaxe compatível com o Postman, `pm.*`) para validar respostas;
* importar comandos **cURL** e coleções do Postman.

### Instalação

1. Abra o VS Code e vá em **Extensions** (`Ctrl+Shift+X` / `Cmd+Shift+X`).
2. Pesquise por **EchoAPI** e instale *EchoAPI for VS Code*.
3. Um ícone do EchoAPI aparece na barra lateral. O login é opcional para uso local.

## 2. Preparando a API

A API está em `src/` e expõe o modelo `Produto` por meio de um `ModelViewSet` registrado em um `DefaultRouter`.

```python title="src/app/models.py"
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)
```

!!! warning "Dependências e migrações"
    A pasta `src/app/migrations/` não existe. Antes de subir o servidor, instale as dependências e gere as migrações:

    ```bash
    pip install -r requirements.txt
    cd src
    python manage.py makemigrations app
    python manage.py migrate
    python manage.py runserver
    ```

A API fica disponível em `http://127.0.0.1:8000/`. Como `project/urls.py` inclui `app.urls` duas vezes, os mesmos endpoints respondem com e sem o prefixo `/api/`. Neste guia usamos o prefixo `/api/`.

### Endpoints gerados pelo router

| Método   | URL                          | Ação                    | Status de sucesso |
|----------|------------------------------|-------------------------|-------------------|
| `GET`    | `/api/produtos/`             | Listar produtos         | `200 OK`          |
| `POST`   | `/api/produtos/`             | Criar produto           | `201 Created`     |
| `GET`    | `/api/produtos/{id}/`        | Detalhar um produto     | `200 OK`          |
| `PUT`    | `/api/produtos/{id}/`        | Substituir (todos os campos) | `200 OK`     |
| `PATCH`  | `/api/produtos/{id}/`        | Atualizar parcialmente  | `200 OK`          |
| `DELETE` | `/api/produtos/{id}/`        | Remover produto         | `204 No Content`  |

!!! tip "Barra final"
    O DRF exige a barra no final (`/api/produtos/1/`). Sem ela, o Django tenta redirecionar e requisições `POST`/`PUT` falham.

## 3. Configurando o ambiente no EchoAPI

1. No painel do EchoAPI, abra **Environments** e crie o ambiente `Local`.
2. Adicione as variáveis:

| Variável     | Valor inicial                 |
|--------------|-------------------------------|
| `base_url`   | `http://127.0.0.1:8000/api`   |
| `produto_id` | `1`                           |

3. Selecione o ambiente `Local` no seletor do canto superior.
4. Crie uma **coleção** chamada `Produtos API`; todas as requisições abaixo ficam dentro dela.

## 4. Requisições CRUD

Em todas as requisições com corpo, use a aba **Body → raw → JSON** (isso define o cabeçalho `Content-Type: application/json`).

### 4.1 Criar produto — `POST`

```
POST {{base_url}}/produtos/
```

```json
{
  "nome": "Teclado",
  "preco": "149.90",
  "descricao": "Mecânico ABNT2"
}
```

Resposta esperada (`201 Created`):

```json
{"id": 1, "nome": "Teclado", "preco": "149.90", "descricao": "Mecânico ABNT2", "disponivel": true}
```

Observe que `id` é gerado pelo servidor (`read_only_fields`) e `disponivel` assume o valor padrão `true`.

**Script de pós-resposta** (aba *Post-response* / *Tests*), que guarda o `id` criado para as próximas requisições:

```javascript
pm.test("Status 201", function () {
  pm.response.to.have.status(201);
});

const produto = pm.response.json();
pm.environment.set("produto_id", produto.id);
```

### 4.2 Listar produtos — `GET`

```
GET {{base_url}}/produtos/
```

```javascript
pm.test("Retorna uma lista", function () {
  pm.expect(pm.response.json()).to.be.an("array");
});
```

### 4.3 Detalhar produto — `GET`

```
GET {{base_url}}/produtos/{{produto_id}}/
```

### 4.4 Atualizar parcialmente — `PATCH`

```
PATCH {{base_url}}/produtos/{{produto_id}}/
```

```json
{ "preco": "129.90" }
```

```javascript
pm.test("Preço atualizado", function () {
  pm.expect(pm.response.json().preco).to.eql("129.90");
});
```

### 4.5 Substituir — `PUT`

`PUT` exige **todos** os campos obrigatórios (`nome`, `preco`, `descricao`):

```json
{
  "nome": "Teclado Pro",
  "preco": "199.90",
  "descricao": "Mecânico ABNT2, switch brown",
  "disponivel": false
}
```

### 4.6 Remover — `DELETE`

```
DELETE {{base_url}}/produtos/{{produto_id}}/
```

Resposta: `204 No Content` (corpo vazio). Um `GET` no mesmo `id` passa a retornar `404 Not Found`.

## 5. Explorando erros de validação

Envie um `POST` inválido para ver como o serializer responde:

```json
{ "nome": "X", "preco": "99999.99" }
```

Resposta `400 Bad Request`:

```json
{
  "preco": ["Ensure that there are no more than 6 digits in total."],
  "descricao": ["This field is required."]
}
```

* `preco` estoura o limite de `max_digits=6` (4 dígitos inteiros + 2 decimais, ou seja, no máximo `9999.99`).
* `descricao` é um `TextField` sem `blank=True`, logo é obrigatório.

## 6. Importando via cURL

O EchoAPI aceita colar um comando cURL (**Import → cURL**) e o converte em requisição:

```bash
curl -X POST http://127.0.0.1:8000/api/produtos/ -H "Content-Type: application/json" -d '{"nome":"Mouse","preco":"89.90","descricao":"Sem fio"}'
```

## 7. Executando a coleção

Ordene as requisições na coleção como **POST → GET lista → GET detalhe → PATCH → PUT → DELETE** e use o **Runner** da coleção para executar todas em sequência. Como o `POST` grava `produto_id` no ambiente, o fluxo inteiro roda sem editar URLs à mão, e os `pm.test` mostram quais etapas passaram.

## 8. Exercícios

- [ ] Criar três produtos e conferir a listagem.
- [ ] Escrever um teste que verifique se `disponivel` é `true` por padrão.
- [ ] Testar um `PUT` sem o campo `descricao` e explicar o erro retornado.
- [ ] Adicionar um teste de tempo de resposta: `pm.expect(pm.response.responseTime).to.be.below(500);`
- [ ] Exportar a coleção e versioná-la no repositório (ex.: `docs/assets/api/produtos.collection.json`).
