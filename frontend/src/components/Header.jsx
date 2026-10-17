import { Link } from 'react-router'

export default function Header() {
  return (
    <header className="header">
      <Link to="/" className="header__logo">
        WorkHub
      </Link>
    </header>
  )
}
