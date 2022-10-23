CREATE DATABASE IF NOT EXISTS recipeappdb;
use recipeappdb;

CREATE TABLE IF NOT EXISTS DairyIngrediant(
    name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS GlutenIngrediant(
    name VARCHAR(255) PRIMARY KEY
);

