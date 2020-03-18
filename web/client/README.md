# Gruppe 2 EiT web frontend

## Quickstart

For å kjøre frontend client:

`npm install` <- bare nødvendig første gang eller ved endringer i hvilke pakker vi bruker

`npm start` <- starter React development server, reload on file change


## Struktur

Prosjektet er organisert i containers og components for å skille logikk og presentasjon.

- Containers er React-komponenter som ikke viser innhold men holder styr på logikk, state osv
- Components er rent "presentational", dvs de bare presenterer informasjon og ikke har egen logikk.


This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

