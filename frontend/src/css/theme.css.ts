/**
 * @author Yousif Abdulkarim
 */



import { createTheme } from "@vanilla-extract/css";



export const [ theme, themeVars ] = createTheme({
    color: {
        primary: "",
        secondary: "",
        neutral: "",
        danger: "",
        success: "",
        warning: "",
    },
    space: {
        xxs: "",
        xs: "",
        sm: "",
        md: "",
        lg: "",
        xl: "",
        xxl: ""
    },
    size: {
        xxs: "",
        xs: "",
        sm: "",
        md: "",
        lg: "",
        xl: "",
        xxl: "",
    },
    fluid: {
        "1/5": "20%",
        "1/4": "25%",
        "1/3": "33.33%",
        "1/2": "50%",
        "2/3": "66.66%",
        "2/5": "40%",
        "3/5": "60%",
        "3/4": "75%",
        "4/5": "80%",
        full: "100%"
    },
    borderRadius: {
        xxs: "",
        xs: "",
        sm: "",
        md: "",
        lg: "",
        xl: "",
        xxl: "",
        round: ""
    },
    borderWidth: {
        sm: "1px",
        md: "2px",
        lg: "4px"
    },
    opacity: {
        12.5: "0.125",
        25: "0.25",
        50: "0.5",
        75: "0.75",
        87.5: "0.875",
    },
    shadow: {
        xss: "",
        xs: "",
        sm: "",
        md: "",
        lg: "",
        xl: "",
        xxl: ""
    },
    zIndex: {
        0: "0",
        10: "10",
        20: "20",
        30: "30",
        40: "40",
        50: "50",
    }
});

export type ThemeVars = typeof themeVars;