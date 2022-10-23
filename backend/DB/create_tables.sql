CREATE DATABASE recipeappdb;
use recipeappdb;

CREATE TABLE Recipe(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    thambnail VARCHAR(255),
    href VARCHAR(255)
);

CREATE TABLE Ingrediant(
    name VARCHAR(255) PRIMARY KEY,
    glutenFree BOOLEAN,
    dairyFree BOOLEAN
);

CREATE TABLE RecipeIngrediant(
    recipeId INT,
    ingrediantName VARCHAR(255),
    PRIMARY KEY(recipeId, ingrediantName),
    FOREIGN KEY(recipeId) REFERENCES Recipe(id),
    FOREIGN KEY(ingrediantName) REFERENCES Ingrediant(name)
);