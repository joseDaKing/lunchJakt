/**
 * @author Yousif Abdulkarim
 */



import { property, utility } from "../helpers";



export const userSelect = utility({
    values: {
        all: "all",
        none: "none",
        text: "text"
    },
    styles: property("userSelect")
});

export const pointerEvents = utility({
    values: {
        none: "none",
        auto: "auto"
    },
    styles: property("pointerEvents")
});

export const cursor = utility({
    values: {
        default: "default",
        pointer: "pointer",
        text: "text",
        grab: "grab",
        grabbing: "grabbing"
    },
    styles: property("cursor")
});