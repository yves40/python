select  p.nom_pizza, prix, ingredient from pizzas p, ingredients i 

select  p.nom_pizza, prix, ingredient from pizzas p, ingredients i 
	where  i.nom_pizza = p.nom_pizza

select  p.nom_pizza, prix, ingredient from pizzas p, ingredients i 
	where  i.nom_pizza = p.nom_pizza and ingredient like '%fraiche%'
