<script>
  import { Menu, X } from "lucide-svelte";
  import { createEventDispatcher } from "svelte";
  export { username, profileImg, opned };
  let username = "";
  let profileImg = "public/profile.png";
  let opned = true;
  const dispatch = createEventDispatcher();
  function toggleNav() {
    dispatch("toggle");
  }
</script>

<header
  class="fixed top-0 left-0 w-full max-w-full text-white flex items-center justify-between
         backdrop-blure-xl bg-slate-900 px-4 sm:px-6 py-3 shadow-xl z-40"
>
  <button on:click={toggleNav} class="flex-shrink-0">
    {#if !opned}
      <Menu class="w-6 h-6 text-white cursor-pointer" />
    {:else}
      <X class="w-6 h-6 text-white cursor-pointer" />
    {/if}
  </button>

  <h1 class="text-lg sm:text-2xl font-bold text-center flex-1 
             whitespace-nowrap overflow-hidden text-ellipsis">
    Course Management
  </h1>

  <div class="flex items-center gap-2 sm:gap-3 flex-shrink-0">
    <span class="font-medium hidden sm:block xs:inline">{username}</span>
    <img
      src={profileImg}
      alt="Profile"
      class="w-9 h-9 sm:w-10 sm:h-10 rounded-full object-cover"
    />
  </div>
</header>

