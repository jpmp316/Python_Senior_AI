import PropTypes from 'prop-types';

/**
 * Header.jsx
 * Cabecera principal del sistema de tareas, orientada a la bienvenida del usuario.
 * @component
 * @author Cursor AI
 * @param {object} props - Propiedades del componente.
 * @param {string} props.title - Título principal mostrado en la cabecera.
 * @param {string} props.subtitle - Mensaje secundario o de bienvenida.
 * @returns {JSX.Element}
 */
const Header = ({ title, subtitle }) => (
  <header className="w-full bg-white/90 py-8 shadow-lg shadow-sky-100 backdrop-blur">
    <div className="mx-auto flex max-w-5xl flex-col gap-4 px-4 text-center sm:flex-row sm:items-center sm:justify-between sm:text-left">
      <div>
        <h1 className="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl lg:text-5xl">
          {title}
        </h1>
        <p className="mt-2 text-sm text-slate-600 sm:text-base">{subtitle}</p>
      </div>
      {/* Etiqueta que refuerza el contexto del sistema en vistas de escritorio */}
      <span className="inline-flex items-center justify-center rounded-full bg-sky-50 px-4 py-2 text-xs font-semibold uppercase tracking-wide text-sky-600 shadow sm:text-sm">
        Panel principal
      </span>
    </div>
  </header>
);

Header.propTypes = {
  title: PropTypes.string.isRequired,
  subtitle: PropTypes.string,
};

Header.defaultProps = {
  subtitle: 'Gestiona tus tareas y mantén el foco diario.',
};

export default Header;

/** IA Refactor Summary: Se creó una cabecera reutilizable con tipado de props, estilos responsivos y documentación conforme a los requisitos. */

