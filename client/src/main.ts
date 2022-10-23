(function(){
    const data: Data = new Data();
    const render = RenderModule();
    		
    $("#search-btn").on("click", function(){
        let ingredient: string = <string> $("#ingredient-input").val()
        let dairyFree: boolean = $("#dairy-checkbox").is(":checked")
        let glutenFree: boolean = $("#gluten-checkbox").is(":checked")

        data.generateRecipes(ingredient, dairyFree, glutenFree).then(() => {
            render.renderRecipes(data)
        })
    });
})()