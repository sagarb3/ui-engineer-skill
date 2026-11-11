import type { ReactNode } from 'react';
type Props = { children: ReactNode };
export function ActionButton({ children }: Props) {
  return <button type="button" style={{ background: 'var(--action)', padding: 'var(--space-control)' }}>{children}</button>;
}
