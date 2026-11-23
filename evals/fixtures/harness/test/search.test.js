import assert from 'node:assert/strict';
import test from 'node:test';
import { search } from '../src/search.js';
test('matches an exact name', () => {
  assert.deepEqual(search([{ name: 'Oak' }], 'Oak'), [{ name: 'Oak' }]);
});
