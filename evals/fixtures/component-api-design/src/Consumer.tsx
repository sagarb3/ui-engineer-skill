import { TextField } from './TextField';
export function Consumer() {
  return <TextField value="" onValueChange={(value) => console.log(value)} />;
}
