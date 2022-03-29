import { useState } from "react";

import { useOnChange } from "./useOnChange";



export function useValue({
    initialValue,
    defaultValue,
    value,
    onValueChange = () => {} 
}) {

    const [internalState, setInternalState] = useState(defaultValue ?? initialValue);

    useOnChange(() => {
        
        if (value !== undefined && onValueChange) {

            onValueChange(internalState);
        }
    }, [
        JSON.stringify(internalState)
    ]);

    return [
        value ? value : internalState,
        (state) => {

            if (value !== undefined) {

                if (typeof state === "function") {

                    onValueChange((state)(value))
                }
                else {

                    onValueChange(state);
                }
            }
            else {

                if (typeof state === "function") {

                    setInternalState(prevState => (state)(prevState))
                }
                else {

                    setInternalState(state);
                }
            }
        }
    ];
}