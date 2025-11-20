async function generateASCII() {
    const text = document.getElementById("inputText").value;

    const res = await fetch("/api/generate?text=" + encodeURIComponent(text));
    const data = await res.json();

    document.getElementById("output").innerText = data.ascii;
}

function copyASCII() {
    const text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text);
    alert("ASCII berhasil disalin!");
}
