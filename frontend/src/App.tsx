import { NotFoundPage, HomePage } from "pages";

import { BrowserRouter, Routes, Route } from "react-router-dom";



const App: React.FC = () => {
    return (
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
    );
}

export default App;