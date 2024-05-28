/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend:{
      colors:{
        electric_blue: '#65DEF1',
        tiffany_blue: '#A8DCD1',
        beige: '#DCE2C8',
        desert_sand:'#FAE8D9',
        pumpkin: '#F96900',
        safety_orange: '#F17F29'
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}