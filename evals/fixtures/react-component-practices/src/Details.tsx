import { useEffect, useState } from 'react';
export function Details({ id, load }: { id: string; load: (id: string) => Promise<string> }) {
  const [value, setValue] = useState('');
  useEffect(() => { load(id).then(setValue); }, [id, load]);
  return <p>{value}</p>;
}
