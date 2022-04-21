/**
 * Code taken from normalize.css
 * 
 * @link https://github.com/necolas/normalize.css/blob/master/normalize.css
 */

import { globalStyle, style } from "@vanilla-extract/css";



export const resetClassName = style({});

globalStyle("html", {
    lineHeight: 1.15,
    WebkitTextSizeAdjust: "100%"
});

globalStyle("body", {
    margin: 0
});

globalStyle(`${resetClassName} main`, {
    display: "block"
});
  
globalStyle(`${resetClassName} h1`, {
    fontSize: "2em",
    margin: "0.67em 0"
});

globalStyle(`${resetClassName} hr`, {
    boxSizing: "content-box",
    height: "0",
    overflow: "visible"
});
  
globalStyle(`${resetClassName} pre`, {
    fontFamily: "monospace, monospace",
    fontSize: "1em"
});

globalStyle(`${resetClassName} a`, {
    backgroundColor: "transparent"
});
  
globalStyle(`${resetClassName} abbr[title]`, {
    borderBottom: "none",
    textDecoration: ["underline", "underline dotted"],
});

globalStyle(`${resetClassName} b, ${resetClassName} strong`, {
    fontWeight: "bolder"
});

globalStyle(`${resetClassName} code, ${resetClassName} kbd, ${resetClassName} samp`, {
    fontFamily: "monospace, monospace",
    fontSize: "1em",
});

globalStyle(`${resetClassName} small`, {
    fontSize: "80%"
});

globalStyle(`${resetClassName} sub, ${resetClassName} sup`, {
    fontSize: "75%",
    lineHeight: "0",
    position: "relative",
    verticalAlign: "baseline"
});
  
globalStyle(`${resetClassName} sub`, {
    bottom: "-0.25em"
});
  
globalStyle(`${resetClassName} sup`, {
    top: "-0.5em"
});

globalStyle(`${resetClassName} img`, {
    borderStyle: "none"
});
  
globalStyle(`${resetClassName} button, ${resetClassName} input, ${resetClassName} optgroup, ${resetClassName} select, ${resetClassName} textarea`, {
    fontFamily: "inherit",
    fontSize: "100%",
    lineHeight: "1.15",
    margin: "0",
});

globalStyle(`${resetClassName} button, ${resetClassName} input`, {
    overflow: "visible"
});

globalStyle(`${resetClassName} button, ${resetClassName} select`, {
    textTransform: "none"
});
  
globalStyle(`${resetClassName} button, ${resetClassName} [type="button"], ${resetClassName} [type="reset"], ${resetClassName} [type="submit"]`, {
    WebkitAppearance: "button"
});

globalStyle(`${resetClassName} button::-moz-focus-inner, ${resetClassName} [type="button"]::-moz-focus-inner, ${resetClassName} [type="reset"]::-moz-focus-inner, ${resetClassName} [type="submit"]::-moz-focus-inner`, {
    borderStyle: "none",
    padding: 0
});
  
globalStyle(`${resetClassName} button:-moz-focusring, ${resetClassName} [type="button"]:-moz-focusring, ${resetClassName} [type="reset"]:-moz-focusring, ${resetClassName} [type="submit"]:-moz-focusring`, {
    outline: "1px dotted ButtonText"
});

globalStyle(`${resetClassName} fieldset`, {
    padding: "0.35em 0.75em 0.625em"
});

globalStyle(`${resetClassName} legend`, {
    boxSizing: "border-box",
    color: "inherit",
    display: "table",
    maxWidth: "100%",
    padding: "0",
    whiteSpace: "normal"
});

globalStyle(`${resetClassName} progress`, {
    verticalAlign: "baseline"
});
  
globalStyle(`${resetClassName} textarea`, {
    overflow: "auto"
});

globalStyle(`${resetClassName} [type="checkbox"], ${resetClassName} [type="radio"]`, {
    boxSizing: "border-box",
    padding: "0"
});

globalStyle(`${resetClassName} [type="number"]::-webkit-inner-spin-button, ${resetClassName} [type="number"]::-webkit-outer-spin-button`, {
    height: "auto"
});

globalStyle(`${resetClassName} [type="search"]`, {
    WebkitAppearance: "textfield",
    outlineOffset: "-2px"
});

globalStyle(`${resetClassName} [type="search"]::-webkit-search-decoration`, {
    WebkitAppearance: "none"
});

globalStyle(`${resetClassName} ::-webkit-file-upload-button`, {
    WebkitAppearance: "button",
    font: "inherit"
});

globalStyle(`${resetClassName} details`, {
    display: "block"
});

globalStyle(`${resetClassName} summary`, {
    display: "list-item"
});

globalStyle(`${resetClassName} template`, {
    display: "none"
});

globalStyle(`${resetClassName} [hidden]`, {
    display: "none"
});