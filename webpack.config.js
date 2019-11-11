module.exports = {
    entry: ".src/app.tsx",
    output:{
        filename: "./public/bundle.js"
    },
    devtool : "eval",
    resolve: {
        extensions: [".ts", ".tsx"]
    },
    module:{
        use:[
            { 
                test: /\.tsx?$/,
                loader: "ts-loader" 
            },
            {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader',
                ]
            },
        ]
    }
}