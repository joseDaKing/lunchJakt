import { Disclosure } from "@headlessui/react";

import { ChevronUpIcon } from '@heroicons/react/solid'



export const Collapsible = ({ label, children }) => {

    return (
        <div className="block rounded-sm bg-blue-50">
            <Disclosure>
                {({ open }) => (
                    <>
                        <Disclosure.Button 
                        className="p-4 w-full text-blue-800 font-medium text-left flex hover:bg-blue-100 focus:bg-blue-100 focus:outline-none">
                            <span>
                                {label} 
                            </span>

                            <ChevronUpIcon
                            className={`h-6 w-6 ml-auto transition-transform ${open ? "rotate-180": ""}`}/>
                        </Disclosure.Button>
                        
                        {open && 
                        <Disclosure.Panel className="p-4 pt-2">
                            {children}
                        </Disclosure.Panel>}
                    </>
                )}
            </Disclosure>
        </div>
    );
}