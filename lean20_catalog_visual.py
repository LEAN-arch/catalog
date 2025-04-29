import streamlit as st
import re

# --- Page config ---
st.set_page_config(page_title="Catálogo Lean 2.0", layout="wide")
st.markdown(
    """
    <style>
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

# --- Helper function ---
def format_bold(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = text.replace('\n', '<br>')
    return text
# Definimos las herramientas como texto plano (sin st.markdown adentro)
# --- Tools ---
tools = { "Kaizen Colectivo": """
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
    """,

   "Gemba con Propósito": """
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
    """,

 "Kanban Ético": """
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
    """,

 "Mapeo de Causa-Humano": """
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
    """,
 "Andon Humano 4.0": """
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
    """,

 "Poka-Yoke Humano": """
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
    """,

"PDCA / PDSA Saludable": """
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
    """,

"Hoshin Kanri Humano": """
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
    """,

"5S+2 Centrado en las Personas": """
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
    """,
"Ethical FMEA": """
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
    """,

"VSM de Equilibrio Laboral": """
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
    """,

"Takt Time Laboral": """
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
    """,

"Jidoka Ético": """
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
    """,

"Heijunka Humano": """
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
    """,

"Standard of Work Humano": """
    **¿Qué es?**
    - Define la mejor forma de trabajar priorizando la dignidad, la salud mental y el bienestar, no solo la eficiencia.

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
    """,      
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
