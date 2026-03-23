export default async function handler(req, res) {
const BACKEND = process.env.BACKEND_URL || 'https://your-backend.onrender.com'
const path = req.query.path || ''
const url = `${BACKEND}/${path}`
try {
const fetchRes = await fetch(url, {
method: req.method,
headers: { 'Content-Type': 'application/json' },
body: req.method === 'GET' ? undefined : JSON.stringify(req.body)
})
const data = await fetchRes.json()
res.status(fetchRes.status).json(data)
} catch (err) {
res.status(500).json({ error: 'proxy error', details: err.message })
}
}
