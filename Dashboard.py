import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import base64
import tempfile
import os

# Configuración de la página
st.set_page_config(page_title="Dashboard Corporativo: Cumplimiento NOM-035 y Evolución LEAN 2.0", layout="wide")

# Encabezado con logo y título
st.image("logo_empresa.png", width=150)  # Asegúrate de que el archivo 'logo_empresa.png' esté en el mismo directorio
st.markdown("<h1 style='text-align: center; font-size: 36px; font-weight: bold; color: #2d3e50;'>🏛️ Dashboard Corporativo: Cumplimiento NOM-035 y Evolución LEAN 2.0</h1>", unsafe_allow_html=True)
st.subheader("Monitoreo Estratégico de Bienestar, Cultura y Mejora Continua")
st.caption("Última actualización: Abril 2025")
st.markdown("---")

# Filtros en la barra lateral
st.sidebar.header("🔎 Filtros Dinámicos")
departamentos = st.sidebar.multiselect("Selecciona Departamentos:", ['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'], default=['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'])

# Sección de KPIs
st.header("📊 KPIs Estratégicos")

def semaforo(kpi_value):
    if kpi_value > 90:
        return "🟢", "#d4edda"
    elif 70 <= kpi_value <= 89:
        return "🟡", "#fff3cd"
    else:
        return "🔴", "#f8d7da"

col1, col2, col3 = st.columns(3)

with col1:
    kpi_1 = 92
    icon, color = semaforo(kpi_1)
    st.markdown(f"<div style='padding: 20px; background-color:{color}; border-radius: 8px; text-align: center;'><h3>{icon} Cumplimiento NOM-035</h3><p style='font-size: 28px; font-weight: bold;'>{kpi_1}%</p></div>", unsafe_allow_html=True)

with col2:
    kpi_2 = 80
    icon, color = semaforo(kpi_2)
    st.markdown(f"<div style='padding: 20px; background-color:{color}; border-radius: 8px; text-align: center;'><h3>{icon} Cumplimiento en Calidad</h3><p style='font-size: 28px; font-weight: bold;'>{kpi_2}%</p></div>", unsafe_allow_html=True)

with col3:
    kpi_3 = 70
    icon, color = semaforo(kpi_3)
    st.markdown(f"<div style='padding: 20px; background-color:{color}; border-radius: 8px; text-align: center;'><h3>{icon} Cumplimiento en Logística</h3><p style='font-size: 28px; font-weight: bold;'>{kpi_3}%</p></div>", unsafe_allow_html=True)

# Gráfico de barras
df_kpi = pd.DataFrame({
    'Departamento': ['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'],
    'Evaluaciones Aplicadas (%)': [95, 90, 85, 80, 75]
})

fig1 = px.bar(df_kpi, x='Evaluaciones Aplicadas (%)', y='Departamento', orientation='h', color='Departamento',
              title="Evaluaciones Aplicadas por Departamento",
              labels={'Evaluaciones Aplicadas (%)': 'Cumplimiento (%)', 'Departamento': 'Departamentos'})
fig1.update_layout(template="plotly_dark", showlegend=False)
st.plotly_chart(fig1, use_container_width=True)

# Tabla de KPIs
st.subheader("📋 Esquema de KPIs Visualizados")

kpi_table = pd.DataFrame({
    'Indicador': ['Evaluaciones Aplicadas', 'Protocolos Implementados', 'Acciones Preventivas vs Correctivas', 'Reportes Psicosociales',
                  'Índice de Bienestar Organizacional', 'Adopción Herramientas LEAN 2.0', 'Participación en Programas de Bienestar',
                  'Índice de Equidad Laboral', 'Reducción de Ausentismo por Estrés'],
    'Tipo de Gráfico': ['Gauge Chart', 'KPI Card', 'Bar Chart', 'Line Chart', 'KPI Card + Line Chart', 'KPI Card', 'Donut Chart', 'KPI Card', 'Line Chart'],
    'Frecuencia de Actualización': ['Trimestral', 'Anual', 'Trimestral', 'Mensual', 'Semestral', 'Trimestral', 'Semestral', 'Anual', 'Trimestral']
})

st.dataframe(kpi_table, use_container_width=True)

# Sección de alertas
st.markdown("<div style='background-color:#ffeeba; padding: 20px; border-radius: 8px; margin-top: 20px;'><h4 style='text-align: center; font-weight: bold;'>🚨 Alerta: KPI Crítico en Cumplimiento NOM-035</h4><p>Se ha detectado que el KPI de Cumplimiento ha caído por debajo del 90%. Valor actual: 85%.</p></div>", unsafe_allow_html=True)

# Pie de página
st.markdown("""
    <div style="background-color:#2e3b4e; color:white; text-align:center; padding: 10px; font-size: 14px; border-radius: 8px;">
        <p>📧 Contáctanos: soporte@empresa.com | 📍 Visítanos en: Calle Ejemplo 123, Tijuana</p>
        <p>© 2025 Empresa XYZ - Todos los derechos reservados.</p>
    </div>
""", unsafe_allow_html=True)

# Función para generar el PDF
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Reporte de Cumplimiento LEAN 2.0 y NOM-035", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt="Fecha: 25 de Abril de 2025", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Resumen: Evaluación de KPIs y alertas del sistema.", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="KPIs:", ln=True)
    pdf.cell(200, 10, txt=" - Cumplimiento NOM-035: 92%", ln=True)
    pdf.cell(200, 10, txt=" - Cumplimiento en Calidad: 80%", ln=True)
    pdf.cell(200, 10, txt=" - Cumplimiento en Logística: 70%", ln=True)

    return pdf.output(dest='S').encode('latin-1')

# Botón para generar y descargar el PDF
if st.button('Generar Reporte PDF'):
    pdf_data = generate_pdf()
    b64 = base64.b64encode(pdf_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="reporte_lean_2_0.pdf">📄 Descargar Reporte PDF</a>'
    st.markdown(href, unsafe_allow_html=True)

