/**
 * @author Yousif Abdulkarim
 */



import { createBox } from "styles/createBox";

import { styles } from "styles/index.css";

import { resetClassName } from "styles/normalize.css";



export const Box = createBox({
    atoms: styles,
    resetClassName: resetClassName
});