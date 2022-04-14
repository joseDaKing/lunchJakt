/**
 * @author Yousif Abdulkarim
 */



import { compose, property, utility } from "../helpers";

import { createVar, fallbackVar } from "@vanilla-extract/css";

import { calc } from "@vanilla-extract/css-utils";

import { themeVars } from "../theme.css";



const borderStyleValues = { solid: "solid" };

const divideExtendedSelector = "& > :not(:last-child):not([hidden])";

export const divideYStyle = utility({
    values: borderStyleValues,
    extend: divideExtendedSelector,
    styles: property("borderStyle")
});

export const divideYColor = utility({
    values: themeVars.color,
    extend: divideExtendedSelector,
    styles: property("borderColor")
});

const divideYReverseVar = createVar("divide-y-reverse");

export const divideYReverse = utility({
    values: {
        reverse: "1"
    },
    extend: divideExtendedSelector,
    styles: value => ({
        vars: {
            [divideYReverseVar]: value
        }
    })
});

export const divideYWidth = utility({
    values: themeVars.color,
    extend: divideExtendedSelector,
    styles: value => ({
        borderTopWidth: (
            calc(value)
            .multiply(
                calc(1)
                .subtract(fallbackVar(divideYReverseVar, "0"))
            )
            .toString()
        ),
        borderBottomWidth: (
            calc(value)
            .multiply(fallbackVar(divideYReverseVar, "0"))
            .toString()
        ) 
    })
});

export const divideXStyle = utility({
    values: borderStyleValues,
    extend: divideExtendedSelector,
    styles: property("borderStyle")
});

export const divideXColor = utility({
    values: themeVars.color,
    extend: divideExtendedSelector,
    styles: property("borderColor")
});

const divideXReverseVar = createVar("divide-y-reverse");

export const divideXReverse = utility({
    values: {
        reverse: "1"
    },
    extend: divideExtendedSelector,
    styles: value => ({
        vars: {
            [divideXReverseVar]: value
        }
    })
});

export const divideXWidth = utility({
    values: themeVars.color,
    extend: divideExtendedSelector,
    styles: value => ({
        borderLeftWidth: (
            calc(value)
            .multiply(
                calc(1)
                .subtract(fallbackVar(divideYReverseVar, "0"))
            )
            .toString()
        ),
        borderRightWidth: (
            calc(value)
            .multiply(fallbackVar(divideYReverseVar, "0"))
            .toString()
        ) 
    })
});

export const borderStyle = utility({
    values: borderStyleValues,
    styles: property("borderStyle")
});

export const borderTopColor = utility({
   values: themeVars.color,
   styles: property("borderTopColor") 
});

export const borderBottomColor = utility({
    values: themeVars.color,
    styles: property("borderBottomColor") 
});

export const borderLeftColor = utility({
    values: themeVars.color,
    styles: property("borderLeftColor") 
});

export const borderRightColor = utility({
    values: themeVars.color,
    styles: property("borderRightColor") 
});

export const borderColor = compose(
    borderTopColor,
    borderBottomColor,
    borderLeftColor,
    borderRightColor
);

export const borderXColor = compose(
    borderLeftColor,
    borderRightColor
);

export const borderYColor = compose(
    borderTopColor,
    borderBottomColor
);

export const borderTopWidth = utility({
   values: themeVars.borderWidth,
   styles: property("borderTopWidth") 
});

export const borderBottomWidth = utility({
    values: themeVars.borderWidth,
    styles: property("borderBottomWidth") 
});

export const borderLeftWidth = utility({
    values: themeVars.borderWidth,
    styles: property("borderLeftWidth") 
});

export const borderRightWidth = utility({
    values: themeVars.borderWidth,
    styles: property("borderRightWidth") 
});

export const borderWidth = compose(
    borderTopWidth,
    borderBottomWidth,
    borderLeftWidth,
    borderRightWidth
);

export const borderXWidth = compose(
    borderLeftWidth,
    borderRightWidth
);

export const borderYWidth = compose(
    borderTopWidth,
    borderBottomWidth
);

export const borderTopRightRadius = utility({
    values: themeVars.borderRadius,
    styles: property("borderTopRightRadius")
});

export const borderBottomRightRadius = utility({
    values: themeVars.borderRadius,
    styles: property("borderBottomRightRadius")
});

export const borderTopLeftRadius = utility({
    values: themeVars.borderRadius,
    styles: property("borderTopLeftRadius")
});

export const borderBottomLeftRadius = utility({
    values: themeVars.borderRadius,
    styles: property("borderBottomLeftRadius")
});

export const borderRadius = compose(
    borderTopLeftRadius,
    borderTopRightRadius,
    borderBottomLeftRadius,
    borderBottomRightRadius
);

export const borderTopRadius = compose(
    borderTopLeftRadius,
    borderTopRightRadius,
);

export const borderBottomRadius = compose(
    borderBottomLeftRadius,
    borderBottomRightRadius
);

export const borderLeftRadius = compose(
    borderTopLeftRadius,
    borderBottomLeftRadius
);

export const borderRightRadius = compose(
    borderTopRightRadius,
    borderBottomRightRadius
);