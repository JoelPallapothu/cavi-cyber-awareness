"""
CAVI - Cyber Aware Village Initiative
Dedicated Left Sidebar Navigation, Bilingual Language Switcher (Telugu | English),
Accessibility Controls, and Top Emergency Alert Bar.
Desktop-First, Full-Width Design with Zero Text Clipping.
"""

import streamlit as st
import streamlit.components.v1 as components
from data.translations import get_text
from utils.helpers import get_current_lang, set_current_lang, get_current_page, navigate_to, calculate_safety_score
from utils.styling import render_html

def render_sidebar_nav():
    """
    Renders the dedicated, full-featured Left Sidebar Navigation.
    Includes CAVI Branding, Complete Section Names, Active Highlights (Blue + White),
    Emergency 1930 Quick Dial, Text Size Accessibility, and Bottom Language Switcher.
    """
    lang = get_current_lang()
    current_page = get_current_page()
    current_font = st.session_state.get("font_size_mode", "normal")
    score = calculate_safety_score()

    with st.sidebar:
        # 1. Sidebar Brand Header
        render_html(f"""
        <div style="background: linear-gradient(135deg, #063970 0%, #0b63ce 100%); 
                    color: white; border-radius: 18px; padding: 18px 16px; margin-bottom: 16px;
                    box-shadow: 0 6px 20px rgba(6,57,112,0.2); border: 1.5px solid rgba(255,255,255,0.2);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                <span style="font-size: 2.0rem;">🛡️</span>
                <span style="font-size: 1.45rem; font-weight: 950; letter-spacing: 0.5px; color: #ffffff;">CAVI</span>
            </div>
            <div style="font-size: 1.05rem; font-weight: 850; color: #ffffff; line-height: 1.3;">
                {get_text('app_full_name', lang)}
            </div>
            <div style="font-size: 0.82rem; font-weight: 700; color: #bae6fd; margin-top: 5px;">
                {get_text('tagline', lang)}
            </div>
            <div style="margin-top: 8px;">
                <span style="background: rgba(255,255,255,0.18); color: #ffffff; font-size: 0.76rem; font-weight: 800; padding: 3px 8px; border-radius: 9999px; border: 1px solid rgba(255,255,255,0.3);">
                    📍 {get_text('ap_focus', lang)}
                </span>
            </div>
        </div>
        """)

        # 2. Navigation Menu Label
        nav_menu_label = "📌 ప్రధాన మెనూ (Navigation)" if lang == "te" else "📌 Main Navigation"
        render_html(f"<div style='font-size: 0.82rem; font-weight: 850; color: #64748b; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px; padding-left: 4px;'>{nav_menu_label}</div>")

        # 10 Full Navigation Items - Complete names, zero truncation
        nav_items = [
            {"id": "home", "icon": "🏠", "label": get_text('nav_home', lang)},
            {"id": "frauds", "icon": "⚠️", "label": get_text('nav_frauds', lang)},
            {"id": "videos", "icon": "🎥", "label": get_text('nav_videos', lang)},
            {"id": "rules", "icon": "🛡️", "label": get_text('nav_rules', lang)},
            {"id": "quiz", "icon": "🧠", "label": get_text('nav_quiz', lang)},
            {"id": "simulations", "icon": "🎭", "label": get_text('nav_simulations', lang)},
            {"id": "report", "icon": "🚨", "label": get_text('nav_report', lang)},
            {"id": "field_activities", "icon": "📸", "label": get_text('nav_field_activities', lang)},
            {"id": "chatbot", "icon": "🤖", "label": get_text('nav_chatbot', lang)},
            {"id": "about", "icon": "ℹ️", "label": get_text('nav_about', lang)}
        ]

        for item in nav_items:
            is_active = (current_page == item["id"])
            btn_type = "primary" if is_active else "secondary"
            btn_title = f"{item['icon']}  {item['label']}"
            if st.button(btn_title, key=f"sidebar_nav_{item['id']}", type=btn_type, use_container_width=True):
                navigate_to(item["id"])

        # 3. Sidebar Safety Progress Card
        prog_label = "రక్షక్ స్కోరు" if lang == "te" else "Safety Score"
        render_html(f"""
        <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 12px 14px; margin: 16px 0 12px 0; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 0.88rem; font-weight: 800; color: #063970;">📊 {prog_label}</span>
                <span style="font-size: 1.1rem; font-weight: 950; color: #0b63ce;">{score}%</span>
            </div>
        </div>
        """)
        st.sidebar.progress(score / 100)

        # 4. Emergency Quick Call in Sidebar
        em_side_title = "24x7 సైబర్ హెల్ప్‌లైన్" if lang == "te" else "24x7 Cyber Helpline"
        em_side_btn = "1930 కి కాల్" if lang == "te" else "Call 1930"
        em_side_sub = "మోసపోయిన వెంటనే డయల్ చేయండి" if lang == "te" else "Dial immediately if scammed"
        render_html(f"""
        <div style="background: linear-gradient(135deg, #991b1b 0%, #dc2626 100%); border-radius: 14px; padding: 14px 12px; margin: 16px 0; color: white; text-align: center; border: 1.5px solid #fca5a5; box-shadow: 0 4px 12px rgba(220,38,38,0.25);">
            <div style="font-size: 0.84rem; font-weight: 800; color: #fee2e2; margin-bottom: 4px;">
                🚨 {em_side_title}
            </div>
            <a href="tel:1930" style="background: #ffffff; color: #dc2626; padding: 8px 18px; border-radius: 9999px; font-weight: 950; font-size: 1.15rem; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                <span>📞</span> <span>{em_side_btn}</span>
            </a>
            <div style="font-size: 0.74rem; color: #fecaca; margin-top: 6px;">
                {em_side_sub}
            </div>
        </div>
        """)

        # 5. Text Size Accessibility Controls
        render_html(f"<div style='font-size: 0.82rem; font-weight: 800; color: #64748b; margin: 12px 0 4px 4px;'>{get_text('font_size_label', lang)}:</div>")
        s1, s2, s3 = st.columns(3)
        with s1:
            btn_type_sm = "primary" if current_font == "normal" else "secondary"
            if st.button("A−", key="side_font_normal", type=btn_type_sm, help=get_text('font_normal', lang), use_container_width=True):
                st.session_state.font_size_mode = "normal"
                st.rerun()
        with s2:
            btn_type_md = "primary" if current_font == "large" else "secondary"
            if st.button("A", key="side_font_large", type=btn_type_md, help=get_text('font_large', lang), use_container_width=True):
                st.session_state.font_size_mode = "large"
                st.rerun()
        with s3:
            btn_type_lg = "primary" if current_font == "xlarge" else "secondary"
            if st.button("A+", key="side_font_xlarge", type=btn_type_lg, help=get_text('font_xlarge', lang), use_container_width=True):
                st.session_state.font_size_mode = "xlarge"
                st.rerun()

        # 6. Bilingual Language Switcher at Bottom of Sidebar (Strictly Telugu & English)
        render_html("<div style='font-size: 0.82rem; font-weight: 850; color: #64748b; margin: 14px 0 6px 4px;'>🌐 భాష / Language:</div>")
        l1, l2 = st.columns(2)
        with l1:
            is_te = (lang == "te")
            if st.button("🇮🇳 తెలుగు" + (" ✓" if is_te else ""), key="side_lang_te", type="primary" if is_te else "secondary", use_container_width=True):
                set_current_lang("te")
                st.rerun()
        with l2:
            is_en = (lang == "en")
            if st.button("🇬🇧 English" + (" ✓" if is_en else ""), key="side_lang_en", type="primary" if is_en else "secondary", use_container_width=True):
                set_current_lang("en")
                st.rerun()

        render_html("<div style='margin-bottom: 20px;'></div>")

