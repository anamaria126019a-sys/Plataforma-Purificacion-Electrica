import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import math


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Plataforma de Purificación Eléctrica",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# ESTADO
# ============================================================

if "tema" not in st.session_state:
    st.session_state.tema = "Claro"

if "acento" not in st.session_state:
    st.session_state.acento = "Azul"


# ============================================================
# FUNCIÓN PARA RENDERIZAR HTML
# CORRECCIÓN DEL PROBLEMA DE HTML VISIBLE
# ============================================================

def render_html(contenido):
    """
    Renderiza HTML directamente cuando la versión de Streamlit
    lo permite. Si no, utiliza st.markdown como respaldo.
    """
    if hasattr(st, "html"):
        st.html(contenido)
    else:
        st.markdown(contenido, unsafe_allow_html=True)


# ============================================================
# COLORES
# ============================================================

if st.session_state.tema == "Claro":

    BG = "#F4F8FC"
    CARD = "#FFFFFF"
    CARD2 = "#EDF4FA"
    TEXT = "#162033"
    MUTED = "#63748A"
    BORDER = "#D8E2EC"

else:

    BG = "#09111F"
    CARD = "#111C2D"
    CARD2 = "#17253A"
    TEXT = "#F3F7FC"
    MUTED = "#AAB8C8"
    BORDER = "#2B3C54"


ACCENTS = {
    "Azul": "#2563EB",
    "Turquesa": "#0891B2",
    "Violeta": "#7C3AED",
    "Verde": "#059669"
}

ACCENT = ACCENTS[st.session_state.acento]
ACCENT2 = "#06B6D4"


# ============================================================
# BARRA LATERAL
# ============================================================

render_html(f"""
<div style="
    padding: 10px 5px 18px 5px;
    text-align:center;
">
    <div style="
        font-size:28px;
        font-weight:800;
        color:{ACCENT};
    ">
        ⚡
    </div>

    <div style="
        font-size:18px;
        font-weight:800;
        color:{TEXT};
        margin-top:4px;
    ">
        Plataforma científica
    </div>

    <div style="
        font-size:12px;
        color:{MUTED};
        margin-top:3px;
    ">
        Física II · Ingeniería
    </div>
</div>
""")


st.sidebar.markdown("### Apariencia")

st.session_state.tema = st.sidebar.selectbox(
    "Tema",
    ["Claro", "Oscuro"],
    index=0 if st.session_state.tema == "Claro" else 1
)

st.session_state.acento = st.sidebar.selectbox(
    "Color de acento",
    ["Azul", "Turquesa", "Violeta", "Verde"],
    index=["Azul", "Turquesa", "Violeta", "Verde"].index(
        st.session_state.acento
    )
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
<style>

.stApp {{
    background: {BG};
    color: {TEXT};
}}

section[data-testid="stSidebar"] {{
    background: {CARD};
    border-right: 1px solid {BORDER};
}}

section[data-testid="stSidebar"] * {{
    color: {TEXT};
}}

h1, h2, h3, h4 {{
    color: {TEXT};
}}

p {{
    color: {TEXT};
}}

.hero {{
    padding: 42px 38px;
    border-radius: 24px;
    margin-bottom: 30px;

    background:
        radial-gradient(
            circle at top right,
            rgba(37,99,235,0.18),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            {CARD},
            {CARD2}
        );

    border: 1px solid {BORDER};
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    text-align: center;
}}

.hero-title {{
    font-size: 42px;
    font-weight: 900;
    color: {ACCENT};
    line-height: 1.1;
    margin-bottom: 15px;
}}

.hero-subtitle {{
    max-width: 900px;
    margin: auto;
    font-size: 17px;
    line-height: 1.7;
    color: {MUTED};
}}

.hero-tags {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 9px;
    margin-top: 22px;
}}

.tag {{
    padding: 7px 13px;
    border-radius: 999px;
    background: {CARD2};
    border: 1px solid {BORDER};
    color: {ACCENT};
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.5px;
}}

.section-title {{
    font-size: 30px;
    font-weight: 900;
    color: {TEXT};
    text-align: center;
    margin-top: 15px;
}}

.section-subtitle {{
    text-align: center;
    color: {MUTED};
    font-size: 15px;
    margin-bottom: 12px;
}}

.card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 18px;
    padding: 24px;
    margin: 10px 0 20px 0;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}}

.card-title {{
    font-size: 20px;
    font-weight: 850;
    color: {ACCENT};
    margin-bottom: 12px;
}}

.card-text {{
    color: {TEXT};
    line-height: 1.7;
    font-size: 15px;
}}

.small-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 19px;
    min-height: 130px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.04);
}}

.small-title {{
    font-size: 17px;
    font-weight: 800;
    color: {ACCENT};
    margin-bottom: 8px;
}}

.small-text {{
    color: {TEXT};
    line-height: 1.55;
    font-size: 14px;
}}

.process {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 18px;
    padding: 20px 15px;
    text-align: center;
    min-height: 175px;
    box-shadow: 0 7px 20px rgba(0,0,0,0.05);
}}

.process-number {{
    width: 42px;
    height: 42px;
    margin: 0 auto 12px auto;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: {ACCENT};
    color: white;
    font-weight: 900;
    font-size: 17px;
}}

.process-title {{
    color: {TEXT};
    font-size: 16px;
    font-weight: 850;
}}

.process-text {{
    color: {MUTED};
    font-size: 13px;
    line-height: 1.45;
    margin-top: 8px;
}}

.variable-box {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-left: 5px solid {ACCENT};
    border-radius: 16px;
    padding: 18px;
    min-height: 165px;
    box-shadow: 0 7px 20px rgba(0,0,0,0.04);
}}

.variable-title {{
    font-size: 17px;
    font-weight: 850;
    color: {ACCENT};
    margin-bottom: 10px;
}}

.variable-box ul {{
    margin-top: 5px;
    padding-left: 20px;
}}

.variable-box li {{
    color: {TEXT};
    margin-bottom: 7px;
    font-size: 14px;
}}

.formula-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 17px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 7px 20px rgba(0,0,0,0.04);
}}

.formula-name {{
    font-size: 18px;
    font-weight: 850;
    color: {ACCENT};
    margin-bottom: 8px;
}}

.formula {{
    background: {CARD2};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 13px;
    text-align: center;
    font-size: 21px;
    font-weight: 700;
    color: {TEXT};
    margin: 10px 0;
}}

.formula-vars {{
    color: {MUTED};
    font-size: 13px;
    line-height: 1.6;
}}

.metric-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 17px;
    padding: 18px;
    text-align: center;
    min-height: 115px;
    box-shadow: 0 7px 20px rgba(0,0,0,0.04);
}}

