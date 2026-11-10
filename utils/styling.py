"""
CAVI - Cyber Aware Village Initiative
Senior UI/UX Design System, Animations, Mobile Responsiveness, Accessibility Styling
and Safe HTML Rendering Engine
"""

import streamlit as st

def render_html(html_content: str):
    """
    Renders HTML safely using Streamlit's native st.html() engine, completely bypassing
    CommonMark markdown parsing to eliminate any possibility of raw code block leakage (<pre><code>).
    """
    if not html_content:
        return
    lines = html_content.strip().splitlines()
    cleaned = " ".join(line.strip() for line in lines if line.strip())
    if hasattr(st, "html"):
        st.html(cleaned)
    else:
        st.markdown(cleaned, unsafe_allow_html=True)

def get_custom_css(font_size_mode: str = "normal") -> str:
    """
    Returns production-grade, desktop-first public portal CSS with modern glassmorphism,
    pulsing alerts, responsive touch controls, and dynamic font accessibility.
    """
    base_font_size = "17px"
    heading_scale = "1.0"
    card_padding = "26px"
    
    if font_size_mode == "large":
        base_font_size = "20px"
        heading_scale = "1.15"
        card_padding = "30px"
    elif font_size_mode == "xlarge":
        base_font_size = "23px"
        heading_scale = "1.3"
        card_padding = "34px"

    return f"""
    <style>
        /* Google Fonts: Noto Sans Telugu + Plus Jakarta Sans + Material Symbols Rounded */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Noto+Sans+Telugu:wght@400;500;600;700;800;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

        :root {{
            --font-main: 'Plus Jakarta Sans', 'Noto Sans Telugu', 'Segoe UI', system-ui, sans-serif;
            --font-telugu: 'Noto Sans Telugu', 'Segoe UI', sans-serif;
            --primary-navy: #063970;
            --primary-blue: #0b63ce;
            --cyber-blue: #1688d8;
            --cyber-light: #e0f2fe;
            --safe-green: #168447;
            --safe-light: #f0fdf4;
            --safe-border: #86efac;
            --danger-red: #d62828;
            --danger-dark: #991b1b;
            --danger-light: #fef2f2;
            --danger-border: #fca5a5;
            --warning-amber: #f4b400;
            --warning-light: #fffbeb;
            --bg-slate: #f8fafc;
            --card-border: #e2e8f0;
            --text-dark: #091b36;
            --text-muted: #475569;
        }}

        /* Base Typography & Background */
        html, body, .stApp, .stMarkdown, .stText, p, li {{
            font-family: var(--font-main) !important;
            font-size: {base_font_size};
            color: var(--text-dark);
            -webkit-font-smoothing: antialiased;
        }}

        div:not([data-testid*="Icon"]):not([class*="material-symbols"]):not([class*="material-icons"]),
        p, li, a {{
            font-family: var(--font-main);
        }}

        /* PRESERVE STREAMLIT MATERIAL SYMBOLS & ICONS LIGATURES (FIXES keyboard_double...) */
        [data-testid*="stIconMaterial"],
        .material-symbols-rounded,
        .material-symbols-outlined,
        [class*="material-symbols"],
        [class*="material-icons"],
        [data-testid="stSidebarCollapseButton"] *,
        [data-testid="collapsedControl"] *,
        header button * {{
            font-family: 'Material Symbols Rounded', 'Material Icons', sans-serif !important;
            font-weight: normal !important;
            font-style: normal !important;
            font-size: 24px !important;
            line-height: 1 !important;
            letter-spacing: normal !important;
            text-transform: none !important;
            display: inline-block !important;
            white-space: nowrap !important;
            word-wrap: normal !important;
            direction: ltr !important;
            -webkit-font-feature-settings: 'liga' !important;
            font-feature-settings: 'liga' !important;
            -webkit-font-smoothing: antialiased !important;
        }}

        /* Generous line-height for Telugu script to prevent vowel mark clipping */
        p, li, div {{
            line-height: 1.68 !important;
        }}

        /* Clean Streamlit Default Chrome */
        header[data-testid="stHeader"] {{
            background: rgba(248, 250, 252, 0.98) !important;
            backdrop-filter: blur(12px) !important;
            border-bottom: 1px solid #e2e8f0 !important;
        }}

        #MainMenu, footer {{
            visibility: hidden !important;
        }}

        /* Desktop Full-Screen Viewport Container */
        .block-container {{
            padding-top: 0.8rem !important;
            padding-bottom: 3.5rem !important;
            max-width: 1540px !important;
            width: 96% !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }}

        /* Keyframe Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes shieldFloat {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-6px); }}
        }}

        @keyframes pulse-emergency {{
            0% {{
                box-shadow: 0 0 0 0 rgba(214, 40, 40, 0.5);
                transform: scale(1);
            }}
            50% {{
                box-shadow: 0 0 0 10px rgba(214, 40, 40, 0);
                transform: scale(1.004);
            }}
            100% {{
                box-shadow: 0 0 0 0 rgba(214, 40, 40, 0);
                transform: scale(1);
            }}
        }}

        /* Eradicate Any Errant Pre/Code Rendering of HTML */
        pre:has(div), pre:has(span), pre:has(p), pre:has(h1), pre:has(h2), pre:has(h3),
        code:has(div), code:has(span) {{
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
            box-shadow: none !important;
        }}

        /* Modern Glass Card */
        .cavi-card {{
            background: #ffffff;
            border-radius: 20px;
            padding: {card_padding};
            border: 1px solid var(--card-border);
            box-shadow: 0 4px 18px rgba(15, 43, 92, 0.05);
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
            position: relative;
            overflow: hidden;
            margin-bottom: 22px;
        }}

        .cavi-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 14px 30px rgba(15, 43, 92, 0.1);
            border-color: #cbd5e1;
        }}

        /* Interactive Fraud Card */
        .fraud-grid-card {{
            background: #ffffff;
            border-radius: 20px;
            padding: 22px;
            border: 1px solid var(--card-border);
            box-shadow: 0 4px 16px rgba(15, 43, 92, 0.05);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 270px;
        }}

        .fraud-grid-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 16px 36px rgba(15, 43, 92, 0.12);
        }}

        /* Modern Light Hero Banner */
        .hero-banner-light {{
            background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 45%, #ffffff 100%);
            border-radius: 26px;
            padding: 38px 36px;
            color: #091b36;
            box-shadow: 0 10px 30px rgba(11, 99, 206, 0.08);
            margin-bottom: 26px;
            position: relative;
            border: 2px solid #bae6fd;
            overflow: hidden;
        }}

        .hero-banner-light h1 {{
            font-size: calc(2.3rem * {heading_scale}) !important;
            font-weight: 950 !important;
            color: #062b55 !important;
            margin-bottom: 12px !important;
            line-height: 1.25 !important;
            letter-spacing: -0.5px;
        }}

        .hero-banner-light p {{
            font-size: calc(1.15rem * {heading_scale}) !important;
            color: #1e3a5f !important;
            font-weight: 600 !important;
            line-height: 1.6 !important;
            margin-bottom: 0 !important;
        }}

        /* Emergency Action Strip */
        .emergency-strip {{
            background: linear-gradient(90deg, #991b1b 0%, #dc2626 55%, #b91c1c 100%);
            border-radius: 18px;
            padding: 16px 24px;
            color: #ffffff !important;
            box-shadow: 0 6px 22px rgba(220, 38, 38, 0.28);
            margin-bottom: 22px;
            border: 2px solid #fecaca;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 14px;
            animation: pulse-emergency 3.5s infinite;
        }}

        .emergency-strip-title {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 850;
            font-size: 1.05rem;
            color: #ffffff !important;
        }}

        .emergency-strip-actions {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        /* 1930 Call Button: High contrast, minimum width to prevent collapse */
        .cavi-call-1930-btn {{
            background: #ffffff !important;
            color: #b91c1c !important;
            border: 2px solid #ffffff !important;
            padding: 9px 24px !important;
            border-radius: 9999px !important;
            font-weight: 950 !important;
            font-size: 1.15rem !important;
            line-height: 1 !important;
            text-decoration: none !important;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.22) !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 8px !important;
            min-width: 140px !important;
            text-align: center !important;
            transition: transform 0.18s ease, box-shadow 0.18s ease !important;
        }}

        .cavi-call-1930-btn:hover {{
            transform: scale(1.04) !important;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.3) !important;
            color: #991b1b !important;
        }}

        .cavi-call-1930-btn span {{
            color: #b91c1c !important;
            font-weight: 950 !important;
        }}

        /* Cybercrime Portal Button */
        .cavi-portal-btn {{
            background: #063970 !important;
            color: #ffffff !important;
            padding: 9px 20px !important;
            border-radius: 9999px !important;
            font-weight: 850 !important;
            font-size: 1.0rem !important;
            line-height: 1 !important;
            text-decoration: none !important;
            border: 1.5px solid rgba(255, 255, 255, 0.5) !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 8px !important;
            min-width: 190px !important;
            text-align: center !important;
            box-shadow: 0 4px 12px rgba(6, 57, 112, 0.25) !important;
            transition: transform 0.18s ease !important;
        }}

        .cavi-portal-btn:hover {{
            transform: scale(1.03) !important;
            background: #0a4f9d !important;
            color: #ffffff !important;
        }}

        .cavi-portal-btn span {{
            color: #ffffff !important;
            font-weight: 850 !important;
        }}

        /* Left Sidebar Navigation Styling */
        [data-testid="stSidebar"] {{
            background-color: #f8fafc !important;
            border-right: 1.5px solid #e2e8f0 !important;
        }}

        [data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {{
            padding-top: 1.2rem !important;
            padding-left: 1.0rem !important;
            padding-right: 1.0rem !important;
        }}

        /* ==========================================================================
           UNIVERSAL BUTTON CONTRAST ENGINE (BLUE BACKGROUNDS -> PURE WHITE TEXT)
           Covers all button variants: Primary, Yes Understood, Quiz, Nav, Sims, Lightbox
           Covers all interaction states: Default, Hover, Active, Focus, Focus-Visible, Selected
           Enforces white text on button AND all descendants (p, span, div, strong, svg)
           ========================================================================== */

        /* 1. General Secondary Button Defaults */
        .stButton > button,
        [data-testid="stBaseButton-secondary"] {{
            border-radius: 14px !important;
            padding: 12px 18px !important;
            font-weight: 750 !important;
            font-size: calc(0.98rem * {heading_scale}) !important;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
            border: 1px solid #cbd5e1 !important;
            background: #ffffff !important;
            color: #091b36 !important;
            box-shadow: 0 3px 10px rgba(15, 43, 92, 0.06) !important;
            min-height: 46px !important;
        }}

        .stButton > button *,
        [data-testid="stBaseButton-secondary"] * {{
            color: #091b36;
        }}

        /* Secondary Button Hover (Crisp ice-blue background with navy text) */
        .stButton > button:not([kind="primary"]):not([data-testid="stBaseButton-primary"]):hover,
        [data-testid="stBaseButton-secondary"]:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 18px rgba(15, 43, 92, 0.14) !important;
            border-color: #0b63ce !important;
            background: #f0f7ff !important;
            color: #0b63ce !important;
        }}

        .stButton > button:not([kind="primary"]):not([data-testid="stBaseButton-primary"]):hover *,
        [data-testid="stBaseButton-secondary"]:hover * {{
            color: #0b63ce !important;
            -webkit-text-fill-color: #0b63ce !important;
        }}

        /* 2. Primary Buttons & All Buttons with Blue Backgrounds (Default State) */
        .stButton > button[kind="primary"],
        .stButton > button[data-testid="stBaseButton-primary"],
        .stButton > button[data-testid="baseButton-primary"],
        button[kind="primary"],
        button[data-testid="stBaseButton-primary"],
        button[data-testid="baseButton-primary"],
        button[kind="primaryFormSubmit"],
        [data-testid="stSidebar"] .stButton > button[kind="primary"],
        [data-testid="stSidebar"] button[kind="primary"],
        [data-testid="stSidebar"] [data-testid="stBaseButton-primary"],
        [data-testid="stModal"] button[kind="primary"],
        [data-testid="stDialog"] button[kind="primary"],
        [data-testid="stPopover"] button[kind="primary"],
        button[aria-selected="true"],
        button[aria-pressed="true"],
        .stButton > button[aria-selected="true"],
        .stButton > button[aria-pressed="true"] {{
            background: linear-gradient(135deg, #0b63ce 0%, #063970 100%) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            border: 1px solid #063970 !important;
            box-shadow: 0 4px 14px rgba(11, 99, 206, 0.35) !important;
            font-weight: 850 !important;
        }}

        /* Explicit White Text Enforcement on ALL Child Elements */
        .stButton > button[kind="primary"] *,
        .stButton > button[data-testid="stBaseButton-primary"] *,
        .stButton > button[data-testid="baseButton-primary"] *,
        button[kind="primary"] *,
        button[data-testid="stBaseButton-primary"] *,
        button[data-testid="baseButton-primary"] *,
        button[kind="primaryFormSubmit"] *,
        [data-testid="stSidebar"] .stButton > button[kind="primary"] *,
        [data-testid="stSidebar"] button[kind="primary"] *,
        [data-testid="stSidebar"] [data-testid="stBaseButton-primary"] *,
        [data-testid="stModal"] button[kind="primary"] *,
        [data-testid="stDialog"] button[kind="primary"] *,
        [data-testid="stPopover"] button[kind="primary"] *,
        button[aria-selected="true"] *,
        button[aria-pressed="true"] *,
        .stButton > button[aria-selected="true"] *,
        .stButton > button[aria-pressed="true"] *,
        .stButton > button[kind="primary"] p,
        .stButton > button[data-testid="stBaseButton-primary"] p,
        button[kind="primary"] p,
        button[data-testid="stBaseButton-primary"] p,
        .stButton > button[kind="primary"] [data-testid="stMarkdownContainer"] p,
        .stButton > button[data-testid="stBaseButton-primary"] [data-testid="stMarkdownContainer"] p,
        button[kind="primary"] [data-testid="stMarkdownContainer"] p,
        button[data-testid="stBaseButton-primary"] [data-testid="stMarkdownContainer"] p,
        .stButton > button[kind="primary"] span,
        .stButton > button[data-testid="stBaseButton-primary"] span,
        button[kind="primary"] span,
        button[data-testid="stBaseButton-primary"] span,
        .stButton > button[kind="primary"] div,
        .stButton > button[data-testid="stBaseButton-primary"] div,
        button[kind="primary"] div,
        button[data-testid="stBaseButton-primary"] div {{
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            fill: #ffffff !important;
        }}

        /* 3. Primary Button Hover State */
        .stButton > button[kind="primary"]:hover,
        .stButton > button[data-testid="stBaseButton-primary"]:hover,
        .stButton > button[data-testid="baseButton-primary"]:hover,
        button[kind="primary"]:hover,
        button[data-testid="stBaseButton-primary"]:hover,
        button[data-testid="baseButton-primary"]:hover,
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover,
        [data-testid="stSidebar"] button[kind="primary"]:hover,
        [data-testid="stSidebar"] [data-testid="stBaseButton-primary"]:hover {{
            background: linear-gradient(135deg, #0284c7 0%, #0b63ce 100%) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            border-color: #0284c7 !important;
            box-shadow: 0 6px 18px rgba(11, 99, 206, 0.45) !important;
            transform: translateY(-2px) !important;
        }}

        .stButton > button[kind="primary"]:hover *,
        .stButton > button[data-testid="stBaseButton-primary"]:hover *,
        .stButton > button[data-testid="baseButton-primary"]:hover *,
        button[kind="primary"]:hover *,
        button[data-testid="stBaseButton-primary"]:hover *,
        button[data-testid="baseButton-primary"]:hover *,
        .stButton > button[kind="primary"]:hover p,
        .stButton > button[data-testid="stBaseButton-primary"]:hover p,
        button[kind="primary"]:hover p,
        button[data-testid="stBaseButton-primary"]:hover p,
        .stButton > button[kind="primary"]:hover [data-testid="stMarkdownContainer"] p,
        .stButton > button[data-testid="stBaseButton-primary"]:hover [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover * {{
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            fill: #ffffff !important;
        }}

        /* 4. Active / Clicked State (When ANY button is clicked and becomes blue) */
        .stButton > button[kind="primary"]:active,
        .stButton > button[data-testid="stBaseButton-primary"]:active,
        .stButton > button[data-testid="baseButton-primary"]:active,
        button[kind="primary"]:active,
        button[data-testid="stBaseButton-primary"]:active,
        button[data-testid="baseButton-primary"]:active,
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:active,
        [data-testid="stSidebar"] button[kind="primary"]:active,
        [data-testid="stSidebar"] [data-testid="stBaseButton-primary"]:active,
        .stButton > button:active,
        [data-testid*="stBaseButton"]:active {{
            background: linear-gradient(135deg, #063970 0%, #091b36 100%) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            border-color: #063970 !important;
            transform: translateY(1px) !important;
        }}

        .stButton > button[kind="primary"]:active *,
        .stButton > button[data-testid="stBaseButton-primary"]:active *,
        .stButton > button[data-testid="baseButton-primary"]:active *,
        button[kind="primary"]:active *,
        button[data-testid="stBaseButton-primary"]:active *,
        button[data-testid="baseButton-primary"]:active *,
        .stButton > button:active *,
        [data-testid*="stBaseButton"]:active *,
        .stButton > button:active p,
        [data-testid*="stBaseButton"]:active p,
        .stButton > button:active [data-testid="stMarkdownContainer"] p,
        [data-testid*="stBaseButton"]:active [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:active * {{
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            fill: #ffffff !important;
        }}

        /* 5. Focus & Focus-Visible States (Keyboard Navigation & Touch Taps) */
        .stButton > button[kind="primary"]:focus,
        .stButton > button[kind="primary"]:focus-visible,
        .stButton > button[data-testid="stBaseButton-primary"]:focus,
        .stButton > button[data-testid="stBaseButton-primary"]:focus-visible,
        button[kind="primary"]:focus,
        button[kind="primary"]:focus-visible,
        button[data-testid="stBaseButton-primary"]:focus,
        button[data-testid="stBaseButton-primary"]:focus-visible {{
            background: linear-gradient(135deg, #0b63ce 0%, #063970 100%) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            outline: 2px solid #38bdf8 !important;
            outline-offset: 2px !important;
        }}

        .stButton > button[kind="primary"]:focus *,
        .stButton > button[kind="primary"]:focus-visible *,
        .stButton > button[data-testid="stBaseButton-primary"]:focus *,
        .stButton > button[data-testid="stBaseButton-primary"]:focus-visible *,
        button[kind="primary"]:focus *,
        button[kind="primary"]:focus-visible *,
        button[data-testid="stBaseButton-primary"]:focus *,
        button[data-testid="stBaseButton-primary"]:focus-visible *,
        .stButton > button[kind="primary"]:focus p,
        .stButton > button[data-testid="stBaseButton-primary"]:focus p,
        button[kind="primary"]:focus p,
        button[data-testid="stBaseButton-primary"]:focus p {{
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            fill: #ffffff !important;
        }}

        /* 6. Disabled Primary State (High Contrast Readability) */
        .stButton > button[kind="primary"]:disabled,
        .stButton > button[data-testid="stBaseButton-primary"]:disabled,
        button[kind="primary"]:disabled,
        button[data-testid="stBaseButton-primary"]:disabled {{
            background: #94a3b8 !important;
            color: #f8fafc !important;
            -webkit-text-fill-color: #f8fafc !important;
            opacity: 0.8 !important;
            cursor: not-allowed !important;
        }}

        .stButton > button[kind="primary"]:disabled *,
        .stButton > button[data-testid="stBaseButton-primary"]:disabled *,
        button[kind="primary"]:disabled *,
        button[data-testid="stBaseButton-primary"]:disabled * {{
            color: #f8fafc !important;
            -webkit-text-fill-color: #f8fafc !important;
        }}

        /* 7. Sidebar Navigation Specific Styling */
        [data-testid="stSidebar"] .stButton > button {{
            width: 100% !important;
            text-align: left !important;
            justify-content: flex-start !important;
            padding: 11px 16px !important;
            margin-bottom: 6px !important;
            border-radius: 12px !important;
            font-weight: 800 !important;
            font-size: calc(0.96rem * {heading_scale}) !important;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
            border: 1px solid #e2e8f0 !important;
            background: #ffffff !important;
            color: #091b36 !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04) !important;
            min-height: 44px !important;
        }}

        [data-testid="stSidebar"] .stButton > button:hover {{
            background: #e0f2fe !important;
            color: #0b63ce !important;
            border-color: #38bdf8 !important;
            transform: translateX(3px) !important;
        }}

        [data-testid="stSidebar"] .stButton > button:hover * {{
            color: #0b63ce !important;
            -webkit-text-fill-color: #0b63ce !important;
        }}

        [data-testid="stSidebar"] .stButton > button[kind="primary"],
        [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] {{
            background: linear-gradient(135deg, #0b63ce 0%, #063970 100%) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            border-left: 5px solid #38bdf8 !important;
            border-top: none !important;
            border-right: none !important;
            border-bottom: none !important;
            box-shadow: 0 4px 14px rgba(11, 99, 206, 0.3) !important;
            font-weight: 900 !important;
        }}

        [data-testid="stSidebar"] .stButton > button[kind="primary"] *,
        [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] * {{
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }}

        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover,
        [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"]:hover {{
            background: linear-gradient(135deg, #0284c7 0%, #0b63ce 100%) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }}

        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover *,
        [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"]:hover * {{
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }}

        /* Strict Contrast Enforcement for Footer */
        .cavi-footer * {{
            color: #e2e8f0;
        }}
        .cavi-footer h1, .cavi-footer h2, .cavi-footer h3, .cavi-footer h4, .cavi-footer strong, .cavi-footer b {{
            color: #ffffff !important;
        }}

        /* Badges */
        .badge-pill {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 5px 13px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 800;
            letter-spacing: 0.3px;
        }}

        .badge-safe {{
            background: var(--safe-light);
            color: var(--safe-green);
            border: 1px solid var(--safe-border);
        }}

        .badge-danger {{
            background: var(--danger-light);
            color: var(--danger-red);
            border: 1px solid var(--danger-border);
        }}

        .badge-warning {{
            background: var(--warning-light);
            color: var(--warning-amber);
            border: 1px solid #fde68a;
        }}

        .badge-info {{
            background: var(--cyber-light);
            color: var(--cyber-blue);
            border: 1px solid #bae6fd;
        }}

        /* Flowchart Steps for Villagers */
        .workflow-step-box {{
            background: #ffffff;
            border-radius: 16px;
            padding: 16px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.03);
            text-align: center;
            position: relative;
            transition: all 0.2s ease;
        }}

        .workflow-step-box:hover {{
            border-color: #0284c7;
            transform: translateY(-2px);
        }}

        /* WhatsApp / Phone Chat Bubbles */
        .chat-bubble-scammer {{
            background: #fee2e2;
            color: #7f1d1d;
            border-radius: 20px 20px 20px 4px;
            padding: 16px 20px;
            margin-bottom: 14px;
            border: 1px solid #fecaca;
            font-size: calc(1.05rem * {heading_scale});
            line-height: 1.55;
            box-shadow: 0 2px 8px rgba(220, 38, 38, 0.06);
        }}

        .chat-bubble-villager {{
            background: #dcfce7;
            color: #14532d;
            border-radius: 20px 20px 4px 20px;
            padding: 16px 20px;
            margin-bottom: 14px;
            margin-left: 28px;
            border: 1px solid #bbf7d0;
            font-size: calc(1.05rem * {heading_scale});
            line-height: 1.55;
            box-shadow: 0 2px 8px rgba(22, 163, 74, 0.06);
        }}

        /* Do vs Don't Split Boards */
        .do-box {{
            background: var(--safe-light);
            border: 2px solid var(--safe-border);
            border-radius: 20px;
            padding: 24px;
            height: 100%;
            box-shadow: 0 4px 16px rgba(22, 163, 74, 0.06);
        }}

        .dont-box {{
            background: var(--danger-light);
            border: 2px solid var(--danger-border);
            border-radius: 20px;
            padding: 24px;
            height: 100%;
            box-shadow: 0 4px 16px rgba(220, 38, 38, 0.06);
        }}

        /* Footer */
        .cavi-footer {{
            background: #06152b;
            color: #cbd5e1;
            border-radius: 24px;
            padding: 36px 32px;
            margin-top: 45px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.08);
        }}

        /* Section Numbering & Headers */
        .section-header-box {{
            margin-bottom: 24px;
            padding-bottom: 12px;
            border-bottom: 2px solid #e2e8f0;
            display: flex;
            align-items: baseline;
            gap: 14px;
            flex-wrap: wrap;
        }}

        .section-number {{
            font-size: 1.15rem;
            font-weight: 900;
            color: var(--primary-blue);
            background: #e0f2fe;
            padding: 4px 12px;
            border-radius: 8px;
            letter-spacing: 1px;
        }}

        /* Field Activities Photo Gallery & Information Panel */
        .field-info-panel {{
            background: #ffffff;
            border-radius: 20px;
            padding: 24px;
            border: 1.5px solid #e2e8f0;
            box-shadow: 0 4px 16px rgba(15, 43, 92, 0.05);
            margin-bottom: 28px;
        }}

        .field-info-table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-top: 14px;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
        }}

        .field-info-table th, .field-info-table td {{
            padding: 12px 18px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
            font-size: 0.98rem;
        }}

        .field-info-table th {{
            background: #f8fafc;
            color: #063970;
            font-weight: 850;
            width: 32%;
        }}

        .field-info-table td {{
            background: #ffffff;
            color: #1e293b;
            font-weight: 600;
        }}

        .field-info-table tr:last-child th,
        .field-info-table tr:last-child td {{
            border-bottom: none;
        }}

        /* Photo Gallery Cards */
        .field-photo-card {{
            background: #ffffff;
            border-radius: 20px;
            border: 1.5px solid #e2e8f0;
            padding: 22px;
            margin-bottom: 26px;
            box-shadow: 0 4px 18px rgba(15, 43, 92, 0.06);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .field-photo-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 16px 32px rgba(15, 43, 92, 0.12);
            border-color: #38bdf8;
        }}

        .field-photo-title {{
            color: #063970;
            font-weight: 900;
            font-size: 1.25rem;
            margin-bottom: 12px;
            line-height: 1.35;
        }}

        .field-photo-desc {{
            color: #475569;
            font-size: 0.98rem;
            line-height: 1.6;
            margin-top: 12px;
            margin-bottom: 14px;
            font-weight: 500;
        }}

        /* Lightbox Container */
        .field-lightbox-box {{
            background: linear-gradient(135deg, #091b36 0%, #063970 100%);
            border-radius: 24px;
            padding: 28px;
            color: #ffffff;
            margin-bottom: 32px;
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
            border: 2px solid #38bdf8;
        }}

        /* Activity Cards */
        .field-activity-card {{
            background: #ffffff;
            border-radius: 16px;
            padding: 20px;
            border: 1.5px solid #e2e8f0;
            border-left: 5px solid #0b63ce;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.04);
            margin-bottom: 16px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .field-activity-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(11, 99, 206, 0.09);
        }}

        /* Responsive Mobile Layout Adjustments */
        @media (max-width: 768px) {{
            .hero-banner {{
                padding: 24px 18px !important;
            }}
            .cavi-card {{
                padding: 18px !important;
            }}
            .emergency-strip {{
                flex-direction: column !important;
                align-items: stretch !important;
                text-align: center !important;
            }}
            .chat-bubble-villager {{
                margin-left: 10px !important;
            }}
        }}
    </style>
    """