def render_header_nav():
    """
    Renders:
    1. Dedicated Left Sidebar with full navigation menu and bottom language switcher.
    2. Clean Main Page Utility Header and Top Emergency Strip.
    3. Automatic Scroll-to-Top Anchor to ensure sections always start from the top.
    """
    lang = get_current_lang()
    current_page = get_current_page()

    # Render Left Sidebar Navigation
    render_sidebar_nav()

    # Page friendly titles for breadcrumb
    page_labels = {
        "home": get_text('nav_home', lang),
        "frauds": get_text('nav_frauds', lang),
        "videos": get_text('nav_videos', lang),
        "rules": get_text('nav_rules', lang),
        "quiz": get_text('nav_quiz', lang),
        "simulations": get_text('nav_simulations', lang),
        "report": get_text('nav_report', lang),
        "field_activities": get_text('nav_field_activities', lang),
        "chatbot": get_text('nav_chatbot', lang),
        "about": get_text('nav_about', lang)
    }
    active_label = page_labels.get(current_page, "")

    # Top Utility Bar in Main Area
    help_txt = "హెల్ప్‌లైన్" if lang == "te" else "Helpline"
    render_html(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; padding: 8px 0 12px 0;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="background: linear-gradient(135deg, #063970 0%, #0b63ce 100%); 
                        color: white; border-radius: 12px; padding: 6px 12px; font-weight: 900; 
                        font-size: 1.15rem; display: flex; align-items: center; gap: 6px;">
                <span>🛡️</span> <span>CAVI</span>
            </div>
            <div>
                <span style="font-size: 0.95rem; font-weight: 800; color: #475569;">
                    {get_text('app_full_name', lang)}
                </span>
                <span style="margin: 0 6px; color: #94a3b8;">/</span>
                <span style="font-size: 0.95rem; font-weight: 900; color: #0b63ce;">
                    {active_label}
                </span>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 12px;">
            <a href="tel:1930" style="background: #fee2e2; color: #dc2626; border: 1.5px solid #fca5a5; padding: 6px 16px; border-radius: 9999px; font-weight: 900; text-decoration: none; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
                <span>📞</span> <span>1930 {help_txt}</span>
            </a>
            <span style="background: #f0f9ff; color: #0284c7; border: 1px solid #bae6fd; padding: 5px 12px; border-radius: 9999px; font-weight: 800; font-size: 0.85rem;">
                🌐 {('తెలుగు' if lang == 'te' else 'English')}
            </span>
        </div>
    </div>
    """)

    # Emergency Alert Strip (Top notification - exactly one icon per element)
    render_html(f"""
    <div class="emergency-strip">
        <div class="emergency-strip-title">
            <span style="font-size: 1.5rem; line-height: 1;">🚨</span>
            <span style="color: #ffffff;">{get_text('emergency_alert_title', lang)}</span>
        </div>
        <div class="emergency-strip-actions">
            <a href="tel:1930" class="cavi-call-1930-btn">
                <span>📞</span> <span>1930</span>
            </a>
            <a href="https://cybercrime.gov.in" target="_blank" class="cavi-portal-btn">
                <span>🌐</span> <span>cybercrime.gov.in ↗</span>
            </a>
        </div>
    </div>
    <div id="cavi-page-top" style="position: relative; top: 0; left: 0; height: 1px; width: 1px; opacity: 0; pointer-events: none;"></div>
    <div style="margin-bottom: 18px;"></div>
    """)

    # Seamless instant scroll-to-top on navigation (resets parent container scroll position)
    components.html("""
    <script>
    (function() {
        function resetScroll() {
            try {
                if (window.parent && window.parent !== window) {
                    window.parent.scrollTo({ top: 0, left: 0, behavior: 'instant' });
                    var pDoc = window.parent.document;
                    if (pDoc) {
                        if (pDoc.documentElement) pDoc.documentElement.scrollTop = 0;
                        if (pDoc.body) pDoc.body.scrollTop = 0;
                        var targets = pDoc.querySelectorAll('.main, section.main, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"], .block-container');
                        for (var i = 0; i < targets.length; i++) {
                            if (targets[i]) targets[i].scrollTop = 0;
                        }
                        var anchor = pDoc.getElementById('cavi-page-top');
                        if (anchor && anchor.scrollIntoView) {
                            anchor.scrollIntoView({ behavior: 'instant', block: 'start' });
                        }
                    }
                }
            } catch(e) {}
        }
        resetScroll();
        requestAnimationFrame(resetScroll);
        setTimeout(resetScroll, 30);
        setTimeout(resetScroll, 100);
        setTimeout(resetScroll, 250);
    })();
    </script>
    """, height=0, width=0)
