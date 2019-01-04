
-- All orders
select p.nom_pizza, c.NUMERO_COMMANDE from pizzas p, commandes c where p.nom_pizza = c.nom_pizza order by c.NUMERO_COMMANDE;
-- All orders group by order number
select count (*) "Ordered Pizzas", c.NUMERO_COMMANDE from pizzas p, commandes c where p.nom_pizza = c.nom_pizza 
  group by c.NUMERO_COMMANDE order by c.NUMERO_COMMANDE;
-- Orders, with count for each pizzas
select count (*), p.NOM_PIZZA from pizzas p, commandes c where p.nom_pizza = c.nom_pizza 
  group by p.NOM_PIZZA order by p.NOM_PIZZA;
-- All ordered pizzas
select count (*), nom_pizza from pizzas p
  where exists (select c.nom_pizza from commandes c where p.NOM_PIZZA = c.NOM_PIZZA ) 
  group by nom_pizza;
-- Unordered pizzas
select count (*), nom_pizza from pizzas p
  where not exists (select c.nom_pizza from commandes c where p.NOM_PIZZA = c.NOM_PIZZA ) 
  group by nom_pizza;
  
-- list all ingredients of Pizzas with foiegras
select nom_pizza, ingredient from ingredients where INGREDIENT = 'foiegras';
select nom_pizza, ingredient from ingredients i where NOM_PIZZA in (select nom_pizza from ingredients ii where ingredient = 'foiegras' and i.NOM_PIZZA = i.NOM_PIZZA);

