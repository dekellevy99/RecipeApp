class Recipe{
    private _title: string;
    private _thumbnail : string;
    private _href: string;
    private _ingredients: string[];

    constructor(title: string, thumbnail : string, href: string, ingredients: string[]){
        this._title = title;
        this._thumbnail = thumbnail;
        this._href = href;
        this._ingredients = ingredients
    }

    // === GET METHODS ===
    get title(): string{
        return this._title;
    }

    get thumbnail(): string{
        return this._thumbnail;
    }

    get href(): string{
        return this._href;
    }

    get ingredients(): string[]{
        return [...this._ingredients]
    }

    // === SET METHODS ===
    set title(title: string){
        this._title = title;
    }

    set thumbnail(thumbnail: string){
        this._thumbnail = thumbnail
    }

    set href(href: string){
        this._href = href;
    }

    set ingredients(ingredients: string[]){
        this._ingredients = ingredients;
    }
}