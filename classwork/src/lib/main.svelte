<script>
  import Form from "./form.svelte";
  import { Search } from "lucide-svelte";
  import { onMount } from "svelte";
  let showModal = false;
  let cours = []; // will come from backend
  let searchKey = '';
  let selected = '';
  let itemopt = '';
  let itemlng = '';
  let types = '';
  let selectedMatier = 'Algorithme'; // from navbar

$: filteredCourses = cours.filter(c => {
    // Search by title
    const matchSearch = c.title?.toLowerCase().includes(searchKey.toLowerCase());

    // Filter by type select (All / Video / PDF)
    const matchType = types ? c.file_type === types : true;

    // Filter by selected matier from navbar
    const matchMatier = c.matier_name === selectedMatier;

    return matchSearch && matchType && matchMatier;
});

  // ✅ Fetch all courses
  async function fetchCourses() {
    try {
      const res = await fetch("http://127.0.0.1:5000/getCourses");
      if (!res.ok) throw new Error("Failed to fetch courses");
      cours = await res.json();
      console.log("Fetched courses:", cours);
    } catch (err) {
      console.error("Error fetching courses:", err);
    }
  }

  // ✅ When component mounts
  onMount(() => {
    fetchCourses();
  });

  // Modal logic
  function openModal() {
    showModal = true;
  }

  function handleModalClose() {
    console.log("Modal closed!");
    fetchCourses(); // refresh after adding new course
  }

  $: cour = cours.filter(c => {
  const matchSearch = c.title?.toLowerCase().includes(searchKey.toLowerCase());
  const matchType = types ? c.file_type === types : true; // use file_type from backend
  return matchSearch && matchType; // remove langdoc filters for now
});

  $: if (selected) {
    if (selected === 'Language') {
      itemlng = '';
    } else if (selected === 'Options') {
      itemopt = '';
    }
    types = '';
  }
</script>
<main class="relative bg-slate-900 border border-white/10 shadow-lg w-full mt-[50px] rounded-lg min-h-[calc(100vh-60px)] p-6 md:p-8 backdrop-blur-md">
    <h2 class="text-3xl text-center text-white mb-5">{selected}</h2>
    <div class="flex justify-start items-center gap-5 flex-wrap mb-5">
        <div class="relative flex-1 min-w-[200px]">
          <input type="text" placeholder="Search..." bind:value={searchKey} class="w-full pl-10 pr-4 py-2 shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)]         text-white rounded-full focus:outline-none focus:ring-2 focus:ring-blue-200 transition-all"/>
          <Search class="w-5 h-5 text-gray-500 absolute left-3 top-1/2 transform -translate-y-1/2" />
        </div>
        <div class="">
            <select bind:value={types} class="bg-slate-900 backdrop-blur-xl shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] pl-2 pr-4 py-2 rounded-md text-semibold text-white focus:outline-none focus:ring-2 focus:ring-blue-200 transition-all">
              <option value="">All Documents</option>
              <option value="vd">Video Types</option>
              <option value="pdf">Pdf Types</option>
            </select>
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
  <div
    class="bg-white/10 backdrop-blur-sm border border-white/20 shadow-md rounded-2xl w-full h-40 flex flex-col justify-center items-center text-white text-lg font-semibold hover:scale-105 hover:shadow-lg cursor-pointer transition-transform duration-300"
    on:click={() => window.open(c.file_path, "_blank")}
  >
    <h3 class="text-lg font-semibold mb-2">{c.title}</h3>
    <p class="text-sm text-white/70">{c.subtitle}</p>
  </div>
{/each}
    </div>
    

    <button on:click={openModal} class="absolute bottom-6 right-8 backdrop-blur-3xl bg-white/10 shadow-xl border border-white/20 
        rounded-full flex justify-center items-center text-white hover:scale-110 transition-transform duration-300 cursor-pointer p-4 size-16">
        <img class="w-6 h-6" src="/public/plus.png" alt="add">
    </button>
    <Form bind:show = {showModal} onClose = {handleModalClose}/>
</main>
