/**
 * @author Yousif Abdulkarim
 */



import { property, utility } from "../helpers";

import { themeVars } from "../theme.css";



export const boxShadow = utility({
    values: themeVars.shadow,
    styles: property("boxShadow")
});