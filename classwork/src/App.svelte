<script>
  import { onMount } from "svelte";
  import Header from "./lib/header.svelte";
  import Navbar from "./lib/navbar.svelte";
  import Main from "./lib/main.svelte";
  import Login from './lib/login.svelte';
  import Signup from './lib/signup.svelte';
  import AlertLogout from "./lib/alertLogout.svelte";
  import AdminLayout from "./lib/AdminLayout.svelte";

  let pop = false;
  let currentPage = 'login';
  let username = "Fakeuser";
  let opned = true;         
  let selected = "Algorithme";
  let loading = false;
  let page = "dashboard";
  const setPage = p => page = p;

  const setSelected = item => selected = item;

  function toggleNavbar() {
    opned = !opned;
  }

  function handleAuthSuccess(userData) {
    username = userData.username;
    console.log(userData)
    currentPage = userData.role === 'admin' ? 'appDash' : 'app';
  }

  onMount(async () => {
    try {
      loading = true;
      const res = await fetch(`${import.meta.env.VITE_API_URL}/me`, {
        method: 'GET',
        credentials: 'include'
      });
      const data = await res.json();
      if(!res.ok || !data.username) throw new Error();
      username = data.username;
      currentPage = data.role === 'admin' ? 'appDash' : 'app';
    } catch(e) {
      console.error(e);
      currentPage = 'login';
    } finally {
      setTimeout(() => loading = false, 300);
    }
  });
</script>

{#if loading}
  <div class="flex flex-col gap-4 w-full items-center justify-center min-h-screen bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950">
    <div class="w-20 h-20 border-4 border-transparent animate-spin border-t-blue-800 rounded-full flex items-center justify-center">
      <div class="w-16 h-16 border-4 border-transparent animate-spin border-t-blue-300 rounded-full"></div>
    </div>
  </div>
{:else}
  {#if currentPage === 'login'}
    <Login 
      on:goToSignup={() => currentPage = 'signup'}
      on:authSuccess={(e) => handleAuthSuccess(e.detail)}
    />
  {:else if currentPage === 'signup'}
    <Signup 
      on:goToLogin={() => currentPage = 'login'}
      on:auth_singedup={() => currentPage = 'login'}
    />
  {:else if currentPage === 'app'}
    <div class="flex flex-col min-h-screen bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 overflow-hidden">
      <Header {username} {opned} on:toggle={toggleNavbar}/>
      <div class="flex flex-1 overflow-hidden">
        {#if opned}
          <Navbar onselect={setSelected} on:onLogout={() => pop = true} on:onselect={(e) => selected = e.detail}/>
        {/if}
        <div class="flex flex-1 p-5">
          <Main {selected}/>
        </div>
      </div>
    </div>
    <AlertLogout 
      {pop} 
      {username} 
      on:logout={() => (currentPage = 'login', pop = false)} 
      on:cancel={() => (pop = false)} 
    />
  {:else if currentPage === 'appDash'}
  <div class="flex flex-col min-h-screen bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 overflow-hidden">
    <Header {username} {opned} on:toggle={toggleNavbar}/>
    <AdminLayout {page} {setPage} on:logout={() => pop = true} />
    <AlertLogout 
      {pop} 
      {username} 
      on:logout={() => (currentPage = 'login', pop = false)} 
      on:cancel={() => (pop = false)} 
    />
  </div>
{/if}

{/if}
