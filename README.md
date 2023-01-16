# Pet Kare

## Descrição:

Nesse projeto foi desenvolvido uma aplicação para ajudar donos de PetShop a guardar dados de animais. Utilizando conceitos de serializers e relacionamentos entre apps.

## Tecnologias utilizadas:

- python (ipython)
- django
- djangorestframework
- ipdb
- black
- jedi
- sqlparse

## Diagrama da aplicação:

![DER-petkare](https://github.com/Ltavio/api_PetKare/blob/main/pet-kare.drawio.png?raw=true)

## Endpoints do serviço:

<table>
    <thead>
        <tr>
            <th>Método</th>
            <th>Endpoint</th>
            <th>Objetivo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>POST</td>
            <td>api/pets/</td>
            <td>Cadastrar pet</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>api/pets/</td>
            <td>Listar pets</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>api/pets/int:pet_id/</td>
            <td>Filtragem de pet</td>
        </tr>
        <tr>
            <td>PATCH</td>
            <td>api/pets/int:pet_id/</td>
            <td>Atualização de pet</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>api/movies/</td>
            <td>Cadastrar movie</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>api/pets/<pet_id>/</td>
            <td>Deleção de pet</td>
        </tr>
    </tbody>
</table>

### Para inicializar a aplicação:
````
python manage.py runserver
````
