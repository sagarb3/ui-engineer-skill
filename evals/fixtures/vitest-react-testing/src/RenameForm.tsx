import { useState } from 'react';
export function RenameForm({ onSave }: { onSave: (name: string) => Promise<void> }) {
  const [name, setName] = useState('Draft');
  const [status, setStatus] = useState('');
  async function save() {
    setStatus('Saving');
    try { await onSave(name); setStatus('Saved'); }
    catch { setStatus('Save failed'); }
  }
  return <form onSubmit={(event) => { event.preventDefault(); void save(); }}>
    <label htmlFor="name">Project name</label>
    <input id="name" value={name} onChange={(event) => setName(event.target.value)} />
    <button type="submit" disabled={status === 'Saving'}>Save</button>
    <p role="status">{status}</p>
  </form>;
}
