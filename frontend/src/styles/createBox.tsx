/**
 * @author Yousif Abdulkarim
 */


import composeClassNames from "classnames";



type InferComponentProps<T> = T extends ((props: infer R) => any) ? R : {};

type Component = keyof JSX.IntrinsicElements | React.ComponentType<any>;

type BoxConfig<T, K extends Component> = {
    atoms: T,
    defaultComponent?: K;
    resetClassName?: string;
}

const defaultComponent = "div";

type BoxProps<T extends Component, ExtraProps> = (
    { as?: T } 
    & ExtraProps 
    & (
        T extends keyof JSX.IntrinsicElements ? 
            Omit<JSX.IntrinsicElements[T], "as">
        :
            InferComponentProps<T>
    )
);

type AtomProps<T> = T extends ((...args: any[]) => any)? Parameters<T>[0] : {};

export function createBox<Atoms, K extends Component = typeof defaultComponent>(config: BoxConfig<Atoms, K>) {

    return function<T extends Component = K>(props: BoxProps<T, AtomProps<Atoms>>) {

        const {
            as,
            className,
            ...restProps
        } = props;


        const atomProps = extractAtomProps(restProps, config.atoms);

        const htmlProps = extractComponentProps(restProps, config.atoms);

        const stylesClassName: string = (config.atoms as any)(atomProps);
    
        const Component: any = as ?? config.defaultComponent ?? defaultComponent;

        return (
            <Component
            {...(htmlProps as any)}
            className={composeClassNames(
                className,
                stylesClassName,
                config.resetClassName,
            )}>
                {htmlProps.children}
            </Component>
        );
    }
}

function extractAtomProps(props: any, atoms: any): any {

    const atomProps: Record<string, any> = {};

    for (const key in props) {

        const value = props[key];

        if (atoms.properties.has(key)) {

            atomProps[key] = value;
        }
    }

    return atomProps;
}

function extractComponentProps(props: any, atoms: any): any {

    const componentProps: Record<string, any> = {};

    for (const key in props) {

        const value = props[key];

        if (!atoms.properties.has(key)) {

            componentProps[key] = value;
        }
    }

    return componentProps;
}