.metric-label {{
    color: {MUTED};
    font-size: 12px;
    font-weight: 700;
}}

.metric-value {{
    color: {ACCENT};
    font-size: 25px;
    font-weight: 900;
    margin-top: 6px;
}}

.note {{
    background: {CARD2};
    border-left: 5px solid {ACCENT};
    border-radius: 13px;
    padding: 17px;
    color: {TEXT};
    line-height: 1.6;
    margin: 18px 0;
}}

.info-box {{
    background: linear-gradient(
        135deg,
        {CARD2},
        {CARD}
    );
    border: 1px solid {BORDER};
    border-radius: 18px;
    padding: 22px;
    margin: 18px 0;
}}

.info-title {{
    color: {ACCENT};
    font-size: 18px;
    font-weight: 850;
    margin-bottom: 8px;
}}

.team-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    min-height: 205px;
}}

.team-icon {{
    font-size: 30px;
    margin-bottom: 8px;
}}

.team-name {{
    font-size: 16px;
    font-weight: 850;
    color: {TEXT};
}}

.team-data {{
    color: {MUTED};
    font-size: 13px;
    margin-top: 8px;
    line-height: 1.5;
}}

.footer {{
    margin-top: 45px;
    padding: 22px;
    border-top: 1px solid {BORDER};
    text-align: center;
    color: {MUTED};
    font-size: 12px;
}}

.warning-box {{
    background: rgba(245,158,11,0.10);
    border: 1px solid rgba(245,158,11,0.35);
    border-left: 5px solid #F59E0B;
    border-radius: 14px;
    padding: 17px;
    color: {TEXT};
    line-height: 1.6;
}}

.stButton > button {{
    border-radius: 10px;
}}

div[data-baseweb="select"] > div {{
    background: {CARD};
    border-color: {BORDER};
}}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# FUNCIONES VISUALES
# ============================================================

def title_block(title, subtitle):

    render_html(f"""
    <div class="section-title">
        {title}
    </div>

    <div class="section-subtitle">
        {subtitle}
    </div>
    """)

    st.divider()


def card(title, body):

    render_html(f"""
    <div class="card">

        <div class="card-title">
            {title}
        </div>

        <div class="card-text">
            {body}
        </div>

    </div>
    """)


def metric(label, value, unit=""):

    render_html(f"""
    <div class="metric-card">

        <div class="metric-label">
            {label}
        </div>

        <div class="metric-value">
            {value}
            <span style="font-size:13px;color:{MUTED};">
                {unit}
            </span>
        </div>

    </div>
    """)


