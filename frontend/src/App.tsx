/**
 * @author Yousif Abdulkarim
 */



import { animated } from "react-spring";

import { Box } from "components/layout";

import { NotFoundPage, HomePage } from "pages";

import { BrowserRouter, Routes, Route } from "react-router-dom";



const App: React.FC = () => {
    
    return (
        <Box
        as="div"
        height="screen"
        display="flex"
        flexDirection="column"
        backgroundColor="neutral300">
            <Box
            as={animated.div}        
            padding="sm"
            flexGrow="1">
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
            </Box>
            <Box
            padding="sm"
            backgroundColor="inverted"
            borderTopRadius="lg"
            boxShadow="md"/>
        </Box>
    );
}

export default App;