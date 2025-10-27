<script>
    import {Menu,X} from 'lucide-svelte'
    import {createEventDispatcher} from 'svelte'
    export {username,profileImg,opned};
    let username = "";
    let profileImg = "";
    let opned = true;
    const dispatch = createEventDispatcher();
    function toggleNav(){
      dispatch('toggle');
    }
</script>

<header class="fixed top-0 w-full text-white flex backdrop-blure-xl bg-white/5 items-center justify-between px-6 py-3 shadow-xl z-40">
  {#if !opned}
    <button on:click={toggleNav}><Menu class = 'w-6 h-6 text-white cursor-pointer'/></button>
  {/if}
  {#if opned}
    <button on:click={toggleNav}><X class = 'w-6 h-6 text-white cursor-pointer'/></button>
  {/if}
  <div class="w-10 sm:w-20"></div>
  <h1 class="text-xl sm:text-2xl font-bold text-center flex-1">
    Course Management
  </h1>
  <div class="flex items-center gap-3">
    <span class="font-medium">{username}</span>
    <img
      src={profileImg}
      alt="Profile"
      class="w-10 h-10 rounded-full  object-cover"
    />
  </div>
</header>