import PropTypes from 'prop-types'

const Navbar = ({ title }) => (
  <header className="w-full bg-white/80 py-6 shadow-lg shadow-sky-100 backdrop-blur">
    <div className="mx-auto flex max-w-4xl items-center justify-between px-4">
      <p className="text-lg font-semibold tracking-tight text-slate-900">{title}</p>
      <span className="hidden rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold uppercase tracking-wide text-sky-600 sm:inline">
        Panel principal
      </span>
    </div>
  </header>
)

Navbar.propTypes = {
  title: PropTypes.string.isRequired,
}

export default Navbar

