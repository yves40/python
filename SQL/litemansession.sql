select nomcommune, nomdepartement,codepostal from insee where nomcommune like 'PONTA%';
delete from  insee ;


CREATE TABLE "insee" (
    "circo" TEXT,
    "coderegion" INTEGER,
    "region" TEXT,
    "cheflieu" TEXT,
    "departement" INTEGER,
    "nomdepartement" TEXT,
	"prefecture" TEXT,
	"circonsccription" INTEGER,
	"nomcommune" TEXT,
	"codepostal"  INTEGER,
	"codeinsee" INTEGER,
	"latitude" REAL,
	"longitude" REAL,
	"eloigne" REAL
);