const RenderModule = function(){

    const renderRecipes = function(data: Data): void{
        $("#recipes-container").remove()
        let source = $("#recipe-card-template").html()
        let template = Handlebars.compile(source)
        $("#recipes-container").append(template({recipes: data.recipes}))
    }

    return {
        renderRecipes: renderRecipes,
    }
}