import streamlit as st

# Título de la aplicación
st.title("Catálogo Visual de Herramientas LEAN 2.0")

# Descripción general
st.markdown("""
Este catálogo interactivo te permite explorar las principales herramientas **LEAN 2.0**. 
Haz clic en cada herramienta para conocer su descripción, beneficios y cómo implementarla.
""")

# Lista de herramientas LEAN 2.0
tools = {
    "Kaizen Colectivo": "Una herramienta que promueve la mejora continua mediante la colaboración colectiva.",
    "Gemba con Propósito": "Visita el lugar donde se realiza el trabajo para identificar oportunidades de mejora.",
    "5S+2 Centrado en las Personas": "Un enfoque que organiza el lugar de trabajo para optimizar la productividad y el bienestar.",
    "Ethical FMEA": "Análisis de modos de falla con un enfoque ético que prioriza la seguridad y el bienestar de las personas.",
    "Diagrama de Causa-Efecto (Ishikawa)": "Diagrama utilizado para identificar las causas raíz de un problema.",
    "Análisis Colaborativo": "Un enfoque de resolución de problemas en equipo, buscando soluciones compartidas.",
    "VSM de Equilibrio Laboral": "Mapeo de flujo de valor centrado en el equilibrio entre la eficiencia operativa y el bienestar humano.",
    "Kanban Ético": "Sistema visual de control de flujo de trabajo con énfasis en el bienestar de los empleados.",
    "Takt Time Laboral": "Medición del tiempo requerido para cumplir con la demanda sin sobrecargar a los empleados.",
    "Andon 4.0": "Sistema visual de alerta para identificar problemas en tiempo real con tecnología avanzada.",
    "Jidoka Ético": "Autonomización de procesos con enfoque en la seguridad y ética del trabajo."
}

# Selección de herramientas
tool_name = st.selectbox("Selecciona una herramienta LEAN 2.0", list(tools.keys()))

# Descripción de la herramienta seleccionada
st.subheader(f"Descripción de {tool_name}")
st.write(tools[tool_name])

# Información adicional para cada herramienta
if tool_name == "Kaizen Colectivo":
    st.markdown("""
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
    """)

elif tool_name == "Gemba con Propósito":
    st.markdown("""
    **¿Qué es?**  
    Gemba con Propósito implica que los líderes y empleados vayan al lugar de trabajo (el "gemba") para observar directamente los procesos y comprender mejor los problemas.

    **Beneficios Clave (Operativos y Humanos):**
    - Mejora en la toma de decisiones basadas en la realidad del proceso.
    - Mayor comprensión de las necesidades de los empleados.

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
    """)

# Añadir más herramientas como en los ejemplos anteriores...

