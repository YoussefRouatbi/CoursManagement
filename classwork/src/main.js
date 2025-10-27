import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'
import Login from './lib/login.svelte',
import MainPage from "./lib/main.svelte";

export default {
  "/": Login,
  "/main": MainPage,
};

const app = mount(App, {
  target: document.getElementById('app'),
})

export default app
