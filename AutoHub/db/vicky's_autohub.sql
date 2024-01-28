CREATE DATABASE vickys_auto_hub;
USE vickys_auto_hub;

CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year YEAR NOT NULL,
    color VARCHAR(50) NOT NULL,
    body_style ENUM('Sedan', 'SUV', 'Truck', 'Van', 'Coupe', 'Convertible') NOT NULL,
    kms_driven INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,
    UNIQUE KEY make_model_year_color (make, model, year, color)
);


CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

DELIMITER $$
CREATE PROCEDURE PopulateVehicles()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 100;
    DECLARE make VARCHAR(50);
    DECLARE model VARCHAR(50);
    DECLARE year YEAR;
    DECLARE color VARCHAR(50);
    DECLARE body_style ENUM('Sedan', 'SUV', 'Truck', 'Van', 'Coupe', 'Convertible');
    DECLARE kms_driven INT;
    DECLARE stock_quantity INT;
    DECLARE price DECIMAL(10,2);

    -- Seed the random number generator
    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        -- Generate random values
        SET make = ELT(FLOOR(1 + RAND() * 10), 'Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia', 'Subaru', 'Volkswagen', 'BMW');
        SET model = ELT(FLOOR(1 + RAND() * 5), 'Camry', 'Accord', 'F-150', 'Silverado', 'Altima');
        SET year = FLOOR(2015 + RAND() * 7);
        SET color = ELT(FLOOR(1 + RAND() * 5), 'Red', 'Blue', 'Black', 'White', 'Silver');
        SET body_style = ELT(FLOOR(1 + RAND() * 6), 'Sedan', 'SUV', 'Truck', 'Van', 'Coupe', 'Convertible');
        SET kms_driven = FLOOR(10000 + RAND() * 10000);
        SET stock_quantity = FLOOR(RAND()*10);
        SET price = FLOOR(10000 + RAND() * 40000);

        -- Attempt to insert a new record
        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END; -- Handle duplicate key error
            INSERT INTO vehicles (make, model, year, color, body_style, kms_driven, price ,stock_quantity)
            VALUES (make, model, year, color, body_style, kms_driven, price, stock_quantity);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

CALL PopulateVehicles();

INSERT INTO discounts (vehicle_id, pct_discount)
SELECT vehicle_id, FLOOR(1 + RAND() * 25) + YEAR(CURDATE()) - year
FROM vehicles
WHERE stock_quantity > 4
AND year < YEAR(CURDATE()) - 3
ORDER BY RAND()
LIMIT 10;
