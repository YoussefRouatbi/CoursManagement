<script>
  let courses = [
    { title: "Python Basics", file: "/python.pdf" },
    { title: "Math", file: "/math.pdf" }
  ];
</script>

<h2 class="text-3xl font-bold mb-6">Manage Courses</h2>

<table class="w-full border-collapse">
  <thead class="bg-slate-800 text-slate-300">
    <tr>
      <th class="p-3 text-left">Title</th>
      <th class="p-3 text-left">Actions</th>
    </tr>
  </thead>

  <tbody>
    {#each courses as c}
      <tr class="border-b border-white/10">
        <td class="p-3">{c.title}</td>
        <td class="p-3 space-x-3">
          <a href={c.file} target="_blank" class="text-cyan-400 hover:underline">View</a>
          <button class="text-red-400 hover:text-red-300">Delete</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>
