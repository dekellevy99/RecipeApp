"use strict";
const RenderModule = function () {
    const renderRecipes = function (data) {
        $("#recipes-container").empty();
        let source = $("#recipe-card-template").html();
        let template = Handlebars.compile(source);
        $("#recipes-container").append(template({ recipes: data.recipes }));
    };
    return {
        renderRecipes: renderRecipes,
    };
};
