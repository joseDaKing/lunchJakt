/**
 * @author Yousif Abdulkarim
 */



import { property, utility } from "../helpers";



export const overflow = utility({
    values: {
        hidden: "hidden",
        visible: "visible",
        scroll: "scroll",
        auto: "auto"
    },
    styles: property("overflow")
});