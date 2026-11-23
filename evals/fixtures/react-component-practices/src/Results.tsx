import { useEffect, useState } from 'react';
type Item = { id: string; name: string };
export function Results({ items, query }: { items: Item[]; query: string }) {
  const [visible, setVisible] = useState(items);
  useEffect(() => setVisible(items.filter((item) => item.name.includes(query))), [items]);
  return <ul>{visible.map((item, index) => <li key={index}>{item.name}</li>)}</ul>;
}
