CREATE TABLE aerolineas (
    id_aerolinea int,
    nombre_aerolinea varchar(255)
);

INSERT INTO aerolineas(id_aerolinea, nombre_aerolinea)
VALUES (1,'Volaris'),
       (2,'Aeromar'),
       (3,'Interjet'),
       (4,'Aeromexico');

CREATE TABLE aeropuertos (
    id_aeropuerto int,
    nombre_aeropuerto varchar(255)
);

INSERT INTO aeropuertos(id_aeropuerto, nombre_aeropuerto)
VALUES (1,'Benito Juarez'),
       (2,'Guanajuato'),
       (3,'La Paz'),
       (4,'Oaxaca');

CREATE TABLE movimientos (
    id_movimiento int,
    descripcion varchar(255)
);

INSERT INTO movimientos(id_movimiento, descripcion)
VALUES (1,'Salida'),
       (2,'Llegada');

CREATE TABLE vuelos (
    id_aerolinea int,
	id_aeropuerto int,
    id_movimiento int,
    dia date
);

INSERT INTO vuelos(id_aerolinea, id_aeropuerto, id_movimiento, dia)
VALUES (1, 1, 1, '2021-05-02'),
       (2, 1, 1, '2021-05-02'),
       (3, 2, 2, '2021-05-02'),
       (4, 3, 2, '2021-05-02'),
       (1, 3, 2, '2021-05-02'),
       (2, 1, 1, '2021-05-02'),
       (2, 3, 1, '2021-05-04'),
       (3, 4, 1, '2021-05-04'),
       (3, 4, 1, '2021-05-02');

/*
#1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?
*/
SELECT aeropuertos.nombre_aeropuerto, COUNT(*) movimientos
FROM aeropuertos
INNER JOIN vuelos
ON aeropuertos.id_aeropuerto = vuelos.id_aeropuerto
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
/*
3. ¿En qué día se han tenido mayor número de vuelos?
*/

SELECT dia, count(*) as vuelos_dia
FROM vuelos 
GROUP BY dia
LIMIT 1;


