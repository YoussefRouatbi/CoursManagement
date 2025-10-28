<script>
    import { fly, fade } from 'svelte/transition';
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    let show = false;
    let username = '';
    let password = '';
    let loader = false;

    onMount(() => {
        show = true;
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!VerifInfo(username)){
            alert('verify your username');
            username = '';
            return;
        }
        LoginUser();
    };

    function VerifInfo(username){
        if (username.length > 15) return false;
        const pattern = /^[A-Za-z][A-Za-z0-9_]*$/;
        return pattern.test(username);
    }

    async function LoginUser(){
        loader = true;
        const formData = new FormData()
        formData.append('username',username);
        formData.append('password',password);
        try{
            const res = await fetch('http://127.0.0.1:5000/login', {
                method: 'POST',
                body: formData
            });
            if(!res.ok) throw new Error('User Not found')
            const data = await res.json();
            alert(data.message);
        }catch(e){
            alert(e)
        }
        finally{
            loader = false
        }
    }
</script>
{#if loader}
    <div class="min-h-screen flex flex-row gap-2 justify-center items-center bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950">
        <div class="w-8 h-8 rounded-full bg-blue-800 animate-bounce"></div>
        <div class="w-8 h-8 rounded-full bg-blue-800 animate-bounce [animation-delay:-.3s]"></div>
        <div class="w-8 h-8 rounded-full bg-blue-800 animate-bounce [animation-delay:-.5s]"></div>
    </div>
{/if}
{#if !loader}
<section class="bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 min-h-screen flex items-center justify-center">
    <div 
        class="bg-slate-900/80 backdrop-blur-md p-10 rounded-2xl shadow-2xl w-full max-w-md"
        transition:fly={{ y: 50, duration: 500 }}>
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
                <label class="block text-slate-200 mb-1">Password</label>
                <input type="password" bind:value={password} placeholder="Enter your password" 
                    class="w-full p-3 rounded-lg bg-slate-800 text-slate-100 focus:outline-none focus:ring-2 focus:ring-cyan-500" required />
            </div>

            <button type="submit" on:click={VerifInfo}
                class="w-full py-3 shadow-[0_0_20px_rgba(255,255,255,0.2),0_0_30px_rgba(59,130,246,0.4)] hover:scale-104 cursor-pointer rounded-lg text-white font-semibold transition">
                Login
            </button>
        </form>

        <p class="text-slate-400 text-center mt-4 text-sm">
            Don't have an account? <a class="text-cyan-500 hover:underline cursor-pointer" on:click={() => dispatch('goToSignup')}>Sign Up</a>
        </p>
    </div>
</section>
{/if}
