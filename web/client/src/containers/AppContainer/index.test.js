import React from 'react';
import { render } from '@testing-library/react';
import AppContainer from './';

test('renders learn react link', () => {
  const { getByText } = render(<AppContainer />);
  expect(true).to.equal(false); // expect tests to be defined
});
