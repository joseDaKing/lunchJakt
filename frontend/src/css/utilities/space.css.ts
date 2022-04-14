/**
 * @author Yousif Abdulkarim
 */



import { createVar, fallbackVar } from "@vanilla-extract/css";

import { calc } from "@vanilla-extract/css-utils";

import { utility, property, compose } from "../helpers";

import { themeVars } from "../theme.css";



const spaceExtendedSelector = "& > :not(:last-child):not([hidden])";

const spaceYReverseVar = createVar("space-y-reverse");

export const spaceYReverse = utility({
    values: {
        reverse: "1"
    },
    extend: spaceExtendedSelector,
    styles: value => ({
        vars: {
            [spaceYReverseVar]: value
        }
    })
});

export const spaceY = utility({
    values: themeVars.space,
    extend: spaceExtendedSelector,
    styles: value => ({
        marginTop: (
            calc(value)
            .multiply(
                calc(1)
                .subtract(fallbackVar(spaceYReverseVar, "0"))
            )
            .toString()
        ),
        marginBottom: (
            calc(value)
            .multiply(fallbackVar(spaceYReverseVar, "0"))
            .toString()
        ),
    })
});

const spaceXReverseVar = createVar("space-x-reverse");

export const spaceXReverse = utility({
    values: {
        reverse: "1"
    },
    extend: spaceExtendedSelector,
    styles: value => ({
        vars: {
            [spaceXReverseVar]: value
        }
    })
});

export const spaceX = utility({
    values: themeVars.space,
    extend: spaceExtendedSelector,
    styles: value => ({
        marginLeft: (
            calc(value)
            .multiply(
                calc(1)
                .subtract(fallbackVar(spaceXReverseVar, "0"))
            )
            .toString()
        ),
        marginRight: (
            calc(value)
            .multiply(fallbackVar(spaceXReverseVar, "0"))
            .toString()
        ),
    })
});

const marginValues = {
    ...themeVars.space,
    auto: "auto"
}

export const marginTop = utility({
    values: marginValues,
    styles: property("marginTop")
});

export const marginBottom = utility({
    values: marginValues,
    styles: property("marginBottom")
});

export const marginLeft = utility({
    values: marginValues,
    styles: property("marginLeft")
});

export const marginRight = utility({
    values: marginValues,
    styles: property("marginRight")
});

export const margin = compose(
    marginTop,
    marginBottom,
    marginLeft,
    marginRight
);

export const marginX = compose(
    marginLeft,
    marginRight
);

export const marginY = compose(
    marginTop,
    marginBottom,
);

export const paddingTop = utility({
    values: themeVars.space,
    styles: property("paddingTop")
});

export const paddingBottom = utility({
    values: themeVars.space,
    styles: property("paddingBottom")
});

export const paddingLeft = utility({
    values: themeVars.space,
    styles: property("paddingLeft")
});

export const paddingRight = utility({
    values: themeVars.space,
    styles: property("paddingRight")
});

export const padding = compose(
    paddingTop,
    paddingBottom,
    paddingLeft,
    paddingRight
);

export const paddingX = compose(
    paddingLeft,
    paddingRight
);

export const paddingY = compose(
    paddingTop,
    paddingBottom,
);