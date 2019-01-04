select * from pizzas;
select nom_pizza, min(prix), max(prix) from pizzas group by nom_pizza;


select * from commande;
select count (*) 'Nombre de commandes' from commande;
select sum(prix) 'Facture', numero_client, numero_commande from commande group by numero_commande;

select p.nom_pizza, i.ingredient from pizzas p, ingredients i
	where p.nom_pizza = i.nom_pizza;
	
select p.nom_pizza, i.ingredient, p.prix from pizzas p, ingredients i
	where p.nom_pizza = i.nom_pizza and (i.ingredient = 'Champignons' or i.ingredient =  'crème');

select p.nom_pizza, i.ingredient, p.prix from pizzas p, ingredients i
	where p.nom_pizza = i.nom_pizza and (i.ingredient = 'Caviar' or i.ingredient =  'crème');
	
select p.nom_pizza, i.ingredient, p.prix from pizzas p, ingredients i
	where p.nom_pizza = i.nom_pizza and (i.ingredient = 'Caviar' or i.ingredient =  'crème');

select p.nom_pizza, i.ingredient, p.prix from pizzas p, ingredients i where p.nom_pizza = i.nom_pizza and i.ingredient = 'crème fraiche';
select p.nom_pizza, i.ingredient, p.prix from pizzas p, ingredients i where p.nom_pizza = i.nom_pizza and i.ingredient = 'Champignons';
 
select p.nom_pizza, i.ingredient, p.prix from pizzas p, ingredients i where p.nom_pizza = i.nom_pizza and i.ingredient = 'crème fraiche'
intersect 
select p.nom_pizza, i.ingredient, p.prix from pizzas p, ingredients i where p.nom_pizza = i.nom_pizza and i.ingredient = 'Champignons';

 