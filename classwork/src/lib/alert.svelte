<script>
  import { fly } from 'svelte/transition';
  import { onDestroy } from 'svelte';

  export let succes = true;
  export let msg = '';
  export let show = false;

</script>

{#if show}
  <div
    class="fixed top-5 left-1/2 transform -translate-x-1/2 w-[100%] sm:w-auto min-w-md border-l-4 p-4 rounded-lg shadow-lg bg-gray-900 flex items-center space-x-3 z-40" class:border-green-400={succes} class:border-red-500={!succes}
    style="box-shadow: 0 0 15px {succes ? '#00ff99' : '#ff3300'};"
    in:fly={{ y: -50, duration: 400 }}
    out:fly={{ y: -50, duration: 400 }}
  >
    <svg 
      class="w-6 h-6 flex-shrink-0" 
      fill="none" stroke="currentColor" stroke-width="2" 
      viewBox="0 0 24 24"
      class:text-green-400={succes}
      class:text-red-500={!succes}
    >
      {#if succes}
        <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
      {:else}
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
      {/if}
    </svg>
    <div>
      <p class="font-bold text-lg" class:text-green-400={succes} class:text-red-500={!succes}>
        {succes ? 'Success' : 'Error'}
      </p>
      <p class="text-sm font-semibold mt-1" class:text-green-300={succes} class:text-red-400={!succes}>
        {msg}
      </p>
    </div>
  </div>
{/if}
