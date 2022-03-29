import { useState } from "react";

import { Combobox } from "@headlessui/react";

import { useValue } from "../../hooks/useValue";

import { SearchIcon } from "@heroicons/react/solid";



export const SearchField = ({ 
    value,
    defaultValue,
    onValueChange,
    items = [],
    className
}) => {

    const [state, setState] = useValue({
        initialValue: "",
        value,
        defaultValue,
        onValueChange
    });

    const [query, setQuery] = useState()

    const filteredItems = query === "" ? items : items.filter(item => item.toLowerCase().includes(query));

    console.log(filteredItems)

    return (
        <div className={`bg-neutral-100 rounded-sm text-md text-blue-900 shadow-md ${className ?? ""}`}>
            <Combobox 
            value={state}
            onChange={setState}>
                {({ activeOption }) => (
                    <>
                        <div className="flex items-center">
                            <Combobox.Input
                            className="bg-transparent py-1 px-2 focus:outline-none flex-grow selection:bg-blue-300"
                            onChange={event => setQuery(event.currentTarget.value)}/>
                            
                            <SearchIcon 
                            className="h-8 w-8 py-1 pr-2 fill-blue-500"/>
                        </div>

                        <div
                        className="h-0">
                            <Combobox.Options
                            className="bg-slate-50 relative top-2 rounded-sm shadow-lg w-11/12 m-auto">
                                {filteredItems.map(item => (
                                    <Combobox.Option
                                    value={item}
                                    key={item}
                                    className={`py-1 px-2 cursor-pointer hover:bg-blue-100 select-none ${activeOption === item ? "bg-blue-100" : ""}`}>
                                        {item}
                                    </Combobox.Option>
                                ))}
                            </Combobox.Options>
                        </div>
                    </>
                )}
            </Combobox>
        </div>
    );
}