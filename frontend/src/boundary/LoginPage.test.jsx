import { test, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import LoginPage from './LoginPage';

test('shows email, password and login button', () => {
  render(<LoginPage />);
  expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /log in/i })).toBeInTheDocument();
});