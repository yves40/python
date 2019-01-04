drop table clients;
drop table commandes;
drop table ingredients;
drop table pizzas;


-- Describe CLIENTS
CREATE TABLE clients (
    "nom" TEXT,
    "prenom" TEXT,
    "adresse" TEXT,
    "numero" INTEGER
);

-- Describe COMMANDE
CREATE TABLE commandes (
    "numero_client" INTEGER,
    "nom_pizza" TEXT,
    "prix" REAL,
    "numero_commande" INTEGER,
    "date" TEXT
);

-- Describe INGREDIENTS
CREATE TABLE ingredients (
    "nom_pizza" TEXT,
    "ingredient" TEXT
);

-- Describe PIZZAS
CREATE TABLE pizzas (
    "nom_pizza" TEXT,
    "prix" REAL
);



