/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        darkbg: "#030712",
        cardbg: "rgba(10, 15, 30, 0.7)",
        cyanNeon: "#00f5ff",
        purpleNeon: "#7c3aed",
      },
      boxShadow: {
        glow: "0 0 30px rgba(0, 245, 255, 0.25)",
        purpleGlow: "0 0 30px rgba(124, 58, 237, 0.25)",
      }
    },
  },
  plugins: [],
}
