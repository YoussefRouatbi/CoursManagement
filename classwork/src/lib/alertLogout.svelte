<script>
    export openPopup
	let showPopup = false;

    function openPopup() {
		showPopup = true;
	}

	function closePopup() {
		showPopup = false;
	}

	function confirmLogout() {
		alert(`Goodbye ${username} 👋`);
		showPopup = false;
	}
</script>

<!-- Popup (s’affiche seulement si showPopup est true) -->
{#if showPopup}
	<div class="overlay">
		<div class="popup">
			<h2>Confirm Logout</h2>
			<p>
				You are logged in as <strong>{username}</strong>.<br>
				Password: <strong>{password}</strong>
			</p>

			<div class="btns">
				<button class="confirm" on:click={confirmLogout}>Confirm</button>
				<button class="cancel" on:click={closePopup}>Cancel</button>
			</div>
		</div>
	</div>
{/if}

<style>

	/* Arrière-plan flou */
	.overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: rgba(0, 0, 0, 0.5);
		backdrop-filter: blur(4px);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 1000;
	}


	.popup {
		background: white;
		padding: 25px 35px;
		border-radius: 15px;
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
		text-align: center;
		width: 320px;
		animation: popIn 0.25s ease;
	}

	.popup h2 {
		margin-bottom: 10px;
	}

	.popup p {
		color: #555;
		margin-bottom: 20px;
	}

	.btns {
		display: flex;
		justify-content: space-around;
	}

	.confirm {
		background-color: #4CAF50;
		color: white;
		border: none;
		padding: 8px 18px;
		border-radius: 8px;
		cursor: pointer;
		transition: background 0.3s;
	}

	.confirm:hover {
		background-color: #388e3c;
	}

	.cancel {
		background-color: #9e9e9e;
		color: white;
		border: none;
		padding: 8px 18px;
		border-radius: 8px;
		cursor: pointer;
		transition: background 0.3s;
	}

	.cancel:hover {
		background-color: #757575;
	}

	@keyframes popIn {
		from {
			transform: scale(0.9);
			opacity: 0;
		}
		to {
			transform: scale(1);
			opacity: 1;
		}
	}
</style>