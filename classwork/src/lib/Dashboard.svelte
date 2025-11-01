<script>
  let stats = { courses: 120, users: 450, views: 8500 };
</script>

<h2 class="text-3xl font-bold mb-6">Dashboard</h2>

<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
  {#each Object.entries(stats) as [label, value]}
    <div class="p-6 bg-slate-900/60 rounded-xl border border-white/10 shadow-lg">
      <p class="text-lg capitalize text-slate-400">{label}</p>
      <p class="text-4xl font-bold">{value}</p>
    </div>
  {/each}
</div>