def plot_layout(fig, height=450):

    fig.update_layout(
        template="plotly_white" if st.session_state.tema == "Claro" else "plotly_dark",
        height=height,
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font=dict(
            color=TEXT,
            family="Arial"
        ),
        margin=dict(
            l=50,
            r=30,
            t=60,
            b=50
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    return fig


# ============================================================
# MODELO DE AIRE
# NO MODIFICADO
# ============================================================

def air_model(
    voltage,
    distance_cm,
    flow_lpm,
    particle_um,
    charge_fC,
    residence_s
):

    distance_m = max(distance_cm / 100.0, 1e-4)
    radius_m = max(particle_um * 1e-6 / 2.0, 1e-9)
    charge_C = charge_fC * 1e-15

    electric_field = voltage / distance_m

    viscosity = 1.81e-5

    drift_velocity = (
        abs(charge_C) * abs(electric_field) /
        (6 * math.pi * viscosity * radius_m)
    )

    flow_m3s = flow_lpm * 1e-3 / 60.0

    reference_area = max(distance_m ** 2, 1e-5)

    air_velocity = flow_m3s / reference_area

    displacement = drift_velocity * residence_s

    ratio = displacement / max(distance_m / 2.0, 1e-8)

    efficiency = 100 * (1 - math.exp(-max(ratio, 0)))

    efficiency = float(np.clip(efficiency, 0, 99.9))

    resistance = max(
        distance_cm * 1000 / max(voltage, 1),
        1.0
    )

    current_A = voltage / resistance

    power_W = voltage * current_A

    energy_Wh = power_W * residence_s / 3600

    return {
        "electric_field": electric_field,
        "drift_velocity": drift_velocity,
        "air_velocity": air_velocity,
        "displacement": displacement,
        "efficiency": efficiency,
        "current": current_A,
        "power": power_W,
        "energy": energy_Wh
    }


# ============================================================
# TRAYECTORIA DE AIRE
# NO MODIFICADO
# ============================================================

def air_trajectory(
    voltage,
    distance_cm,
    particle_um,
    charge_fC,
    residence_s,
    points=250
):

    distance_m = max(distance_cm / 100, 1e-4)

    radius_m = max(
        particle_um * 1e-6 / 2,
        1e-9
    )

    charge_C = charge_fC * 1e-15

    E = voltage / distance_m

    viscosity = 1.81e-5

    drift_velocity = (
        abs(charge_C) * abs(E) /
        (6 * math.pi * viscosity * radius_m)
    )

    t = np.linspace(
        0,
        max(residence_s, 0.01),
        points
    )

    longitudinal = t / max(
        residence_s,
        0.01
    )

    transversal = drift_velocity * t

    transversal = np.clip(
        transversal,
        0,
        distance_m / 2
    )

    return {
        "x": longitudinal,
        "y": transversal * 1000,
        "distance_mm": distance_m * 1000
    }


# ============================================================
# MODELO DE AGUA
# NO MODIFICADO
# ============================================================

def water_model(
    voltage,
    current,
    time_min,
    flow_lpm,
    conductivity,
    pH,
    gap_cm,
    concentration_initial
):

    time_s = time_min * 60

    flow_lpm = max(flow_lpm, 0.01)

    volume_L = flow_lpm * time_min

    charge_dose = (
        current * time_s /
        max(volume_L, 1e-6)
    )

    electrical_factor = (
        1 - math.exp(-charge_dose / 900)
    )

    pH_factor = math.exp(
        -((pH - 7) ** 2) /
        (2 * 2.2 ** 2)
    )

    conductivity_factor = (
        0.35 +
        0.65 *
        (
            conductivity /
            (conductivity + 500)
        )
    )

    gap_factor = math.exp(
        -max(gap_cm - 1, 0) / 4
    )

    efficiency = (
        100 *
        electrical_factor *
        pH_factor *
        conductivity_factor *
        gap_factor
    )

    efficiency = float(
        np.clip(
            efficiency,
            0,
            99.9
        )
    )

    concentration_final = (
        concentration_initial *
        (1 - efficiency / 100)
    )

    power_W = voltage * current

    energy_Wh = (
        power_W * time_s / 3600
    )

    volume_m3 = volume_L / 1000

    SEC = (
        (energy_Wh / 1000) /
        max(volume_m3, 1e-9)
    )

    return {
        "charge_dose": charge_dose,
        "efficiency": efficiency,
        "concentration_final": concentration_final,
        "power": power_W,
        "energy": energy_Wh,
        "volume": volume_L,
        "SEC": SEC
    }


# ============================================================
# BARRIDO AIRE
# NO MODIFICADO
# ============================================================

def air_sweep(variable):

    variables = {

        "Voltaje (V)": np.linspace(
            100, 3000, 60
        ),

        "Distancia entre electrodos (cm)": np.linspace(
            0.5, 5, 60
        ),

        "Caudal de aire (L/min)": np.linspace(
            1, 30, 60
        ),

        "Tamaño de partícula (µm)": np.linspace(
            0.5, 20, 60
        ),

        "Carga de partícula (fC)": np.linspace(
            0.1, 10, 60
        ),

        "Tiempo de residencia (s)": np.linspace(
            0.05, 5, 60
        )
    }

    values = variables[variable]

    efficiencies = []
    energies = []

    for value in values:

        params = {
            "voltage": 1200,
            "distance_cm": 2,
            "flow_lpm": 10,
            "particle_um": 5,
            "charge_fC": 2,
            "residence_s": 1
        }

        if variable == "Voltaje (V)":
            params["voltage"] = value

        elif variable == "Distancia entre electrodos (cm)":
            params["distance_cm"] = value

        elif variable == "Caudal de aire (L/min)":
            params["flow_lpm"] = value

        elif variable == "Tamaño de partícula (µm)":
            params["particle_um"] = value

        elif variable == "Carga de partícula (fC)":
            params["charge_fC"] = value

        elif variable == "Tiempo de residencia (s)":
            params["residence_s"] = value

        result = air_model(**params)

        efficiencies.append(
            result["efficiency"]
        )

        energies.append(
            result["energy"]
        )

    return (
        values,
        np.array(efficiencies),
        np.array(energies)
    )


# ============================================================
# BARRIDO AGUA
# NO MODIFICADO
# ============================================================

def water_sweep(variable):

    variables = {

        "Voltaje (V)": np.linspace(
            5, 50, 60
        ),

        "Corriente (A)": np.linspace(
            0.05, 5, 60
        ),

        "Tiempo de tratamiento (min)": np.linspace(
            1, 30, 60
        ),

        "Caudal (L/min)": np.linspace(
            0.1, 10, 60
        ),

        "Conductividad (µS/cm)": np.linspace(
            50, 2500, 60
        ),

        "pH": np.linspace(
            3, 11, 60
        ),

        "Distancia entre electrodos (cm)": np.linspace(
            0.5, 5, 60
        ),

        "Concentración inicial (mg/L)": np.linspace(
            10, 500, 60
        )
    }

    values = variables[variable]

    efficiencies = []
    concentrations = []
    energies = []

    for value in values:

        params = {
            "voltage": 20,
            "current": 1,
            "time_min": 10,
            "flow_lpm": 1,
            "conductivity": 500,
            "pH": 7,
            "gap_cm": 2,
            "concentration_initial": 100
        }

        if variable == "Voltaje (V)":
            params["voltage"] = value

        elif variable == "Corriente (A)":
            params["current"] = value

        elif variable == "Tiempo de tratamiento (min)":
            params["time_min"] = value

        elif variable == "Caudal (L/min)":
            params["flow_lpm"] = value

        elif variable == "Conductividad (µS/cm)":
            params["conductivity"] = value

        elif variable == "pH":
            params["pH"] = value

        elif variable == "Distancia entre electrodos (cm)":
            params["gap_cm"] = value

        elif variable == "Concentración inicial (mg/L)":
            params["concentration_initial"] = value

        result = water_model(**params)

        efficiencies.append(
            result["efficiency"]
        )

        concentrations.append(
            result["concentration_final"]
        )

        energies.append(
            result["energy"]
        )

    return (
        values,
        np.array(efficiencies),
        np.array(concentrations),
        np.array(energies)
    )


# ============================================================
# SISTEMA CONCEPTUAL
# NO MODIFICADO
# ============================================================

def conceptual_system():

    fig = go.Figure()

    fig.add_shape(
        type="rect",
        x0=0,
        x1=10,
        y0=0,
        y1=6,
        line=dict(
            color=ACCENT,
            width=3
        ),
        fillcolor="rgba(0,0,0,0)"
    )

    fig.add_shape(
        type="line",
        x0=3,
        x1=3,
        y0=0.5,
        y1=5.5,
        line=dict(
            color=ACCENT,
            width=5
        )
    )

    fig.add_shape(
        type="line",
        x0=7,
        x1=7,
        y0=0.5,
        y1=5.5,
        line=dict(
            color=ACCENT2,
            width=5
        )
    )

    particles_x = [
        1.0,
        1.7,
        2.2,
        4.0,
        4.7,
        5.4,
        6.2,
        8.0,
        8.7
    ]

    particles_y = [
        1.2,
        3.4,
        5.0,
        1.8,
        4.2,
        2.7,
        5.0,
        2.0,
        4.7
    ]

    fig.add_trace(
        go.Scatter(
            x=particles_x,
            y=particles_y,
            mode="markers",
            marker=dict(
                size=12,
                color=ACCENT2
            ),
            name="Partículas"
        )
    )

    fig.add_annotation(
        x=3,
        y=5.9,
        text="Electrodo",
        showarrow=False
    )

    fig.add_annotation(
        x=7,
        y=5.9,
        text="Electrodo",
        showarrow=False
    )

    fig.add_annotation(
        x=5,
        y=0.3,
        text="Región de tratamiento",
        showarrow=False
    )

    fig.update_xaxes(
        visible=False,
        range=[0, 10]
    )

    fig.update_yaxes(
        visible=False,
        range=[0, 6]
    )

    fig.update_layout(
        height=430,
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        ),
        showlegend=False
    )

    return fig


# ============================================================
# INICIO
# ============================================================

def page_inicio():

    render_html("""
    <div class="hero">

        <div class="hero-title">
            ⚡ Plataforma de Purificación Eléctrica
        </div>

        <div class="hero-subtitle">
            Plataforma experimental y computacional para estudiar la influencia
            de los fenómenos eléctricos en el tratamiento de aire y agua,
            relacionando variables físicas, eficiencia de tratamiento y consumo energético.
        </div>

        <div class="hero-tags">

            <span class="tag">FÍSICA II</span>
            <span class="tag">MODELAMIENTO</span>
            <span class="tag">SIMULACIÓN</span>
            <span class="tag">INNOVACIÓN</span>
            <span class="tag">ODS 9</span>
            <span class="tag">ODS 11</span>

        </div>

    </div>
    """)

    card(
        "🔬 ¿Qué propone esta plataforma?",
        """
        Esta plataforma integra principios de Física II, modelamiento matemático,
        simulación computacional y experimentación para estudiar procesos de
        purificación eléctrica aplicados al tratamiento de aire y agua.
        <br><br>
        El propósito no es solamente observar si existe una mejora en el tratamiento,
        sino analizar cómo las condiciones de operación modifican la eficiencia,
        el comportamiento físico del sistema y el consumo energético.
        <br><br>
        De esta manera, el proyecto conecta teoría, simulación, prototipo y medición
        experimental dentro de una misma herramienta de análisis.
        """
    )

    render_html("""
    <div class="section-title">
        🧭 Ruta de investigación
    </div>

    <div class="section-subtitle">
        Del fenómeno físico a la interpretación de resultados
    </div>
    """)

    cols = st.columns(7)

    procesos = [
        (
            "1",
            "Teoría",
            "Principios físicos y relaciones fundamentales."
        ),
        (
            "2",
            "Modelo",
            "Representación matemática de las variables."
        ),
        (
            "3",
            "Simulación",
            "Variación de condiciones y visualización."
        ),
        (
            "4",
            "Prototipo",
            "Implementación experimental a pequeña escala."
        ),
        (
            "5",
            "Medición",
            "Obtención de datos experimentales."
        ),
        (
            "6",
            "Comparación",
            "Contraste entre modelo y experimento."
        ),
        (
            "7",
            "Optimización",
            "Búsqueda de condiciones favorables."
        )
    ]

    for col, proceso in zip(cols, procesos):

        with col:

            render_html(f"""
            <div class="process">

                <div class="process-number">
                    {proceso[0]}
                </div>

                <div class="process-title">
                    {proceso[1]}
                </div>

                <div class="process-text">
                    {proceso[2]}
                </div>

            </div>
            """)

    st.write("")

    render_html("""
    <div class="section-title">
        ⚙️ Representación conceptual
    </div>
    """)

    st.plotly_chart(
        conceptual_system(),
        use_container_width=True
    )

    render_html(f"""
    <div class="note">

        <strong>Idea central:</strong><br>

        El objetivo es estudiar la relación entre
        <strong>eficiencia de tratamiento</strong>,
        <strong>condiciones de operación</strong> y
        <strong>consumo energético</strong>,
        buscando identificar condiciones de funcionamiento
        técnicamente favorables mediante el análisis conjunto
        de teoría, simulación y experimentación.

    </div>
    """)

    render_html("""
    <div class="section-title">
        🌎 Conexión con los ODS
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                🏭 ODS 9 · Industria, innovación e infraestructura
            </div>

            <div class="small-text">
                El proyecto relaciona ciencia, modelamiento y tecnología
                para estudiar alternativas de tratamiento eléctrico y
                analizar su comportamiento energético.
            </div>

        </div>
        """)

    with c2:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                🏙️ ODS 11 · Ciudades y comunidades sostenibles
            </div>

            <div class="small-text">
                La investigación aborda fenómenos relacionados con la calidad
                del aire y del agua desde una perspectiva experimental,
                tecnológica y de eficiencia energética.
            </div>

        </div>
        """)

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        👩‍🔬 Equipo del proyecto
    </div>
    """)

    team_cols = st.columns(3)

    equipo = [
        (
            "👩‍🔬",
            "Ana Maria Florez Barbosa",
            "2245047",
            "Ingeniería Química"
        ),
        (
            "👩‍🔬",
            "Ines Marai Rincon Manosalva",
            "2245072",
            "Ingeniería Química"
        ),
        (
            "👩‍🔬",
            "Maria Fernanada Ardila Peña",
            "2255127",
            "Estudiante UIS"
        )
    ]

    for col, persona in zip(team_cols, equipo):

        with col:

            render_html(f"""
            <div class="team-card">

                <div class="team-icon">
                    {persona[0]}
                </div>

                <div class="team-name">
                    {persona[1]}
                </div>

                <div class="team-data">
                    Código: {persona[2]}<br>
                    {persona[3]}<br>
                    Universidad Industrial de Santander
                </div>

            </div>
            """)

    render_html("""
    <div class="footer">
        Universidad Industrial de Santander · Sede Barbosa · 2026
        <br>
        Física II · Ingeniería Química · Modelamiento y simulación
    </div>
    """)


