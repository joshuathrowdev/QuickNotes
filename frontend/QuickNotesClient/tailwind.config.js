/** Enables IntelliSense and type checking for the Tailwind config in editors like VS Code */

/** @type {import('tailwindcss').Config} */

module.exports = {
  // Tells Tailwind which files to scan for utility class names to generate CSS
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  // Define your custom design system
  theme: {
    extend: {
      // Extend Tailwind's default them
      colors: {
        mainPurple: '#535bf2',
        mainLime: '#9AE69C',
      },
    },

  },
  // Plugins from the Tailwindcss/JS community
  plugins: [],
}