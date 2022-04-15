import { createBox } from "@dessert-box/react";

import { styles } from "styles/index.css";

import { resetClassName } from "styles/normalize.css";



export const Box = createBox({
    atoms: styles,
    defaultClassName: resetClassName
});