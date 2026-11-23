type Item = { id: string; name: string };
export function Results({ items, query }: { items: Item[]; query: string }) {
  const visible = items.sort((a, b) => a.name.localeCompare(b.name)).filter((item) => item.name.includes(query));
  return <ul>{visible.map((item) => <li key={item.id}>{item.name}</li>)}</ul>;
}
