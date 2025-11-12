<script>
  import { createEventDispatcher, onMount } from "svelte";
  export { setPage, page };
  const dispatch = createEventDispatcher();

  let page = 'dashboard';
  const setPage = p => page = p;
  let showConfirm = false

  let allUsers = [];
  let filteredUsers = [];
  let search = "";
  let currentPage = 1;
  const rowsPerPage = 10;
  let totalPages = 1;
  let loading = false

  let courses = [];
  let stats = { users: 0, courses: 0, views: 0 };

  let title = '';
  let fileInput;

  onMount(async () => {
    await fetchData();
    await FetchView()
  });

  async function FetchView(){
    try {
      const res = await fetch('http://localhost:5000/');
      const data = await res.json();
      stats.views = data.views;
    } catch (err) {
      console.error('Error fetching views:', err);
    }
  }

  async function fetchData() {
    try{
      loading = true
      const res = await fetch('http://127.0.0.1:5000/import')
      const data = await res.json();
      allUsers = data.users
      stats.users = data.nbUsers
      stats.courses = data.nbCourse
      courses = data.course
      if(!res.ok){throw new Error}
    }catch(e){
      alert(e)
    }finally{
      loading = false
    }
  }

  async function deleteFile(c) {
    const dataForm = new FormData()
    dataForm.append('title',c[0])
    dataForm.append('fileUrl',c[1])
    try{
      loading = true
      const res = await fetch(`http://127.0.0.1:5000/delete`,{
        method : 'POST',
        body : dataForm
      })
      const data = await res.json();
      if(!res.ok){throw new Error(data.message)}
      courses = courses.filter(course => course !== c);
      fetchData();
      alert(data.message)
      page = 'dashboard'
    }catch(e){
      alert(e)
    }finally{
      loading = false
    }
  }

  function updatePagination() {
    const filtered = allUsers.filter(u => u.username.toLowerCase().includes(search.toLowerCase()));
    totalPages = Math.ceil(filtered.length / rowsPerPage);
    if (currentPage > totalPages) currentPage = totalPages || 1;
    filteredUsers = filtered.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage);
  }

  function goToPage(p) { currentPage = p; updatePagination(); }
  function nextPage() { if(currentPage < totalPages) { currentPage++; updatePagination(); } }
  function prevPage() { if(currentPage > 1) { currentPage--; updatePagination(); } }

  $: updatePagination();
