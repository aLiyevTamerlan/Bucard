/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,js}"],
  theme: {
    extend: {
      animation: {
        fadeIn: "fadeIn 500ms ease-in-out",
        fadeInModal: "fadeInModal 400ms ease-in-out",
        fadeOutModal: "fadeOutModal 400ms ease-in-out",
        fadeInTab: "fadeInTab 300ms ease-in-out",
        fadeOutTab: "fadeOutTab 300ms ease-in-out",
        swipeRight: "swipeRight 300ms ease-in-out",
        swipeLeft: "swipeLeft 300ms ease-in-out",
        opening: "opening 400ms cubic-bezier(0.4, 0, 0.6, 1)",
        drop: "drop 100ms ease-out",
        down: "down 75ms ease-in",
      },

      // that is actual animation
      keyframes: () => ({
        fadeIn: {
          "0%": {
            opacity: 0,
          },
          "100%": {
            opacity: 1,
          },
        },
        fadeInModal: {
          "0%": {
            transform: "translateY(75%)",
            "animation-timing-function": "cubic - bezier(0.8, 0, 1, 1)",
          },
          "100%": {
            transform: "translateY(0)",
            "animation-timing-function": "cubic - bezier(0, 0, 0.2, 1)",
          },
        },
        fadeOutModal: {
          "0%": {
            transform: "translateY(0)",
            "animation-timing-function": "cubic - bezier(0.8, 0, 1, 1)",
          },
          "100%": {
            transform: "translateY(100%)",
            "animation-timing-function": "cubic - bezier(0, 0, 0.2, 1)",
          },
        },
        fadeInTab: {
          "0%": {
            transform: "translateY(-120%)",
          },
          "100%": {
            transform: "translateY(0)",
          },
        },
        fadeOutTab: {
          "100%": {
            transform: "translateY(0)",
          },
          "0%": {
            transform: "translateY(120%)",
          },
        },
        swipeRight: {
          "0%": {
            transform: "translateY(0)",
          },
          "100%": {
            transform: "translateY(120%)",
          },
        },
        swipeLeft: {
          "100%": {
            transform: "translateX(0)",
          },
          "0%": {
            transform: "translateX(120%)",
          },
        },
        opening: {
          "0%": {
            transform: "scale(0.5)",
          },
        },
        drop: {
          "0%": {
            transform: "scale(0.95)",
            opacity: 0,
          },
          "100%": {
            transform: "scale(1)",
            opacity: 1,
          },
        },
        down: {
          "100%": {
            transform: "scale(1)",
            opacity: 1,
          },
          "0%": {
            transform: "scale(0.95)",
            opacity: 0,
          },
        },
      }),
      colors: {
        primary: "#115EED",
        secondary: "#23272F",
        optianal: "#12DB63",
        text: {
          black: "#535861",
        },
        icon: "#292D32",
        "border-primary": "#CBDDEB",
        "border-secondary": "#E5E4E4",
        profile: "#F2F7FF",
        avatar: "#F6F5F8",
        orange: { primary: "#FAA700" },
        bg: { mob: "#F8FBFF" },
      },
      boxShadow: {
        box: "0 0 12px rgba(17,94,237,0.06)",
      },
    },
  },
  plugins: [],
};
