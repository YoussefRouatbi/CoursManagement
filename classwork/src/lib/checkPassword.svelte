<script>
  export let password = "";
  const minLength = 8;
  const hasLower = /[a-z]/;
  const hasUpper = /[A-Z]/;
  const hasDigit = /\d/;
  const hasSymbol = /[^A-Za-z0-9]/;

  $: lengthOk = password.length >= minLength;
  $: lowerOk = hasLower.test(password);
  $: upperOk = hasUpper.test(password);
  $: digitOk = hasDigit.test(password);
  $: symbolOk = hasSymbol.test(password);

  $: score =
    [lengthOk, lowerOk, upperOk, digitOk, symbolOk].filter(Boolean).length;

  $: scorePercent = (score / 5) * 100;

  $: label =
    scorePercent < 40 ? "Weak" :
    scorePercent < 80 ? "Medium" :
    "Strong";

  $: barColor =
    scorePercent < 40 ? "bg-red-500" :
    scorePercent < 80 ? "bg-yellow-400" :
    "bg-green-500";
</script>
<div class="w-full max-w-md mx-auto mt-4">
  <div class="w-full h-2 bg-gray-300 rounded mt-2 overflow-hidden">
    <div
      class={`h-2 rounded ${barColor} transition-all duration-500 ease-in-out`}
      style="width:{scorePercent}%"
    ></div>
  </div>
  <p class="mt-1 text-sm font-medium text-gray-700">Strength: {label}</p>
  <ul class="mt-2 text-sm space-y-1">
    <li class={lengthOk ? "text-green-500" : "text-red-500"}>Min {minLength} characters</li>
    <li class={lowerOk ? "text-green-500" : "text-red-500"}>Lowercase letter</li>
    <li class={upperOk ? "text-green-500" : "text-red-500"}>Uppercase letter</li>
    <li class={digitOk ? "text-green-500" : "text-red-500"}>Number</li>
    <li class={symbolOk ? "text-green-500" : "text-red-500"}>Symbol</li>
  </ul>
</div>