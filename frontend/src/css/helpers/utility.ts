/**
 * @author Yousif Abdulkarim
 */



import { style, globalStyle } from "@vanilla-extract/css";

import { Styles } from "./types";



type UtilityConfig<T extends Record<string, string>> = {
    values: T;
    styles: Styles;
    extend?: string;
}

export const utility = <T extends Record<string, string>>({ values, styles, extend = "" }: UtilityConfig<T>): Record<keyof T, string> => {

    let utilities = {} as Record<keyof T, string>;

    for (const valueName in values) {

        const value = values[valueName];

        let selector = style({});

        const css = styles(value);

        if (extend[0] === "$") {

            selector = `${selector}${extend.slice(1)}`;
        }

        globalStyle(selector, css);

        (utilities as any)[valueName] = selector;
    }

    return utilities;
}