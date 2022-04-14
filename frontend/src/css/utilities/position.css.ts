/**
 * @author Yousif Abdulkarim
 */



import { createVar, fallbackVar } from "@vanilla-extract/css";

import { property, utility } from "../helpers";

import { themeVars } from "../theme.css";



export const position = utility({
    values: {
        relative: "relative",
        absolute: "absolute",
        static: "static",
        fixed: "fixed",
        sticky: "sticky"
    },
    styles: property("position")
});

export const zIndexVar = createVar("z-index");

export const zIndex = utility({
    values: themeVars.zIndex,
    styles: property("zIndex")
});



const alignmentValues = {
    0: "0px",
    25: "25%",
    50: "50%",
    75: "75%",
    100: "100%"
}

export const top = utility({
    values: alignmentValues,
    styles: property("top")
});

export const bottom = utility({
    values: alignmentValues,
    styles: property("bottom")
});

export const left = utility({
    values: alignmentValues,
    styles: property("left")
});

export const right = utility({
    values: alignmentValues,
    styles: property("right")
});

const translateValues = {
    50: "50%",
    100: "100%",
    negative50: "-50%",
    negative100: "-100%"
}

const translateXVar = createVar("translate-x");

const translateYVar = createVar("translate-y");

const transform = `translate-x(${fallbackVar(translateXVar, "0px")}) translate-y(${fallbackVar(translateYVar, "0px")})`;

export const translateX = utility({
    values: translateValues,
    styles: value => ({
        transform,
        vars: {
            [translateXVar]: value
        }
    })
});

export const translateY = utility({
    values: translateValues,
    styles: value => ({
        transform,
        vars: {
            [translateYVar]: value
        }
    })
});