module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'hhttp://localhost:5000/api/users',
                changeOrigin: true,
            },
        },
    },
    publicPath: '/',
};