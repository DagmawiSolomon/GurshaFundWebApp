/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
],
  theme: {
    extend: {
      height: {
        '75': '85vh',
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

