/**
 * @author Yousif Abdulkarim
 */



import { property, utility } from "../helpers";



export const display = utility({
    values: {
        none: "none",
        grid: "grid",
        block: "block",
        inline: "inline",
        inlineBlock: "inline-block",
        inlineFlex: "inline-flex",
        inlineGrid: "inline-grid"
    },
    styles: property("display")
});