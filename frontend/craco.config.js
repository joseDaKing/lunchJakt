const { VanillaExtractPlugin } = require("@vanilla-extract/webpack-plugin");



module.exports = {
    webpack: {
        plugins: [
            new VanillaExtractPlugin()
        ]
    }
}