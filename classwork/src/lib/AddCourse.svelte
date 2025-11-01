<script>
  let title = '';
  let file = null;

  const submit = (e) => {
    e.preventDefault();
    console.log("Upload course:", title, file);
  }
</script>

<h2 class="text-3xl font-bold mb-6">Add Course</h2>

<form class="space-y-5 max-w-lg" on:submit={submit}>
  <div>
    <label class="block mb-1 text-slate-300">Course Title</label>
    <input class="w-full p-3 rounded-lg bg-slate-800 text-white"
      bind:value={title} required />
  </div>

  <div>
    <label class="block mb-1 text-slate-300">Upload PDF</label>
    <input type="file" accept="application/pdf"
       required />
  </div>

  <button class="bg-cyan-600 hover:bg-cyan-500 py-2 px-6 rounded-lg font-bold">
    Upload
  </button>
</form>
