# api-flask-receita
Api de receitas para estudo de Flask

### Body
```sh
{
    "nome": "Arroz com ovo",
    "tempo_de_preparo": 15,
    "serve_quantos": 10,
    "data": return_data(5).strftime("%d/%m/%Y")
} 
```

### Endpoint
/receita
>    method: GET
>    return: LIST[Receita]

/receita
>    method: POST
>    body: Receita
>    return: Receita

/receita/id
>    method: GET
>    return: Receita
