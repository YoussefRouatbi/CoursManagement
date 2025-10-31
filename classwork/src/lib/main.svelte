<script>
  import Form from "./form.svelte";
  import { Search, ExternalLink } from "lucide-svelte";
  import { onMount } from "svelte";
  export {selected}

  let showModal = false;
  let searchKey = '';
  let course = [];
  let selected = 'Algorithme';
  let itemopt = '';
  let itemlng = '';
  let types = '';
  let loading = false

  $: if (selected) {
    if (selected === 'Language') {
      itemlng = '';
    } else if (selected === 'Options') {
      itemopt = '';
    }
    types = '';
  }

  function openModal() {
    showModal = true;
  }
  async function getCourses() {
    try{
      loading = true;
      const res = await fetch(`http://127.0.0.1:5000/courses?matier=${selected}`);
      const cours = await res.json()
      if(!res.ok)throw new Error()
      course = cours
    }catch(e){
      console.log(e)
    }finally{
      loading = false
    }
    
  }
 $: cour = course.filter(c => {
    const matchSearch = c.title?.toLowerCase().includes(searchKey.toLowerCase());
    return matchSearch;
  });

  $: if (selected) {
  getCourses();
}

  onMount(getCourses);
  function handleModalClose() {
    getCourses();
    return
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
{#if !loading}
  <main class="relative bg-slate-900 border border-white/10 shadow-lg w-full mt-[50px] rounded-lg min-h-[calc(100vh-60px)] p-6 md:p-8 backdrop-blur-md">
    <h2 class="text-3xl text-center text-white mb-5">{selected}</h2>
    <div class="flex justify-start items-center gap-5 flex-wrap mb-5">
        <div class="relative flex-1 min-w-[200px]">
          <input type="text" placeholder="Search..." bind:value={searchKey} class="w-full pl-10 pr-4 py-2 shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)]         text-white rounded-full focus:outline-none focus:ring-2 focus:ring-blue-200 transition-all"/>
          <Search class="w-5 h-5 text-gray-500 absolute left-3 top-1/2 transform -translate-y-1/2" />
        </div>
        {#if selected === 'Language'}
            <div class="">
                <select bind:value={itemlng} class="bg-slate-900 backdrop-blur-xl shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] pr-4 py-2 rounded-md text-semibold text-white focus:outline-none focus:ring-2 focus:ring-blue-200 transition-all">
                    <option value="">🌐 Select Language</option>
                    <option value="arabic">Arabic</option>
                    <option value="french">French</option>
                    <option value="english">English</option>
                </select>
            </div>
        {:else if selected === 'Options'}
            <div class="">
                <select bind:value={itemopt} class="bg-slate-900 backdrop-blur-xl shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] pr-4 py-2 rounded-md text-semibold text-white focus:outline-none focus:ring-2 focus:ring-blue-200 transition-all">
                    <option value="">🌐 Select Option</option>
                    <option value="spanish">Spanish</option>
                    <option value="germany">Germany</option>
                    <option value="italy">Italy</option>
                    <option value="art">Art</option>
                </select>
            </div>
        {/if}
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6 place-items-center w-full max-w-[1400px] pt-5">
        {#each cour as c}
  <div class="bg-white/10 backdrop-blur-sm border border-white/20 shadow-md rounded-2xl w-full h-50 flex flex-col justify-center items-center text-white text-lg font-semibold hover:scale-105 hover:shadow-lg transition-transform duration-300">
      <h3 class="text-lg font-semibold mb-2">{c.title}</h3>
      <img src="/public/pdf.png" alt="" class="">
        <p class="text-center text-sm text-white/70">{c.subtitle}</p>
        <a class="flex items-center gap-1 text-sm text-blue-500 cursor-pointer text-center transition-color duration-300 ease-out hover:underline hover:text-blue-600" href="{c.file_url}" target="_blank">Preview <ExternalLink class = 'w-4 h-4'/></a>
  </div>
{/each}
    </div>
    <button on:click={openModal} class="absolute bottom-6 right-8 backdrop-blur-3xl bg-white/10 shadow-xl border border-white/20 
        rounded-full flex justify-center items-center text-white hover:scale-110 transition-transform duration-300 cursor-pointer p-4 size-16">
        <img class="w-6 h-6" src="/public/plus.png" alt="add">
    </button>
    <Form bind:shown = {showModal} onClose = {handleModalClose}/>
</main>
{/if}
