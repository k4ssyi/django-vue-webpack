var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");
var VueLoaderPlugin = require("vue-loader/lib/plugin");

var env = process.env.NODE_ENV;

module.exports = {
  mode: "development",

  context: __dirname,

  entry: {
    main: "./assets/js/main.js" // エントリ名とエントリポイント
  },

  output: {
    path: path.resolve("./assets/webpack_bundles/"), // 出力
    filename: "[name]-[hash].js"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: "babel-loader"
      },
      {
        test: /\.vue$/,
        loader: "vue-loader"
      },
      {
        test: /\.scss$/,
        use: ["style-loader", "css-loader", "sass-loader"]
      },
      {
        test: /\.css$/,
        use: [
          "vue-style-loader",
          "style-loader",
          {
            loader: "css-loader",
            options: {
              url: false,
              sourceMap: true
            }
          }
        ]
      }
    ]
  },
  resolve: {
    extensions: [".js", ".vue"],
    modules: ["node_modules"],
    alias: {
      vue: path.resolve("./node_modules/vue/dist/vue.js")
    }
  },
  plugins: [
    new BundleTracker({ filename: "./webpack-stats.json" }),
    // .vueファイルを読み込めるようにする
    new VueLoaderPlugin()
  ]
};
