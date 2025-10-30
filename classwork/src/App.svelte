<script>
  import { onMount } from "svelte";
  import Header from "./lib/header.svelte";
  import Navbar from "./lib/navbar.svelte";
  import Main from "./lib/main.svelte";
  import Login from './lib/login.svelte';
  import Signup from './lib/signup.svelte';
  import AlertLogout from "./lib/alertLogout.svelte";

  let pop = false
  let currentPage = 'login';
  let username = "Fakeuser";
  let opned = true;
  let selected = "Algorithme";
  let loading = false;

  onMount(async () => {
    try{
      loading = true
      const res = await fetch('http://127.0.0.1:5000/me',{
        method : 'GET',
        credentials : 'include'
      });
      const data = await res.json();
      if(!res.ok || !data.username) throw new Error();
      username = data.username;
      currentPage = 'app';
    }catch(e){
      console.error(e);
      currentPage = 'login';
    }finally{
      setTimeout(() => loading = false, 300);
    };
  });

  function HandelSelect(item) {
    selected = item;
  }
  function toggleNavbar() {
    opned = !opned;
  }

  function handleAuthSuccess(userData) {
    username = userData.username;
    currentPage = 'app';
  }
</script>

{#if loading}
  <div class="flex-col gap-4 w-full flex items-center justify-center min-h-screen z-40 bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950">
    <div class="w-20 h-20 border-4 border-transparent text-blue-400 text-4xl animate-spin flex items-center justify-center border-t-blue-800 rounded-full">
      <div class="w-16 h-16 border-4 border-transparent text-red-400 text-2xl animate-spin flex items-center justify-center border-t-blue-300 rounded-full">
      </div>
    </div>
  </div>
{/if}
{#if currentPage === 'app'}
  <div class="overflow-y-auto min-h-screen flex flex-col overflow-hidden bg-linear-to-b from-slate-800 via-slate-900 to-slate-950">
    <div class="z-40">
      <Header {username} {opned} on:toggle={toggleNavbar} />
    </div>
    <div class="flex flex-1 overflow-hidden">
      {#if opned}
        <Navbar onselect={HandelSelect} on:onLogout = {() => pop = true}/>
      {/if}
      <div class="flex flex-1 p-5">
        <Main {selected} />
      </div>
    </div>
  </div>
  <AlertLogout {pop} {username} on:logout = {() => (currentPage = 'login', pop = false)} on:cancel = {() => (currentPage = 'app', pop = false)}/>
{:else if currentPage === 'login'}
  <Login 
    on:goToSignup={() => currentPage = 'signup'} 
    on:authSuccess={(e) => handleAuthSuccess(e.detail)} 
  />
{:else if currentPage === 'signup'}
  <Signup 
    on:goToLogin={() => currentPage = 'login'} 
    on:auth_singedup={() => currentPage = 'login'} 
  />
{/if}
