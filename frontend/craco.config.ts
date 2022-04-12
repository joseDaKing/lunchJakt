import { WebpackOptions } from "@craco/craco";

import { VanillaExtractPlugin } from "@vanilla-extract/webpack-plugin";



const webpack: WebpackOptions = {
    plugins: {
        add: [
            new VanillaExtractPlugin()
        ]
    }
}


export default {
    webpack
}