import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pdfkit
from datetime import datetime

# ================
# PAGE CONFIGURATION
# ================
st.set_page_config(
    page_title="Dashboard Corporativo: Cumplimiento NOM-035 y Evolución LEAN 2.0",
    layout="wide",
    page_icon="📊"
)
# ================
# CUSTOM CSS
# ================
st.markdown("""
<style>
    /* Main container padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Card styling */
    .card {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 20px;
        margin-bottom: 20px;
        background: white;
    }
    
    /* KPI card colors */
    .kpi-good {
        background: linear-gradient(135deg, #4CAF50 0%, #81C784 100%);
        color: white;
    }
    
    .kpi-warning {
        background: linear-gradient(135deg, #FFC107 0%, #FFD54F 100%);
        color: #333;
    }
    
    .kpi-danger {
        background: linear-gradient(135deg, #F44336 0%, #E57373 100%);
        color: white;
    }
    
    /* Alert styling */
    .alert {
        border-left: 5px solid;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
    }
    
    .alert-warning {
        background-color: #FFF3CD;
        border-left-color: #FFC107;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2c3e50 0%, #1a252f 100%);
        color: white;
    }
    
    /* Custom metric styling */
    .metric-value {
        font-size: 2.5rem !important;
        font-weight: bold !important;
        margin-bottom: 0 !important;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .metric-value {
            font-size: 1.8rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ================
# HEADER SECTION
# ================
header_col1, header_col2 = st.columns([1, 4])
with header_col1:
    st.image("https://via.placeholder.com/150x50.png?text=Company+Logo", width=150)
    
with header_col2:
    st.markdown("""
    <h1 style='margin-bottom: 0.2rem; color: #2d3e50;'>🏛️ Dashboard Corporativo</h1>
    <h3 style='margin-top: 0; color: #4a6fa5;'>Cumplimiento NOM-035 y Evolución LEAN 2.0</h3>
    <p style='color: #666; font-size: 0.9rem;'>Monitoreo Estratégico de Bienestar, Cultura y Mejora Continua</p>
    """, unsafe_allow_html=True)

st.markdown(f"<div style='text-align: right; color: #666; font-size: 0.8rem;'>Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>", unsafe_allow_html=True)
st.markdown("---")

# ================
# SIDEBAR FILTERS
# ================
with st.sidebar:
    st.markdown("""
    <div style='margin-bottom: 30px;'>
        <h2 style='color: white;'>🔎 Filtros Dinámicos</h2>
        <p style='color: #bdc3c7; font-size: 0.9rem;'>Seleccione los parámetros para filtrar los datos</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📅 Rango de Fechas", expanded=True):
        date_range = st.date_input(
            "Seleccionar rango:",
            value=[datetime(2025, 1, 1), datetime(2025, 4, 1)],
            format="DD/MM/YYYY",
            label_visibility="collapsed"
        )
    
    with st.expander("🏢 Departamentos", expanded=True):
        departamentos = st.multiselect(
            "Selecciona Departamentos:",
            ['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'],
            default=['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'],
            label_visibility="collapsed"
        )
    
    with st.expander("📊 Métricas", expanded=True):
        metricas = st.multiselect(
            "Selecciona Métricas:",
            ['NOM-035', 'Calidad', 'Logística', 'Bienestar', 'LEAN 2.0'],
            default=['NOM-035', 'Calidad', 'Logística'],
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: #bdc3c7; font-size: 0.8rem;'>© 2025 Empresa XYZ</p>
    </div>
    """, unsafe_allow_html=True)

# ================
# KPI SECTION
# ================
st.markdown("""
<div class='card'>
    <h2 style='margin-top: 0; color: #2d3e50;'>📊 KPIs Estratégicos</h2>
    <p style='color: #666;'>Indicadores clave de desempeño para el seguimiento de NOM-035 y LEAN 2.0</p>
</div>
""", unsafe_allow_html=True)

# KPI cards in columns
col1, col2, col3, col4 = st.columns(4)

# Function to create KPI cards
def create_kpi_card(title, value, delta, status="neutral"):
    color_map = {
        "good": "#4CAF50",
        "warning": "#FFC107",
        "danger": "#F44336",
        "neutral": "#2196F3"
    }
    
    delta_color = color_map.get(status, "#2196F3")
    delta_icon = "↑" if delta >= 0 else "↓"
    
    return f"""
    <div class='card' style='border-top: 4px solid {delta_color};'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <h3 style='margin-top: 0; color: #555;'>{title}</h3>
            <span style='background-color: {delta_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem;'>
                {delta_icon} {abs(delta)}%
            </span>
        </div>
        <p class='metric-value'>{value}%</p>
        <div style='height: 6px; background-color: #eee; border-radius: 3px; margin-top: 10px;'>
            <div style='width: {value}%; height: 6px; background-color: {delta_color}; border-radius: 3px;'></div>
        </div>
    </div>
    """

with col1:
    st.markdown(create_kpi_card("Cumplimiento NOM-035", 92, 2.5, "good"), unsafe_allow_html=True)

with col2:
    st.markdown(create_kpi_card("Cumplimiento Calidad", 80, -1.2, "warning"), unsafe_allow_html=True)

with col3:
    st.markdown(create_kpi_card("Cumplimiento Logística", 70, -5.8, "danger"), unsafe_allow_html=True)

with col4:
    st.markdown(create_kpi_card("Adopción LEAN 2.0", 65, 8.3, "neutral"), unsafe_allow_html=True)

# ================
# MAIN CHARTS SECTION
# ================
tab1, tab2, tab3 = st.tabs(["📈 Evaluaciones", "📊 Cumplimiento", "📌 Detalles"])

with tab1:
    # Horizontal bar chart with improved styling
    eval_data = pd.DataFrame({
        'Departamento': ['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'],
        'Evaluaciones Aplicadas (%)': [95, 90, 85, 80, 75],
        'Meta': [90, 90, 90, 90, 90]
    })
    
    fig1 = go.Figure()
    
    # Add actual values
    fig1.add_trace(go.Bar(
        y=eval_data['Departamento'],
        x=eval_data['Evaluaciones Aplicadas (%)'],
        name='Evaluaciones Aplicadas',
        orientation='h',
        marker=dict(color='#4a6fa5'),
        hovertemplate='<b>%{y}</b><br>Evaluaciones: %{x}%<extra></extra>'
    ))
    
    # Add target line
    fig1.add_trace(go.Scatter(
        y=eval_data['Departamento'],
        x=eval_data['Meta'],
        name='Meta',
        mode='markers+lines',
        line=dict(color='#FFC107', dash='dot', width=2),
        marker=dict(symbol='diamond', size=10, color='#FFC107'),
        hovertemplate='<b>%{y}</b><br>Meta: %{x}%<extra></extra>'
    ))
    
    fig1.update_layout(
        title="Evaluaciones Aplicadas por Departamento vs Meta (90%)",
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title='Porcentaje de Cumplimiento'),
        yaxis=dict(title='Departamentos'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    # Gauge charts for compliance metrics
    def create_gauge(value, title):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': title},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "#4a6fa5"},
                'steps': [
                    {'range': [0, 70], 'color': "#F44336"},
                    {'range': [70, 90], 'color': "#FFC107"},
                    {'range': [90, 100], 'color': "#4CAF50"}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': value
                }
            }
        ))
        
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        return fig
    
    gauge_col1, gauge_col2, gauge_col3 = st.columns(3)
    
    with gauge_col1:
        st.plotly_chart(create_gauge(92, "NOM-035 Compliance"), use_container_width=True)
    
    with gauge_col2:
        st.plotly_chart(create_gauge(80, "Calidad Compliance"), use_container_width=True)
    
    with gauge_col3:
        st.plotly_chart(create_gauge(70, "Logística Compliance"), use_container_width=True)

with tab3:
    # Detailed KPI table with interactive elements
    st.markdown("""
    <div class='card'>
        <h3 style='margin-top: 0;'>📋 Esquema de KPIs Visualizados</h3>
        <p style='color: #666;'>Detalle completo de los indicadores monitoreados</p>
    </div>
    """, unsafe_allow_html=True)
    
    kpi_table = pd.DataFrame({
        'Indicador': ['Evaluaciones Aplicadas', 'Protocolos Implementados', 'Acciones Preventivas vs Correctivas', 
                     'Reportes Psicosociales', 'Índice de Bienestar Organizacional', 'Adopción Herramientas LEAN 2.0', 
                     'Participación en Programas de Bienestar', 'Índice de Equidad Laboral', 'Reducción de Ausentismo por Estrés'],
        'Tipo de Gráfico': ['Gauge Chart', 'KPI Card', 'Bar Chart', 'Line Chart', 'KPI Card + Line Chart', 
                           'KPI Card', 'Donut Chart', 'KPI Card', 'Line Chart'],
        'Frecuencia': ['Trimestral', 'Anual', 'Trimestral', 'Mensual', 'Semestral', 
                      'Trimestral', 'Semestral', 'Anual', 'Trimestral'],
        'Responsable': ['RH', 'Calidad', 'Operaciones', 'RH', 'RH', 
                        'Mejora Continua', 'RH', 'RH', 'Salud Ocupacional'],
        'Última Medición': ['25/04/2025', '15/04/2025', '20/04/2025', '22/04/2025', '10/04/2025', 
                            '18/04/2025', '05/04/2025', '01/04/2025', '23/04/2025']
    })
    
    # Add interactive features to the table
    gb = st.grid(kpi_table.shape[0], height=400)
    gb.dataframe(kpi_table, use_container_width=True)
    gb.download_button("Descargar como CSV", kpi_table.to_csv(index=False).encode('utf-8'), "kpis_detallados.csv", "text/csv")

# ================
# ALERTS SECTION
# ================
st.markdown("""
<div class='alert alert-warning'>
    <div style='display: flex; align-items: center;'>
        <span style='font-size: 1.5rem; margin-right: 10px;'>⚠️</span>
        <div>
            <h4 style='margin: 0 0 5px 0;'>Alerta: KPI Crítico en Cumplimiento NOM-035</h4>
            <p style='margin: 0;'>Se ha detectado que el KPI de Cumplimiento ha caído por debajo del 90% en los departamentos de Logística (70%) y Ventas (85%).</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ================
# REPORT GENERATION
# ================
st.markdown("""
<div class='card'>
    <h3 style='margin-top: 0;'>📄 Generar Reporte</h3>
    <p style='color: #666;'>Exporte los datos actuales en diferentes formatos</p>
    
    <div style='display: flex; gap: 10px; margin-top: 15px;'>
""", unsafe_allow_html=True)

# PDF Report Generation
def generate_pdf():
    html_content = """
    <html>
        <head>
            <title>Reporte LEAN 2.0</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #2d3e50; }
                .header { display: flex; justify-content: space-between; margin-bottom: 20px; }
                .kpi-card { border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin-bottom: 10px; }
                .good { background-color: #e8f5e9; }
                .warning { background-color: #fff8e1; }
                .danger { background-color: #ffebee; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <div class='header'>
                <div>
                    <h1>Reporte de Cumplimiento</h1>
                    <p><b>Fecha:</b> """ + datetime.now().strftime("%d/%m/%Y %H:%M") + """</p>
                </div>
                <div>
                    <img src='https://via.placeholder.com/150x50.png?text=Company+Logo' width='120'>
                </div>
            </div>
            
            <h2>Resumen Ejecutivo</h2>
            <div style='display: flex; justify-content: space-between; margin-bottom: 20px;'>
                <div class='kpi-card good' style='width: 23%;'>
                    <h3>Cumplimiento NOM-035</h3>
                    <p style='font-size: 24px; font-weight: bold;'>92%</p>
                </div>
                <div class='kpi-card warning' style='width: 23%;'>
                    <h3>Cumplimiento Calidad</h3>
                    <p style='font-size: 24px; font-weight: bold;'>80%</p>
                </div>
                <div class='kpi-card danger' style='width: 23%;'>
                    <h3>Cumplimiento Logística</h3>
                    <p style='font-size: 24px; font-weight: bold;'>70%</p>
                </div>
                <div class='kpi-card' style='width: 23%;'>
                    <h3>Adopción LEAN 2.0</h3>
                    <p style='font-size: 24px; font-weight: bold;'>65%</p>
                </div>
            </div>
            
            <h2>Detalle de Indicadores</h2>
            <table>
                <tr>
                    <th>Indicador</th>
                    <th>Tipo de Gráfico</th>
                    <th>Frecuencia</th>
                    <th>Responsable</th>
                    <th>Última Medición</th>
                </tr>
                <tr>
                    <td>Evaluaciones Aplicadas</td>
                    <td>Gauge Chart</td>
                    <td>Trimestral</td>
                    <td>RH</td>
                    <td>25/04/2025</td>
                </tr>
                <!-- More rows would go here -->
            </table>
        </body>
    </html>
    """
    pdf = pdfkit.from_string(html_content, False)
    return pdf

# Report buttons in columns
report_col1, report_col2, report_col3 = st.columns(3)

with report_col1:
    if st.button('📄 Generar Reporte PDF', use_container_width=True):
        pdf_data = generate_pdf()
        st.download_button(
            label="⬇️ Descargar PDF",
            data=pdf_data,
            file_name=f"reporte_nom35_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

with report_col2:
    st.download_button(
        label="📊 Exportar Datos (CSV)",
        data=kpi_table.to_csv(index=False).encode('utf-8'),
        file_name="kpis_detallados.csv",
        mime="text/csv",
        use_container_width=True
    )

with report_col3:
    if st.button('📧 Enviar por Correo', use_container_width=True):
        with st.spinner('Enviando reporte...'):
            # Email sending logic would go here
            st.success('¡Reporte enviado exitosamente!')

st.markdown("</div></div>", unsafe_allow_html=True)

# ================
# FOOTER SECTION
# ================
st.markdown("""
<div style='background-color: #2d3e50; color: white; padding: 15px; border-radius: 8px; margin-top: 30px;'>
    <div style='display: flex; justify-content: space-between; align-items: center;'>
        <div>
            <p style='margin: 5px 0;'>📧 <a href='mailto:soporte@empresa.com' style='color: white;'>soporte@empresa.com</a></p>
            <p style='margin: 5px 0;'>📍 Calle Ejemplo 123, Tijuana</p>
        </div>
        <div style='text-align: right;'>
            <p style='margin: 5px 0;'>📞 +52 664 123 4567</p>
            <p style='margin: 5px 0;'>© 2025 Empresa XYZ - Todos los derechos reservados</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
