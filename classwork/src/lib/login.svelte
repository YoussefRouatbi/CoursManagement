<script>
  import { navigate } from "svelte-spa-router";

  let username = "";
  let password = "";
  let error = "";

  function handleLogin() {
    // simple check (you can later replace this with a real API)
    if (username === "admin" && password === "1234") {
      localStorage.setItem("loggedIn", "true");
      navigate("/main");
    } else {
      error = "Invalid username or password.";
    }
  }
</script>

<div class="login-container">
  <h2>Login</h2>
  {#if error}
    <p class="error">{error}</p>
  {/if}

  <input type="text" bind:value={username} placeholder="Username" />
  <input type="password" bind:value={password} placeholder="Password" />

  <button on:click={handleLogin}>Login</button>
</div>

<style>
  .login-container {
    max-width: 300px;
    margin: 100px auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .error {
    color: red;
  }
</style>