# ============================================================
# PLANTA DE AIRE
# ============================================================

def page_aire():

    title_block(
        "🌬️ Planta de Purificación de Aire",
        "Simulación interactiva del efecto de las variables eléctricas y de flujo sobre la separación de partículas."
    )

    card(
        "🌬️ ¿Cómo funciona el módulo de aire?",
        """
        El módulo representa de manera computacional el comportamiento de partículas
        suspendidas en una corriente de aire sometida a un campo eléctrico entre
        electrodos. La interacción entre la carga de las partículas y el campo
        eléctrico permite estudiar su desplazamiento y estimar una eficiencia
        de separación.
        <br><br>
        El modelo permite modificar las condiciones eléctricas, geométricas,
        de flujo y características de las partículas para observar cómo cambian
        las variables calculadas.
        <br><br>
        La simulación está diseñada como una herramienta de análisis del fenómeno
        físico y no como una garantía del comportamiento de un equipo industrial real.
        """
    )

    render_html("""
    <div class="section-title">
        🧩 Variables estudiadas
    </div>
    """)

    c1, c2, c3 = st.columns(3)

    with c1:

        render_html("""
        <div class="variable-box">

            <div class="variable-title">
                ⚡ Variables eléctricas
            </div>

            <ul>
                <li>Diferencia de potencial</li>
                <li>Campo eléctrico</li>
                <li>Carga de partícula</li>
            </ul>

        </div>
        """)

    with c2:

        render_html("""
        <div class="variable-box">

            <div class="variable-title">
                🌪️ Variables de flujo
            </div>

            <ul>
                <li>Caudal de aire</li>
                <li>Velocidad del aire</li>
                <li>Tiempo de residencia</li>
            </ul>

        </div>
        """)

    with c3:

        render_html("""
        <div class="variable-box">

            <div class="variable-title">
                🔬 Características
            </div>

            <ul>
                <li>Tamaño de partícula</li>
                <li>Distancia entre electrodos</li>
                <li>Eficiencia de separación</li>
            </ul>

        </div>
        """)

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        🎛️ Condiciones de operación
    </div>

    <div class="section-subtitle">
        Modifica las variables y observa cómo cambia el comportamiento del modelo.
    </div>
    """)

    c1, c2, c3 = st.columns(3)

    with c1:

        voltage = st.slider(
            "Voltaje (V)",
            100.0,
            3000.0,
            1200.0,
            50.0
        )

        distance = st.slider(
            "Distancia entre electrodos (cm)",
            0.5,
            5.0,
            2.0,
            0.1
        )

    with c2:

        particle = st.slider(
            "Tamaño de partícula (µm)",
            0.5,
            20.0,
            5.0,
            0.5
        )

        flow = st.slider(
            "Caudal de aire (L/min)",
            1.0,
            30.0,
            10.0,
            0.5
        )

    with c3:

        charge = st.slider(
            "Carga de partícula (fC)",
            0.1,
            10.0,
            2.0,
            0.1
        )

        residence = st.slider(
            "Tiempo de residencia (s)",
            0.05,
            5.0,
            1.0,
            0.05
        )

    result = air_model(
        voltage,
        distance,
        flow,
        particle,
        charge,
        residence
    )

    st.write("")

    render_html("""
    <div class="section-title">
        📊 Resultados instantáneos
    </div>
    """)

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        metric(
            "Campo eléctrico",
            f"{result['electric_field']/1000:.2f}",
            "kV/m"
        )

    with m2:
        metric(
            "Velocidad de deriva",
            f"{result['drift_velocity']:.5f}",
            "m/s"
        )

    with m3:
        metric(
            "Eficiencia de separación",
            f"{result['efficiency']:.2f}",
            "%"
        )

    with m4:
        metric(
            "Potencia",
            f"{result['power']:.3f}",
            "W"
        )

    m5, m6 = st.columns(2)

    with m5:
        metric(
            "Velocidad del aire",
            f"{result['air_velocity']:.5f}",
            "m/s"
        )

    with m6:
        metric(
            "Energía",
            f"{result['energy']:.5f}",
            "Wh"
        )

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        🌀 Trayectoria de una partícula
    </div>

    <div class="section-subtitle">
        Visualización conceptual del desplazamiento transversal debido al campo eléctrico.
    </div>
    """)

    trajectory = air_trajectory(
        voltage,
        distance,
        particle,
        charge,
        residence
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=trajectory["x"],
            y=trajectory["y"],
            mode="lines",
            name="Trayectoria",
            line=dict(
                color=ACCENT,
                width=4
            )
        )
    )

    fig.update_layout(
        title="Trayectoria simulada",
        xaxis_title="Posición longitudinal normalizada",
        yaxis_title="Desplazamiento transversal (mm)"
    )

    st.plotly_chart(
        plot_layout(fig, 450),
        use_container_width=True
    )

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        📈 Análisis de sensibilidad
    </div>

    <div class="section-subtitle">
        Selecciona una variable para estudiar su influencia sobre el sistema.
    </div>
    """)

    variable = st.selectbox(
        "Variable que deseas modificar",
        [
            "Voltaje (V)",
            "Distancia entre electrodos (cm)",
            "Caudal de aire (L/min)",
            "Tamaño de partícula (µm)",
            "Carga de partícula (fC)",
            "Tiempo de residencia (s)"
        ]
    )

    values, efficiencies, energies = air_sweep(
        variable
    )

    fig_eff = go.Figure()

    fig_eff.add_trace(
        go.Scatter(
            x=values,
            y=efficiencies,
            mode="lines",
            name="Eficiencia",
            line=dict(
                color=ACCENT,
                width=4
            )
        )
    )

    current_value = {
        "Voltaje (V)": voltage,
        "Distancia entre electrodos (cm)": distance,
        "Caudal de aire (L/min)": flow,
        "Tamaño de partícula (µm)": particle,
        "Carga de partícula (fC)": charge,
        "Tiempo de residencia (s)": residence
    }[variable]

    current_result = air_model(
        voltage,
        distance,
        flow,
        particle,
        charge,
        residence
    )

    fig_eff.add_trace(
        go.Scatter(
            x=[current_value],
            y=[current_result["efficiency"]],
            mode="markers",
            name="Condición actual",
            marker=dict(
                size=13,
                symbol="diamond",
                color=ACCENT2
            )
        )
    )

    fig_eff.update_layout(
        title="Eficiencia de separación vs variable seleccionada",
        xaxis_title=variable,
        yaxis_title="Eficiencia (%)"
    )

    st.plotly_chart(
        plot_layout(fig_eff, 450),
        use_container_width=True
    )

    fig_energy = go.Figure()

    fig_energy.add_trace(
        go.Scatter(
            x=values,
            y=energies,
            mode="lines",
            name="Energía",
            line=dict(
                color=ACCENT2,
                width=4
            )
        )
    )

    fig_energy.update_layout(
        title="Energía vs variable seleccionada",
        xaxis_title=variable,
        yaxis_title="Energía (Wh)"
    )

    st.plotly_chart(
        plot_layout(fig_energy, 450),
        use_container_width=True
    )

    render_html(f"""
    <div class="note">

        <strong>Interpretación:</strong><br>

        La gráfica permite observar cómo la modificación de una variable
        puede cambiar la eficiencia y el consumo energético del modelo.
        La condición marcada con el rombo corresponde a los valores
        actualmente seleccionados por el usuario.

    </div>
    """)

    render_html("""
    <div class="section-title">
        📋 Rangos de entrada
    </div>
    """)

    air_ranges = pd.DataFrame({
        "Variable": [
            "Voltaje",
            "Distancia",
            "Caudal",
            "Partícula",
            "Carga",
            "Residencia"
        ],
        "Unidad": [
            "V",
            "cm",
            "L/min",
            "µm",
            "fC",
            "s"
        ],
        "Mínimo": [
            100,
            0.5,
            1,
            0.5,
            0.1,
            0.05
        ],
        "Máximo": [
            3000,
            5,
            30,
            20,
            10,
            5
        ]
    })

    st.dataframe(
        air_ranges,
        use_container_width=True,
        hide_index=True
    )

    render_html("""
    <div class="warning-box">

        <strong>Nota científica:</strong><br>

        Los resultados mostrados corresponden al modelo matemático
        implementado en esta plataforma. La eficiencia calculada
        representa una estimación computacional y debe contrastarse
        con mediciones experimentales antes de extrapolar los resultados
        a sistemas reales.

    </div>
    """)


# ============================================================
# PLANTA DE AGUA
# ============================================================

def page_agua():

    title_block(
        "💧 Planta de Purificación de Agua",
        "Modelo interactivo para estudiar la influencia de las variables eléctricas y fisicoquímicas sobre el tratamiento."
    )

    card(
        "💧 ¿Cómo funciona el módulo de agua?",
        """
        El módulo representa un proceso de tratamiento eléctrico de agua
        mediante el estudio de la interacción entre variables eléctricas,
        hidráulicas y fisicoquímicas.
        <br><br>
        El modelo permite analizar cómo el voltaje, la corriente,
        el tiempo de tratamiento, el caudal, la conductividad, el pH,
        la distancia entre electrodos y la concentración inicial pueden
        modificar la eficiencia estimada y el consumo energético.
        <br><br>
        El sistema está planteado como una herramienta de simulación
        y análisis para relacionar las condiciones de operación con
        los resultados del tratamiento.
        """
    )

    render_html("""
    <div class="section-title">
        🧩 Variables estudiadas
    </div>
    """)

    c1, c2, c3 = st.columns(3)

    with c1:

        render_html("""
        <div class="variable-box">

            <div class="variable-title">
                ⚡ Variables eléctricas
            </div>

            <ul>
                <li>Voltaje</li>
                <li>Corriente</li>
                <li>Potencia</li>
            </ul>

        </div>
        """)

    with c2:

        render_html("""
        <div class="variable-box">

            <div class="variable-title">
                🌊 Variables hidráulicas
            </div>

            <ul>
                <li>Caudal</li>
                <li>Tiempo de tratamiento</li>
                <li>Volumen tratado</li>
            </ul>

        </div>
        """)

    with c3:

        render_html("""
        <div class="variable-box">

            <div class="variable-title">
                🧪 Características del agua
            </div>

            <ul>
                <li>Conductividad</li>
                <li>pH</li>
                <li>Concentración inicial</li>
            </ul>

        </div>
        """)

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        🎛️ Condiciones de operación
    </div>

    <div class="section-subtitle">
        Todas las variables del modelo pueden modificarse dentro de los rangos establecidos.
    </div>
    """)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        voltage = st.slider(
            "Voltaje (V)",
            5.0,
            50.0,
            20.0,
            1.0
        )

        current = st.slider(
            "Corriente (A)",
            0.05,
            5.0,
            1.0,
            0.05
        )

    with c2:

        time_min = st.slider(
            "Tiempo de tratamiento (min)",
            1.0,
            30.0,
            10.0,
            1.0
        )

        flow = st.slider(
            "Caudal (L/min)",
            0.1,
            10.0,
            1.0,
            0.1
        )

    with c3:

        conductivity = st.slider(
            "Conductividad (µS/cm)",
            50.0,
            2500.0,
            500.0,
            50.0
        )

        pH = st.slider(
            "pH",
            3.0,
            11.0,
            7.0,
            0.1
        )

    with c4:

        gap = st.slider(
            "Distancia entre electrodos (cm)",
            0.5,
            5.0,
            2.0,
            0.1
        )

        concentration_initial = st.slider(
            "Concentración inicial (mg/L)",
            10.0,
            500.0,
            100.0,
            5.0
        )

    result = water_model(
        voltage,
        current,
        time_min,
        flow,
        conductivity,
        pH,
        gap,
        concentration_initial
    )

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        📊 Resultados instantáneos
    </div>
    """)

    m1, m2, m3 = st.columns(3)

    with m1:

        metric(
            "Eficiencia estimada",
            f"{result['efficiency']:.2f}",
            "%"
        )

    with m2:

        metric(
            "Concentración final",
            f"{result['concentration_final']:.2f}",
            "mg/L"
        )

    with m3:

        metric(
            "Potencia",
            f"{result['power']:.2f}",
            "W"
        )

    m4, m5, m6 = st.columns(3)

    with m4:

        metric(
            "Energía",
            f"{result['energy']:.3f}",
            "Wh"
        )

    with m5:

        metric(
            "Volumen tratado",
            f"{result['volume']:.2f}",
            "L"
        )

    with m6:

        metric(
            "SEC",
            f"{result['SEC']:.3f}",
            "kWh/m³"
        )

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        📉 Evolución de concentración
    </div>

    <div class="section-subtitle">
        Representación conceptual de la disminución de la concentración durante el tratamiento.
    </div>
    """)

    times = np.linspace(
        0,
        time_min,
        100
    )

    concentration_curve = (
        concentration_initial *
        np.exp(
            -(
                result["efficiency"] /
                100
            ) *
            times /
            max(time_min, 0.01)
        )
    )

    fig_conc = go.Figure()

    fig_conc.add_trace(
        go.Scatter(
            x=times,
            y=concentration_curve,
            mode="lines",
            name="Concentración",
            line=dict(
                color=ACCENT,
                width=4
            )
        )
    )

    fig_conc.update_layout(
        title="Concentración estimada durante el tratamiento",
        xaxis_title="Tiempo (min)",
        yaxis_title="Concentración (mg/L)"
    )

    st.plotly_chart(
        plot_layout(fig_conc, 450),
        use_container_width=True
    )

    st.write("")
    st.write("")

    render_html("""
    <div class="section-title">
        📈 Análisis de sensibilidad
    </div>

    <div class="section-subtitle">
        Estudia individualmente la influencia de cada variable del modelo.
    </div>
    """)

    variable = st.selectbox(
        "Variable que deseas modificar",
        [
            "Voltaje (V)",
            "Corriente (A)",
            "Tiempo de tratamiento (min)",
            "Caudal (L/min)",
            "Conductividad (µS/cm)",
            "pH",
            "Distancia entre electrodos (cm)",
            "Concentración inicial (mg/L)"
        ]
    )

    values, efficiencies, concentrations, energies = water_sweep(
        variable
    )

    current_value = {
        "Voltaje (V)": voltage,
        "Corriente (A)": current,
        "Tiempo de tratamiento (min)": time_min,
        "Caudal (L/min)": flow,
        "Conductividad (µS/cm)": conductivity,
        "pH": pH,
        "Distancia entre electrodos (cm)": gap,
        "Concentración inicial (mg/L)": concentration_initial
    }[variable]

    fig_eff = go.Figure()

    fig_eff.add_trace(
        go.Scatter(
            x=values,
            y=efficiencies,
            mode="lines",
            name="Eficiencia",
            line=dict(
                color=ACCENT,
                width=4
            )
        )
    )

    fig_eff.add_trace(
        go.Scatter(
            x=[current_value],
            y=[result["efficiency"]],
            mode="markers",
            name="Condición actual",
            marker=dict(
                size=13,
                symbol="diamond",
                color=ACCENT2
            )
        )
    )

    fig_eff.update_layout(
        title="Eficiencia vs variable seleccionada",
        xaxis_title=variable,
        yaxis_title="Eficiencia (%)"
    )

    st.plotly_chart(
        plot_layout(fig_eff, 450),
        use_container_width=True
    )

    fig_conc_sens = go.Figure()

    fig_conc_sens.add_trace(
        go.Scatter(
            x=values,
            y=concentrations,
            mode="lines",
            name="Concentración final",
            line=dict(
                color=ACCENT,
                width=4
            )
        )
    )

    fig_conc_sens.update_layout(
        title="Concentración final vs variable seleccionada",
        xaxis_title=variable,
        yaxis_title="Concentración final (mg/L)"
    )

    st.plotly_chart(
        plot_layout(fig_conc_sens, 450),
        use_container_width=True
    )

    fig_energy = go.Figure()

    fig_energy.add_trace(
        go.Scatter(
            x=values,
            y=energies,
            mode="lines",
            name="Energía",
            line=dict(
                color=ACCENT2,
                width=4
            )
        )
    )

    fig_energy.update_layout(
        title="Energía vs variable seleccionada",
        xaxis_title=variable,
        yaxis_title="Energía (Wh)"
    )

    st.plotly_chart(
        plot_layout(fig_energy, 450),
        use_container_width=True
    )

    render_html("""
    <div class="note">

        <strong>Interpretación:</strong><br>

        Las gráficas permiten estudiar cómo la modificación de una
        variable afecta la eficiencia estimada, la concentración final
        y el consumo energético. Esto permite analizar el sistema desde
        una perspectiva conjunta de tratamiento y energía.

    </div>
    """)

    render_html("""
    <div class="section-title">
        📋 Rangos de entrada
    </div>
    """)

    water_ranges = pd.DataFrame({
        "Variable": [
            "Voltaje",
            "Corriente",
            "Tiempo",
            "Caudal",
            "Conductividad",
            "pH",
            "Distancia",
            "Concentración inicial"
        ],
        "Unidad": [
            "V",
            "A",
            "min",
            "L/min",
            "µS/cm",
            "—",
            "cm",
            "mg/L"
        ],
        "Mínimo": [
            5,
            0.05,
            1,
            0.1,
            50,
            3,
            0.5,
            10
        ],
        "Máximo": [
            50,
            5,
            30,
            10,
            2500,
            11,
            5,
            500
        ]
    })

    st.dataframe(
        water_ranges,
        use_container_width=True,
        hide_index=True
    )

    render_html("""
    <div class="warning-box">

        <strong>Nota científica:</strong><br>

        La concentración final calculada corresponde únicamente
        a una simulación matemática. Un resultado numérico de menor
        concentración no significa que el agua sea potable ni que
        cumpla automáticamente criterios de calidad para consumo humano.

    </div>
    """)


