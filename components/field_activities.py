"""
CAVI - Cyber Aware Village Initiative
Field Activities & Community Engagement Showcase Component.
Bilingual: Telugu (Default) and English.
Includes:
1. Field Visit Documentation Panel with GPS coordinates and audit trail.
2. Photo Gallery with 5 original field photographs, individual titles ABOVE and descriptions BELOW.
3. Interactive Click-to-Enlarge Lightbox with Previous/Next navigation.
4. Field Visit Activities Breakdown (What We Did During Our Field Visit).
5. Community Impact & Cyber-Safe Community Guidelines with 1930 Emergency Banner.
"""

import streamlit as st
import os
from utils.helpers import get_current_lang, navigate_to
from utils.styling import render_html
from data.field_activities_data import (
    FIELD_VISIT_INFO,
    FIELD_PHOTOS,
    FIELD_ACTIVITIES_LIST,
    COMMUNITY_IMPACT_RULES
)

def render_field_activities():
    lang = get_current_lang()
    is_te = (lang == "te")
    
    # Base directory for field activity images
    img_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "field-activities")
    
    # Initialize lightbox state
    if "field_lightbox_idx" not in st.session_state:
        st.session_state.field_lightbox_idx = None

    # ==============================================================================
    # 1. SECTION INTRO HEADER & BANNER
    # ==============================================================================
    main_heading = "మా క్షేత్రస్థాయి కార్యకలాపాలు మరియు సమాజ అవగాహన కార్యక్రమం" if is_te else "Our Field Activities & Community Engagement"
    main_subtitle = "సైబర్ భద్రతను ప్రోత్సహించడానికి మరియు ఆన్లైన్ మోసాలను నివారించడానికి సమాజంతో ప్రత్యక్ష అవగాహన కార్యక్రమాలు." if is_te else "Real-world community engagement to promote cyber safety and prevent online fraud."
    csp_badge = "🎓 కమ్యూనిటీ సర్వీస్ ప్రాజెక్ట్ (CSP) ప్రత్యక్ష నివేదిక" if is_te else "🎓 Official Community Service Project (CSP) Field Report"
    loc_badge = "📍 గుడివాడ, కృష్ణా జిల్లా, ఆంధ్రప్రదేశ్" if is_te else "📍 Gudivada, Krishna District, Andhra Pradesh"
    
    render_html(f"""
    <div class="cavi-card" style="border-top: 6px solid #063970; margin-bottom: 26px; padding: 26px 30px;">
        <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 12px;">
            <span style="background: #e0f2fe; color: #0369a1; padding: 5px 14px; border-radius: 9999px; font-weight: 850; font-size: 0.88rem; border: 1px solid #bae6fd;">
                {csp_badge}
            </span>
            <span style="background: #f0fdf4; color: #15803d; padding: 5px 14px; border-radius: 9999px; font-weight: 850; font-size: 0.88rem; border: 1px solid #bbf7d0;">
                {loc_badge}
            </span>
        </div>
        <h1 style="color: #063970; margin: 0 0 10px 0; font-size: 2.1rem; font-weight: 950; line-height: 1.3;">
            {main_heading}
        </h1>
        <p style="color: #475569; font-size: 1.15rem; margin: 0; font-weight: 600; line-height: 1.6;">
            {main_subtitle}
        </p>
    </div>
    """)

    # ==============================================================================
    # 2. FIELD VISIT INFORMATION PANEL (TABLE & GPS EVIDENCE)
    # ==============================================================================
    info_heading = FIELD_VISIT_INFO["heading"]["te"] if is_te else FIELD_VISIT_INFO["heading"]["en"]
    info_sub = FIELD_VISIT_INFO["sub"]["te"] if is_te else FIELD_VISIT_INFO["sub"]["en"]
    gps_note = FIELD_VISIT_INFO["gps_evidence"]["te"] if is_te else FIELD_VISIT_INFO["gps_evidence"]["en"]
    col_head_field = "వివరాలు (Field)" if is_te else "Field"
    col_head_val = "సమాచారం (Information)" if is_te else "Information"
    
    table_rows_html = ""
    for item in FIELD_VISIT_INFO["fields"]:
        label = item["label_te"] if is_te else item["label_en"]
        val = item["val_te"] if is_te else item["val_en"]
        table_rows_html += f"""
        <tr>
            <th>{label}</th>
            <td>{val}</td>
        </tr>
        """
        
    render_html(f"""
    <div class="field-info-panel">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
            <span style="font-size: 1.5rem;">📋</span>
            <h3 style="color: #063970; margin: 0; font-size: 1.45rem; font-weight: 900;">
                {info_heading}
            </h3>
        </div>
        <p style="color: #64748b; font-size: 1.0rem; margin-bottom: 16px; font-weight: 500;">
            {info_sub}
        </p>
        <table class="field-info-table">
            <thead>
                <tr>
                    <th style="background: #063970; color: #ffffff;">{col_head_field}</th>
                    <th style="background: #0b63ce; color: #ffffff;">{col_head_val}</th>
                </tr>
            </thead>
            <tbody>
                {table_rows_html}
            </tbody>
        </table>
        <div style="margin-top: 16px; background: #f8fafc; border-left: 4px solid #0b63ce; border-radius: 8px; padding: 12px 16px; font-size: 0.92rem; color: #334155; font-weight: 600;">
            🛰️ <b>{gps_note}</b>
        </div>
    </div>
    """)

    # ==============================================================================
    # 3. INTERACTIVE LIGHTBOX (IF AN IMAGE IS ENLARGED)
    # ==============================================================================
    current_idx = st.session_state.field_lightbox_idx
    if current_idx is not None and 0 <= current_idx < len(FIELD_PHOTOS):
        active_photo = FIELD_PHOTOS[current_idx]
        active_title = active_photo["title"]["te"] if is_te else active_photo["title"]["en"]
        active_desc = active_photo["description"]["te"] if is_te else active_photo["description"]["en"]
        active_badge = active_photo["badge"]["te"] if is_te else active_photo["badge"]["en"]
        active_img_path = os.path.join(img_dir, active_photo["filename"])
        
        close_txt = "✕ మూసివేయండి (Close)" if is_te else "✕ Close Lightbox"
        prev_txt = "◀ మునుపటి ఫోటో" if is_te else "◀ Previous Photo"
        next_txt = "తదుపరి ఫోటో ▶" if is_te else "Next Photo ▶"
        counter_txt = f"{len(FIELD_PHOTOS)} లో {current_idx + 1} వ ఫోటో" if is_te else f"Photo {current_idx + 1} of {len(FIELD_PHOTOS)}"
        
        st.markdown("<div id='cavi-lightbox-anchor'></div>", unsafe_allow_html=True)
        render_html(f"""
        <div class="field-lightbox-box">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 14px;">
                <span style="background: rgba(255,255,255,0.2); color: #ffffff; padding: 4px 14px; border-radius: 9999px; font-weight: 850; font-size: 0.88rem;">
                    {active_badge} • {counter_txt}
                </span>
                <span style="font-size: 0.92rem; color: #bae6fd; font-weight: 600;">
                    {active_photo['time']}
                </span>
            </div>
            <h2 style="color: #ffffff; margin: 0 0 14px 0; font-size: 1.7rem; font-weight: 950;">
                📸 {active_title}
            </h2>
        </div>
        """)
        
        # Display large image in Streamlit
        if os.path.exists(active_img_path):
            st.image(active_img_path, caption=active_title, use_container_width=True)
        else:
            st.warning("Photograph file loading...")
            
        render_html(f"""
        <div style="background: #ffffff; border-radius: 14px; padding: 18px 22px; margin: 12px 0 20px 0; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 14px rgba(0,0,0,0.06);">
            <p style="color: #1e293b; font-size: 1.12rem; line-height: 1.65; margin: 0; font-weight: 600;">
                {active_desc}
            </p>
        </div>
        """)
        
        # Lightbox Controls Row
        lb_c1, lb_c2, lb_c3 = st.columns([1, 1, 1])
        with lb_c1:
            if st.button(prev_txt, key="lightbox_btn_prev", use_container_width=True):
                st.session_state.field_lightbox_idx = (current_idx - 1) % len(FIELD_PHOTOS)
                st.rerun()
        with lb_c2:
            if st.button(close_txt, key="lightbox_btn_close", type="primary", use_container_width=True):
                st.session_state.field_lightbox_idx = None
                st.rerun()
        with lb_c3:
            if st.button(next_txt, key="lightbox_btn_next", use_container_width=True):
                st.session_state.field_lightbox_idx = (current_idx + 1) % len(FIELD_PHOTOS)
                st.rerun()
                
        render_html("<hr style='border: none; border-top: 2px dashed #94a3b8; margin: 28px 0;'>")

    # ==============================================================================
    # 4. ALL FIVE PHOTOGRAPHS WITH INDIVIDUAL TITLES (GALLERY GRID)
    # ==============================================================================
    gallery_head = "క్షేత్రస్థాయి ఛాయాచిత్రాల గ్యాలరీ (Photo Gallery)" if is_te else "Field Visit Photographs Gallery"
    gallery_sub = "ప్రతి ఫోటోకు ప్రత్యేకమైన శీర్షిక మరియు వివరణ క్రింద ఇవ్వబడ్డాయి (క్లిక్ చేసి పెద్దదిగా చూడవచ్చు):" if is_te else "Each photograph features its own individual title above and meaningful description below. Click to enlarge:"
    
    render_html(f"""
    <div style="margin-bottom: 22px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.6rem;">🖼️</span>
            <h2 style="color: #063970; margin: 0; font-size: 1.7rem; font-weight: 950;">
                {gallery_head}
            </h2>
        </div>
        <p style="color: #64748b; font-size: 1.05rem; margin: 6px 0 0 0; font-weight: 600;">
            {gallery_sub}
        </p>
    </div>
    """)

    # Grid of Photos: 2 columns for 4 landscape photos + full width card for Poster photo
    col_g1, col_g2 = st.columns(2)
    
    # First 4 photos in 2x2 grid
    for idx in range(4):
        target_col = col_g1 if idx % 2 == 0 else col_g2
        p_data = FIELD_PHOTOS[idx]
        p_title = p_data["title"]["te"] if is_te else p_data["title"]["en"]
        p_desc = p_data["description"]["te"] if is_te else p_data["description"]["en"]
        p_badge = p_data["badge"]["te"] if is_te else p_data["badge"]["en"]
        p_file = os.path.join(img_dir, p_data["filename"])
        
        btn_view_label = "🔍 పెద్దదిగా చూడండి (Enlarge)" if is_te else "🔍 Enlarge Photo"
        
        with target_col:
            # 1. Title ABOVE the image (Mandatory Requirement)
            render_html(f"""
            <div style="background: #ffffff; border-radius: 18px; border: 1.5px solid #e2e8f0; padding: 18px 20px; margin-bottom: 22px; box-shadow: 0 4px 16px rgba(15,43,92,0.06);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="background: #e0f2fe; color: #0284c7; padding: 4px 10px; border-radius: 8px; font-weight: 800; font-size: 0.8rem;">
                        {p_badge}
                    </span>
                    <span style="font-size: 0.85rem; color: #64748b; font-weight: 700;">
                        🕒 {p_data['time']}
                    </span>
                </div>
                <h3 style="color: #063970; font-size: 1.25rem; font-weight: 900; margin: 0 0 12px 0; line-height: 1.35;">
                    📸 {p_title}
                </h3>
            </div>
            """)
            
            # 2. Original photograph in the middle
            if os.path.exists(p_file):
                st.image(p_file, use_container_width=True)
            else:
                st.error(f"Image not found: {p_data['filename']}")
                
            # 3. Short description BELOW the image & Enlarge button (Mandatory Requirement)
            render_html(f"""
            <div style="background: #f8fafc; border-radius: 14px; padding: 14px 16px; margin: 10px 0 14px 0; border: 1px solid #e2e8f0;">
                <p style="color: #334155; font-size: 0.98rem; line-height: 1.6; margin: 0; font-weight: 550;">
                    {p_desc}
                </p>
            </div>
            """)
            
            if st.button(btn_view_label, key=f"btn_enlarge_{idx}", use_container_width=True):
                st.session_state.field_lightbox_idx = idx
                st.rerun()
                
            render_html("<div style='margin-bottom: 24px;'></div>")

    # Photo 5: Educational Poster Featured Card
    p5_data = FIELD_PHOTOS[4]
    p5_title = p5_data["title"]["te"] if is_te else p5_data["title"]["en"]
    p5_desc = p5_data["description"]["te"] if is_te else p5_data["description"]["en"]
    p5_badge = p5_data["badge"]["te"] if is_te else p5_data["badge"]["en"]
    p5_file = os.path.join(img_dir, p5_data["filename"])
    
    render_html(f"""
    <div style="background: #ffffff; border-radius: 22px; border: 2px solid #bae6fd; padding: 24px 28px; margin: 16px 0 28px 0; box-shadow: 0 8px 24px rgba(11,99,206,0.08);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
            <span style="background: #fef3c7; color: #b45309; padding: 5px 14px; border-radius: 9999px; font-weight: 850; font-size: 0.88rem; border: 1px solid #fde68a;">
                {p5_badge} • PHOTO 5
            </span>
            <span style="font-size: 0.9rem; color: #0284c7; font-weight: 800;">
                🌟 CAVI Official Awareness Material
            </span>
        </div>
        <h3 style="color: #063970; font-size: 1.55rem; font-weight: 950; margin: 0 0 10px 0;">
            🎨 {p5_title}
        </h3>
        <p style="color: #475569; font-size: 1.05rem; line-height: 1.6; margin: 0 0 18px 0; font-weight: 550;">
            {p5_desc}
        </p>
    </div>
    """)
    
    col_p5_left, col_p5_right = st.columns([5, 4])
    with col_p5_left:
        if os.path.exists(p5_file):
            st.image(p5_file, caption=p5_title, use_container_width=True)
        else:
            st.error(f"Image not found: {p5_data['filename']}")
    with col_p5_right:
        poster_info_head = "పోస్టర్‌లోని ముఖ్య సమాచారం:" if is_te else "Key Sections Covered on the Poster:"
        render_html(f"""
        <div style="background: #f8fafc; border-radius: 18px; padding: 22px; border: 1.5px solid #e2e8f0;">
            <div style="font-weight: 900; color: #063970; font-size: 1.2rem; margin-bottom: 14px;">
                📌 {poster_info_head}
            </div>
            <div style="font-size: 0.98rem; color: #334155; line-height: 1.9;">
                <div>🔐 <b>ఓటీపీ మోసాలు (OTP Fraud)</b>: ఎవరికీ ఓటీపీ చెప్పకూడదు.</div>
                <div>🏦 <b>నకిలీ కేవైసీ (Fake KYC)</b>: లింకులు నొక్కవద్దు.</div>
                <div>🎁 <b>లాటరీ స్కామ్స్ (Lottery Fraud)</b>: ముందస్తు డబ్బు చెల్లించవద్దు.</div>
                <div>💳 <b>యూపీఐ జాగ్రత్తలు (UPI Safety)</b>: డబ్బు పొందడానికి పిన్ అవసరం లేదు.</div>
                <div>📲 <b>స్క్రీన్ షేరింగ్ (Screen-Sharing)</b>: AnyDesk ఎక్కించవద్దు.</div>
                <div>🚨 <b>1930 హెల్ప్‌లైన్</b>: మోసం జరిగితే వెంటనే కాల్ చేయాలి.</div>
                <div>🌐 <b>cybercrime.gov.in</b>: అధికారిక ప్రభుత్వ పోర్టల్.</div>
            </div>
        </div>
        """)
        
        btn_view_p5 = "🔍 పోస్టర్‌ను పెద్దదిగా చూడండి (Enlarge Poster)" if is_te else "🔍 Enlarge Poster Lightbox"
        if st.button(btn_view_p5, key="btn_enlarge_4", type="primary", use_container_width=True):
            st.session_state.field_lightbox_idx = 4
            st.rerun()

    render_html("<div style='margin-bottom: 34px;'></div>")

    # ==============================================================================
    # 5. WHAT WE DID DURING OUR FIELD VISIT (8 ACTIVITIES)
    # ==============================================================================
    act_title = "మా క్షేత్రస్థాయి పర్యటనలో నిర్వహించిన కార్యక్రమాలు" if is_te else "What We Did During Our Field Visit"
    act_sub = "గ్రామీణ ప్రాంతంలో డిజిటల్ భద్రతా అవగాహనను పెంచడానికి మేము చేపట్టిన ముఖ్యమైన దశలు:" if is_te else "Key awareness activities and practical steps conducted with rural community members:"
    
    render_html(f"""
    <div class="cavi-card" style="border-top: 6px solid #0b63ce; margin-bottom: 28px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 6px;">
            <span style="font-size: 1.7rem;">🎯</span>
            <h2 style="color: #063970; margin: 0; font-size: 1.75rem; font-weight: 950;">
                {act_title}
            </h2>
        </div>
        <p style="color: #64748b; font-size: 1.08rem; margin: 0; font-weight: 600;">
            {act_sub}
        </p>
    </div>
    """)
    
    act_col1, act_col2 = st.columns(2)
    for idx, act in enumerate(FIELD_ACTIVITIES_LIST):
        target_act_col = act_col1 if idx % 2 == 0 else act_col2
        a_title = act["title"]["te"] if is_te else act["title"]["en"]
        a_desc = act["desc"]["te"] if is_te else act["desc"]["en"]
        
        with target_act_col:
            render_html(f"""
            <div class="field-activity-card">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 1.45rem;">{act['icon']}</span>
                        <span style="color: #063970; font-weight: 900; font-size: 1.12rem;">{a_title}</span>
                    </div>
                    <span style="background: #e0f2fe; color: #0369a1; font-weight: 900; font-size: 0.82rem; padding: 2px 10px; border-radius: 9999px;">
                        #{act['step']}
                    </span>
                </div>
                <p style="color: #475569; font-size: 0.98rem; line-height: 1.6; margin: 0; font-weight: 500;">
                    {a_desc}
                </p>
            </div>
            """)

    render_html("<div style='margin-bottom: 34px;'></div>")

    # ==============================================================================
    # 6. COMMUNITY IMPACT SECTION (CREATING A CYBER-SAFE COMMUNITY)
    # ==============================================================================
    impact_title = "సైబర్ సురక్షిత సమాజ నిర్మాణం" if is_te else "Creating a Cyber-Safe Community"
    impact_sub = "గ్రామీణ పౌరులను సైబర్ మోసాల బారిన పడకుండా రక్షించే 8 అత్యంత ముఖ్యమైన సూత్రాలు:" if is_te else "Core cyber safety messages and precautions shared directly with village citizens to prevent online fraud:"
    
    render_html(f"""
    <div class="cavi-card" style="border-top: 6px solid #168447; margin-bottom: 28px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 6px;">
            <span style="font-size: 1.7rem;">🛡️</span>
            <h2 style="color: #063970; margin: 0; font-size: 1.75rem; font-weight: 950;">
                {impact_title}
            </h2>
        </div>
        <p style="color: #64748b; font-size: 1.08rem; margin: 0; font-weight: 600;">
            {impact_sub}
        </p>
    </div>
    """)
    
    imp_col1, imp_col2 = st.columns(2)
    for idx, rule in enumerate(COMMUNITY_IMPACT_RULES):
        target_imp_col = imp_col1 if idx % 2 == 0 else imp_col2
        r_txt = rule["te"] if is_te else rule["en"]
        
        with target_imp_col:
            render_html(f"""
            <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 14px; padding: 14px 18px; margin-bottom: 14px; display: flex; align-items: flex-start; gap: 12px; box-shadow: 0 2px 6px rgba(22,132,71,0.04);">
                <span style="font-size: 1.35rem; line-height: 1.2;">{rule['icon']}</span>
                <span style="color: #14532d; font-size: 0.98rem; font-weight: 700; line-height: 1.55;">
                    {r_txt}
                </span>
            </div>
            """)

    # ==============================================================================
    # 7. PROMINENT 1930 EMERGENCY HELPLINE CALLOUT (MANDATORY REQUIREMENT)
    # ==============================================================================
    em_card_title = "సైబర్ మోసం జరిగిందా? భయపడకండి — వెంటనే 1930 కు కాల్ చేయండి!" if is_te else "Cyber Fraud Happened? Don't Panic — Report Immediately!"
    em_card_desc = "మోసం జరిగిన మొదటి 2-3 గంటల 'గోల్డెన్ అవర్' లో 1930 కు కాల్ చేస్తే మోసగాళ్ల ఖాతాలను స్తంభింపజేసి, మీ సొమ్మును కాపాడే అవకాశం చాలా ఎక్కువ." if is_te else "Golden Hour Reporting: Dialing 1930 within the first 2-3 hours dramatically increases the chances of freezing scammer accounts and recovering your hard-earned funds."
    
    render_html(f"""
    <div style="background: linear-gradient(90deg, #7f1d1d 0%, #b91c1c 45%, #991b1b 100%); 
                border-radius: 20px; padding: 22px 28px; color: #ffffff; margin-top: 20px; 
                box-shadow: 0 8px 24px rgba(185,28,28,0.25); display: flex; justify-content: space-between; 
                align-items: center; flex-wrap: wrap; gap: 16px; border: 2px solid #fca5a5;">
        <div style="flex: 1 1 520px;">
            <div style="font-size: 1.35rem; font-weight: 950; color: #ffffff; margin-bottom: 6px; display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.6rem;">🚨</span> <span>{em_card_title}</span>
            </div>
            <div style="font-size: 1.02rem; color: #fee2e2; line-height: 1.55; font-weight: 550;">
                {em_card_desc}
            </div>
        </div>
        <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
            <a href="tel:1930" class="cavi-call-1930-btn">
                <span>📞</span> <span>1930</span>
            </a>
            <a href="https://cybercrime.gov.in" target="_blank" class="cavi-portal-btn">
                <span>🌐</span> <span>cybercrime.gov.in ↗</span>
            </a>
        </div>
    </div>
    """)
    
    render_html("<div style='margin-bottom: 24px;'></div>")
