drop table clients;
drop table commandes;
drop table ingredients;
drop table pizzas;

CREATE TABLE clients (
    nom varchar2(64),
    prenom varchar2(64),
    adresse varchar2(128),
    numero INTEGER
);

CREATE TABLE commandes (
    numero_client INTEGER,
    nom_pizza varchar2(64),
    prix REAL,
    numero_commande INTEGER,
    date_commande DATE
);

CREATE TABLE ingredients (
    nom_pizza  varchar2(64),
    ingredient  varchar2(64)
);

CREATE TABLE pizzas (
    nom_pizza varchar2(64),
    prix REAL
);
