type Item = { name: string };
export function search(items: Item[], query: string) {
  return items.filter((item) => item.name.includes(query));
}
