import { useState } from 'react'


export default function Home() {
const [text, setText] = useState('')
const [result, setResult] = useState(null)


async function callAPI(path, body) {
const res = await fetch(`/api/proxy?path=${path}`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(body)
})
return res.json()
}


async function analyzeResume() {
const r = await callAPI('predict_resume', { text })
setResult(r)
}


async function scoreAnswer() {
const r = await callAPI('score_answer', { answer: text })
setResult(r)
}


return (
<div style={{ padding: 24, fontFamily: 'Arial' }}>
<h1>hireHEAD — Demo frontend</h1>
<textarea value={text} onChange={e => setText(e.target.value)} rows={8} cols={80} />
<div style={{ marginTop: 12 }}>
<button onClick={analyzeResume}>Analyze Resume</button>
<button onClick={scoreAnswer} style={{ marginLeft: 12 }}>Score Answer</button>
</div>
<pre style={{ marginTop: 16 }}>{JSON.stringify(result, null, 2)}</pre>
</div>
)
}
