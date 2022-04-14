import classNames from "classnames"

import { padding } from "css/utilities";

import { forwardRef, PropsWithChildren } from "react";



export const AppContainer = forwardRef<HTMLDivElement, PropsWithChildren<{}>>((props, ref) => {

    return (
        <div
        ref={ref}
        className={classNames(
            padding.sm
        )}>
            {props.children}
        </div>
    );
})