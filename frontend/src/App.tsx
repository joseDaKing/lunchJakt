/**
 * @author Yousif Abdulkarim
 */



import { NotFoundPage, HomePage } from "pages";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import "css/normalize.css";

import classNames from "classnames";

import { padding } from "css/utilities";



const App: React.FC = () => {
    
    return (
        <div
        className={classNames(
            padding.sm
        )}>
            <BrowserRouter>
                <Routes>
                    <Route
                    path="/"
                    element={<HomePage/>}/>

                    <Route
                    path="*"
                    element={<NotFoundPage/>}/>
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;