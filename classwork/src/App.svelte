<script>
  import Header from "./lib/header.svelte";
  import Navbar from "./lib/navbar.svelte";
  import Main from "./lib/main.svelte";

  let username = "Habib";
  let profileImg = "public/profile.png";
  let opned = true;
  let selected = "Algorithme";
  function HandelSelect(item) {
    selected = item;
  }

  function toggleNavbar() {
    opned = !opned;
  }
</script>

<div
  class="overflow-y-auto min-h-screen flex flex-col overflow-hidden bg-linear-to-b from-slate-800 via-slate-900 to-slate-950"
>
  <div class="z-40">
    <Header {username} {profileImg} {opned} on:toggle={toggleNavbar} />
  </div>
  <div class="flex flex-1 overflow-hidden">
    {#if opned}
      <Navbar onselect={HandelSelect} />
    {/if}
    <div class="flex flex-1 p-5">
      <Main  />
    </div>
  </div>
</div>
