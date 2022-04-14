/**
 * @author Yousif Abdulkarim
 */



import { GlobalStyleRule } from "@vanilla-extract/css";

import { Styles } from "./types";



export const merge = (...stylesFNS: Styles[]): Styles => {

    return value => {

        let mergedStyles: GlobalStyleRule = {}

        for (const stylesFN of stylesFNS) {

            const styles = stylesFN(value);

            mergedStyles = {
                ...mergedStyles,
                ...styles
            }
        }

        return mergedStyles;
    }
}