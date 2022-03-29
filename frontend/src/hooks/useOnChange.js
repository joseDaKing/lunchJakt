import { useEffect, useRef } from "react";



export function useOnChange(cb, dependencies) {

    const isMountedRef = useRef(false);

    /* eslint-disable */
    useEffect(() => {

        if (isMountedRef.current) {

            const unmountCB = cb();

            if (unmountCB) {

                return unmountCB;
            }
        }

        isMountedRef.current = true;
    }, dependencies);
    /* eslint-enable */
}