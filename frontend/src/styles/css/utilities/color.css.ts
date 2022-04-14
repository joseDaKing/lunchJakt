/**
 * @author Yousif Abdulkarim
 */



import { property, utility } from "../helpers";

import { themeVars } from "../theme.css";



export const textColor = utility({
    values: themeVars.color,
    styles: property("color")
});

export const bgColor = utility({
    values: themeVars.color,
    styles: property("backgroundColor")
});

export const opacity = utility({
    values: themeVars.opacity,
    styles: property("opacity")
});