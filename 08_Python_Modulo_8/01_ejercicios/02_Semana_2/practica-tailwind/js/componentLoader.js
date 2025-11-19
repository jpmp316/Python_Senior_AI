/**
 * ComponentLoader - Sistema seguro de carga de componentes HTML
 *
 * Cumple con OWASP Secure Coding Practices:
 * - No usa innerHTML (previene XSS)
 * - Usa DOMParser para parseo seguro
 * - Valida y sanitiza rutas de archivos
 *
 * @module ComponentLoader
 */

(function () {
  "use strict";

  /**
   * Carga un componente HTML de forma segura
   * @param {string} componentPath - Ruta relativa al componente
   * @param {string} targetSelector - Selector CSS del contenedor destino
   * @returns {Promise<void>}
   */
  async function loadComponent(componentPath, targetSelector) {
    try {
      // Validación de ruta (prevención de path traversal)
      if (
        !componentPath ||
        !componentPath.match(/^components\/[a-zA-Z0-9_-]+\.html$/)
      ) {
        throw new Error("Ruta de componente inválida");
      }

      // Obtener contenedor destino
      const targetElement = document.querySelector(targetSelector);
      if (!targetElement) {
        throw new Error(`Contenedor no encontrado: ${targetSelector}`);
      }

      // Cargar componente mediante fetch con timeout
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 5000); // 5 segundos timeout

      let response;
      try {
        response = await fetch(componentPath, { signal: controller.signal });
        clearTimeout(timeoutId);
      } catch (fetchError) {
        clearTimeout(timeoutId);
        if (fetchError.name === "AbortError") {
          throw new Error("Timeout al cargar el componente");
        }
        throw fetchError;
      }

      if (!response.ok) {
        throw new Error(
          `Error HTTP ${response.status}: ${response.statusText}`
        );
      }

      const htmlContent = await response.text();

      if (!htmlContent || htmlContent.trim().length === 0) {
        throw new Error("El componente está vacío");
      }

      // Parseo seguro usando DOMParser (no innerHTML)
      const parser = new DOMParser();
      const doc = parser.parseFromString(htmlContent, "text/html");

      // Extraer todos los elementos del body (ignorar comentarios y texto)
      const bodyElements = Array.from(doc.body.children);

      if (bodyElements.length === 0) {
        throw new Error("Componente vacío o inválido");
      }

      // Si hay múltiples elementos, crear un fragmento; si hay uno, usar ese
      const fragment = document.createDocumentFragment();
      bodyElements.forEach((element) => {
        // Clonar el elemento para evitar problemas de referencia
        const clonedElement = element.cloneNode(true);
        fragment.appendChild(clonedElement);
      });

      // Insertar componente de forma segura
      targetElement.appendChild(fragment);

      // Re-inicializar Flowbite después de un breve delay para asegurar que el DOM esté actualizado
      setTimeout(() => {
        if (typeof Flowbite !== "undefined" && Flowbite.init) {
          try {
            Flowbite.init();
          } catch (e) {
            console.warn("Error al inicializar Flowbite:", e);
          }
        }
      }, 100);
    } catch (error) {
      console.error(`Error cargando componente ${componentPath}:`, error);
      // Fallback: mostrar mensaje de error al usuario solo si el contenedor está vacío
      const targetElement = document.querySelector(targetSelector);
      if (targetElement && targetElement.children.length === 0) {
        const errorDiv = document.createElement("div");
        errorDiv.className =
          "bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-4";
        errorDiv.setAttribute("role", "alert");
        errorDiv.textContent = `Error al cargar componente: ${error.message}. Verifica la consola para más detalles.`;
        targetElement.appendChild(errorDiv);
      }
    }
  }

  /**
   * Inicializa la carga de todos los componentes
   */
  function initComponents() {
    let attempts = 0;
    const maxAttempts = 50; // Máximo 5 segundos de espera (50 * 100ms)

    // Esperar a que el DOM esté listo y Flowbite esté disponible
    function waitForFlowbite() {
      if (typeof Flowbite !== "undefined") {
        loadAllComponents();
      } else if (attempts < maxAttempts) {
        attempts++;
        // Reintentar después de 100ms si Flowbite aún no está disponible
        setTimeout(waitForFlowbite, 100);
      } else {
        console.warn(
          "Flowbite no se cargó a tiempo, cargando componentes de todas formas"
        );
        loadAllComponents();
      }
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", waitForFlowbite);
    } else {
      waitForFlowbite();
    }
  }

  /**
   * Carga todos los componentes definidos
   */
  async function loadAllComponents() {
    const components = [
      { path: "components/Header.html", target: "#header-container" },
      { path: "components/FormBookingDemo.html", target: "#form-container" },
      { path: "components/Footer.html", target: "#footer-container" },
    ];

    // Cargar componentes en paralelo
    await Promise.all(
      components.map((comp) => loadComponent(comp.path, comp.target))
    );
  }

  // Exponer API pública
  window.ComponentLoader = {
    load: loadComponent,
    init: initComponents,
  };

  // Auto-inicializar
  initComponents();
})();
