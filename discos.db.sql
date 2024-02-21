BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "discos" (
	"Identificador"	INTEGER,
	"artista"	TEXT,
	"anio"	INTEGER,
	"titulo"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
INSERT INTO "discos" VALUES (1,'Iron Maiden',1980,'Iron Maiden');
COMMIT;
