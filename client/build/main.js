"use strict";
(function () {
    const data = new Data();
    const render = RenderModule();
    $("#search-btn").on("click", function () {
        let ingredient = $("#ingredient-input").val();
        let dairyFree = $("#dairy-checkbox").is(":checked");
        let glutenFree = $("#gluten-checkbox").is(":checked");
        data.generateRecipes(ingredient, dairyFree, glutenFree).then(() => {
            render.renderRecipes(data);
        });
    });
})();
