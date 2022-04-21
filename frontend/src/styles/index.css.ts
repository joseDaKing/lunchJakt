import { createSprinkles, defineProperties } from "@vanilla-extract/sprinkles";

import { themeVars } from "./theme.css";



const marginValues = {
    ...themeVars.space,
    auto: "auto"
} as const;

const sizeValues = {
    ...themeVars.size,
    ...themeVars.fluid,
    fitContent: "fit-content",
    maxContent: "max-content",
    minContent: "min-content",
    auto: "auto"
} as const;

const heightValues = {
    ...sizeValues,
    screen: "100vh"
} as const;

const widthValues = {
    ...sizeValues,
    screen: "100vw"
} as const;

const flexShrinkGrowValues = [
    "0",
    "1"
] as const

const alignValues = [
    "stretch",
    "center",
    "flex-start",
    "flex-end",
    "baseline"
] as const;

const borderStyleValues = [
    "solid",
    "none"
] as const;

const positionValues = {
    ...themeVars.space,
    ...themeVars.fluid
}

const conditions = {
    _: {},
    ...getMediaConditions(themeVars.media),
    hover: {
        selector: "&:hover"
    },
    focus: {
        selector: "&:focus"
    },
    focusVisible: {
        selector: "&:focus-visible"
    },
    focusWithin: {
        selector: "&:focus-within"
    },
    active: {
        selector: "&:active"
    }
}

const defaultCondition = "_";

const properties = defineProperties({
    conditions,
    defaultCondition,
    properties: {
        marginTop: marginValues,
        marginBottom: marginValues,
        marginLeft: marginValues,
        marginRight: marginValues,
        paddingTop: themeVars.space,
        paddingBottom: themeVars.space,
        paddingLeft: themeVars.space,
        paddingRight: themeVars.space,
        textAlign: [
            "left",
            "center",
            "right"
        ],
        textTransform: [
            "uppercase",
            "capitalize",
            "lowercase"
        ],
        textDecoration: [
            "underline",
            "overline",
            "line-through"
        ],
        height: heightValues,
        minHeight: heightValues,
        maxHeight: heightValues,
        width: widthValues,
        minWidth: widthValues,
        maxWidth: widthValues,
        shadow: themeVars.shadow,
        overflow: [
            "hidden",
            "visible",
            "scroll",
            "auto"
        ],
        userSelect: [
            "all",
            "none",
            "text"
        ],
        pointerEvents: [
            "none",
            "auto"
        ],
        cursor: [
            "default",
            "pointer",
            "text",
            "grab",
            "grabbing"
        ],
        flexBasis: sizeValues,
        flexGrow: flexShrinkGrowValues,
        flexShrink: flexShrinkGrowValues,
        flexJustifyContent: [
            "flex-start",
            "flex-end",
            "center",
            "strethc",
            "space-between",
            "space-around",
            "space-evenly"
        ],
        flexAlignItems: alignValues,
        flexAlignSelf: [
            ...alignValues,
            "auto"
        ],
        flexDirection: [
            "row",
            "row-reverse",
            "column",
            "column-reverse",
        ],
        flexWrap: [
            "nowrap",
            "wrap",
            "wrap-reverse",
        ],
        rowGap: themeVars.space,
        columnGap: themeVars.space,
        display: [
            "none",
            "grid",
            "flex",
            "block",
            "inline",
            "inline-block",
            "inline-flex",
            "inline-grid"
        ],
        color: themeVars.color,
        backgroundColor: themeVars.color,
        opacity: themeVars.opacity,
        borderLeftStyle: borderStyleValues,
        borderRightStyle: borderStyleValues,
        borderTopStyle: borderStyleValues,
        borderBottomStyle: borderStyleValues,
        borderLeftColor: themeVars.color,
        borderRightColor: themeVars.color,
        borderTopColor: themeVars.color,
        borderBottomColor: themeVars.color,
        borderLeftWidth: themeVars.borderWidth,
        borderRightWidth: themeVars.borderWidth,
        borderTopWidth: themeVars.borderWidth,
        borderBottomWidth: themeVars.borderWidth,
        borderTopLeftRadius: themeVars.borderRadius,
        borderTopRightRadius: themeVars.borderRadius,
        borderBottomLeftRadius: themeVars.borderRadius,
        borderBottomRightRadius: themeVars.borderRadius,
        position: [
            "relative",
            "absolute",
            "static",
            "fixed",
            "sticky"
        ],
        top: positionValues,
        bottom: positionValues,
        left: positionValues,
        right: positionValues,
        boxShadow: themeVars.shadow
    },
    shorthands: {
        marginX: [
            "marginLeft",
            "marginRight"
        ],
        marginY: [
            "marginTop",
            "marginBottom"
        ],
        margin: [
            "marginLeft",
            "marginRight",
            "marginTop",
            "marginBottom"
        ],
        paddingX: [
            "paddingLeft",
            "paddingRight"
        ],
        paddingY: [
            "paddingTop",
            "paddingBottom"
        ],
        padding: [
            "paddingLeft",
            "paddingRight",
            "paddingTop",
            "paddingBottom"
        ],
        size: [
            "height",
            "width"
        ],
        mazSize: [
            "maxHeight",
            "maxWidth"
        ],
        minSize: [
            "minHeight",
            "minWidth"
        ],
        gap: [
            "rowGap",
            "columnGap"
        ],
        borderXStyle: [
            "borderLeftStyle",
            "borderRightStyle"
        ],
        borderYStyle: [
            "borderTopStyle",
            "borderBottomStyle"
        ],
        borderStyle: [
            "borderLeftStyle",
            "borderRightStyle",
            "borderTopStyle",
            "borderBottomStyle"
        ],
        borderXColor: [
            "borderLeftColor",
            "borderRightColor"
        ],
        borderYColor: [
            "borderTopColor",
            "borderBottomColor"
        ],
        borderColor: [
            "borderLeftColor",
            "borderRightColor",
            "borderTopColor",
            "borderBottomColor"
        ],
        borderXWidth: [
            "borderLeftWidth",
            "borderRightWidth"
        ],
        borderYWidth: [
            "borderTopWidth",
            "borderBottomWidth"
        ],
        borderWidth: [
            "borderLeftWidth",
            "borderRightWidth",
            "borderTopWidth",
            "borderBottomWidth"
        ],
        borderRadius: [
            "borderTopLeftRadius",
            "borderBottomLeftRadius",
            "borderTopRightRadius",
            "borderBottomRightRadius"
        ],
        borderLeftRadius: [
            "borderTopLeftRadius",
            "borderBottomLeftRadius"
        ],
        borderRightRadius: [
            "borderTopRightRadius",
            "borderBottomRightRadius"
        ],
        borderTopRadius: [
            "borderTopLeftRadius",
            "borderTopRightRadius"
        ],
        borderBottomRadius: [
            "borderBottomLeftRadius",
            "borderBottomRightRadius"
        ],
        insetX: [
            "left",
            "right"
        ],
        insetY: [
            "top",
            "bottom"
        ]
    }
});

export const styles = createSprinkles(properties);

type MediaConditions<T extends string> = {
    [K in T]: {
        "@media": string
    }
}

function getMediaConditions<T extends string>(media: Record<T, string>): MediaConditions<T> {

    let mediaConditions: any = {}

    for (const key in media) {

        const value = (media as any)[key];

        mediaConditions[key] = {
            "@media": value
        }
    }

    return mediaConditions;
}