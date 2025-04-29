import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Page configuration
st.set_page_config(
    page_title="Dashboard Corporativo: Cumplimiento NOM-035 y Evolución LEAN 2.0", 
    layout="wide",
    page_icon="📊"
)

# Custom CSS for styling
st.markdown("""
<style>
    .card {
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        background: white;
    }
    .kpi-good { background-color: #e6f7e6; border-left: 5px solid #4CAF50; }
    .kpi-warning { background-color: #fff9e6; border-left: 5px solid #FFC107; }
    .kpi-danger { background-color: #ffebee; border-left: 5px solid #F44336; }
    .stAlert { padding: 15px !important; }
</style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://via.placeholder.com/150x50.png?text=Company+Logo", width=150)
with col2:
    st.title("🏛️ Dashboard Corporativo")
    st.markdown("**Cumplimiento NOM-035 y Evolución LEAN 2.0**")
    st.caption(f"Última actualización: {datetime.datetime.now().strftime('%d/%m/%Y')}")

st.markdown("---")

# Sidebar filters
with st.sidebar:
    st.header("🔎 Filtros")
    departments = st.multiselect(
        "Departamentos:",
        ['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'],
        default=['Producción', 'Calidad', 'Logística']
    )
    date_range = st.date_input(
        "Rango de fechas:",
        value=[datetime.date(2025, 1, 1), datetime.date(2025, 4, 1)]
    )

# KPI Cards
st.header("📊 KPIs Estratégicos")

def kpi_card(title, value, status="neutral"):
    colors = {
        "good": ("#4CAF50", "🟢"),
        "warning": ("#FFC107", "🟡"),
        "danger": ("#F44336", "🔴"),
        "neutral": ("#2196F3", "🔵")
    }
    color, icon = colors.get(status, ("#2196F3", "🔵"))
    
    return f"""
    <div class="card kpi-{status}">
        <div style="display:flex; justify-content:space-between;">
            <h3>{title}</h3>
            <span style="font-size:24px">{icon}</span>
        </div>
        <h2 style="color:{color}; margin-top:5px;">{value}%</h2>
        <div style="height:6px; background:#eee; border-radius:3px;">
            <div style="width:{value}%; height:6px; background:{color}; border-radius:3px;"></div>
        </div>
    </div>
    """

cols = st.columns(3)
with cols[0]:
    st.markdown(kpi_card("Cumplimiento NOM-035", 92, "good"), unsafe_allow_html=True)
with cols[1]:
    st.markdown(kpi_card("Cumplimiento Calidad", 80, "warning"), unsafe_allow_html=True)
with cols[2]:
    st.markdown(kpi_card("Cumplimiento Logística", 70, "danger"), unsafe_allow_html=True)

# Data visualization with Seaborn
st.subheader("📈 Evaluaciones por Departamento")
eval_data = pd.DataFrame({
    'Departamento': ['Producción', 'Calidad', 'Logística', 'Administración', 'Ventas'],
    'Evaluaciones (%)': [95, 90, 85, 80, 75],
    'Meta': [90, 90, 90, 90, 90]
})

# Create Seaborn plot
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    data=eval_data.melt(id_vars='Departamento', var_name='Tipo', value_name='Porcentaje'),
    x='Porcentaje',
    y='Departamento',
    hue='Tipo',
    palette={'Evaluaciones (%)': '#4a6fa5', 'Meta': '#FFC107'},
    orient='h'
)
plt.title('Evaluaciones Aplicadas vs Meta por Departamento', pad=20)
plt.xlabel('Porcentaje')
plt.ylabel('')
plt.legend(title='')
st.pyplot(plt)

# KPI Table
st.subheader("📋 Esquema de KPIs")
kpi_table = pd.DataFrame({
    'Indicador': ['Evaluaciones Aplicadas', 'Protocolos Implementados', 'Acciones Preventivas'],
    'Tipo': ['Porcentaje', 'Conteo', 'Ratio'],
    'Frecuencia': ['Mensual', 'Trimestral', 'Semanal'],
    'Responsable': ['RH', 'Calidad', 'Operaciones']
})
st.dataframe(kpi_table, use_container_width=True)

# Alert
st.markdown("""
<div class="card kpi-warning">
    <h3>🚨 Atención: Cumplimiento en Logística</h3>
    <p>El departamento de Logística está por debajo de la meta (70% vs 90% esperado).</p>
</div>
""", unsafe_allow_html=True)

# Export button
if st.button('📊 Exportar Datos a CSV'):
    csv = eval_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name="evaluaciones_departamentos.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#666; font-size:small;">
    <p>© 2025 Empresa XYZ | soporte@empresa.com</p>
</div>
""", unsafe_allow_html=True)