# ============================================================
# FUNDAMENTO CIENTÍFICO
# ============================================================

def page_fundamento():

    title_block(
        "🧠 Fundamento científico",
        "Relación entre los principios de Física II y el modelamiento de la plataforma."
    )

    card(
        "⚡ Relación con Física II",
        """
        El funcionamiento conceptual de la plataforma se fundamenta
        en relaciones entre diferencia de potencial, corriente,
        campo eléctrico, fuerza sobre cargas, potencia y energía.
        <br><br>
        Estas relaciones permiten conectar las variables de operación
        con los fenómenos físicos que intervienen en los módulos de
        aire y agua.
        """
    )

    render_html("""
    <div class="section-title">
        📐 Relaciones físicas y matemáticas
    </div>
    """)

    formulas = [

        (
            "Ley de Ohm",
            "V = IR",
            "V: voltaje (V) · I: corriente (A) · R: resistencia (Ω)"
        ),

        (
            "Potencia eléctrica",
            "P = VI",
            "P: potencia (W) · V: voltaje (V) · I: corriente (A)"
        ),

        (
            "Potencia mediante corriente",
            "P = I²R",
            "P: potencia (W) · I: corriente (A) · R: resistencia (Ω)"
        ),

        (
            "Potencia mediante voltaje",
            "P = V²/R",
            "P: potencia (W) · V: voltaje (V) · R: resistencia (Ω)"
        ),

        (
            "Campo eléctrico",
            "E = −∇V",
            "E: campo eléctrico · V: potencial eléctrico"
        ),

        (
            "Ley de Gauss",
            "∇·E = ρ/ε₀",
            "E: campo eléctrico · ρ: densidad de carga · ε₀: permitividad del vacío"
        ),

        (
            "Ecuación de Poisson",
            "∇²V = −ρ/ε₀",
            "V: potencial eléctrico · ρ: densidad de carga · ε₀: permitividad"
        ),

        (
            "Fuerza eléctrica",
            "F = qE",
            "F: fuerza eléctrica · q: carga eléctrica · E: campo eléctrico"
        ),

        (
            "Aproximación entre electrodos",
            "E ≈ ΔV/d",
            "E: campo eléctrico · ΔV: diferencia de potencial · d: separación"
        ),

        (
            "Eficiencia de remoción",
            "η = [(Ci − Cf)/Ci] × 100",
            "Ci: concentración inicial · Cf: concentración final"
        ),

        (
            "Consumo energético específico",
            "SEC = Energía/Volumen",
            "SEC: consumo energético específico · Energía: energía consumida · Volumen: volumen tratado"
        )
    ]

    for nombre, formula, variables in formulas:

        render_html(f"""
        <div class="formula-card">

            <div class="formula-name">
                {nombre}
            </div>

            <div class="formula">
                {formula}
            </div>

            <div class="formula-vars">
                {variables}
            </div>

        </div>
        """)

    render_html("""
    <div class="info-box">

        <div class="info-title">
            🔗 ¿Para qué se utilizan estas relaciones?
        </div>

        Las ecuaciones permiten construir la conexión entre las
        variables de entrada y los resultados de la simulación.

        <br><br>

        <strong>Cadena física principal:</strong><br>

        Voltaje → Campo eléctrico → Fuerza sobre cargas →
        movimiento/interacción → tratamiento

        <br><br>

        <strong>Cadena energética:</strong><br>

        Voltaje + Corriente → Potencia → Energía →
        consumo energético

        <br><br>

        De esta forma, la plataforma no analiza únicamente la eficiencia
        del tratamiento, sino también el costo energético asociado
        a las condiciones de operación.

    </div>
    """)

    render_html("""
    <div class="section-title">
        🔬 Del fenómeno a la aplicación
    </div>
    """)

    c1, c2, c3 = st.columns(3)

    with c1:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                1 · Fenómeno físico
            </div>

            <div class="small-text">
                Se estudia la interacción de campos eléctricos,
                cargas y variables del medio.
            </div>

        </div>
        """)

    with c2:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                2 · Modelo matemático
            </div>

            <div class="small-text">
                Las variables físicas se relacionan mediante
                ecuaciones y aproximaciones matemáticas.
            </div>

        </div>
        """)

    with c3:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                3 · Simulación
            </div>

            <div class="small-text">
                Se modifican condiciones y se observan los cambios
                en eficiencia, energía y comportamiento del sistema.
            </div>

        </div>
        """)


# ============================================================
# INNOVACIÓN
# ============================================================

def page_innovacion():

    title_block(
        "🚀 Innovación y aplicaciones",
        "Una plataforma que conecta fenómenos eléctricos, tratamiento y eficiencia energética."
    )

    card(
        "💡 ¿Dónde está la innovación?",
        """
        La propuesta integra en una misma plataforma el estudio experimental,
        el modelamiento matemático, la simulación computacional y el análisis
        energético de dos procesos de tratamiento: aire y agua.
        <br><br>
        La innovación no se plantea únicamente como una modificación del equipo,
        sino como una metodología de análisis que permite relacionar directamente
        las condiciones de operación con la eficiencia y el consumo energético.
        <br><br>
        Esto facilita estudiar diferentes escenarios antes de llevarlos a una
        implementación física más compleja.
        """
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                🏭 Industria
            </div>

            <div class="small-text">
                Puede servir como herramienta académica para estudiar
                variables de operación relacionadas con procesos de
                separación y tratamiento.
            </div>

        </div>
        """)

    with c2:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                🧪 Laboratorios
            </div>

            <div class="small-text">
                Permite comparar resultados de modelos matemáticos,
                simulaciones y mediciones experimentales.
            </div>

        </div>
        """)

    with c3:

        render_html("""
        <div class="small-card">

            <div class="small-title">
                🏙️ Entornos urbanos
            </div>

            <div class="small-text">
                El enfoque puede relacionarse con problemáticas de
                calidad del aire, tratamiento de agua y eficiencia energética.
            </div>

        </div>
        """)

    card(
        "🏠 ¿Y qué relación puede tener con la vida cotidiana?",
        """
        Aunque el proyecto se desarrolla desde una perspectiva académica
        y experimental, los fenómenos estudiados tienen relación con
        problemas cotidianos asociados a la calidad del aire, el tratamiento
        del agua y el uso eficiente de la energía.
        <br><br>
        La plataforma permite comprender cómo modificar una condición física
        puede afectar simultáneamente el resultado del tratamiento y el
        consumo energético requerido.
        """
    )

    render_html("""
    <div class="section-title">
        🔎 Comparación conceptual
    </div>
    """)

    comparison = pd.DataFrame({
        "Aspecto": [
            "Tratamiento",
            "Variables",
            "Simulación",
            "Medición",
            "Energía",
            "Optimización"
        ],
        "Enfoques convencionales": [
            "Proceso específico",
            "Condiciones preestablecidas",
            "Limitada",
            "Separada del modelo",
            "Puede analizarse aparte",
            "Condiciones operativas"
        ],
        "Plataforma propuesta": [
            "Aire + agua",
            "Variables modificables",
            "Integrada",
            "Relacionada con el modelo",
            "Analizada directamente",
            "Eficiencia + energía + operación"
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    render_html("""
    <div class="note">

        <strong>Proyección del modelo:</strong><br>

        La eficiencia puede representarse conceptualmente como una función
        de las condiciones de operación:

        <br><br>

        <strong>
            η = f(V, I, Q, t, d, pH, Ci, ...)
        </strong>

        <br><br>

        El objetivo futuro es utilizar los datos experimentales y simulados
        para identificar relaciones y condiciones de operación favorables.

    </div>
    """)


# ============================================================
# ÉTICA
# ============================================================

def page_etica():

    title_block(
        "🛡️ Ética y responsabilidad científica",
        "Alcances, limitaciones y uso responsable de los resultados."
    )

    c1, c2 = st.columns(2)

    with c1:

        render_html("""
        <div class="card">

            <div class="card-title">
                ✅ El proyecto sí busca
            </div>

            <div class="card-text">

                • Estudiar fenómenos físicos.<br><br>

                • Construir modelos matemáticos.<br><br>

                • Comparar simulaciones y mediciones.<br><br>

                • Analizar eficiencia energética.<br><br>

                • Identificar variables relevantes.<br><br>

                • Desarrollar una herramienta experimental y académica.

            </div>

        </div>
        """)

    with c2:

        render_html("""
        <div class="card">

            <div class="card-title">
                🚫 El proyecto no pretende
            </div>

            <div class="card-text">

                • Reemplazar sistemas industriales completos.<br><br>

                • Garantizar potabilidad del agua mediante la simulación.<br><br>

                • Presentar resultados simulados como resultados experimentales.<br><br>

                • Afirmar que una única configuración funciona para todos los casos.<br><br>

                • Extrapolar directamente el modelo a escala industrial sin validación.

            </div>

        </div>
        """)

    render_html("""
    <div class="warning-box">

        <strong>Simulación ≠ experimento:</strong><br>

        Los resultados obtenidos mediante el modelo matemático son
        estimaciones computacionales. Para validar las predicciones,
        es necesario realizar mediciones experimentales bajo condiciones
        controladas y comparar los resultados.

    </div>
    """)

    render_html("""
    <div class="section-title">
        📋 Limitaciones del proyecto
    </div>
    """)

    limitations = pd.DataFrame({
        "Aspecto": [
            "Modelo matemático",
            "Escala",
            "Datos experimentales",
            "Calidad del agua",
            "Calidad del aire",
            "Escalamiento"
        ],
        "Consideración": [
            "Representa una aproximación del fenómeno",
            "Se plantea a escala piloto",
            "Requieren validación experimental",
            "Debe evaluarse mediante parámetros específicos",
            "Depende de las características de las partículas",
            "No puede asumirse directamente"
        ]
    })

    st.dataframe(
        limitations,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# NAVEGACIÓN
# ============================================================

pagina = st.sidebar.radio(
    "Módulos",
    [
        "Inicio",
        "Planta de aire",
        "Planta de agua",
        "Fundamento científico",
        "Innovación",
        "Ética y responsabilidad"
    ]
)


# ============================================================
# INFORMACIÓN LATERAL
# ============================================================

render_html(f"""
<div style="
    margin-top:25px;
    padding:16px;
    border-radius:15px;
    background:{CARD2};
    border:1px solid {BORDER};
">

    <div style="
        color:{ACCENT};
        font-weight:850;
        font-size:14px;
        margin-bottom:7px;
    ">
        ⚡ Plataforma de investigación
    </div>

    <div style="
        color:{MUTED};
        font-size:12px;
        line-height:1.55;
    ">
        Física II · Ingeniería Química<br>
        UIS · Sede Barbosa<br>
        2026
    </div>

</div>
""")


# ============================================================
# EJECUCIÓN DE PÁGINAS
# ============================================================

if pagina == "Inicio":

    page_inicio()

elif pagina == "Planta de aire":

    page_aire()

elif pagina == "Planta de agua":

    page_agua()

elif pagina == "Fundamento científico":

    page_fundamento()

elif pagina == "Innovación":

    page_innovacion()

elif pagina == "Ética y responsabilidad":

    page_etica()
    