/**
 * @author Yousif Abdulkarim
 */



import { createTheme } from "@vanilla-extract/css";



export const [ theme, cssVariables ] = createTheme({
    color: {
        primary50: "#f0f9ff",
        primary100: "#e0f2fe",
        primary200: "#bae6fd",
        primary300: "#7dd3fc",
        primary400: "#38bdf8",
        primary500: "#0ea5e9",
        primary600: "#0284c7",
        primary700: "#0369a1",
        primary800: "#075985",
        primary900: "#0c4a6e",

        neutral50: "#f8fafc",
        neutral100: "#f1f5f9",
        neutral200: "#e2e8f0",
        neutral300: "#cbd5e1",
        neutral400: "#94a3b8",
        neutral500: "#64748b",
        neutral600: "#475569",
        neutral700: "#334155",
        neutral800: "#1e293b",
        neutral900: "#0f172a",
    },
    space: {
        xxs: "8px",
        xs: "16px",
        sm: "32px",
        md: "48px",
        lg: "64px",
        xl: "80px",
        xxl: "96px"
    },
    size: {
        xxs: "",
        xs: "",
        sm: "",
        md: "",
        lg: "",
        xl: "",
        xxl: "",
    }
});

const constVariables = {
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
        xxs: "2px",
        xs: "4px",
        sm: "8px",
        md: "16px",
        lg: "32px",
        xl: "64px",
        xxl: "128px",
        round: "9999px"
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
        sm: "0 .125rem .25rem rgba(0,0,0,.075)",
        md: "0 .5rem 1rem rgba(0,0,0,.15)",
        lg: "0 1rem 3rem rgba(0,0,0,.175)",
    },
    zIndex: {
        0: "0",
        10: "10",
        20: "20",
        30: "30",
        40: "40",
        50: "50",
    }
}

export const themeVariables = {
    ...cssVariables,
    ...constVariables
}