/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "chirpper-blue": "#1DA1F2",
        "chirpper-darkblue": "#107DC1",
        "chirpper-black": "#14171A",
        "chirpper-gray": "#657786",
        "chirpper-dark": "#AAB8C2",
        "chirpper-brown" : "#D9D9D9",
        "chirpper-brown-lite" : "#6F6F6F"
      },
    },
  },
  plugins: [],
};
