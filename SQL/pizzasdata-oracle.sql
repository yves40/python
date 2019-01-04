-- Clients
delete from clients;
insert into clients values ('toubhans', 'baptiste', '21 rue de la piste saint martin, 77800', 12);
insert into clients values ('toubhans', 'benoit', '21 rue des roses, , 69800', 13);
insert into clients values ('toubhans', 'bastien', '21 rue du fleuve, 44800', 14);
insert into clients values ('toubhans', 'baboule', '21 rue des fauves, 40800', 15);
insert into clients values ('barros', 'JIP', '21 rue des petits loups, 40800', 16);
insert into clients values ('barros', 'Totie', '21 rue des dunes d''arcachon, 40800', 17);
insert into clients values ('barros', 'Jeanine', '21 rue des patissiers landais, 40800', 18);
select * from clients;
-- Ingredients
delete from ingredients;
insert into ingredients values ('royale', 'farine');
insert into ingredients values ('royale', 'oeufs');
insert into ingredients values ('royale', 'anchoix');
insert into ingredients values ('royale', 'poivrons verts');

insert into ingredients values ('supreme', 'farine');
insert into ingredients values ('supreme', 'oeufs');
insert into ingredients values ('supreme', 'anchoix');
insert into ingredients values ('supreme', 'poivrons verts');
insert into ingredients values ('supreme', 'creme');
insert into ingredients values ('supreme', 'saumon');

insert into ingredients values ('calzone', 'poivrons verts');
insert into ingredients values ('calzone', 'farine');
insert into ingredients values ('calzone', 'oeufs');
insert into ingredients values ('calzone', 'lardons');
insert into ingredients values ('calzone', 'nutella');

insert into ingredients values ('4fromages', 'poivrons verts');
insert into ingredients values ('4fromages', 'farine');
insert into ingredients values ('4fromages', 'oeufs');
insert into ingredients values ('4fromages', 'mozarella');
insert into ingredients values ('4fromages', 'roquefort');
insert into ingredients values ('4fromages', 'gruyere');
insert into ingredients values ('4fromages', 'camembert');

insert into ingredients values ('basque', 'poivrons verts');
insert into ingredients values ('basque', 'farine');
insert into ingredients values ('basque', 'oeufs');
insert into ingredients values ('basque', 'piment');
insert into ingredients values ('basque', 'foiegras');

insert into ingredients values ('basquespeciale', 'poivrons verts');
insert into ingredients values ('basquespeciale', 'farine');
insert into ingredients values ('basquespeciale', 'oeufs');
insert into ingredients values ('basquespeciale', 'piment');
insert into ingredients values ('basquespeciale', 'foiegras');
insert into ingredients values ('basquespeciale', 'magrets');
insert into ingredients values ('basquespeciale', 'gesiersconfits');

insert into ingredients values ('mexicaine', 'poivrons verts');
insert into ingredients values ('mexicaine', 'farine');
insert into ingredients values ('mexicaine', 'oeufs');
insert into ingredients values ('mexicaine', 'piment');
insert into ingredients values ('mexicaine', 'guacamole');
insert into ingredients values ('mexicaine', 'avocat');
insert into ingredients values ('mexicaine', 'tabasco');

insert into ingredients values ('viet', 'poivrons verts');
insert into ingredients values ('viet', 'farine');
insert into ingredients values ('viet', 'oeufs');
insert into ingredients values ('viet', 'piment');
insert into ingredients values ('viet', 'guacamole');
insert into ingredients values ('viet', 'avocat');
insert into ingredients values ('viet', 'tabasco');
insert into ingredients values ('viet', 'gniocman');
insert into ingredients values ('viet', 'poissonsdumekong');

commit;

select * from ingredients;
-- Pizzas
delete from pizzas;
insert into pizzas values('royale', 17.50);
insert into pizzas values('calzone', 15.50);
insert into pizzas values('4fromages', 14.50);
insert into pizzas values('basque', 13.50);
insert into pizzas values('basquespeciale', 23.50);
insert into pizzas values('mexicaine', 21.50);
insert into pizzas values('viet', 28.50);
commit;

select * from pizzas;
-- Commandes
delete from commandes;
commit;
insert into commandes values (12, 'royale', 0, 10000, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (12, 'basquespeciale', 0, 10000, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (12, 'calzone', 0, 10000, to_date('2016-08-11', 'YYYY-MM-DD'));

insert into commandes values (13, 'royale', 0, 10001, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (13, '4fromages', 0, 10001, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (13, 'calzone', 0, 10001, to_date('2016-08-11', 'YYYY-MM-DD'));

insert into commandes values (14, 'royale', 0, 10002, to_date('2016-08-11', 'YYYY-MM-DD'));

insert into commandes values (15, 'royale', 0, 10003, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (15, 'basquespeciale', 0, 10003, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (15, 'calzone', 0, 10003, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (15, 'calzone', 0, 10003, to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (15, 'basque', 0, 10003,to_date('2016-08-11', 'YYYY-MM-DD'));
insert into commandes values (15, '4fromages', 0, 10003, to_date('2016-08-11', 'YYYY-MM-DD'));

insert into commandes values (16, 'calzone', 0, 10004, to_date('2016-08-11', 'YYYY-MM-DD'));

insert into commandes values (17, '4fromages', 0, 10005, to_date('2016-08-11', 'YYYY-MM-DD'));

insert into commandes values (18, 'royale', 0, 10006, to_date('2016-08-11', 'YYYY-MM-DD'));

commit;
--
--  Update the commandes table price column
--  Interesting join...
--
update commandes c set 
  (c.prix)  =
  (
    (select p.prix from pizzas p where p.nom_pizza = c.nom_pizza )
  )
  where exists (select * from pizzas where pizzas.NOM_PIZZA = c.NOM_PIZZA)
  ;
select * from commandes;
select * from pizzas;
commit;

-- To delete later
update commandes set prix = 0;
commit;
