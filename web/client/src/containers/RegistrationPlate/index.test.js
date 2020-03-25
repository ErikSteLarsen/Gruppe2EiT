import React from 'react';
import { render } from '@testing-library/react';
import RegistrationPlate from './';

test('renders learn react link', () => {
  const { getByText } = render(<RegistrationPlate />);
  expect(true).to.equal(false); // expect tests to be defined
});
