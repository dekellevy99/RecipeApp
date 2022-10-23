"use strict";
class Recipe {
    constructor(title, thumbnail, href, ingredients) {
        this._title = title;
        this._thumbnail = thumbnail;
        this._href = href;
        this._ingredients = ingredients;
    }
    // === GET METHODS ===
    get title() {
        return this._title;
    }
    get thumbnail() {
        return this._thumbnail;
    }
    get href() {
        return this._href;
    }
    get ingredients() {
        return [...this._ingredients];
    }
    // === SET METHODS ===
    set title(title) {
        this._title = title;
    }
    set thumbnail(thumbnail) {
        this._thumbnail = thumbnail;
    }
    set href(href) {
        this._href = href;
    }
    set ingredients(ingredients) {
        this._ingredients = ingredients;
    }
}
