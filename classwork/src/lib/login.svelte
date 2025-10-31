<script>
    import Alert from './alert.svelte';
    import { fly, fade } from 'svelte/transition';
    import { createEventDispatcher } from 'svelte';
    import PassEye from './passEye.svelte';
    const dispatch = createEventDispatcher();
    let showPassword = false
    let show = false;
    let username = '';
    let password = '';
    let loader = false;
    let msg = '';
    let succes = true;
    const handleSubmit = (e) => {
        e.preventDefault();
        if (!VerifInfo(username)){
            msg = 'Please Check your username';
            show = true;
            succes = false
            loader = false
            setTimeout(() => {
                show = false
            }, 2000);
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
                body: formData,
                credentials: 'include'
            });
            const data = await res.json();
            if(!res.ok) throw new Error(data.message)
            msg = data.message
            succes = true
            show = true
            dispatch('authSuccess',{username: data.username})
        }catch(e){
            succes = false
            show = true
            msg = e
        }
        finally{
            loader = false
            setTimeout(() => {
                show = false
            }, 2000);
        }
    }
</script>

<Alert {show} {msg} {succes}/>

{#if loader}
    <div class="min-h-screen flex flex-row gap-2 justify-center items-center bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950">
        <div class="w-8 h-8 rounded-full bg-blue-800 animate-bounce"></div>
        <div class="w-8 h-8 rounded-full bg-blue-800 animate-bounce [animation-delay:-.3s]"></div>
        <div class="w-8 h-8 rounded-full bg-blue-800 animate-bounce [animation-delay:-.5s]"></div>
    </div>
{/if}
{#if !loader}
<section class="bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 min-h-screen flex flex-col items-center justify-center">
    <h1 class="text-center text-5xl text-white font-bold mb-5">Login</h1>
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
            <div class="relative">
                <label class="block text-slate-200 mb-1 ">Password</label>
                <input type={showPassword ? 'text' : 'password'} bind:value={password} placeholder="Enter your password" 
                    class="w-full p-3 pr-10 rounded-lg bg-slate-800 text-slate-100 focus:outline-none focus:ring-2 focus:ring-cyan-500" required />
                <PassEye bind:showPassword/>
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

