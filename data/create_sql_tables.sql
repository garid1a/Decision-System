-- Drop the database if it exists
DROP DATABASE IF EXISTS FarmData;

-- Create the database
CREATE DATABASE FarmData;

-- Use the database
USE FarmData;

-- Create the Consumer table
CREATE TABLE Consumer (
    ConsumerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    Location VARCHAR(255),
    UserName VARCHAR(255),
    Password VARCHAR(255)
);

-- Create a trigger to generate UserName and Password
-- DELIMITER //
-- CREATE TRIGGER GenerateUserCredentials
-- BEFORE INSERT ON Consumer
-- FOR EACH ROW
-- BEGIN
--     SET NEW.UserName = CONCAT('Consumer', NEW.ConsumerID);
--     SET NEW.Password = CONCAT('Password', NEW.ConsumerID);
-- END;
-- //
-- DELIMITER ;

-- Create the Product table
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(255),
    Season VARCHAR(255),
    SoilType VARCHAR(255)
);

-- Create the Preference table
CREATE TABLE Preference (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY,
    ConsumerID INT,
    Month VARCHAR(255),
    FOREIGN KEY (ConsumerID) REFERENCES Consumer(ConsumerID)
);

-- Create the ProductPreference table (junction table)
CREATE TABLE ProductPreference (
    ProductID INT,
    PreferenceID INT,
    PRIMARY KEY (ProductID, PreferenceID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (PreferenceID) REFERENCES Preference(PreferenceID)
);

-- Create the Farmer table
CREATE TABLE Farmer (
    FarmerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Location VARCHAR(255),
    SoilType VARCHAR(255),
    UserName VARCHAR(255),
    Password VARCHAR(255)
);

-- Create a trigger to generate UserName and Password for Farmers
-- DELIMITER //
-- CREATE TRIGGER GenerateFarmerUserCredentials
-- BEFORE INSERT ON Farmer
-- FOR EACH ROW
-- BEGIN
--     SET NEW.UserName = CONCAT('Farmer', NEW.FarmerID);
--     SET NEW.Password = CONCAT('Password', NEW.FarmerID);
-- END;
-- //
-- DELIMITER ;