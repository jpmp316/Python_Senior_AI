/**
 * Footer.jsx
 * Pie de página con información institucional vinculada al sistema de tareas.
 * @component
 * @author Cursor AI
 * @returns {JSX.Element}
 */
const Footer = () => (
  <footer className="w-full bg-slate-900 py-6 text-center text-slate-200">
    <div className="mx-auto flex max-w-5xl flex-col gap-2 px-4 sm:flex-row sm:items-center sm:justify-between">
      <p className="text-sm sm:text-base">Sistema de Tareas © 2025</p>
      {/* Se ofrece un enlace neutro para extender documentación futura */}
      <a
        href="https://owasp.org/www-project-proactive-controls/"
        target="_blank"
        rel="noreferrer noopener"
        className="text-xs font-medium uppercase tracking-wide text-sky-300 transition hover:text-sky-200"
      >
        Buenas prácticas OWASP
      </a>
    </div>
  </footer>
);

export default Footer;

/** IA Refactor Summary: Se adicionó un pie informativo con referencia a OWASP y estilos responsivos acordes al resto del layout. */

