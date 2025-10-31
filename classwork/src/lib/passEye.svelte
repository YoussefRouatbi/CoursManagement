<script>
  import { Eye, EyeClosed } from 'lucide-svelte';
  export let showPassword;
  const toggle = () => showPassword = !showPassword;
</script>

<span class="absolute right-2 top-1/2 cursor-pointer text-gray-500 hover:text-white transition" on:click={toggle} aria-label={showPassword ? "Hide password" : "Show password"}>
  {#if showPassword}
    <Eye size={20} />
  {:else}
    <EyeClosed size={20} />
  {/if}
</span>
