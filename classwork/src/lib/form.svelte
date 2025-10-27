<script>
    import { preventDefault } from "svelte/legacy";

  export let show = false;
  export let onClose = () => {}; 
  function closeModal() {
    show = false;
    onClose();
  }
  let typeS = ''
</script>

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

{#if show}
  <div class="modal-backdrop">
    <div class="modal-content max-h-screen p-4 backdrop-blur-xl bg-white/10 shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] border border-white/20 rounded-lg p-3 w-full mb-2">
      <span class="close-btn text-white" on:click={closeModal}>&times;</span>
      <h2 class="text-center text-white text-xl font-bold mb-1">Add Cours</h2>
      <p class="text-center text-sm text-white/50 mb-4">Share your cours with your freinds</p>
      <form>
        <div class="border border-white/10 rounded-md p-4">
        <input type="text" name="title" id="title" placeholder="Title" class="bg-slate-900 text-white border border-white/20 rounded-lg focus:outline-white p-3 w-full mb-2" required>
        <input type="text" name="Subtitle not oblg" id="Subtitle not oblg" placeholder="Subtitle not oblg" class="bg-slate-900 text-white border border-white/20 rounded-lg focus:outline-white p-3 w-full mb-2">
        <select required bind:value={typeS} name="type" id="type" class="text-white bg-slate-900 border border-white/20 rounded-lg focus:outline-white p-3 w-full mb-2">
            <option value="">Select type of cour</option>
            <option value="dc">Document</option>
            <option value="vd">Video</option>
        </select>
        {#if typeS === 'dc'}
            <div class="flex items-center justify-center w-full">
                <label class="flex justify-center items-center bg-slate-900 text-white border border-white/20 rounded-lg focus:outline-white p-3 w-full mb-2 shadow-lg cursor-pointer hover:scale-105 transform transition duration-300">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h10a4 4 0 004-4M16 7l-4-4m0 0L8 7m4-4v12" />
                    </svg>
                    <span class="text-sm font-medium">Choose a file</span>
                    <input required type="file" class="hidden" accept="application/pdf"/>
                </label>
            </div>
            {:else if typeS === 'vd'}
                <input required type="text" name="file" id="file" placeholder="Enter url of video" class="bg-slate-900 text-white border border-white/20 rounded-lg focus:outline-white p-3 w-full mb-2">
        {/if}
      </div>
      <div class="flex gap-3 mt-2">
        <button class="text-white w-full backdrop-blur-xl shadow-lg p-2 rounded-full cursor-pointer hover:scale-105 hover:bg-red-950 transition-all duration-100 ease-in" type="reset">Cancel</button>
        <button class="text-white w-full backdrop-blur-xl shadow-lg p-2 rounded-full cursor-pointer hover:scale-105 transition-all duration-100 ease-in hover:scale-105 hover:bg-green-950 transition-all duration-100 ease-in" type="submit">Add</button>
      </div>
      </form>
    </div>
  </div>
{/if}
