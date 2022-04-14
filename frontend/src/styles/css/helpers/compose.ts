/**
 * @author Yousif Abdulkarim
 */



export const compose = <T extends Record<string, string>>(...stylesArr: T[]): Record<keyof T, string> => {

    const composedStyles = {} as Record<keyof T, string>;

    for (const styles of stylesArr) {

        for (const value in styles) {

            if (!composedStyles[value]) {

                composedStyles[value] = styles[value];
            }
            else {
                
                composedStyles[value] = `${composedStyles[value]} ${styles[value]}`
            }
        }
    }
    
    return composedStyles;
}