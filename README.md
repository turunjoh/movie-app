# movie-app

Tietokannat- ja web-ohjelmoiti -kurssin harjoitustyö.

Tässä harjoitustyössä tarkoitus on tehdä web-sovellus, jossa käyttäjä voi lisätä elokuva-arvosteluja (ensisijainen tietokohde). Arvostelut koostuvat tähdistä (1-5) ja tekstistä. Sovelluksessa pystyy myös katselemaan muiden käyttäjien antamia arvosteluja, sekä mahdollisesti kommentoimaan niitä (toissijainen tietokohde). Käyttäjä pystyy myös muokkaamaan antamiaan arvostelua. Arvostelun antaessa voi asettaa elokuvalle genrejä sekä lisätä elokuvalle kuvan, jos sille ei vielä löydy kuvaa (joku toinen käyttäjä ei ole jo lisännyt).  

Hakutoiminnolla käyttäjä pystyy etsimään elokuvia nimen, genren ja julkaisuvuoden mukaan. 

Käyttäjäsivulla näkee kaikki käyttäjät, näiden arvostelut sekä statistiikka.

Tietokannassa on neljä taulua:

- Reviews
    - ensisijainen tietokohde
- Movies
    - toissijainen tietokohde
- Users
    - käyttäjien hallinnointiin
- Comments
    - toissijainen tietokohde

Alla kuvaus tietokantataulujen suunnitelmasta.

```mermaid
erDiagram
    Movies {
        integer id PK
        string title
        string genre
        integer year
    }
    
    Users {
        integer id PK
        string username
        string name
        string email
    }

    Comments {
        integer id PK
        integer user_id FK
        integer movie_id FK
        integer review_id FK
        string content
        date created_at
    }

    Reviews {
        integer id PK
        integer user_id FK
        integer movie_id FK
        string content
        integer rating
        date created_at
    }

    Reviews many to one Movies : ""
    Comments many to one Reviews : ""
    Reviews many to one Users : ""
    Comments many to one Users : ""
    Comments many to one Movies : ""

```




source venv/bin/activate

flask run
deactivate