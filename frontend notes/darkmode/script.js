// first ensure page has finished loading before doing any operations 
// checking if a theme doesnt exist in localStorage, if it doesnt we set it to "light"
window.addEventListener('load', () => {
    if (!localStorage.getItem('theme')) {
        localStorage.setItem('theme', 'light');
    }
// assigning an emoji to the button using the theme value in localStorage
//also, if current theme is "dark" adding a dark class to the body, this class used to override css properties with dark themee styles
    const themeSelector = document.querySelector('#themeSelector');
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark');
        themeSelector.textContent = '☀️';
    } else {
        themeSelector.textContent = '🌙️';
    }

    // functionality to add click event listener to theme selector button, and conditions to check if theme "dark" or "light" for example, if "light" then set theme value in localStorage to "dark" & set text content of button to a sun emoji else moon emoji and theme value in localStorage to "light"

    themeSelector.addEventListener('click', () => {
        if (localStorage.getItem('theme') === 'light') {
            localStorage.setItem('theme', 'dark');
            themeSelector.textContent = '☀️';
        } else {
            localStorage.setItem('theme', 'light');
            themeSelector.textContent = '🌙️';
        }
    // toggle the "dark" class on the body element, if dark mode enabled, the body tag will have a dark class (this class targets elements in CSS to apply dark theme)
        document.body.classList.toggle('dark');
    });
});
