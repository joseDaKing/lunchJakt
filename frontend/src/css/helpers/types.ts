/**
 * @author Yousif Abdulkarim
 */



import { GlobalStyleRule } from "@vanilla-extract/css";



export type Styles = (value: string) => GlobalStyleRule;

export type ToStr<T> = T extends string | number ? `${T}` : never;

export type InferLiteral<T> = (
    T extends (infer R) & string ? 
        R extends string ?
            R
        : never
    :
         never
)