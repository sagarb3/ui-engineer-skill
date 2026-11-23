type Props = { value?: string; defaultValue?: string; onValueChange?: (value: string) => void };
export function TextField({ value, defaultValue, onValueChange }: Props) {
  return <input value={value || defaultValue || 'Untitled'} onChange={(event) => onValueChange?.(event.target.value)} />;
}
