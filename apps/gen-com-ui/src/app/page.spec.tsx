import { render, screen } from '@testing-library/react';
import Index from './page';

describe('page', () => {
  it('should render component', () => {
    render(<Index />);
    const el = screen.getByTestId('text-content');
    expect(el).toBeTruthy();
  });
});
