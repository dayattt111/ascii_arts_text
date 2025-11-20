async function generate() {
    const text = document.getElementById('input').value;

    const res = await fetch('/api/generate.py', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });

    const data = await res.json();
    document.getElementById('output').textContent = data.ascii;
}

function copyText() {
    const ascii = document.getElementById('output').textContent;
    navigator.clipboard.writeText(ascii);
    alert("Berhasil disalin!");
}
