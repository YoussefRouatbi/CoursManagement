<script>
  export let show = false;
  export let onClose = () => {};
  
  // matier options hardcoded to match your SQL CHECK constraint
  const matiers = ['algo', 'sti', 'math', 'phy', 'lang', 'opt'];
  let selectedMatier = '';

  let typeS = '';
  let file = null;
  let title = '';
  let subtitle = '';
  let fileUrl = '';

  function closeModal() {
    show = false;
    onClose();
  }

  function handleFileSelect(e) {
    file = e.target.files[0];
  }

  async function handleSubmit() {
    try {
      let uploadedUrl = fileUrl;

      if (typeS === 'dc' && file) {
        const formData = new FormData();
        formData.append('file', file);
        const uploadRes = await fetch('http://127.0.0.1:5000/upload', {
          method: 'POST',
          body: formData
        });
        const uploadData = await uploadRes.json();
        if (!uploadRes.ok) throw new Error(uploadData.error || "Upload failed");
        uploadedUrl = uploadData.url;
      }

      const data = new URLSearchParams();
      data.append('title', title);
      data.append('subtitle', subtitle);
      data.append('file', uploadedUrl);
      data.append('type', typeS);
      data.append('matierName', selectedMatier);

      const saveRes = await fetch('http://127.0.0.1:5000/saveData', {
        method: 'POST',
        body: data
      });

      const saveData = await saveRes.json();
      if (!saveRes.ok) throw new Error(saveData.error || "Failed to save course");

      alert("Course added successfully!");
      closeModal();
    } catch (err) {
      console.error("Error:", err);
      alert("Error: " + err.message);
    }
  }
</script>

{#if show}
<div class="modal-backdrop">
  <div class="modal-content max-h-screen p-4 backdrop-blur-xl bg-white/10 shadow-lg border border-white/20 rounded-lg w-full mb-2">
    <span class="close-btn text-white" on:click={closeModal}>&times;</span>
    <h2 class="text-center text-white text-xl font-bold mb-1">Add Course</h2>
    <p class="text-center text-sm text-white/50 mb-4">Share your course with your friends</p>

    <form on:submit|preventDefault={handleSubmit}>
      <div class="border border-white/10 rounded-md p-4">
        <input type="text" bind:value={title} placeholder="Title" class="bg-slate-900 text-white border border-white/20 rounded-lg p-3 w-full mb-2" required>
        <input type="text" bind:value={subtitle} placeholder="Subtitle (optional)" class="bg-slate-900 text-white border border-white/20 rounded-lg p-3 w-full mb-2">

        <select required bind:value={typeS} class="text-white bg-slate-900 border border-white/20 rounded-lg p-3 w-full mb-2">
          <option value="">Select type of course</option>
          <option value="dc">Document</option>
          <option value="vd">Video</option>
        </select>

        <select required bind:value={selectedMatier} class="text-white bg-slate-900 border border-white/20 rounded-lg p-3 w-full mb-2">
          <option value="">Select matier</option>
          {#each matiers as m}
            <option value={m}>{m}</option>
          {/each}
        </select>

        {#if typeS === 'dc'}
        <div class="flex items-center justify-center w-full">
          <label class="flex justify-center items-center bg-slate-900 text-white border border-white/20 rounded-lg p-3 w-full mb-2 cursor-pointer hover:scale-105 transform transition duration-300">
            <span>Choose a PDF</span>
            <input required type="file" class="hidden" accept="application/pdf" on:change={handleFileSelect} />
          </label>
        </div>
        {:else if typeS === 'vd'}
        <input required type="text" bind:value={fileUrl} placeholder="Enter video URL" class="bg-slate-900 text-white border border-white/20 rounded-lg p-3 w-full mb-2">
        {/if}
      </div>

      <div class="flex gap-3 mt-2">
        <button type="reset" class="text-white w-full backdrop-blur-xl shadow-lg p-2 rounded-full hover:scale-105 hover:bg-red-950 transition-all">Cancel</button>
        <button type="submit" class="text-white w-full backdrop-blur-xl shadow-lg p-2 rounded-full hover:scale-105 hover:bg-green-950 transition-all">Add</button>
      </div>
    </form>
  </div>
</div>
{/if}

<style>
  .modal-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 50;
  }
  .modal-content {
    border-radius: 12px;
    padding: 20px;
    width: 90%;
    max-width: 400px;
    position: relative;
  }
  .close-btn {
    position: absolute;
    top: 8px;
    right: 12px;
    cursor: pointer;
    font-size: 20px;
    font-weight: bold;
  }
</style>
