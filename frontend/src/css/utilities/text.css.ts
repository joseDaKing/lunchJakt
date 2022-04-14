/**
 * @author Yousif Abdulkarim
 */



import { utility, property } from "../helpers";



export const textAlign = utility({
    values: {
        right: "right",
        center: "center",
        left: "left"
    },
    styles: property("textAlign")
});

export const textTransform = utility({
    values: {
        uppercase: "uppercase",
        capitalize: "capitalize",
        lowercase: "lowercase"
    },
    styles: property("textTransform")
});

export const textDecoration = utility({
    values: {
        underline: "underline",
        overline: "overline",
        lineThrough: "line-through"
    },
    styles: property("textDecoration")
});