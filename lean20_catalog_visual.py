import streamlit as st
import re


# --- Page config ---
st.set_page_config(page_title="Catálogo de Herramientas Lean 2.0", layout="wide")
# --- Global styles ---
st.markdown(
    """
    <style>
    .page-title {
        text-align: center;
        font-size: 4rem; /* Más grande */
        font-weight: 900; /* Súper bold */
        color: #0d47a1; /* Azul profesional */
        margin-bottom: 2.5rem; /* Margen bajo */
    }
    .card {
        background: linear-gradient(135deg, #f0f4f8 0%, #ffffff 100%);
        border-radius: 1.25rem;
        padding: 1.5rem;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
        transition: transform 0.2s, box-shadow 0.2s;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.12);
    }
    .card-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #2196f3;
    }
    .card-title {
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #333;
    }
    .card-content {
        color: #555;
        font-size: 1rem;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- Page title ---
st.markdown('<div class="page-title">🚀 Catálogo de Herramientas Lean 2.0</div>', unsafe_allow_html=True)
st.image("assets/FOBO2.png", width=150)

# --- Helper function ---
def format_bold(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = text.replace('\n', '<br>')
    return text
# Definimos las herramientas como texto plano (sin st.markdown adentro)
# --- Tools ---
tools = {
    "Kaizen Colectivo": {
    "icon": "🤝",
    "description": """
    **¿Qué es?**  
    Kaizen Colectivo es una práctica que involucra a todos los miembros de una organización en el proceso de mejora continua. 
    Todos trabajan juntos para identificar áreas de mejora y proponer soluciones.

    **Beneficios Clave (Operativos y Humanos):**
    - Mejora continua en todos los niveles.
    - Fomenta la colaboración y comunicación.
    - Aumenta el compromiso y motivación del equipo.

    **Aporte a NOM-035:**
    - Promueve un ambiente de trabajo colaborativo y respetuoso.

    **Cómo Implementarlo:**
    - Organizar sesiones periódicas de Kaizen con equipos interfuncionales.

    **Indicadores de Éxito:**
    - Número de ideas implementadas por ciclo.
    - Participación activa de los empleados.

    **Métricas o KPIs Específicos:**
    - Aumento en la eficiencia operativa.
    - Reducción de costos operativos.

    **¿Por qué Funciona?**
    - Aprovecha la experiencia colectiva para impulsar mejoras reales y sostenibles.
    """,   },

   "Gemba con Propósito":{
    "icon": "👣",
    "description": """
    **¿Qué es?**  
    Gemba con Propósito implica que los líderes y empleados vayan al lugar de trabajo (el "gemba") para observar directamente los procesos y comprender mejor los problemas.

    **Beneficios Clave:**
    - Operativos: Mejora en la toma de decisiones basadas en la realidad del proceso.
    - Humanos: Mayor comprensión de las necesidades de los empleados.

    **Aporte a NOM-035:**
    - Fomenta la empatía y la comunicación en el lugar de trabajo.

    **Cómo Implementarlo:**
    - Los líderes deben visitar regularmente el lugar de trabajo para identificar oportunidades de mejora.

    **Indicadores de Éxito:**
    - Mejora en los tiempos de respuesta a problemas.
    - Satisfacción de los empleados.

    **Métricas o KPIs Específicos:**
    - Número de problemas resueltos tras las visitas de Gemba.
    - Tiempo de resolución de incidencias.

    **¿Por qué Funciona?**
    - Facilita una comprensión directa de los problemas y permite soluciones más efectivas y rápidas.
    """,  },

 "Kanban Ético":{
    "icon": "📋",
    "description": """
    **¿Qué es?**  
    Sistema visual de gestión de tareas, que balancea la carga de trabajo para reducir estrés y aumentar el bienestar.

    **Beneficios Clave:**
    - Operativos: Optimiza flujos de trabajo, identifica cuellos de botella.
    - Humanos: Previene sobrecarga y mejora la colaboración.

    **Aporte a NOM-035:**
    - Fomenta la empatía y la comunicación en el lugar de trabajo.

    **Cómo Implementarlo:**
    - Los líderes deben visitar regularmente el lugar de trabajo para identificar oportunidades de mejora.

    **Indicadores de Éxito:**
    - Mejora en los tiempos de respuesta a problemas.
    - Satisfacción de los empleados.

    **Métricas o KPIs Específicos:**
    - Número de problemas resueltos tras las visitas de Gemba.
    - Tiempo de resolución de incidencias.

    **¿Por qué Funciona?**
    - Facilita una comprensión directa de los problemas y permite soluciones más efectivas y rápidas.
    """,  },

 "Mapeo de Causa-Laboral":{
    "icon": "🧠",
    "description": """
    **¿Qué es?**  
    Herramienta para analizar problemas sistémicos considerando factores humanos y organizacionales.

    **Beneficios Clave:**
    - Operativos: Identifica causas raíz humanas y organizativas.
    - Humanos: Aborda problemas sin culpar a individuos, enfocándose en sistemas.

    **Aporte a NOM-035:**
    - Detecta riesgos psicosociales ocultos y diseña soluciones sistémicas.

    **Cómo Implementarlo:**
    - Realizar sesiones de análisis de causa.
    - Usar diagramas de Ishikawa o 5 Porqués enfocados en personas.

    **Indicadores de Éxito:**
    - Número de causas raíz corregidas.

    **Métricas o KPIs Específicos:**
    - Reducción de incidentes relacionados a fallos humanos.

    **¿Por qué Funciona?**
    - El enfoque sistémico minimiza errores y promueve un ambiente de mejora continua sin culpabilidad.
    """,  },
 "Andon Humano 4.0":{
    "icon": "🚨",
    "description": """
    **¿Qué es?**  
    Sistema visual de alertas donde cualquier colaborador puede señalar problemas en tiempo real.

    **Beneficios Clave:**
    - Operativos: Respuesta inmediata a problemas.
    - Humanos: Empoderamiento para alzar la voz sin represalias.

    **Aporte a NOM-035:**
    - Fomenta un entorno de participación activa y comunicación abierta.

    **Cómo Implementarlo:**
    - Instalar sistemas Andon visuales (luces, apps, pantallas).
    - Capacitar en reporte de incidentes sin miedo.

    **Indicadores de Éxito:**
    - Tiempo de respuesta a alertas.
    - Tasa de resolución en primer intento.

    **Métricas o KPIs Específicos:**
    - # de activaciones de Andon por mes.
    - % de alertas resueltas en menos de 24 horas.

    **¿Por qué Funciona?**
    - Promueve intervención temprana, evitando escaladas de problemas operativos y humanos.
    """,  },

 "Poka-Yoke Inclusivo":{
    "icon": "🛡️",
    "description": """
    **¿Qué es?**  
    Método para prevenir errores humanos antes de que ocurran mediante mejoras simples en procesos.

    **Beneficios Clave:**
    - Operativos: Aumenta la calidad y reduce defectos.
    - Humanos: Reduce el estrés y el miedo a equivocarse.

    **Aporte a NOM-035:**
    - Disminuye errores que puedan generar conflictos, sanciones o desgaste emocional.

    **Cómo Implementarlo:**
    - Identificar errores comunes.
    - Diseñar mecanismos de prevención (checklists, validaciones automáticas, señalizaciones).

    **Indicadores de Éxito:**
    - Reducción de errores operativos.

    **Métricas o KPIs Específicos:**
    - % de reducción de errores recurrentes.

    **¿Por qué Funciona?**
    - Elimina la posibilidad de fallas antes de que afecten al sistema o al colaborador.
    """,  },

"PDCA / PDSA Sostenible":{
    "icon": "🔄",
    "description": """
    **¿Qué es?**  
    Ciclo sistemático para planificar, ejecutar, verificar y actuar sobre mejoras continuas, enfocado en procesos humanos.

    **Beneficios Clave:**
    - Operativos: Mejora constante de procesos.
    - Humanos: Involucra activamente a las personas en la mejora.

    **Aporte a NOM-035:**
    - Promueve participación activa, disminuyendo riesgos psicosociales.

    **Cómo Implementarlo:**
    - Planificar mejoras con el equipo.
    - Ejecutar pequeños cambios.
    - Verificar resultados y ajustar.

    **Indicadores de Éxito:**
    - Número de ciclos PDCA completados.

    **Métricas o KPIs Específicos:**
    - % de mejoras exitosas implementadas.

    **¿Por qué Funciona?**
    - Fomenta experimentación segura y aprendizaje colectivo.
    """,  },

"Hoshin Kanri Humanista":{
    "icon": "🎯",
    "description": """
    **¿Qué es?**  
    Sistema de despliegue estratégico enfocado en el alineamiento entre los objetivos de la organización y las necesidades humanas.

    **Beneficios Clave:**
    - Operativos: Mejora la ejecución estratégica.
    - Humanos: Da sentido y propósito al trabajo cotidiano.

    **Aporte a NOM-035:**
    - Contribuye a la claridad de roles y objetivos, reduciendo ansiedad e incertidumbre.

    **Cómo Implementarlo:**
    - Definir objetivos estratégicos claros.
    - Traducirlos en planes tácticos por equipo.
    - Monitorear cumplimiento en cascada.

    **Indicadores de Éxito:**
    - Nivel de alineación de objetivos personales y organizacionales.

    **Métricas o KPIs Específicos:**
    - % de objetivos estratégicos cumplidos.

    **¿Por qué Funciona?**
    - Genera propósito compartido y compromiso genuino.
    """,  },

"5S+2 Centrado en las Personas": {
    "icon": "🧽",
    "description": """
    **¿Qué es?**  
    Expansión del método 5S tradicional, incluyendo componentes de bienestar y humanización del espacio de trabajo.

    **Beneficios Clave:**
    - Operativos: Entornos de trabajo más limpios y organizados.
    - Humanos: Mejora la ergonomía y el confort.

    **Aporte a NOM-035:**
    - Reduce riesgos físicos y promueve entornos seguros y saludables.

    **Cómo Implementarlo:**
    - Aplicar 5S tradicionales (clasificar, ordenar, limpiar, estandarizar, sostener).
    - Agregar "Salud" y "Socialización" como S adicionales.

    **Indicadores de Éxito:**
    - Orden y limpieza sostenidos.

    **Métricas o KPIs Específicos:**
    - % de áreas auditadas con cumplimiento de 5S+2.

    **¿Por qué Funciona?**
    - Genera orden externo e interno, impactando positivamente en el estado mental.
    """,  },
"Ethical FMEA:Análisis Modal de Fallos Ético":{
    "icon": "⚖️",
    "description": """
    **¿Qué es?**  
    Análisis de modos y efectos de falla aplicado con un enfoque humano, priorizando riesgos psicosociales y operativos.

    **Beneficios Clave:**
    - Operativos: Prevención de fallos críticos en procesos.
    - Humanos: Prevención de riesgos que afectan el bienestar emocional.

    **Aporte a NOM-035:**
    - Identifica y mitiga riesgos psicosociales y físicos.

    **Cómo Implementarlo:**
    - Realizar sesiones FMEA incorporando variables humanas.
    - Evaluar severidad, ocurrencia y detección considerando impacto en personas.

    **Indicadores de Éxito:**
    - Reducción de incidentes y riesgos detectados.

    **Métricas o KPIs Específicos:**
    - % de riesgos mitigados del total identificado.

    **¿Por qué Funciona?**
    - Integra la dimensión humana en la prevención de errores críticos.
    """,  },

"VSM de Equilibrio Laboral": {
    "icon": "🗺️",
    "description": """
    **¿Qué es?**  
    Mapeo del flujo de valor que prioriza tanto la eficiencia operativa como el bienestar humano.

    **Beneficios Clave:**
    - Operativos: Optimiza procesos eliminando desperdicios.
    - Humanos: Identifica sobrecargas y cuellos de botella humanos.

    **Aporte a NOM-035:**
    - Detecta puntos de sobreesfuerzo y estrés laboral.

    **Cómo Implementarlo:**
    - Mapear procesos actuales incluyendo tiempos humanos.
    - Identificar y priorizar mejoras de equilibrio.

    **Indicadores de Éxito:**
    - Reducción de tiempos muertos y sobrecargas.

    **Métricas o KPIs Específicos:**
    - % de reducción de carga laboral desequilibrada.

    **¿Por qué Funciona?**
    - El enfoque dual (operativo y humano) garantiza flujos sostenibles.
    """,  },

"Takt Time Laboral": {
    "icon": "⏱️",
    "description": """
    **¿Qué es?**  
    Medición del ritmo de trabajo ideal para satisfacer la demanda sin sobrecargar a los colaboradores.

    **Beneficios Clave:**
    - Operativos: Establece flujos de trabajo sostenibles.
    - Humanos: Evita cargas de trabajo excesivas.

    **Aporte a NOM-035:**
    - Minimiza riesgos derivados de la presión excesiva.

    **Cómo Implementarlo:**
    - Calcular Takt Time con base en la demanda y capacidad realista de la fuerza laboral.
    - Ajustar cargas de trabajo de acuerdo a resultados.

    **Indicadores de Éxito:**
    - Cumplimiento sostenido de metas sin sobretiempos.

    **Métricas o KPIs Específicos:**
    - % de procesos alineados al Takt Time saludable.

    **¿Por qué Funciona?**
    - Sincroniza productividad con bienestar humano de forma estructurada.
    """,  },

"Jidoka Ético":{
    "icon": "🛑",
    "description": """
    **¿Qué es?**  
    Sistema de autonomización que integra criterios éticos de protección al trabajador en la detección y corrección de errores.

    **Beneficios Clave:**
    - Operativos: Mejora la calidad del producto y procesos.
    - Humanos: Reduce el impacto de errores en los trabajadores.

    **Aporte a NOM-035:**
    - Asegura intervención inmediata ante fallos que puedan afectar la salud mental o física.

    **Cómo Implementarlo:**
    - Instalar mecanismos de detección automática de errores.
    - Empoderar a colaboradores para detener procesos inseguros.

    **Indicadores de Éxito:**
    - Reducción de errores críticos.

    **Métricas o KPIs Específicos:**
    - % de fallos detectados automáticamente y corregidos.

    **¿Por qué Funciona?**
    - Combina calidad técnica con respeto por la dignidad laboral.
    """,  },

"Heijunka Humano": {
    "icon": "⚙️",
    "description": """
    **¿Qué es?**  
    Herramienta para nivelar la carga de trabajo evitando picos de esfuerzo perjudiciales para la salud.

    **Beneficios Clave:**
    - Operativos: Incrementa la eficiencia continua.
    - Humanos: Previene estrés y agotamiento.

    **Aporte a NOM-035:**
    - Reduce las fluctuaciones estresantes en las demandas laborales.

    **Cómo Implementarlo:**
    - Análisis de demanda y redistribución de carga laboral.
    - Promover flujos de trabajo constantes.

    **Indicadores de Éxito:**
    - Variabilidad reducida en la carga de trabajo.

    **Métricas o KPIs Específicos:**
    - % de reducción de variaciones de carga semanal.

    **¿Por qué Funciona?**
    - Nivelar protege la energía y salud mental de los trabajadores.
    """,  },

"Standard of Work Humano": {
    "icon": "📘",
    "description": """
    **¿Qué es?**
    - Define la mejor forma de trabajar priorizando la dignidad, la salud mental y el bienestar, no solo la eficiencia; dando claridad y equidad en la ejecución de labores.

    **Beneficios Clave:**
    - Consistencia en calidad sin desgaste humano.

    **Reducción de errores, fatiga y estrés.**
    - Fortalecimiento de la cultura de respeto y mejora continua.

    **Aporte a NOM-035:**
    - Previene riesgos psicosociales.
    - Evita cargas de trabajo excesivas.
    - Fomenta un ambiente organizacional saludable.

   **Cómo Implementarlo:**
   - Documentar buenas prácticas considerando ergonomía y carga emocional.
   - Integrar retroalimentación de los trabajadores.
   - Capacitar en estándares enfocados en calidad y bienestar.
   - Auditar y ajustar de manera continua.

   **Indicadores de Éxito:
   - Cumplimiento del estándar.
   - Reducción de estrés y fatiga.
   - Mejora en satisfacción laboral y calidad del trabajo.

  **Métricas o KPIs Específicos:**
  - % de actividades estandarizadas con enfoque humano.
  - Cumplimiento de pausas activas.
  - Reducción de ausentismo por estrés.
  - Índice de carga laboral percibida.

  **¿Por qué Funciona?**
  - Porque trabajadores saludables y respetados son más productivos, comprometidos y generan mejores resultados sostenibles.
    """,        },

"Sensores de Bienestar (Wearables & Biofeedback Ético)": {
  "icon": "📶",
  "description": """
  **¿Qué es?**  
  - Dispositivos y tecnologías que monitorean signos vitales, estrés y bienestar en tiempo real, respetando la privacidad.

  **Beneficios Clave (Operativos y Humanos):**
  - Detección temprana de fatiga o estrés.
  - Mejora del clima laboral.
  - Prevención de riesgos psicosociales.

  **Aporte a NOM-035:**
  - Apoya la evaluación y control de factores de riesgo psicosocial.

  **Cómo Implementarlo:**
  - Integrar sensores o wearables en áreas críticas.
  - Garantizar consentimiento informado y protección de datos.

  **Indicadores de Éxito:**
  - Disminución de episodios de estrés laboral.
  - Aumento en la satisfacción laboral.

  **Métricas o KPIs Específicos:**
  - Niveles promedio de variabilidad cardíaca (HRV).
  - Tasa de participación voluntaria.

  **¿Por qué Funciona?**
  - Proporciona datos objetivos para intervenir a tiempo y de forma ética.
    """,        },

"Matriz de Riesgos Psicosociales": {
  "icon": "🧩",
  "description": """
  **¿Qué es?**  
  - Herramienta para identificar, evaluar y priorizar riesgos psicosociales en el entorno laboral.

  **Beneficios Clave (Operativos y Humanos):**
  - Prevención de enfermedades laborales.
  - Mejora de la salud mental.
  - Cumplimiento normativo.

  **Aporte a NOM-035:**
  - Núcleo de cumplimiento de la norma.

  **Cómo Implementarlo:**
  - Aplicar cuestionarios validados y análisis multidimensional.

  **Indicadores de Éxito:**
  - Riesgos identificados por área.
  - Planes de acción derivados.

  **Métricas o KPIs Específicos:**
  - Índice de exposición a riesgos psicosociales.

  **¿Por qué Funciona?**
  - Facilita decisiones estratégicas y preventivas.
    """,        },

"Hansei Restaurativo": {
  "icon": "🪞",
  "description": """
  **¿Qué es?**  
  - Práctica reflexiva y ética para revisar errores, aprender de ellos y restaurar relaciones afectadas.

  **Beneficios Clave (Operativos y Humanos):**
  - Fortalece la confianza.
  - Reduce la repetición de errores.
  - Promueve un ambiente respetuoso.

  **Aporte a NOM-035:**
  - Mejora la gestión de conflictos y resiliencia organizacional.

  **Cómo Implementarlo:**
  - Espacios de reflexión estructurada con enfoque restaurativo.

  **Indicadores de Éxito:**
  - Casos resueltos con aprendizaje documentado.

  **Métricas o KPIs Específicos:**
  - Tasa de reincidencia en errores o conflictos.

  **¿Por qué Funciona?**
  - Transforma el error en oportunidad y promueve la cultura del perdón.
    """,        },

"Shojinka Ético": {
  "icon": "👥",
  "description": """
  **¿Qué es?**  
  - Flexibilidad inteligente en la asignación de personas, respetando capacidades, intereses y límites humanos.

  **Beneficios Clave (Operativos y Humanos):**
  - Mayor adaptabilidad y eficiencia.
  - Reducción de carga excesiva y burnout.

  **Aporte a NOM-035:**
  - Alinea tareas a capacidades reales del personal.

  **Cómo Implementarlo:**
  - Diseño de rotaciones éticas y colaborativas.

  **Indicadores de Éxito:**
  - Reducción de rotación y ausentismo.

  **Métricas o KPIs Específicos:**
  - Índice de carga laboral equilibrada.

  **¿Por qué Funciona?**
  - Permite una operación humana, sostenible y justa.
    """,        },

"Shigoto Shiji Transparente": {
  "icon": "🔎",
  "description": """
  **¿Qué es?**  
  - Claridad y trazabilidad en las órdenes de trabajo, con comunicación directa, abierta y sin ambigüedad.

  **Beneficios Clave (Operativos y Humanos):**
  - Reduce errores y frustración.
  - Mejora la coordinación y seguridad psicológica.

  **Aporte a NOM-035:**
  - Fortalece la certidumbre y disminuye tensiones laborales.

  **Cómo Implementarlo:**
  - Uso de sistemas digitales con retroalimentación clara.

  **Indicadores de Éxito:**
  - Disminución de reprocesos y ambigüedades en tareas.

  **Métricas o KPIs Específicos:**
  - Tasa de errores por malentendidos operativos.

  **¿Por qué Funciona?**
  - Fomenta la confianza y la eficiencia mediante la transparencia.
    """,        },

"Yamazumi Psicosocial": {
  "icon": "📊",
  "description": """
  **¿Qué es?**  
  - Visualización de la carga emocional, cognitiva y organizacional de cada trabajador, más allá del trabajo físico.

  **Beneficios Clave (Operativos y Humanos):**
  - Distribución más justa de tareas.
  - Prevención de sobrecarga psicosocial.

  **Aporte a NOM-035:**
  - Evalúa cargas que afectan el bienestar.

  **Cómo Implementarlo:**
  - Mapas de carga total con datos auto-reportados y observación.

  **Indicadores de Éxito:**
  - Reducción de burnout y errores humanos.

  **Métricas o KPIs Específicos:**
  - Índice de sobrecarga emocional promedio por área.

  **¿Por qué Funciona?**
  - Hace visible lo invisible en la carga laboral humana.
    """,        },

"Jishu Hozen 2.0": {
  "icon": "🛠️",
  "description": """
  **¿Qué es?**  
  - Mantenimiento autónomo enfocado no solo en máquinas, sino en la salud y bienestar del operador.

  **Beneficios Clave (Operativos y Humanos):**
  - Menor ausentismo por fatiga física y mental.
  - Incremento en el desempeño sostenible.

  **Aporte a NOM-035:**
  - Previene riesgos relacionados con ergonomía y salud.

  **Cómo Implementarlo:**
  - Programas integrados de mantenimiento y autocuidado.

  **Indicadores de Éxito:**
  - Disminución de paros por problemas de salud o ergonomía.

  **Métricas o KPIs Específicos:**
  - Frecuencia de pausas activas.

  **¿Por qué Funciona?**
  - Cuida tanto a la máquina como a la persona que la opera.
    """,        },

"Muri Preventivo": {
  "icon": "🚧",
  "description": """
  **¿Qué es?**  
  - Eliminación proactiva de sobrecarga mental, emocional o física en el entorno laboral.

  **Beneficios Clave (Operativos y Humanos):**
  - Reducción de enfermedades laborales.
  - Mejora de la energía disponible para el trabajo.

  **Aporte a NOM-035:**
  - Mitiga factores de riesgo relacionados con el exceso de trabajo.

  **Cómo Implementarlo:**
  - Análisis de carga y rediseño de flujos laborales.

  **Indicadores de Éxito:**
  - Disminución de licencias médicas por estrés.

  **Métricas o KPIs Específicos:**
  - Horas extras promedio por trabajador.

  **¿Por qué Funciona?**
  - Interviene antes del daño, no después.
    """,        },

"Mura Emocional": {
  "icon": "🌊",
  "description": """
  **¿Qué es?**  
  - Identificación y estabilización de fluctuaciones emocionales que afectan el desempeño y la armonía.

  **Beneficios Clave (Operativos y Humanos):**
  - Mejora del clima laboral.
  - Mayor resiliencia emocional colectiva.

  **Aporte a NOM-035:**
  - Reconoce y regula factores de riesgo derivados de la inestabilidad emocional.

  **Cómo Implementarlo:**
  - Programas de apoyo emocional y escucha activa.

  **Indicadores de Éxito:**
  - Estabilidad emocional autorreportada.

  **Métricas o KPIs Específicos:**
  - Fluctuación en escalas de bienestar emocional.

  **¿Por qué Funciona?**
  - Estabiliza la base emocional del trabajo en equipo.
    """,        },

"Muda Ético": {
  "icon": "♻️",
  "description": """
  **¿Qué es?**  
  - Identificación de desperdicios operativos que impactan el bienestar humano, como reuniones innecesarias, estrés evitable o tareas sin propósito.

  **Beneficios Clave (Operativos y Humanos):**
  - Aumento del valor real en las actividades.
  - Reducción de desgaste innecesario.

  **Aporte a NOM-035:**
  - Minimiza factores psicosociales generadores de estrés.

  **Cómo Implementarlo:**
  - Mapas de valor con lente humano y ético.

  **Indicadores de Éxito:**
  - Reducción de actividades sin valor.

  **Métricas o KPIs Específicos:**
  - Horas eliminadas de tareas sin sentido.

  **¿Por qué Funciona?**
  - Mejora la calidad de vida laboral sin sacrificar resultados.
    """,        },

"Nemawashi Inclusivo": {
  "icon": "🌱",
  "description": """
  **¿Qué es?**  
  - Práctica de consenso colaborativo con escucha activa, inclusión y equidad para la toma de decisiones.

  **Beneficios Clave (Operativos y Humanos):**
  - Mejora la implementación de cambios.
  - Fortalece la cohesión organizacional.

  **Aporte a NOM-035:**
  - Reduce tensiones por decisiones unilaterales.

  **Cómo Implementarlo:**
  - Reuniones previas con enfoque inclusivo antes de implementar nuevas políticas.

  **Indicadores de Éxito:**
  - Nivel de aceptación en decisiones organizacionales.

  **Métricas o KPIs Específicos:**
  - Tasa de participación en procesos de cambio.

  **¿Por qué Funciona?**
  - Involucra a las personas desde el inicio, generando compromiso genuino.
    """,        },

    "Checklists / Estándares de Trabajo": {
  "icon": "☑️",
  "description": """
  **¿Qué es?**  
  Los Checklists o Estándares de Trabajo son guías estructuradas que documentan la mejor forma conocida de realizar una tarea. Aseguran consistencia, calidad y seguridad, incorporando buenas prácticas operativas y humanas.

  **Beneficios Clave (Operativos y Humanos):**
  - Reducción de errores y omisiones.
  - Asegura cumplimiento regulatorio y buenas prácticas.
  - Genera tranquilidad y confianza en el trabajador al tener claridad en lo esperado.

  **Aporte a NOM-035:**
  - Disminuye ambigüedad laboral, reduciendo el estrés y la carga mental.
  - Favorece un ambiente predecible y seguro, donde los roles y responsabilidades están claramente definidos.

  **Cómo Implementarlo:**
  - Estandariza tareas clave con participación de quienes las ejecutan.
  - Diseña checklists claros, accesibles y actualizables.
  - Capacita a los equipos y promueve su uso como herramienta de apoyo, no de control punitivo.

  **Indicadores de Éxito:**
  - Reducción de errores repetitivos.
  - Aumento en el cumplimiento de procesos críticos.
  - Mejora en la percepción de claridad y seguridad laboral.

  **Métricas o KPIs Específicos:**
  - % de tareas ejecutadas conforme al estándar.
  - % de reducción de incidencias relacionadas con omisiones o pasos mal realizados.
  - Resultados de encuestas sobre claridad de instrucciones y percepción de carga mental.

  **¿Por qué Funciona?**
  - Porque la claridad operativa reduce el estrés, mejora la calidad y empodera al trabajador. Los estándares bien diseñados son herramientas de apoyo humano y técnico para lograr excelencia sostenible.
    """,        },

}

# --- Layout ---
cols_per_row = 3
columns = st.columns(cols_per_row)

for idx, (tool_name, tool_data) in enumerate(tools.items()):
    col = columns[idx % cols_per_row]
    with col:
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-icon">{tool_data['icon']}</div>
                    <div class="card-title">{tool_name}</div>
                    <div class="card-content">
                        <details>
                            <summary style="cursor: pointer; font-weight: bold; color: #1976d2;">Ver detalles</summary>
                            <div style="margin-top: 0.75rem; text-align: left;">
                                {format_bold(tool_data['description'])}
                            </div>
                        </details>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
