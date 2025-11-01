<script>
  export let page;
  export let setPage;
</script>

<div class="flex min-h-screen bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 text-white">

  <!-- Sidebar -->
  <aside class="w-64 bg-slate-900/60 backdrop-blur-xl border-r border-white/10 p-6 space-y-6">
    <h1 class="text-2xl font-bold">CourseAdmin</h1>

    <nav class="space-y-3">
      <button class="block w-full text-left py-2 px-3 rounded-lg hover:bg-slate-800/70" on:click={() => setPage('dashboard')}>
        📊 Dashboard
      </button>
      <button class="block w-full text-left py-2 px-3 rounded-lg hover:bg-slate-800/70" on:click={() => setPage('add')}>
        ➕ Add Course
      </button>
      <button class="block w-full text-left py-2 px-3 rounded-lg hover:bg-slate-800/70" on:click={() => setPage('manage')}>
        📚 Manage Courses
      </button>
    </nav>

    <div class="absolute bottom-6">
      <button class="w-full bg-red-600 hover:bg-red-500 py-2 rounded-lg">Logout</button>
    </div>
  </aside>

  <!-- Page body -->
  <main class="flex-1 p-8">
    <slot />
  </main>
</div>
