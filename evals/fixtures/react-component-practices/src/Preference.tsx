export function Preference() {
  return <p>{localStorage.getItem('density') || 'comfortable'}</p>;
}
