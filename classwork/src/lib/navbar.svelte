<script>
    import {fade, fly} from 'svelte/transition';
    export {selected}
    export let onselect
    let selected = 'Algorithme';
    function select(item){
        selected = item
        onselect(selected);
    }
</script>
<div class="min-h-[calc(100vh-60px)] w-[200px] backdrop-blure-xl shadow-3xl rounded-xl bg-white/5 flex flex-col space-y-5 p-5 mt-[70px] border border-white/20 " transition:fly = {{x:-99, duration:400}}>
    <div>
        <h1 class="text-white text-2xl">Matiers</h1>
        <hr class="text-white w-full">
    </div>
    <div class="space-y-3">
        <div class = {selected === 'Algorithme' ? "shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] w-full scale-110 text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2" : "text-center hover:bg-white/10 transition-all ease-in-out cursor-pointer p-3 rounded-md duration-300 flex col space-x-2"} on:click={() => select('Algorithme')}>
            <h2 class="text-white text-xl text-start w-full">Algorithme</h2><img class="w-8" src="/public/pc.png" alt="pc">
        </div>
        <div class = {selected === 'STI' ? "shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] w-full scale-110 text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2" : "text-center hover:bg-white/10 transition-all ease-in-out cursor-pointer p-3 rounded-md duration-300 flex col space-x-2"} on:click={() => select('STI')}>
            <h2 class="text-white text-xl text-start w-full">STI</h2><img class="w-8" src="/public/sti.png" alt="sti">
        </div>
        <div class = {selected === 'Math' ? "shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] w-full scale-110 text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2" : "text-center hover:bg-white/10 transition-all ease-in-out cursor-pointer p-3 rounded-md duration-300 flex col space-x-2"} on:click={() => select('Math')}>
            <h2 class="text-white text-xl text-start w-full">Math</h2><img class="w-8" src="/public/math.png" alt="math">
        </div>
        <div class = {selected === 'Physique' ? "shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] w-full scale-110 text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2" : "text-center hover:bg-white/10 transition-all ease-in-out cursor-pointer p-3 rounded-md duration-300 flex col space-x-2"} on:click={() => select('Physique')}>
            <h2 class="text-white text-xl w-full text-start">Physique</h2><img class="w-8" src="/public/phy.png" alt="phy">
        </div>
        <div class = {selected === 'Language' ? "shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] w-full scale-110 text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2" : "text-center hover:bg-white/10 transition-all ease-in-out cursor-pointer p-3 rounded-md duration-300 flex col space-x-2"} on:click={() => select('Language')}>
            <h2 class="text-white text-xl text-start w-full">Language</h2><img class="w-8" src="/public/lang.png" alt="lang">
        </div>
        <div class = {selected === 'Options' ? "shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] w-full scale-110 text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2" : "text-center hover:bg-white/10 transition-all ease-in-out cursor-pointer p-3 rounded-md duration-300 flex col space-x-2"} on:click={() => select('Options')}>
            <h2 class="text-white text-xl text-start w-full">Option</h2><img class="w-8" src="/public/opt1.png" alt="option">
        </div>
    </div>

    <div class="mt-[100px] text-white text-xl">
        <div>
            <h1 class="text-white text-2xl">Settings</h1>
            <hr class="text-white w-full mt-1 mb-3">
        </div>
        <div class="flex flex-col space-y-10">
            <div class="shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] hover:bg-white/5 w-full text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2">
                <h2 class="text-white text-xl text-start w-full">Logout</h2><img class="w-8" src="/public/logout.png" alt="pc">
            </div>
            <div class="shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] hover:bg-white/5 w-full text-center backdrop-blur-3xl border border-white/20 bg-white/10 shadow-3xl transition-out ease cursor-pointer p-3 rounded-md duration-500 flex col space-x-2">
                <h2 class="text-white text-xl text-start w-full" on:click={() => window.open('/about.html', '_blank')}>About Us</h2><img class="w-8" src="/public/abt2.png" alt="pc">
            </div>
        </div>
    </div>
</div>

