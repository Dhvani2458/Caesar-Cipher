async function process(action)
{
    const message = document.getElementById("message").value;
    const shift = document.getElementById("shift").value;

    const res = await fetch("/process",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message,shift,action})
    });

    const data = await res.json();

    document.getElementById("result").value = data.result;
    document.getElementById("status").innerText = data.status;
}

function encrypt(){
    process("encrypt");
}

function decrypt(){
    process("decrypt");
}

function clearAll(){
    document.getElementById("message").value="";
    document.getElementById("result").value="";
    document.getElementById("shift").value=3;
    document.getElementById("status").innerText="Cleared";
}

/* HISTORY PAGE */
async function loadHistory(){
    const res = await fetch("/get_history");
    const data = await res.json();

    const box = document.getElementById("historyBox");

    if(data.length === 0){
        box.innerHTML = "<p>No history found</p>";
        return;
    }

    box.innerHTML = data.map(item=>`
        <div class="card">
            <b>${item.action}</b><br>
            ${item.message}<br>
            Shift: ${item.shift}<br>
            Result: ${item.result}<br>
            <small>${item.time}</small>
        </div>
    `).join("");
}

async function clearHistory(){
    await fetch("/clear_history");
    loadHistory();
}