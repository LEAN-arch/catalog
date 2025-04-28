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
    "Kanban Ético": "Sistema visual de control de flujo de trabajo con énfasis en el bienestar de los empleados y eficiencia laboral.",
    "Mapeo de Causa-Humano": "Análisis Sistémico para Entornos Laborales Saludables.",
    "Andon Humano 4.0": "Sistema visual de alerta para dar voz y visibilidad a cada miembro del equipo.",
    "Poka-Yoke Humano": "Prevención Inteligente para el Bienestar y la Calidad Total.",    
    "PDCA / PDSA Saludable": Mejorar con Ciencia y Humanidad.", 
    "Hoshin Kanri Humano": "Alineación Estratégica con Propósito Humano." 
    "5S+2 Centrado en las Personas": "Un enfoque que organiza el lugar de trabajo para optimizar la productividad y el bienestar.",
    "Gemba con Propósito": "Visita el lugar donde se realiza el trabajo para identificar oportunidades de mejora.",
    "Ethical FMEA": "Gestión de Riesgos con Enfoque Humano.",
    "VSM de Equilibrio Laboral": "Mapeo de flujo de valor centrado en el equilibrio entre la eficiencia operativa y el bienestar humano.",
    "Takt Time Laboral": "Medición del tiempo requerido para cumplir con la demanda sin sobrecargar a los empleados.",
    "Jidoka Ético": "Autonomización de procesos con enfoque en la seguridad y ética del trabajo."
    "Heijunka Humano": "Balancear el Trabajo y la Vida."
    "Takt Time Laboral": "Medición del tiempo requerido para cumplir con la demanda sin sobrecargar a los empleados.",
  
   
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
    """)

elif tool_name == "Kanban Ético":
    st.markdown("""
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
    """)

elif tool_name == "Mapeo de Causa-Humano":
    st.markdown("""
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
    """)
elif tool_name == "Andon Humano 4.0":
    st.markdown("""
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
    """)

elif tool_name == "Poka-Yoke Humano":
    st.markdown("""
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
    """)

elif tool_name == "PDCA / PDSA Saludable":
    st.markdown("""
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
    """)

elif tool_name == "Hoshin Kanri Humano":
    st.markdown("""
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
    """)

elif tool_name == "5S+2 Centrado en las Personas":
    st.markdown("""
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
    """)
elif tool_name == "Ethical FMEA":
    st.markdown("""
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
    """)

elif tool_name == "VSM de Equilibrio Laboral":
    st.markdown("""
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
    """)

elif tool_name == "Takt Time Laboral":
    st.markdown("""
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
    """)

elif tool_name == "Jidoka Ético":
    st.markdown("""
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
    """)

elif tool_name == "Heijunka Humano":
    st.markdown("""
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
    """)




