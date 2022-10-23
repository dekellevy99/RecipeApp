class Data{
    private _recipes: Recipe[];

    constructor(){
        this._recipes = [];
    }

    get recipes(){
        return [...this._recipes];
    }

    async generateRecipes(ingredient: string, dairyFree: boolean, glutenFree: boolean){
        this._recipes.splice(0);
        let response = await $.get(`/recipes?ingredient=${ingredient}&dairyFree=${dairyFree}&glutenFree=${glutenFree}`);      
        for(const recipe of response["recipes"]){
            const {title, thumbnail, href, ingredients} = recipe;
            this._recipes.push(new Recipe(title, thumbnail, href, ingredients));
        }
    }
}
