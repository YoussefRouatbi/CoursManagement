<script>
  import { fade, fly } from 'svelte/transition';
  import { createEventDispatcher } from 'svelte';

  export let pop = false;
  export let username = '';
  const dispatch = createEventDispatcher();

  const handleLogout = () => {
    dispatch('logout');
  };

  const handleCancel = () => {
    dispatch('cancel');
  };

  async function Logout() {
	try{
		const res = await fetch('http://127.0.0.1:5000/logout',{
			method: "POST",
  			credentials: "include"
		})
		const data = await res.json(); 
		if(!res.ok) throw new Error();
		console.log(data.message)
		handleLogout();
	}catch(e){
		alert(e)
	}
  }
</script>

{#if pop}
  <div
    class="fixed inset-0 bg-black/70 backdrop-blur-md flex justify-center items-center z-50"
    transition:fade={{ duration: 200 }}
  >
    <div
      class="relative bg-slate-900 border border-slate-700/80 rounded-2xl shadow-[0_0_25px_rgba(15,23,42,0.9)] 
             p-8 w-[90%] sm:w-[420px] text-center text-white"
      in:fly={{ y: -40, duration: 300 }}
      out:fly={{ y: 40, duration: 200 }}
    >
      <div class="absolute -top-10 -right-10 w-40 h-40 bg-slate-700/20 blur-3xl rounded-full"></div>
      <div class="absolute -bottom-10 -left-10 w-40 h-40 bg-slate-700/20 blur-3xl rounded-full"></div>

      <h2 class="text-2xl font-semibold mb-3 text-gray-100">Confirm Logout</h2>
      <p class="text-gray-400 mb-6">
        Log out of Course Management as <span class="shadow-[0_0_25px_rgba(15,23,42,0.9)] font-bold text-white">{username}</span>
      </p>

      <div class="flex justify-center gap-4">
        <button
          on:click={handleCancel}
          class="px-5 py-2 rounded-lg border border-slate-600 bg-slate-800/70 cursor-pointer
                 hover:bg-slate-700 transition duration-200 text-gray-300 font-medium 
                 shadow-[0_0_10px_rgba(15,23,42,0.6)]"
        >
          Cancel
        </button>

        <button
          on:click={Logout}
          class="px-5 py-2 rounded-lg bg-gradient-to-r from-slate-700 to-slate-600 cursor-pointer
                 hover:from-slate-600 hover:to-slate-500 text-white font-semibold 
                 shadow-[0_0_15px_rgba(30,41,59,0.7)] hover:shadow-[0_0_20px_rgba(30,41,59,0.9)] 
                 transition duration-200"
        >
          Logout
        </button>
      </div>
    </div>
  </div>
{/if}
