import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom'
import { Example } from '@/components/Example'

describe('Example', () => {
  it('Should Display', () => {
    render(<Example />)
    expect(screen.getByTestId('Example')).toBeInTheDocument()
    expect(screen.getByTestId('Example')).toHaveTextContent('Example Component')
  })
})
