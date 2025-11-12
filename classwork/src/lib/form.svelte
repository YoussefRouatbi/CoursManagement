<script>
  import Alert from "./alert.svelte";
  export let shown = true;
  export {selectedMatier}
  export let onClose = () => {};
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();
  const matiers = ['Algorithme', 'STI', 'Math', 'Physique', 'Language', 'Options'];
  let selectedMatier = '';
  let file = null;
  let title = '';
  let subtitle = '';
  let loader = false
  let succes = false
  let msg = '';
  let show = false
  function closeModal() {
    shown = false;
    onClose();
  }
  function handleFileSelect(e) {
    file = e.target.files[0];
  }

  async function UploadFile() {
    if (!file) {
      msg = "Please select a PDF file!";
      succes = false;
      show = true;
      setTimeout(() => show = false, 2000);
      return;
    }

    const DataInfo = new FormData();
    DataInfo.append('file', file);
    DataInfo.append('title', title);
    DataInfo.append('subtitle', subtitle);
    DataInfo.append('matier', selectedMatier);

    try {
      loader = true;
      const res = await fetch(`${import.meta.env.VITE_API_URL}/upload_file`, {
        method: 'POST',
        body: DataInfo
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.message);
      msg = data.message;
      succes = true;
      show = true;
      dispatch('added', selectedMatier);
      setTimeout(() => closeModal(), 500);
    } catch(e) {
      msg = e;
      succes = false;
      show = true;
    } finally {
      loader = false;
      setTimeout(() => show = false, 2000);
    }
}
</script>
<Alert {show} {msg} {succes}/>
{#if loader}
  <div class="mx-auto w-100 flex items-center justify-center h-100 z-40 bg-transparent backdrop-blur-xl">
    <div class="w-20 h-20 border-4 border-transparent text-blue-400 text-4xl animate-spin flex items-center justify-center border-t-blue-800 rounded-full">
      <div class="w-16 h-16 border-4 border-transparent text-red-400 text-2xl animate-spin flex items-center justify-center border-t-blue-300 rounded-full">
      </div>
    </div>
  </div>
{/if}
{#if shown}
<div class="modal-backdrop">
  <div class="modal-content max-h-screen p-4 backdrop-blur-xl bg-white/10 shadow-lg border border-white/20 rounded-lg w-full mb-2">
    <span class="close-btn text-white" on:click={closeModal}>&times;</span>
    <h2 class="text-center text-white text-xl font-bold mb-1">Add Course</h2>
    <p class="text-center text-sm text-white/50 mb-4">Share your course with your friends</p>

    <form on:submit|preventDefault = {UploadFile}>
      <div class="border border-white/10 rounded-md p-4">
        <input type="text" bind:value={title} placeholder="Title" class="bg-slate-900 text-white border border-white/20 rounded-lg p-3 w-full mb-2" required>
        <input type="text" bind:value={subtitle} placeholder="Subtitle (optional)" class="bg-slate-900 text-white border border-white/20 rounded-lg p-3 w-full mb-2">
        <select required bind:value={selectedMatier} class="text-white bg-slate-900 border border-white/20 rounded-lg p-3 w-full mb-2">
          <option value="">Select matier</option>
          {#each matiers as m}
            <option value={m}>{m}</option>
          {/each}
        </select>
        <div class="flex items-center justify-center w-full">
          <label class="flex justify-center items-center bg-slate-900 text-white border border-white/20 rounded-lg p-3 w-full mb-2 cursor-pointer hover:scale-105 transform transition duration-300">
            <span>Choose a PDF</span>
            <input type="file" class="hidden" name = 'file' accept="application/pdf" on:change={handleFileSelect} />
          </label>
        </div>
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
