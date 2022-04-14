/**
 * @author Yousif Abdulkarim
 */



import { compose, property, utility } from "../helpers";

import { themeVars } from "../theme.css";



const sizeValues = {
    ...themeVars.size,
    ...themeVars.fluid,
    auto: "auto"
};

const heightvalues = {
    ...sizeValues,
    screen: "100vh"
}

export const height = utility({
    values: heightvalues,
    styles: property("height")
});

export const maxHeight = utility({
    values: heightvalues,
    styles: property("maxHeight")
});

export const minHeight = utility({
    values: heightvalues,
    styles: property("minHeight")
});

const widthValues = {
    ...sizeValues,
    screen: "100vw"
}

export const width = utility({
    values: widthValues,
    styles: property("width")
});

export const maxWidth = utility({
    values: widthValues,
    styles: property("maxWidth")
});

export const minWidth = utility({
    values: widthValues,
    styles: property("minWidth")
});

export const size = compose(
    height,
    width
);

export const maxSize = compose(
    maxHeight,
    maxWidth
);

export const minSize = compose(
    minHeight,
    minWidth
);