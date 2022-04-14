/**
 * @author Yousif Abdulkarim
 */



import { createVar, fallbackVar } from "@vanilla-extract/css";

import { utility, property, compose } from "../helpers";

import { themeVars } from "../theme.css";



export const flexBasis = utility({
    values: {
        ...themeVars.size,
        ...themeVars.fluid,
        auto: "auto"
    },
    styles: property("flexBasis")
});

export const flexGrowVar = createVar("flex-grow-var");

export const flexGrow = utility({
    values: {
        dynamic: fallbackVar(flexGrowVar, "0")
    },
    styles: value => ({
        flexGrow: value
    })
});

export const flexShrinkVar = createVar("flex-shrink-var");

export const flexShrink = utility({
    values: {
        dynamic: fallbackVar(flexShrinkVar, "0")
    },
    styles: value => ({
        flexGrow: value
    })
});

export const flexJustifyContent = utility({
    values: {
        flexStart: "flex-start",
        flexEnd: "flex-end",
        center: "center",
        spaceBetween: "space-between",
        spaceAround: "space-around",
        spaceEvenly: "space-evenly"
    },
    styles: property("justifyContent")
});

const alignValues = {
    stretch: "stretch",
    center: "center",
    flexStart: "flex-start",
    flexEnd: "flex-end",
    baseline: "baseline"
};

export const flexAlignItems = utility({
    values: alignValues,
    styles: property("alignItems")
});

export const flexAlignSelf = utility({
    values: {
        ...alignValues,
        auto: "auto"
    },
    styles: property("alignSelf")
});

export const flexDirection = utility({
    values: {
        row: "row",
        rowReverse: "row-reverse",
        column: "column",
        columnReverse: "column-reverse",
    },
    styles: property("flexDirection")
});

export const flexWrap = utility({
    values: {
        nowrap: "nowrap",
        wrap: "wrap",
        wrapReverse: "wrap-reverse",
    },
    styles: property("flexWrap")
});

export const rowGap = utility({
    values: themeVars.space,
    styles: property("rowGap")
});

export const columnGap = utility({
    values: themeVars.space,
    styles: property("columnGap")
});

export const gap = compose(
    rowGap,
    columnGap
);