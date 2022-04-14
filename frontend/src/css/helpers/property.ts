/**
 * @author Yousif Abdulkarim
 */



import { CSSProperties } from "@vanilla-extract/css";

import { Styles } from "./types";



export const property = (property: keyof CSSProperties): Styles => value => ({
    [property]: value
});