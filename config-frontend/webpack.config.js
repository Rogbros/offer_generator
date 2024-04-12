const path = require('path');

module.exports = {
  entry: './app/assets/js/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'app/static/js')
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        include: path.resolve(__dirname, 'app/assets/css'),
        use: ['style-loader', 'css-loader', 'postcss-loader'],
      }
    ]
  }
}