</script>
{#if loading}
  <div class="relative bg-slate-900 border border-white/10 shadow-lg w-full mt-[50px] rounded-lg min-h-[calc(100vh-60px)] p-6 md:p-8 backdrop-blur-md flex-col gap-4 w-full flex items-center justify-center bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950">
    <div class="w-20 h-20 border-4 border-transparent text-blue-400 text-4xl animate-spin flex items-center justify-center border-t-blue-800 rounded-full">
      <div class="w-16 h-16 border-4 border-transparent text-red-400 text-2xl animate-spin flex items-center justify-center border-t-blue-300 rounded-full">
      </div>
    </div>
  </div>
  {:else}
    <div class="flex min-h-screen bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 text-white">
  <aside class="w-64 bg-slate-900/60 backdrop-blur-xl border-r border-white/10 p-6 space-y-6">
    <h1 class="text-2xl font-bold">CourseAdmin</h1>
    <nav class="space-y-3">
      <button class="block w-full text-left py-2 px-3 rounded-lg hover:bg-slate-800/70" on:click={() => setPage('dashboard')}>📊 Dashboard</button>
      <button class="block w-full text-left py-2 px-3 rounded-lg hover:bg-slate-800/70" on:click={() => setPage('add')}>➕ Add Course</button>
      <button class="block w-full text-left py-2 px-3 rounded-lg hover:bg-slate-800/70" on:click={() => setPage('manage')}>📚 Manage Courses</button>
    </nav>
    <div class="absolute bottom-6">
      <button class="w-full bg-slate-800 cursor-pointer hover:bg-blue-900 p-3 rounded-lg" on:click={() => dispatch('logout')}>Leave</button>
    </div>
  </aside>

  <main class="flex-1 p-8 overflow-y-auto">
    {#if page === 'dashboard'}
      <h2 class="text-3xl font-bold mb-6">Dashboard</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {#each Object.entries(stats) as [label, value]}
          <div class="p-4 bg-slate-900/60 rounded-xl border border-white/10 shadow-lg">
            <p class="text-sm text-slate-400 uppercase">{label}</p>
            <p class="text-2xl font-bold">{value}</p>
          </div>
        {/each}
      </div>
      <div class="flex flex-col md:flex-row md:justify-between mb-2">
        <h3 class="text-xl font-bold mb-2 md:mb-0">Users</h3>
        <input
          type="text"
          placeholder="Search username..."
          bind:value={search}
          class="p-2 rounded-lg bg-slate-800 text-white border border-white/10 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        />
      </div>
      <div class="overflow-x-auto bg-slate-900/60 rounded-xl border border-white/10 shadow-lg">
        <table class="min-w-full text-sm divide-y divide-white/10">
          <thead class="bg-slate-800 text-slate-300">
            <tr>
              <th class="px-4 py-2 text-left">#</th>
              <th class="px-4 py-2 text-left">Username</th>
              <th class="px-4 py-2 text-left">Role</th>
              <th class="px-4 py-2 text-left">Date Inscription</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/10">
            {#each allUsers as user, i}
              <tr class="hover:bg-slate-800/40 transition">
                <td class="px-4 py-2">{(currentPage - 1) * rowsPerPage + i + 1}</td>
                <td class="px-4 py-2">{user[0]}</td>
                <td class="px-4 py-2">{user[1]}</td>
                <td class="px-4 py-2">{user[2]}</td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>

      <div class="mt-4 flex justify-center items-center space-x-2 text-sm">
        <button class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded-lg" on:click={prevPage} disabled={currentPage===1}>Previous</button>
        {#each Array(totalPages) as _, i}
          <button
            class="px-3 py-1 rounded-lg {currentPage===i+1 ? 'bg-cyan-600' : 'bg-slate-700 hover:bg-slate-600'}"
            on:click={()=>goToPage(i+1)}
          >{i+1}</button>
        {/each}
        <button class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded-lg" on:click={nextPage} disabled={currentPage===totalPages}>Next</button>
      </div>

    {:else if page === 'add'}
      <h2 class="text-3xl font-bold mb-6 mt-[100px]">Soon...</h2>
      <form class="space-y-5 max-w-lg">
        <div>
          <label class="block mb-1 text-slate-300">Course Title</label>
          <input class="w-full p-3 rounded-lg bg-slate-800 text-white" bind:value={title} required />
        </div>
        <div>
          <label class="block mb-1 text-slate-300">Upload PDF</label>
          <input type="file" accept="application/pdf" bind:this={fileInput} required />
        </div>
        <button class="bg-cyan-600 hover:bg-cyan-500 py-2 px-6 rounded-lg font-bold">Upload</button>
      </form>

    {:else if page === 'manage'}
      <h2 class="text-3xl font-bold mb-6 mt-[100px]">Manage Courses</h2>
      <table class="w-full border-collapse">
        <thead class="bg-slate-800 text-slate-300">
          <tr>
            <th class="p-3 text-left">Title</th>
            <th class="p-3 text-left">Actions</th>
          </tr>
        </thead>
        <tbody>
          {#each courses as c, i}
            <tr class="border-b border-white/10">
              <td class="p-3">{c[0]}</td>
              <td class="p-3 space-x-3">
                <a href={c[1]} target="_blank" class="text-cyan-400 hover:underline">View</a>
                <button class="text-red-400 hover:text-red-300" on:click={() => showConfirm = true}>Delete</button>
              </td>
            </tr>
            {#if showConfirm}
              <div class="fixed inset-0 flex items-center justify-center z-50">
                <div class="absolute inset-0 bg-black/50 backdrop-blur-sm"></div>
                <div class="relative bg-slate-900 text-white p-6 rounded-xl shadow-lg w-80">
                  <h2 class="text-lg font-bold mb-4">Delete File?</h2>
                  <p class="mb-6">Are you sure you want to delete this file?</p>
                  <div class="flex justify-end space-x-3">
                    <button class="bg-gray-700 hover:bg-gray-600 px-4 py-2 rounded-lg" on:click={() => showConfirm = false}>Cancel</button>
                    <button class="bg-red-600 hover:bg-red-500 px-4 py-2 rounded-lg" on:click={() => deleteFile(c)} on:click={() => showConfirm = false}>Delete</button>
                  </div>
                </div>
              </div>
            {/if}
          {/each}
        </tbody>
      </table>
    {/if}
  </main>
</div>
{/if}

