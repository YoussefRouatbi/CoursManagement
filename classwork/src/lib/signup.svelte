<script>
    import { fly, fade } from 'svelte/transition';
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    let show = false;
    let username = '';
    let email = '';
    let password = '';
    let confirmPassword = '';

    onMount(() => {
        show = true;
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }
        console.log({ username, email, password });
    };
</script>

{#if show}
<section class="bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 min-h-screen flex items-center justify-center">
    <div 
        class="bg-slate-900/80 backdrop-blur-md p-10 rounded-2xl shadow-2xl w-full max-w-md" transition:fly={{ y: 50, duration: 500 }}>
        <div class="flex justify-center mb-6">
            <img src="./public/profile.png" alt="Profile" class="w-24 h-24 rounded-full border-4 border-cyan-500" />
        </div>
        <form on:submit={handleSubmit} class="space-y-5">
            <div>
                <label class="block text-slate-200 mb-1">Username</label>
                <input type="text" bind:value={username} placeholder="Enter your username" 
                    class="w-full p-3 rounded-lg bg-slate-800 text-slate-100 focus:outline-none focus:ring-2 focus:ring-cyan-500" required />
            </div>

            <div>
                <label class="block text-slate-200 mb-1">Email</label>
                <input type="email" bind:value={email} placeholder="Enter your email" 
                    class="w-full p-3 rounded-lg bg-slate-800 text-slate-100 focus:outline-none focus:ring-2 focus:ring-cyan-500" required />
            </div>

            <div>
                <label class="block text-slate-200 mb-1">Password</label>
                <input type="password" bind:value={password} placeholder="Enter your password" 
                    class="w-full p-3 rounded-lg bg-slate-800 text-slate-100 focus:outline-none focus:ring-2 focus:ring-cyan-500" required />
            </div>

            <div>
                <label class="block text-slate-200 mb-1">Confirm Password</label>
                <input type="password" bind:value={confirmPassword} placeholder="Confirm your password" 
                    class="w-full p-3 rounded-lg bg-slate-800 text-slate-100 focus:outline-none focus:ring-2 focus:ring-cyan-500" required />
            </div>

            <button type="submit" 
                class="w-full py-3 shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] hover:scale-104 cursor-pointer rounded-lg text-white font-semibold transition">
                Sign Up
            </button>
        </form>

        <p class="text-slate-400 text-center mt-4 text-sm">
            Already have an account? <a on:click={() => dispatch('goToLogin')} class="text-cyan-500 hover:underline cursor-pointer">Login</a>
        </p>
    </div>
</section>
{/if}
