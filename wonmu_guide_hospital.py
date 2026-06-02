import streamlit as st

st.set_page_config(
    page_title="원무 온보딩 가이드 [병원급]",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Gmarket+Sans:wght@300;500;700&display=swap');

html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }

/* 병원급: 딥 그린 계열 테마 */
.stApp { background: linear-gradient(135deg, #e8f5e9 0%, #e0f2f1 50%, #e8eaf6 100%); }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 60%, #388e3c 100%);
    border-right: none;
}
[data-testid="stSidebar"] * { color: #e8f5e9 !important; }
[data-testid="stSidebar"] .stRadio label {
    padding: 8px 12px; border-radius: 8px;
    transition: background 0.2s; display: block;
}
[data-testid="stSidebar"] .stRadio label:hover { background: rgba(255,255,255,0.12); }

.hero-banner {
    background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #43a047 100%);
    border-radius: 20px; padding: 48px 40px; margin-bottom: 32px;
    color: white; position: relative; overflow: hidden;
    box-shadow: 0 8px 32px rgba(27,94,32,0.35);
}
.hero-banner::before {
    content:''; position:absolute; top:-60px; right:-60px;
    width:240px; height:240px; background:rgba(255,255,255,0.06); border-radius:50%;
}
.hero-banner::after {
    content:''; position:absolute; bottom:-40px; left:30%;
    width:160px; height:160px; background:rgba(255,255,255,0.04); border-radius:50%;
}
.hero-title {
    font-family:'Gmarket Sans','Noto Sans KR',sans-serif;
    font-size:2.4rem; font-weight:700; margin:0 0 8px 0; line-height:1.2;
}
.hero-sub { font-size:1.05rem; opacity:0.85; margin:0; font-weight:300; }
.hero-badge {
    display:inline-block; background:rgba(255,255,255,0.18);
    border:1px solid rgba(255,255,255,0.3); border-radius:20px;
    padding:4px 14px; font-size:0.78rem; font-weight:500;
    margin-bottom:16px; letter-spacing:0.5px;
}

.card {
    background:white; border-radius:16px; padding:24px; margin-bottom:20px;
    box-shadow:0 2px 16px rgba(27,94,32,0.07);
    border:1px solid rgba(56,142,60,0.15);
    transition:transform 0.2s,box-shadow 0.2s;
}
.card:hover { transform:translateY(-2px); box-shadow:0 6px 24px rgba(27,94,32,0.13); }

.step-card {
    background:white; border-radius:16px; padding:24px 28px; margin-bottom:18px;
    box-shadow:0 2px 16px rgba(27,94,32,0.07);
    border-left:5px solid #2e7d32; position:relative;
}
.step-number {
    position:absolute; top:-14px; left:24px;
    background:linear-gradient(135deg,#2e7d32,#43a047); color:white;
    font-weight:700; font-size:0.82rem; padding:4px 14px;
    border-radius:12px; letter-spacing:0.5px;
}
.step-title { font-size:1.15rem; font-weight:700; color:#1b5e20; margin:10px 0 8px 0; }
.step-desc { color:#546e7a; font-size:0.92rem; line-height:1.7; }

.tip-box {
    background:linear-gradient(135deg,#e8f5e9,#f1f8e9);
    border-radius:12px; padding:16px 20px; margin:12px 0; border-left:4px solid #43a047;
}
.warn-box {
    background:linear-gradient(135deg,#fff3e0,#fff8e1);
    border-radius:12px; padding:16px 20px; margin:12px 0; border-left:4px solid #fb8c00;
}
.info-box {
    background:linear-gradient(135deg,#e3f2fd,#e0f2f1);
    border-radius:12px; padding:16px 20px; margin:12px 0; border-left:4px solid #00897b;
}
.danger-box {
    background:linear-gradient(135deg,#fce4ec,#ffeee8);
    border-radius:12px; padding:16px 20px; margin:12px 0; border-left:4px solid #e53935;
}

.section-header {
    font-family:'Gmarket Sans',sans-serif; font-size:1.5rem; font-weight:700;
    color:#1b5e20; padding-bottom:10px; border-bottom:3px solid #2e7d32;
    margin:32px 0 20px 0;
}
.section-sub { color:#388e3c; font-size:0.95rem; margin-top:-14px; margin-bottom:20px; }

.checklist-item {
    display:flex; align-items:flex-start; gap:10px; padding:10px 0;
    border-bottom:1px solid #f0f0f0; font-size:0.93rem; color:#37474f;
}
.check-icon { font-size:1.1rem; flex-shrink:0; }

.term-card {
    background:white; border-radius:12px; padding:16px 20px; margin-bottom:12px;
    border:1px solid #e8f5e9; box-shadow:0 1px 8px rgba(27,94,32,0.05);
}
.term-name { font-weight:700; color:#1b5e20; font-size:0.98rem; }
.term-eng { font-size:0.78rem; color:#9e9e9e; font-weight:400; }
.term-def { color:#546e7a; font-size:0.88rem; margin-top:6px; line-height:1.6; }

.flow-wrap { display:flex; flex-wrap:wrap; align-items:center; gap:6px; margin:16px 0; }
.flow-box {
    background:linear-gradient(135deg,#e8f5e9,#c8e6c9);
    border-radius:10px; padding:10px 16px; font-size:0.85rem;
    font-weight:600; color:#1b5e20; text-align:center; min-width:80px;
}
.flow-arrow { font-size:1.2rem; color:#66bb6a; }

.fee-table { width:100%; border-collapse:collapse; font-size:0.88rem; }
.fee-table th {
    background:linear-gradient(135deg,#2e7d32,#43a047);
    color:white; padding:10px 14px; text-align:left; font-weight:600;
}
.fee-table td { padding:9px 14px; border-bottom:1px solid #e8f5e9; color:#37474f; }
.fee-table tr:nth-child(even) td { background:#f5fff5; }
.fee-table tr:hover td { background:#e8f5e9; }

.qa-box {
    background:white; border-radius:14px; padding:20px 24px; margin-bottom:16px;
    border:1px solid #e8f5e9; box-shadow:0 1px 8px rgba(27,94,32,0.05);
}
.qa-q { font-weight:700; color:#1b5e20; font-size:0.95rem; margin-bottom:8px; }
.qa-a { font-size:0.88rem; color:#37474f; line-height:1.8; }

.scenario-box {
    background:linear-gradient(135deg,#e8f5e9,#f1f8e9);
    border-radius:14px; padding:20px 24px; margin-bottom:16px;
    border-left:5px solid #2e7d32;
}

.dept-badge {
    display:inline-block; background:#e8f5e9; color:#1b5e20;
    border-radius:6px; padding:2px 10px; font-size:0.78rem;
    font-weight:700; margin:2px 3px;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# 공통 헬퍼
# ══════════════════════════════════════════════

def render_hero(title, subtitle, badge="병원급 원무 온보딩 가이드"):
    st.markdown(f"""
    <div class='hero-banner'>
        <div class='hero-badge'>🏨 {badge}</div>
        <div class='hero-title'>{title}</div>
        <p class='hero-sub'>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def tip(text, kind="tip"):
    icons  = {"tip":"💡","warn":"⚠️","info":"ℹ️","danger":"🚨"}
    labels = {"tip":"현장 TIP","warn":"주의사항","info":"참고","danger":"절대 주의"}
    cls    = {"tip":"tip-box","warn":"warn-box","info":"info-box","danger":"danger-box"}
    st.markdown(f"""
    <div class='{cls[kind]}'>
        <b>{icons[kind]} {labels[kind]}</b><br>
        <span style='font-size:0.9rem;color:#37474f;'>{text}</span>
    </div>""", unsafe_allow_html=True)

def flow(*steps):
    html = "<div class='flow-wrap'>"
    for i,s in enumerate(steps):
        html += f"<div class='flow-box'>{s}</div>"
        if i < len(steps)-1:
            html += "<span class='flow-arrow'>→</span>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def checklist(items):
    html = ""
    for icon,text in items:
        html += f"<div class='checklist-item'><span class='check-icon'>{icon}</span><span>{text}</span></div>"
    st.markdown(html, unsafe_allow_html=True)

def sh(text):
    st.markdown(f"<div class='section-header'>{text}</div>", unsafe_allow_html=True)

def sub(text):
    st.markdown(f"<p class='section-sub'>{text}</p>", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# 데이터
# ══════════════════════════════════════════════

MENU_ITEMS = {
    "🏠 홈 — 병원급 로드맵":               "home",
    "📋 STEP 1 · 병원 조직 & 파트 이해":   "step1",
    "🪪 STEP 2 · 보험 & 수가 기초":        "step2",
    "💊 STEP 3 · 외래 접수·수납 실전":     "step3",
    "🏥 STEP 4 · 입원·퇴원 프로세스":      "step4",
    "🔄 STEP 5 · 전원·응급·중환자":        "step5",
    "📂 STEP 6 · 서류 발급 & 민원 대응":   "step6",
    "🗣️ STEP 7 · 환자 커뮤니케이션":      "step7",
    "⚡ 빠른 참조 — 필수 용어 사전":       "terms",
    "📞 긴급 상황 대응 매뉴얼":            "emergency",
}

ROADMAP_STEPS = [
    ("🏗️","병원 조직 & 파트 이해","1~3일차","외래·입원·응급 파트 분업 구조, 부서간 협업 채널, EMR 권한 범위 파악"),
    ("📋","보험 & 수가 기초","1주차","병원급 본인부담률, 종합병원·병원 구분, 의뢰서 체계, DRG 포괄수가 이해"),
    ("🖥️","외래 접수·수납 실전","2주차","다과 동시 접수, 예약 시스템 연동, 검사 후 추가 수납, 보험 유형별 처리"),
    ("🏥","입원·퇴원 프로세스","3~4주차","입원 동의서 체계, 병실 배정 기준, 간호등급 연동, 장기 입원 정산"),
    ("🔄","전원·응급·중환자 프로세스","4~5주차","응급실 수납, 타 병원 전원 서류, 중환자실 별도 수가, 야간 당직 업무"),
    ("📂","서류 발급 & 민원 대응","5~6주차","다부서 서류 연계, 보험사 직접 청구, 복잡 민원 에스컬레이션"),
    ("🗣️","환자 커뮤니케이션","상시","다과 동시 응대, 보호자 안내, 외국인·고령 환자, 콜센터 연계"),
]

TERMS = [
    ("요양급여","Health Insurance Benefit","건강보험에서 인정하는 진료 항목. 행위·약제·치료재료로 구분되며 심평원 기준에 따라 공단이 비용 일부 부담."),
    ("비급여","Non-covered Service","건강보험 미적용으로 전액 환자 부담. 병원이 수가 자율 책정. 반드시 사전 서면 고지 후 징수."),
    ("선별급여","Selective Benefit","급여 인정하되 본인부담 50~80% 높게 적용. MRI 일부·척추 내시경 등. 서면 설명 권고."),
    ("본인부담금","Co-payment","급여 진료비 중 환자 직접 부담액. 병원급 외래 40%, 입원 20%가 기본."),
    ("본인부담상한제","OOP Maximum","연간 본인부담 소득분위별 상한 초과분을 공단이 사후 환급하는 제도."),
    ("상병코드","KCD Code","질병·손상 국제 분류 코드. 수가 청구의 핵심. 진단명과 처방 행위가 코드와 일치해야 함."),
    ("산정특례","Special Criteria","암·희귀·중증난치 등록 환자 본인부담 5~10%로 대폭 낮추는 제도. 등록증·유효기간 매번 확인."),
    ("의료급여","Medical Aid","저소득 수급자 국가 지원. 1종(입원 무료)·2종(외래 15%, 입원 10%). 수급자증·유효기간 필수 확인."),
    ("DRG","Diagnosis Related Groups","7개 수술(백내장·편도·항문·탈장·제왕절개·자궁적출·치질) 포괄수가제. 재원일수 무관 정액 지급."),
    ("진료의뢰서","Referral Letter","1·2차 의료기관에서 병원·상급병원으로 환자를 의뢰하는 서류. 없으면 본인부담률 상승."),
    ("간호등급","Nursing Grade","병상 대비 간호사 수 비율로 결정(1~9등급). 높을수록 입원료 가산. 입원 수납에 자동 반영."),
    ("입원료","Inpatient Care Fee","입원 1일 기본 비용. 간호등급·병실 등급·중환자실 여부에 따라 크게 달라짐."),
    ("중환자실","ICU","일반 병실보다 수가가 2~3배 높은 집중치료실. 별도 입원료·처치료 적용. 가족 면회 제한 안내 필수."),
    ("응급의료관리료","Emergency Fee","응급실 내원 시 부과하는 기본 수가. 응급·비응급 구분에 따라 금액 차이 큼."),
    ("전원","Patient Transfer","치료 지속을 위해 다른 의료기관으로 환자를 이송하는 것. 전원 동의서·진료 요약지 필수."),
    ("임의비급여","Arbitrary Non-benefit","급여 항목임에도 비급여 청구 → 의료법 위반, 전액 환불+행정처분. 절대 금지."),
    ("미수금","Unpaid Bill","당일 미납 진료비. EMR 기록 필수. 3년 소멸시효. 장기 미수는 팀장 보고 후 법적 절차."),
    ("보증금","Deposit","입원 시 선납받는 진료비 담보금. 퇴원 시 정산 후 환불 또는 추가 징수."),
    ("실손보험","Actual Loss Insurance","민간 실손보험. 진료비 영수증+세부내역서 제출로 본인부담금 일부 환급. 보험사 직접 팩스 가능."),
    ("원무파트 분업","Admin Partition","병원급 이상에서 외래접수·입원수납·서류발급·보험청구 파트를 별도 운영하는 조직 구조."),
]

# ══════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════

def page_home():
    render_hero(
        "병원급 원무 온보딩 — 단계별 로드맵",
        "의원과 다릅니다. 파트 분업·다과 운영·응급실·전원까지 — 병원급 원무의 모든 것을 단계별로 안내합니다.",
        "병원급 (30~300병상)",
    )

    st.markdown("""
    <div class='info-box'>
    <b>ℹ️ 병원급과 의원급의 핵심 차이</b><br>
    <span style='font-size:0.9rem;color:#37474f;'>
    병원급(30~300병상)은 외래·입원·응급 파트가 분리 운영됩니다. 혼자 모든 업무를 담당하는 의원과 달리,
    <b>파트별 전담 업무</b>가 있고 부서간 <b>인계·협업</b>이 핵심 역량입니다.
    본인부담률도 의원(30%)보다 높은 <b>40%(외래)</b>가 적용됩니다.
    </span>
    </div>""", unsafe_allow_html=True)

    sh("📍 병원급 원무 학습 로드맵 (7단계)")
    for i,(icon,title,period,desc) in enumerate(ROADMAP_STEPS,1):
        st.markdown(f"""
        <div class='step-card'>
            <div class='step-number'>STEP {i} · {period}</div>
            <div class='step-title'>{icon} {title}</div>
            <div class='step-desc'>{desc}</div>
        </div>""", unsafe_allow_html=True)

    sh("🔄 병원급 원무 업무 전체 흐름")
    flow("환자 내원","외래 접수","진료·검사","처방 확인","외래 수납","입원 결정","입원 수속","병실 배정","재원 중 수납","퇴원 정산")

    sh("⚖️ 의원급 vs 병원급 핵심 비교")
    st.markdown("""
    <table class='fee-table'>
    <thead><tr><th>구분</th><th>의원급</th><th>병원급 (본 가이드)</th></tr></thead>
    <tbody>
    <tr><td><b>병상 수</b></td><td>30병상 미만</td><td>30~300병상</td></tr>
    <tr><td><b>외래 본인부담률</b></td><td>30%</td><td>40%</td></tr>
    <tr><td><b>입원 본인부담률</b></td><td>20%</td><td>20%</td></tr>
    <tr><td><b>원무 조직</b></td><td>1~3명 전담 (풀업무)</td><td>파트별 분업 (외래·입원·서류)</td></tr>
    <tr><td><b>응급실 운영</b></td><td>거의 없음</td><td>응급실 수납 별도 운영</td></tr>
    <tr><td><b>전원 업무</b></td><td>단순 안내</td><td>전원 동의서·서류 처리 필수</td></tr>
    <tr><td><b>진료의뢰서</b></td><td>불필요</td><td>없으면 본인부담 상승</td></tr>
    <tr><td><b>DRG(포괄수가)</b></td><td>적용 가능</td><td>적용 (입원 중심 수술 多)</td></tr>
    <tr><td><b>간호등급 영향</b></td><td>낮음</td><td>높음 (입원료 가산 직결)</td></tr>
    <tr><td><b>보험회사 직접 청구</b></td><td>가끔</td><td>자동차·산재 직접 청구 빈번</td></tr>
    </tbody></table>""", unsafe_allow_html=True)

    sh("📊 병원급 원무 파트별 업무 비중")
    st.markdown("""
    <div class='card'>
    <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:14px;'>
        <div style='background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border-radius:12px;padding:16px;text-align:center;'>
            <div style='font-size:2rem;font-weight:900;color:#1b5e20;'>35%</div>
            <div style='font-size:0.85rem;color:#2e7d32;font-weight:700;margin-top:4px;'>외래 접수·수납</div>
            <div style='font-size:0.78rem;color:#546e7a;margin-top:4px;'>다과 접수, 검사 후 수납, 예약 관리</div>
        </div>
        <div style='background:linear-gradient(135deg,#e3f2fd,#b3e5fc);border-radius:12px;padding:16px;text-align:center;'>
            <div style='font-size:2rem;font-weight:900;color:#01579b;'>30%</div>
            <div style='font-size:0.85rem;color:#0277bd;font-weight:700;margin-top:4px;'>입원·퇴원 수납</div>
            <div style='font-size:0.78rem;color:#546e7a;margin-top:4px;'>입원 수속, 장기 입원 중간 정산, 퇴원</div>
        </div>
        <div style='background:linear-gradient(135deg,#fff3e0,#ffe0b2);border-radius:12px;padding:16px;text-align:center;'>
            <div style='font-size:2rem;font-weight:900;color:#e65100;'>20%</div>
            <div style='font-size:0.85rem;color:#bf360c;font-weight:700;margin-top:4px;'>서류·보험 청구</div>
            <div style='font-size:0.78rem;color:#546e7a;margin-top:4px;'>실손·자동차·산재 서류, 의무기록</div>
        </div>
        <div style='background:linear-gradient(135deg,#f3e5f5,#e1bee7);border-radius:12px;padding:16px;text-align:center;'>
            <div style='font-size:2rem;font-weight:900;color:#6a1b9a;'>15%</div>
            <div style='font-size:0.85rem;color:#7b1fa2;font-weight:700;margin-top:4px;'>응급·전원·야간</div>
            <div style='font-size:0.78rem;color:#546e7a;margin-top:4px;'>응급실 수납, 전원 서류, 당직 대응</div>
        </div>
    </div></div>""", unsafe_allow_html=True)

    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>✅ 병원급 원무 첫 주 핵심</b>
        <div style='font-size:0.88rem;color:#37474f;line-height:2.1;margin-top:10px;'>
        · 내가 속한 파트(외래/입원/서류) 업무 범위 먼저 파악<br>
        · 파트 간 인계 방식·연락 채널 확인 (전화·메신저·EMR 메모)<br>
        · 병원급 본인부담률 40%(외래) 암기<br>
        · 진료의뢰서 유무 확인 습관화<br>
        · 간호등급·병실 등급 연동 입원료 구조 이해<br>
        · 응급실 위치·응급 수납 담당자 파악<br>
        · 야간·주말 당직 체계 확인
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#c62828;'>❌ 병원급에서 특히 주의할 것</b>
        <div style='font-size:0.88rem;color:#37474f;line-height:2.1;margin-top:10px;'>
        · 파트 경계 무시하고 혼자 처리하려 하기<br>
        · 인계 없이 파트 이탈<br>
        · 의뢰서 없는 환자를 일반 본인부담으로 처리 (본인부담 상승 적용)<br>
        · 전원 서류 미확인 상태로 환자 이송<br>
        · 응급 수납을 일반 수납과 동일하게 처리<br>
        · 중간 정산 없이 장기 입원 환자 방치<br>
        · 보험회사 직접 청구 절차 무시
        </div></div>""", unsafe_allow_html=True)

    tip("병원급 원무의 핵심은 '파트 간 협업과 인계'입니다. 혼자 완결하려 하지 말고 적시에 다음 파트로 연결하는 것이 실력입니다.", "info")


# ══════════════════════════════════════════════
# STEP 1 — 병원 조직 & 파트 이해
# ══════════════════════════════════════════════

def page_step1():
    render_hero(
        "STEP 1 · 병원 조직 & 파트 이해",
        "병원급 원무의 핵심은 파트 분업입니다. 내 업무 범위와 협업 채널을 완전히 파악합니다.",
        "1~3일차 완성 목표",
    )

    sh("🏗️ 병원급 원무팀 파트 구성")
    col1,col2,col3,col4 = st.columns(4)
    for col,(icon,title,color,bg,items) in zip([col1,col2,col3,col4],[
        ("🖥️","외래 접수·수납파트","#1b5e20","#e8f5e9",[
            "외래 환자 접수·등록","보험 자격 실시간 조회","외래 수납·영수증 발행","예약 시스템 관리","외래 전화 응대"
        ]),
        ("🏥","입원·퇴원 수납파트","#01579b","#e3f2fd",[
            "입원 수속·동의서","병실 배정 협의","중간 정산 관리","퇴원 정산·환불","보증금 관리"
        ]),
        ("📄","서류·보험 청구파트","#e65100","#fff3e0",[
            "의무기록 사본 발급","진단서·확인서 접수","실손·자동차 보험 서류","민원 상담 대응","보험회사 직접 청구"
        ]),
        ("🚨","응급·당직 파트","#6a1b9a","#f3e5f5",[
            "응급실 수납 처리","야간·주말 전담","응급 입원 수속","전원 서류 지원","당직 중 전 업무 대응"
        ]),
    ]):
        col.markdown(f"""
        <div style='background:{bg};border-radius:14px;padding:16px;height:100%;'>
            <div style='font-size:1.5rem;text-align:center;'>{icon}</div>
            <b style='color:{color};font-size:0.88rem;display:block;text-align:center;margin:6px 0;'>{title}</b>
            <ul style='font-size:0.8rem;color:#37474f;line-height:2.0;padding-left:14px;margin:0;'>
                {''.join(f'<li>{i}</li>' for i in items)}
            </ul>
        </div>""", unsafe_allow_html=True)

    tip("처음 배치받은 파트 업무를 먼저 완전히 익히세요. 다른 파트 업무는 그 다음입니다.", "info")

    sh("🤝 원무팀이 협업하는 주요 부서")
    depts = [
        ("👩‍⚕️ 간호부","병실 배정·입퇴원 일정 조율, 처치·주사 수가 누락 확인, 퇴원 예정 환자 사전 통보"),
        ("🩺 진료부(의사)","진단서·소견서 발급 요청 전달, 처방 수가 오류 수정 요청, 입원 오더·퇴원 지시 확인"),
        ("🔬 검사·영상의학","검사 결과 후 추가 수납 타이밍, 비급여 검사 금액 사전 안내, 검사실 대기 현황 공유"),
        ("💊 약제부","원내 조제 vs 원외처방 구분 확인, 고가 약제 투약 동의서 연계, DRG 해당 수술 약제 포함 여부"),
        ("🏥 간호사실 각 병동","일일 입원 환자 현황 공유, 중간 정산 안내 요청, 병실 변경 시 즉시 연락"),
        ("🚑 응급실","응급 입원 환자 정보 인수인계, 응급 수납 미완료 건 인계, 응급 의료급여 환자 처리"),
        ("📋 원무팀장·행정원장","민원 에스컬레이션, 수납 오류·환불 결재, 보험회사 분쟁 보고, 일 마감 집계 보고"),
        ("🔧 IT·전산","EMR 오류·시스템 다운 신고, 수가 코드 오류 수정 요청, 보안 사고 신고"),
    ]
    for i in range(0,len(depts),2):
        col1,col2 = st.columns(2)
        for col,(title,desc) in zip([col1,col2],depts[i:i+2]):
            col.markdown(f"""
            <div class='card' style='margin-bottom:12px;'>
                <b style='color:#1b5e20;font-size:0.9rem;'>{title}</b>
                <div style='font-size:0.83rem;color:#546e7a;margin-top:8px;line-height:1.8;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    sh("🖥️ 병원급 EMR 핵심 화면 구성")
    tip("병원급 EMR은 의원급보다 권한 체계가 복잡합니다. 파트별로 접근 가능한 메뉴가 다를 수 있습니다.", "warn")
    flow("환자 검색·등록","외래 접수","처방 확인","검사 오더 연동","수납 처리","입원 오더 확인","입원 등록","병동 인계","퇴원 정산")

    tabs = st.tabs(["🔍 외래 접수 화면","🏥 입원 관리 화면","💰 수납·정산 화면","📊 일 마감·보고"])
    with tabs[0]:
        checklist([
            ("✅","<b>다과 동시 접수</b>: 병원급은 여러 진료과를 같은 날 방문하는 환자 多. 과별 순서·대기 안내 필수"),
            ("✅","<b>진료의뢰서 확인</b>: 타 병원에서 의뢰받은 환자는 의뢰서 스캔·등록. 없으면 본인부담률 상이"),
            ("✅","<b>예약 시스템 연동</b>: 전화·온라인 예약이 EMR과 연동되는지 확인. 미연동 병원은 수기 예약장 별도"),
            ("✅","<b>보험 자격 일괄 조회</b>: 오전 첫 예약 환자 명단 조회 후 자격 일괄 선조회 가능한 EMR 확인"),
            ("⚠️","<b>당일 다과 접수 시</b>: 과별 수납을 한 번에 처리할지 과별로 처리할지 병원 방침 확인"),
        ])
    with tabs[1]:
        checklist([
            ("✅","<b>입원 등록 화면</b>: 입원 경로(외래/응급/전원), 담당 의사, 병실 등급 순서로 입력"),
            ("✅","<b>병동·병상 현황</b>: 실시간 병상 현황 조회 후 배정 가능 여부 간호부와 협의"),
            ("✅","<b>중간 정산 기능</b>: 장기 입원(2주 이상) 환자 중간 정산 일정 설정 및 알림"),
            ("✅","<b>보증금 이력</b>: 납부·환불 이력 모두 EMR에 기록. 수기 메모 금지"),
            ("⚠️","<b>DRG 환자 표시</b>: 7개 DRG 수술 해당 환자는 EMR에 별도 표시. 포괄수가 적용 확인"),
        ])
    with tabs[2]:
        checklist([
            ("✅","<b>과별 수납 통합</b>: 같은 날 여러 과 진료 시 수납 화면에서 과별 항목 통합 처리"),
            ("✅","<b>보험 유형별 수납 화면</b>: 건강보험·의료급여·자동차·산재 선택 후 화면이 달라짐"),
            ("✅","<b>입원 중간 정산</b>: 주기적 중간 정산 후 미납 금액 보호자 안내"),
            ("✅","<b>퇴원 정산</b>: 전체 입원 기간 진료비 취합 후 보증금 차감, 최종 정산"),
            ("⚠️","<b>자동차보험 수납</b>: 환자에게 받지 않고 보험회사 직접 청구가 원칙. 병원 방침 확인"),
        ])
    with tabs[3]:
        checklist([
            ("✅","<b>파트별 마감</b>: 외래·입원 파트 각각 마감 후 총괄 집계"),
            ("✅","<b>현금 시재</b>: 파트별 수납창구 시재 확인 후 금고 입금"),
            ("✅","<b>미수금 집계</b>: 당일 미수 건 목록 팀장에게 보고"),
            ("✅","<b>익일 준비</b>: 다음날 예약 환자 수·특이 환자(의료급여·산정특례 등) 사전 파악"),
        ])

    sh("📅 병원급 하루 업무 타임라인")
    timeline = [
        ("07:50","🔓 출근·파트 준비","EMR 로그인·권한 확인, 전날 인계 사항 확인, 수납기 시재 확인, 당일 예약 환자 명단 출력"),
        ("08:00","📞 야간 인계 수령","당직 원무로부터 야간 미수금·응급 입원 현황·특이사항 인계"),
        ("08:30","🔭 사전 자격 조회","오전 예약 환자 보험 자격 일괄 선조회, 의료급여·산정특례 환자 별도 표시"),
        ("09:00","👤 외래 접수 시작","예약 체크인, 미예약 접수, 진료의뢰서 확인, 다과 동시 방문 환자 안내"),
        ("10:00","🏥 입원 수속 처리","야간·응급 입원 환자 서류 보완, 당일 예정 입원 환자 사전 접수"),
        ("12:00","🍱 파트 교대 인계","미완료 수납 건 인계, 오후 특이 환자 전달, 시재 중간 확인"),
        ("13:00","🔁 오후 외래 재개","오후 진료 접수, 오전 검사 결과 후 추가 수납, 서류 신청 접수"),
        ("15:00","💰 중간 정산 안내","장기 입원 환자 중간 정산, 보호자 연락, 추가 보증금 요청"),
        ("17:00","📤 퇴원 정산 집중","당일 퇴원 예정 환자 정산, 보증금 환불, 퇴원 서류 발급"),
        ("17:30","📊 파트 마감","현금·카드 정산, 미수금 목록, 당일 집계 팀장 보고"),
        ("18:00","🌙 야간 당직 인계","야간 담당자에게 미완료 건·특이사항 인계, 응급 연락처 확인"),
    ]
    for time,title,desc in timeline:
        st.markdown(f"""
        <div style='display:flex;gap:16px;margin-bottom:12px;align-items:flex-start;'>
            <div style='min-width:56px;font-weight:700;color:#2e7d32;font-size:0.83rem;padding-top:2px;'>{time}</div>
            <div style='flex:1;background:white;border-radius:10px;padding:12px 16px;border:1px solid #e8f5e9;'>
                <div style='font-weight:700;color:#1b5e20;margin-bottom:3px;'>{title}</div>
                <div style='font-size:0.83rem;color:#546e7a;'>{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# STEP 2 — 보험 & 수가 기초
# ══════════════════════════════════════════════

def page_step2():
    render_hero(
        "STEP 2 · 보험 & 수가 기초",
        "병원급 본인부담률 40%, 진료의뢰서 체계, DRG 포괄수가까지 — 병원급 수가 구조를 완전히 이해합니다.",
        "1주차 완성 목표",
    )

    sh("💰 병원급 본인부담률 완전 암기표")
    tip("병원급 외래 기본 본인부담률은 40%입니다. 의원(30%)과 혼동하지 마세요.", "danger")
    st.markdown("""
    <table class='fee-table'>
    <thead><tr><th>상황</th><th>외래 본인부담률</th><th>입원 본인부담률</th><th>핵심 주의사항</th></tr></thead>
    <tbody>
    <tr><td><b>병원 (30~299병상)</b></td><td><b style='color:#c62828;'>40%</b></td><td>20%</td><td>기본값. 의원 30%와 다름</td></tr>
    <tr><td><b>종합병원 (300병상 이상)</b></td><td>50~60%</td><td>20%</td><td>진료과목 수·병상 수에 따라 상이</td></tr>
    <tr><td><b>진료의뢰서 없는 경우</b></td><td>구간별 차등 상승</td><td>-</td><td>종합·상급은 큰 폭 상승, 병원급도 해당</td></tr>
    <tr><td><b>의료급여 1종 외래</b></td><td>1,000~2,000원 정액</td><td>0%</td><td>수급자증 매번 확인</td></tr>
    <tr><td><b>의료급여 2종 외래</b></td><td>15%</td><td>10%</td><td>-</td></tr>
    <tr><td><b>산정특례 (암·희귀 등)</b></td><td>5%</td><td>5%</td><td>등록증·유효기간 반드시 확인</td></tr>
    <tr><td><b>선별급여</b></td><td>50~80%</td><td>50~80%</td><td>항목별 다름. EMR 수가코드 확인</td></tr>
    <tr><td><b>산재보험</b></td><td>0%</td><td>0%</td><td>근로복지공단 직접 청구</td></tr>
    <tr><td><b>자동차보험</b></td><td>0%</td><td>0%</td><td>보험회사 직접 청구. 환자에게 받지 않음</td></tr>
    <tr><td><b>DRG 포괄수가</b></td><td>-</td><td>정액 (재원일수 무관)</td><td>7개 수술. 항목별 별도 청구 불가</td></tr>
    </tbody></table>""", unsafe_allow_html=True)

    sh("📋 진료의뢰서 체계 완전 이해")
    tip("병원급에서 진료의뢰서 확인은 수납 전 필수 체크 항목입니다. 없으면 본인부담률이 달라집니다.", "warn")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>📄 진료의뢰서란?</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;line-height:2.0;'>
        · 의원·1차 의료기관에서 병원·2차 이상으로 환자를 보낼 때 발급하는 서류<br>
        · 환자가 직접 병원에 올 경우보다 본인부담이 낮아지는 기준 서류<br>
        · 유효기간: 발급일로부터 <b>30일 이내</b><br>
        · 동일 상병으로 같은 병원 재방문 시 <b>재발급 불필요</b> (기간 내)<br>
        · 형식: 건강보험 표준양식 또는 의사 소견서 형태
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#c62828;'>⚠️ 의뢰서 없을 때 대응</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;line-height:2.0;'>
        · 환자에게 의뢰서 유무 먼저 확인<br>
        · 없으면: "의뢰서가 없으시면 본인부담이 조금 높게 적용됩니다" 사전 안내<br>
        · EMR에서 의뢰서 없음 표시 후 접수 진행<br>
        · 환자가 추후 의뢰서 지참 시 소급 적용 여부는 병원 방침 확인<br>
        · 응급으로 내원한 경우: 의뢰서 예외 적용 가능 (응급 코드 확인)
        </div></div>""", unsafe_allow_html=True)

    sh("🔢 병원급 본인부담금 계산 실전 예시")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>🟢 예시 1 — 병원 외래 재진 (건강보험, 의뢰서 있음)</b>
        <div style='font-size:0.88rem;color:#37474f;line-height:2.2;margin-top:10px;'>
        급여 항목<br>
        · 재진 진찰료: 16,200원<br>
        · 혈액검사: 28,500원<br>
        · 초음파 (선별급여 50%): 60,000원<br>
        <b>─────────────────────</b><br>
        · 일반 급여 소계: 44,700원 × 40% = 17,880원<br>
        · 선별급여 소계: 60,000원 × 50% = 30,000원<br>
        · 비급여 (도수치료): 80,000원<br>
        <b style='color:#1b5e20;font-size:1.0rem;'>→ 오늘 내실 금액: 127,880원</b>
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#01579b;'>🔵 예시 2 — 병원 입원 (DRG 포괄수가·충수절제술)</b>
        <div style='font-size:0.88rem;color:#37474f;line-height:2.2;margin-top:10px;'>
        DRG 적용 수술 (복잡 충수절제술)<br>
        · 포괄수가 총액: 1,850,000원 (정액)<br>
        · 재원일수와 무관하게 동일<br>
        · 입원 본인부담: 20%<br>
        <b>─────────────────────</b><br>
        · 환자 부담: 370,000원<br>
        · 식대 별도: 30,000원 (5일)<br>
        · 비급여 (1인실 차액): 200,000원<br>
        <b style='color:#01579b;font-size:1.0rem;'>→ 최종 환자 부담: 600,000원</b>
        </div></div>""", unsafe_allow_html=True)

    st.markdown("""<div style='height:8px;'></div>""", unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#6a1b9a;'>🟣 예시 3 — 산정특례 환자 입원 (암)</b>
        <div style='font-size:0.88rem;color:#37474f;line-height:2.2;margin-top:10px;'>
        · 입원 급여 총 진료비: 3,200,000원<br>
        · 산정특례 본인부담: 5%<br>
        · 급여 본인부담: 160,000원<br>
        · 식대: 40,000원<br>
        · 비급여: 120,000원<br>
        <b style='color:#6a1b9a;font-size:1.0rem;'>→ 환자 부담: 320,000원</b>
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#e65100;'>🟠 예시 4 — 자동차보험 입원</b>
        <div style='font-size:0.88rem;color:#37474f;line-height:2.2;margin-top:10px;'>
        · 총 입원 진료비: 2,400,000원<br>
        · 환자 본인부담: <b>0원</b><br>
        · 전액 보험회사 직접 청구<br>
        · 보험회사 팩스·이메일로 서류 발송<br>
        · 보험회사 담보 한도 초과 시 초과분 환자 부담<br>
        <b style='color:#e65100;font-size:1.0rem;'>→ 환자에게 수납 받지 않음</b>
        </div></div>""", unsafe_allow_html=True)

    sh("📦 DRG 포괄수가 — 병원급 필수 이해")
    st.markdown("""
    <div class='card'>
    <b style='color:#1b5e20;'>DRG(포괄수가제) 7개 수술 — 이것은 반드시 외우세요</b>
    <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:14px;'>
    """, unsafe_allow_html=True)
    for s in ["👁️ 백내장 수술","🦷 편도 수술","🔴 항문 수술","🫁 서혜·대퇴 탈장","🤰 제왕절개","🔬 자궁적출","🩸 치질 수술"]:
        st.markdown(f"""
        <div style='background:#e8f5e9;border-radius:10px;padding:10px;text-align:center;font-size:0.82rem;font-weight:700;color:#1b5e20;'>{s}</div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    checklist([
        ("✅","DRG 수술은 <b>재원일수·치료 방법과 무관하게 진단군별 정액</b> 지급"),
        ("✅","DRG 적용 환자 EMR에 포괄수가 코드 자동 적용 여부 확인"),
        ("⚠️","DRG 항목에서 <b>별도 청구 불가 항목</b>: 의사 진찰료·마취료·수술료는 포함. 별도 행위료 추가 금지"),
        ("✅","DRG 비적용 선택 가능: 환자가 원할 경우 행위별 수가 선택 가능 (사전 설명 후 선택 동의서)"),
        ("⚠️","비급여 항목(상급병실 차액 등)은 DRG와 별도 청구 가능"),
    ])
    st.markdown("</div>", unsafe_allow_html=True)

    sh("👴 병원급 특수 환자 수납 주의사항")
    st.markdown("""
    <div class='card'>
    <div style='display:grid;grid-template-columns:1fr 1fr;gap:14px;'>
        <div style='padding:14px;background:#e8f5e9;border-radius:10px;'>
            <b style='color:#1b5e20;'>🏥 전원 환자 (타 병원에서 이송)</b>
            <div style='font-size:0.83rem;color:#37474f;margin-top:8px;line-height:1.9;'>
            · 전원 의뢰서 + 진료 요약지 수령 확인<br>
            · 기존 병원 진료 기록 인수<br>
            · 보험 자격 재조회 (전원 당일 기준)<br>
            · 응급 전원 시 수납 절차 나중에 진행 가능
            </div>
        </div>
        <div style='padding:14px;background:#e3f2fd;border-radius:10px;'>
            <b style='color:#01579b;'>🚑 응급 입원 환자</b>
            <div style='font-size:0.83rem;color:#37474f;margin-top:8px;line-height:1.9;'>
            · 응급 수납은 환자 안정 후 진행<br>
            · 보호자에게 우선 안내<br>
            · 응급 의료급여 환자: 응급 코드 적용<br>
            · 신원 불명 환자: 무연고자 처리 절차 확인
            </div>
        </div>
        <div style='padding:14px;background:#fff3e0;border-radius:10px;'>
            <b style='color:#e65100;'>🚗 자동차보험 입원</b>
            <div style='font-size:0.83rem;color:#37474f;margin-top:8px;line-height:1.9;'>
            · 사고확인서·보험회사 팩스 번호 수령<br>
            · 환자에게 직접 수납 받지 않음<br>
            · 보험회사 한도 조회 후 초과 시 별도 안내<br>
            · 보험회사 담당자 연락처 확보
            </div>
        </div>
        <div style='padding:14px;background:#f3e5f5;border-radius:10px;'>
            <b style='color:#6a1b9a;'>🔨 산재 환자</b>
            <div style='font-size:0.83rem;color:#37474f;margin-top:8px;line-height:1.9;'>
            · 근로복지공단 승인 여부 먼저 확인<br>
            · 승인 전: 건강보험 적용 후 사후 전환<br>
            · 환자 본인부담 없음 (승인 후)<br>
            · 산재 전담 서식으로 별도 청구
            </div>
        </div>
    </div></div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# STEP 3 — 외래 접수·수납 실전
# ══════════════════════════════════════════════

def page_step3():
    render_hero(
        "STEP 3 · 외래 접수·수납 실전",
        "다과 동시 접수, 검사 후 추가 수납, 보험 유형별 처리 — 병원급 외래의 복잡한 흐름을 완전 정복합니다.",
        "2주차 완성 목표",
    )

    sh("🚶 병원급 외래 접수 전체 프로세스")
    flow("내원 확인","진료의뢰서 확인","보험 자격 조회","초진/재진 판단","과별 접수","대기 안내","진료·검사","추가 처방 확인","수납","영수증")

    sh("📍 병원급 외래 접수 특수 상황")

    tabs = st.tabs(["📋 다과 동시 방문","🔍 초진·재진 판단","💳 수납 유형별 처리","🔄 검사 후 추가 수납","💰 환불 처리"])

    with tabs[0]:
        st.markdown("""
        <div class='scenario-box'>
        <b>시나리오</b>: 환자가 "내과랑 정형외과 같이 보고 싶어요" — 병원급에서 가장 흔한 상황
        </div>""", unsafe_allow_html=True)
        checklist([
            ("1️⃣","각 진료과 접수를 <b>별도로 등록</b> (EMR에서 과별 접수 항목 따로 생성)"),
            ("2️⃣","<b>수납은 한 번에</b>: 모든 진료 완료 후 통합 수납 처리 (병원 방침 확인)"),
            ("3️⃣","진료과 대기 순서 안내: 어느 과를 먼저 갈지 환자에게 명확히 안내"),
            ("4️⃣","한 과 진료 중 다른 과에서 호출 시: 환자 위치 진료실에 알림"),
            ("5️⃣","검사가 끼어 있는 경우: 검사 후 결과 보러 재방문 여부 안내"),
        ])
        tip("다과 동시 방문 시 진찰료는 주된 진료과 1개만 전액 적용, 나머지는 50% 감산 적용. EMR 자동 처리 여부 확인!", "warn")

    with tabs[1]:
        col1,col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class='card'>
            <b style='color:#c62828;'>🔴 초진</b>
            <div style='font-size:0.87rem;color:#37474f;line-height:2.1;margin-top:8px;'>
            · 해당 병원 첫 방문<br>
            · 마지막 진료일로부터 <b>91일 이상</b> 경과<br>
            · 처음 방문하는 진료과<br>
            · 전원 후 첫 방문
            </div></div>""", unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class='card'>
            <b style='color:#1b5e20;'>🟢 재진</b>
            <div style='font-size:0.87rem;color:#37474f;line-height:2.1;margin-top:8px;'>
            · 동일 과 90일 이내 재방문<br>
            · 당일 재방문 (당일 재진 수가)<br>
            · 검사 결과 확인 방문<br>
            · 입원 후 동일 과 외래 전환
            </div></div>""", unsafe_allow_html=True)
        tip("병원급은 다과 방문이 많아 과별 초재진이 복잡합니다. EMR 자동 판단 + 눈으로 90일 재확인 필수.", "info")

    with tabs[2]:
        st.markdown("<b style='color:#1b5e20;'>수납 유형별 핵심 처리 방법</b>", unsafe_allow_html=True)
        checklist([
            ("💳","<b>건강보험</b>: 외래 40% 적용. 카드·현금 수납 후 EMR 확정"),
            ("🟢","<b>의료급여 1종</b>: 외래 정액 1,000~2,000원. 별도 수납 화면 사용"),
            ("🟡","<b>의료급여 2종</b>: 외래 15%. 일반 수납과 유사하나 화면 구분"),
            ("🔴","<b>자동차보험</b>: 환자에게 받지 않음. 보험회사 직접 청구. 사고확인서 수령"),
            ("🔵","<b>산재보험</b>: 환자에게 받지 않음. 근로복지공단 승인 후 청구. 승인 전 건강보험 임시 처리"),
            ("🟣","<b>산정특례</b>: 5% 적용. 등록증 유효기간 반드시 확인"),
            ("⚪","<b>비급여 전액</b>: 해당 수가표 금액 확인 후 전액 수납"),
        ])

    with tabs[3]:
        st.markdown("""
        <div class='scenario-box'>
        <b>시나리오</b>: 혈액검사 결과 보러 왔는데 의사가 CT까지 추가로 처방
        </div>""", unsafe_allow_html=True)
        checklist([
            ("1️⃣","진료 완료 후 처방 화면 최종 확인 (추가 처방 반영 여부)"),
            ("2️⃣","CT 등 영상 검사: 검사 완료 후 판독 결과가 나올 때까지 수납 대기 or 즉시 수납 병원 방침 확인"),
            ("3️⃣","검사 결과 확인 후 재방문 필요 시: 오늘 수납 + 다음 방문 예약 안내"),
            ("4️⃣","검사비 비급여 해당 시 사전에 금액 안내 후 동의 확인"),
            ("5️⃣","당일 수납 어려운 경우: 미수 처리 후 다음 방문 시 합산 수납"),
        ])

    with tabs[4]:
        checklist([
            ("✅","<b>환불 발생 사유</b>: 수납 오류·보험 소급·과납·DRG 재산정·자동차보험 전환"),
            ("📋","<b>절차</b>: 사유 확인 → 팀장 결재 → 환불 처리"),
            ("💳","<b>카드 환불</b>: 원거래 카드로만 환불. 다른 카드 환불 절대 불가"),
            ("🏦","<b>계좌이체 환불</b>: 계좌번호 수령 후 이체. 이체 확인증 보관"),
            ("⚠️","<b>자동차보험→건강보험 전환</b>: 보험회사 미승인 시 건강보험으로 전환 수납. 금액 재산정 필수"),
        ])

    sh("🧾 병원급 진료비 영수증 특이 항목")
    items = [
        ("진찰료 (다과 감산)","주된 과 100%, 나머지 과 50% 감산. 세부내역서에 과별로 표시"),
        ("응급의료관리료","응급실 내원 시 추가 부과. 응급·비응급·중증응급 구분에 따라 금액 다름"),
        ("중환자실 입원료","일반 병실보다 2~3배. 중환자실 종류(내과계·외과계·신생아)에 따라 상이"),
        ("DRG 포괄수가","재원일수 무관 정액. 영수증에 포괄수가 표시"),
        ("전원 관련 비용","전원 당일까지 발생한 진료비 정산. 전원 서류 발급비 별도"),
        ("간호·간병 통합서비스","간병인 필요 없는 통합병동. 급여 적용, 본인부담 별도"),
        ("선별급여 항목","일반 급여와 별도 표시. 본인부담 50~80%로 높음"),
        ("비급여","병원 자율 수가. 상급병실 차액·비급여 처치·비급여 검사 포함"),
    ]
    html = ""
    for name,desc in items:
        html += f"""
        <div style='display:flex;gap:12px;padding:9px 0;border-bottom:1px solid #f0f0f0;'>
            <div style='min-width:120px;font-weight:700;color:#2e7d32;font-size:0.83rem;'>{name}</div>
            <div style='font-size:0.83rem;color:#546e7a;'>{desc}</div>
        </div>"""
    st.markdown(f"<div class='card'>{html}</div>", unsafe_allow_html=True)

    sh("🤔 병원급 외래 자주 묻는 질문")
    faqs = [
        ("의원에서 왔는데 왜 비용이 더 비싸요?","병원급은 건강보험법에 따라 외래 본인부담률이 40%로 의원(30%)보다 높게 적용됩니다. 더 전문적이고 다양한 진료와 검사가 가능한 대신 본인부담이 높은 구조입니다."),
        ("오늘 내과·정형외과 둘 다 봤는데 진찰료가 왜 따로 나와요?","각 진료과에서 의사가 별도로 진찰하셨기 때문에 과별로 진찰료가 발생합니다. 다만 두 번째 과 진찰료는 50%만 적용됩니다."),
        ("의뢰서를 안 가져왔는데 다음에 가져오면 소급 적용되나요?","소급 적용은 병원 방침에 따라 다릅니다. 저희 병원은 [방침 확인 후 안내]. 다음 방문 시 의뢰서를 꼭 지참해 주시면 좋겠습니다."),
        ("CT 찍으러 왔다 갔다 해야 하나요?","오늘 CT 촬영 후 결과가 나오는 데 [OO시간] 정도 걸립니다. 당일 결과 확인하실 경우 대기하셔야 하고, 다음 방문 시 확인도 가능합니다. 어떻게 하시겠어요?"),
    ]
    for q,a in faqs:
        st.markdown(f"""
        <div class='qa-box'>
            <div class='qa-q'>❓ {q}</div>
            <div class='qa-a'>💬 {a}</div>
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# STEP 4 — 입원·퇴원
# ══════════════════════════════════════════════

def page_step4():
    render_hero(
        "STEP 4 · 입원·퇴원 프로세스",
        "병원급 입원은 장기화·복잡 수술이 많습니다. 중간 정산·DRG·보증금 관리까지 완전 정복합니다.",
        "3~4주차 완성 목표",
    )

    sh("🏥 입원 수속 전체 흐름")
    flow("의사 입원 결정","입원 오더 확인","외래→입원 인계","병실 배정 협의","동의서 작성","보증금 수납","EMR 입원 등록","병동 인계","보호자 안내")

    sh("📋 입원 수속 체크리스트")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("<b style='color:#1b5e20;'>📄 필수 서류 징구</b>", unsafe_allow_html=True)
        checklist([
            ("✅","입원 동의서 (환자 서명 원칙, 불가 시 보호자)"),
            ("✅","개인정보 수집·이용·제공 동의서"),
            ("✅","병실 선택 확인서 (상급병실 선택 시 비용 명시)"),
            ("✅","수술 동의서 (수술 예정 환자, 의사 설명 후 원무 접수)"),
            ("✅","마취 동의서 (마취과 연계)"),
            ("✅","DRG 선택 동의서 (해당 수술 시, 행위별 vs 포괄)"),
            ("✅","의료급여 수급자증 (해당자)"),
            ("✅","자동차·산재 사고확인서 (해당자)"),
            ("✅","타 병원 진료의뢰서·진료 요약지 (전원 환자)"),
        ])
    with col2:
        st.markdown("<b style='color:#1b5e20;'>🖥️ EMR 등록 항목</b>", unsafe_allow_html=True)
        checklist([
            ("✅","입원일·입원 경로(외래/응급/전원) 정확 입력"),
            ("✅","담당과·주치의 지정"),
            ("✅","병실 등급 (다인실/준상급/상급) 선택"),
            ("✅","DRG 해당 여부 표시 및 선택 내용 입력"),
            ("✅","보증금 수납 금액 입력·영수증 발행"),
            ("✅","보호자 이름·관계·연락처 등록"),
            ("✅","알레르기·낙상 위험·특이사항 간호 인계"),
            ("✅","간호사실 입원 인계 연락"),
        ])
    tip("입원 동의서 미징구는 분쟁 시 병원 불리. 수술 동의서는 반드시 수술 전날까지 완료!", "danger")

    sh("🏨 병원급 병실 등급 & 본인부담 완전 정리")
    st.markdown("""
    <table class='fee-table'>
    <thead><tr><th>병실 유형</th><th>기준</th><th>급여 여부</th><th>환자 부담</th><th>원무 주의사항</th></tr></thead>
    <tbody>
    <tr><td><b>다인실 (6인 이상)</b></td><td>기준 병실</td><td>급여</td><td>입원료 20%</td><td>기본값. 가장 많음</td></tr>
    <tr><td><b>4~5인실</b></td><td>준기준</td><td>급여</td><td>입원료 30%</td><td>병원별 상이</td></tr>
    <tr><td><b>2~3인실</b></td><td>준상급</td><td>선별급여</td><td>차액 50% 부담</td><td>서면 동의서 필수</td></tr>
    <tr><td><b>1인실</b></td><td>상급병실</td><td>비급여</td><td>전액 환자 부담</td><td>구체적 금액 사전 서면 고지 의무</td></tr>
    <tr><td><b>중환자실(ICU)</b></td><td>집중치료</td><td>급여</td><td>20% (일반보다 수가 높음)</td><td>면회 제한·보호자 안내 필수</td></tr>
    <tr><td><b>간호·간병 통합병동</b></td><td>통합서비스</td><td>급여</td><td>별도 수가</td><td>간병인 불필요. 희망자 우선 배정</td></tr>
    </tbody></table>""", unsafe_allow_html=True)
    tip("상급병실 비급여 금액은 일 단위 금액으로 입원 전 명확히 고지. 장기 입원 시 총액 예상액도 안내하면 민원 예방!", "warn")

    sh("💰 장기 입원 중간 정산 — 병원급 핵심 업무")
    tip("병원급은 입원이 길어지는 케이스가 많습니다. 중간 정산을 하지 않으면 퇴원 시 고액 정산으로 민원 발생!", "danger")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>중간 정산 기준 (병원 방침 따름)</b>
        <div style='font-size:0.87rem;color:#37474f;line-height:2.0;margin-top:10px;'>
        · 입원 2주 초과 시 중간 정산 원칙<br>
        · 누적 진료비가 보증금의 80% 초과 시<br>
        · 보호자 요청 시<br>
        · 수술 등 고액 처치 발생 후
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>중간 정산 절차</b>
        <div style='font-size:0.87rem;color:#37474f;line-height:2.0;margin-top:10px;'>
        ① 보호자 연락 또는 병동 직접 방문 안내<br>
        ② 현재까지 누적 진료비 내역 출력<br>
        ③ 보증금 차감 후 추가 납부 또는 보증금 증액<br>
        ④ 수납 후 영수증 발행<br>
        ⑤ EMR 중간 정산 기록
        </div></div>""", unsafe_allow_html=True)

    sh("🚪 퇴원 정산 완전 가이드")
    flow("퇴원 예정 통보 (전날)","전체 입원 진료비 취합","중간 정산액 차감","보증금 차감","최종 추가 납부/환급","정산 완료","퇴원 영수증","서류 발급")

    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>퇴원 정산 계산 예시 (일반 입원 10일)</b>
        <div style='font-size:0.87rem;color:#37474f;line-height:2.2;margin-top:10px;'>
        · 급여 총 진료비: 2,800,000원<br>
        · 입원 본인부담 (20%): 560,000원<br>
        · 식대 본인부담: 100,000원<br>
        · 비급여 (1인실 10일): 500,000원<br>
        <b>───────────────────</b><br>
        · 환자 총 부담: 1,160,000원<br>
        · 중간 정산 기납부: 500,000원<br>
        · 보증금 기납부: 400,000원<br>
        <b style='color:#c62828;'>→ 추가 납부: 260,000원</b>
        </div></div>""", unsafe_allow_html=True)
    with col2:
        tip("퇴원 전날 오후에 예상 정산 금액을 보호자에게 미리 안내하면 당일 혼란·민원을 크게 줄일 수 있습니다.", "tip")
        tip("DRG 수술 환자는 재원일수와 무관하게 정액 적용. 예상보다 일찍 퇴원해도 금액 변동 없음을 사전 안내!", "info")

    sh("📄 퇴원 시 발급 서류 완전 정리")
    checklist([
        ("📃","<b>진료비 영수증·세부내역서</b>: 기본 발급. 5년 내 재발급 가능"),
        ("🏥","<b>입퇴원 확인서</b>: EMR 즉시 출력. 회사 제출·보험 청구용"),
        ("📋","<b>진단서</b>: 의사 작성·서명. 원무는 접수·수납만. 3~7일 소요 사전 안내"),
        ("💊","<b>퇴원 요약지(소견서)</b>: 의사 작성. 전원 시 타 병원 필수 제출"),
        ("🔒","<b>의무기록 사본</b>: 신청서+신분증+위임장. 14일 이내 발급 의무"),
        ("📋","<b>수술 기록지</b>: 의무기록 사본의 일부. 보험사·법원 제출용 多"),
        ("🏥","<b>영상 CD (X-ray·CT·MRI)</b>: 영상의학과 연계. 별도 비용 발생 가능"),
        ("💊","<b>퇴원 처방전</b>: 퇴원 시 처방한 약 원외처방전. 약국에서 조제"),
    ])


# ══════════════════════════════════════════════
# STEP 5 — 전원·응급·중환자
# ══════════════════════════════════════════════

def page_step5():
    render_hero(
        "STEP 5 · 전원·응급·중환자 프로세스",
        "병원급 원무에만 있는 업무 — 응급실 수납, 타 병원 전원 서류, 야간 당직 대응을 완벽 정리합니다.",
        "4~5주차 완성 목표",
    )

    sh("🚑 응급실 수납 프로세스")
    tip("응급실은 수납보다 치료가 먼저입니다. 환자 안정 후 수납 진행이 원칙.", "warn")
    flow("응급 내원","중증도 분류(트리아지)","응급 등록","진료·처치","안정 확인","수납 진행","입원 or 귀가","서류 발급")

    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>응급의료관리료 구분</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;'>
        <table style='width:100%;font-size:0.82rem;border-collapse:collapse;'>
        <tr style='background:#e8f5e9;'><th style='padding:7px;text-align:left;'>구분</th><th style='padding:7px;'>수가 수준</th></tr>
        <tr><td style='padding:7px;'>중증응급 (1·2등급)</td><td style='padding:7px;font-weight:700;color:#c62828;'>최고</td></tr>
        <tr style='background:#f5fff5;'><td style='padding:7px;'>응급 (3등급)</td><td style='padding:7px;font-weight:700;color:#e65100;'>중간</td></tr>
        <tr><td style='padding:7px;'>비응급 (4·5등급)</td><td style='padding:7px;font-weight:700;color:#1b5e20;'>낮음</td></tr>
        </table>
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>응급 수납 특수 케이스</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;line-height:2.0;'>
        · <b>신원 불명 환자</b>: 무연고자 처리. 신원 확인 후 소급 적용<br>
        · <b>의식 없는 환자</b>: 보호자 동의서 대리 서명<br>
        · <b>미성년자 단독 내원</b>: 보호자 연락 후 동의 확인<br>
        · <b>자살 시도 환자</b>: 정신건강 관련 별도 프로토콜<br>
        · <b>외국인 환자</b>: 여권·외국인등록증 확인
        </div></div>""", unsafe_allow_html=True)

    sh("🔄 전원(타 병원 이송) 프로세스")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>📤 우리 병원 → 타 병원으로 보내는 경우</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;'>
        <b>원무 역할</b>
        </div>""", unsafe_allow_html=True)
        checklist([
            ("✅","전원 동의서 징구 (환자 또는 보호자 서명)"),
            ("✅","현재까지 발생 진료비 정산"),
            ("✅","진료비 영수증·세부내역서 발급"),
            ("✅","전원 서류 패키지 준비: 의무기록 요약·영상 CD·처방 목록"),
            ("✅","수신 병원 원무팀에 연락·서류 팩스 전송"),
            ("✅","구급차 이송 비용 안내 (비급여 가능)"),
        ])
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#01579b;'>📥 타 병원 → 우리 병원으로 오는 경우</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;'>
        <b>원무 역할</b>
        </div>""", unsafe_allow_html=True)
        checklist([
            ("✅","전원 의뢰서·진료 요약지 수령 확인"),
            ("✅","기존 병원 영상 CD·검사 결과 인수"),
            ("✅","보험 자격 재조회 (전원 당일 기준)"),
            ("✅","응급 전원 시 수납 절차 후순위로 진행"),
            ("✅","입원 오더 확인 후 입원 수속 진행"),
            ("✅","전원 서류 EMR 스캔·등록"),
        ])
        st.markdown("</div>", unsafe_allow_html=True)

    sh("🌙 야간·주말 당직 원무 업무")
    tip("야간 당직은 혼자 외래·입원·응급 모든 업무를 담당합니다. 사전에 반드시 당직 업무 범위를 파악하세요.", "warn")
    checklist([
        ("🌙","<b>야간 수납 범위</b>: 응급 수납·응급 입원 수속·긴급 서류 발급이 주 업무"),
        ("📞","<b>당직 연락 체계</b>: 팀장·원장·IT·경비 비상 연락처 숙지"),
        ("💰","<b>야간 현금 수납</b>: 야간 금고 보관 절차 숙지. 고액 현금은 분리 보관"),
        ("📋","<b>야간 서류 발급</b>: 입퇴원 확인서·응급 관련 서류만 발급. 진단서는 의사 출근 후"),
        ("🚨","<b>응급 상황 발생</b>: 의사·간호사 즉시 연락. 원무는 동선 확보·보호자 안내"),
        ("📝","<b>야간 인계</b>: 다음날 주간 근무자에게 미수금·특이사항 인계장 작성"),
        ("⚠️","<b>야간 가산</b>: 야간·공휴일 접수 시 진찰료 가산 자동 적용 여부 EMR 확인"),
    ])

    sh("🏥 중환자실(ICU) 관련 원무 업무")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>중환자실 수납 특이사항</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;line-height:2.0;'>
        · 중환자실 입원료는 일반 병실보다 2~3배 높음<br>
        · 처치료·약제료도 고가 항목 다수<br>
        · <b>중간 정산 필수</b>: 장기 ICU 입원 시 주 1회 이상 정산 권고<br>
        · 보증금 부족 시 즉시 보호자 연락<br>
        · 산정특례 환자 ICU: 5% 본인부담 적용
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>중환자실 보호자 안내</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;line-height:2.0;'>
        · 면회 시간·인원 제한 안내 (병원 방침)<br>
        · 보호자 대기 공간 안내<br>
        · 비용 관련 문의는 원무팀 창구 안내<br>
        · 보호자 연락처 24시간 연락 가능 여부 확인<br>
        · 긴급 연락 시 보호자 여러 명 등록 권고
        </div></div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# STEP 6 — 서류 발급 & 민원 대응
# ══════════════════════════════════════════════

def page_step6():
    render_hero(
        "STEP 6 · 서류 발급 & 민원 대응",
        "병원급은 서류 종류가 많고 보험회사 직접 청구·복잡 민원이 잦습니다. 유형별로 완벽 대응합니다.",
        "5~6주차 완성 목표",
    )

    sh("📄 서류 유형별 발급 가이드")
    docs = [
        ("진료비 영수증·세부내역서","즉시","·수납 즉시 발급\n·재발급: 5년 이내\n·실손보험 청구 필수\n·팩스·이메일 발송 가능","✅ 즉시"),
        ("입퇴원 확인서","즉시","·EMR 자동 출력\n·입원 기간·병명 기재\n·용도 기재란 있음\n·의사 서명 필요 여부 확인","✅ 즉시"),
        ("진단서","3~7일","·의사 직접 작성·서명\n·발급비 수납 후 교부\n·소요기간 반드시 안내\n·용도별 양식 다를 수 있음","⏳ 3~7일"),
        ("의무기록 사본","14일 이내","·신청서+신분증+위임장\n·법정 14일 이내 발급\n·전자 신청 가능 여부 확인\n·복사비 별도","📅 14일"),
        ("영상 CD (CT·MRI 등)","즉시~1일","·영상의학과 연계\n·CD 발급비 별도\n·타 병원 전원 시 필수\n·DICOM 형식","📀 즉시~1일"),
        ("수술 기록지","의무기록 포함","·의무기록 사본에 포함\n·보험사·법원 제출용\n·본인 확인 동일 절차","📋 포함"),
        ("보험사 서류","즉시~7일","·실손: 영수증+세부내역서+진단서\n·자동차: 별도 청구서 양식\n·생명보험: 진단서 중심\n·보험회사 직접 팩스 발송 가능","📋 혼합"),
        ("장애진단서","7~14일","·의사 작성\n·장애 유형별 양식 다름\n·읍면동 제출용\n·방문 전 양식 확인 요청","⏳ 7~14일"),
    ]
    for i in range(0,len(docs),2):
        col1,col2 = st.columns(2)
        for col,(name,period,desc,badge) in zip([col1,col2],docs[i:i+2]):
            badge_color = "#e8f5e9" if "즉시" in badge else "#fff3e0" if "혼합" in badge else "#e3f2fd"
            badge_tc = "#2e7d32" if "즉시" in badge else "#e65100" if "혼합" in badge else "#1565c0"
            col.markdown(f"""
            <div class='card'>
                <div style='display:flex;justify-content:space-between;align-items:flex-start;'>
                    <b style='color:#1b5e20;'>📄 {name}</b>
                    <span style='background:{badge_color};color:{badge_tc};border-radius:8px;padding:2px 10px;font-size:0.75rem;font-weight:700;'>{badge}</span>
                </div>
                <div style='font-size:0.83rem;color:#546e7a;margin-top:10px;white-space:pre-line;line-height:1.9;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    sh("🚗 자동차보험·산재 보험회사 직접 청구")
    tip("병원급은 자동차보험·산재 환자가 많습니다. 보험회사 직접 청구 절차를 반드시 숙지하세요.", "warn")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>🚗 자동차보험 직접 청구 절차</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;'>""", unsafe_allow_html=True)
        checklist([
            ("1️⃣","사고확인서·보험회사 정보 환자로부터 수령"),
            ("2️⃣","보험회사 담당자 연락 후 치료 승인 확인"),
            ("3️⃣","보험사 양식으로 진료비 청구서 작성"),
            ("4️⃣","필요 서류(진단서·세부내역서·의무기록) 첨부"),
            ("5️⃣","팩스 또는 보험사 포털로 청구 전송"),
            ("6️⃣","입금 확인 후 환자에게 정산 완료 통보"),
        ])
        st.markdown("</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#01579b;'>🔨 산재보험 청구 절차</b>
        <div style='font-size:0.87rem;color:#37474f;margin-top:10px;'>""", unsafe_allow_html=True)
        checklist([
            ("1️⃣","근로복지공단 산재 승인 여부 먼저 확인"),
            ("2️⃣","승인 전: 건강보험으로 임시 처리 후 승인 후 전환"),
            ("3️⃣","산재 지정 양식으로 요양급여 청구서 작성"),
            ("4️⃣","근로복지공단 관할 지사로 청구"),
            ("5️⃣","산재 환자 본인부담 없음 (승인 범위 내)"),
            ("6️⃣","요양 기간 연장 시 재승인 필요"),
        ])
        st.markdown("</div></div>", unsafe_allow_html=True)

    sh("😤 병원급 민원 대응 — 복잡 케이스 스크립트")
    tabs = st.tabs(["💬 수납 금액 불만","🏥 병실 배정 불만","⏰ 대기·진료 불만","📋 서류 지연","🔥 고성·폭언"])

    with tabs[0]:
        st.markdown("""
        <div class='scenario-box'>
        <b>시나리오</b>: "의원에서는 3만원 나왔는데 여기는 왜 8만원이에요? 똑같은 주사인데!"
        </div>""", unsafe_allow_html=True)
        checklist([
            ("1️⃣","공감: '금액 차이가 크게 느껴지셨겠어요. 세부내역서를 함께 확인해 드릴게요.'"),
            ("2️⃣","<b>본인부담률 차이 설명</b>: '의원은 30%, 저희 병원급은 40%가 적용되어 같은 진료라도 차이가 납니다.'"),
            ("3️⃣","항목별 차이 설명: 추가 검사·처치 항목 있으면 세부내역서로 확인"),
            ("4️⃣","진료의뢰서 안내: '다음에는 의원 의뢰서를 가져오시면 도움이 될 수 있습니다.'"),
            ("5️⃣","해결 불가 시 팀장 연결"),
        ])
        tip("병원급 외래 40% vs 의원 30% 차이는 자주 나오는 민원입니다. 설명을 암기해두세요.", "info")

    with tabs[1]:
        st.markdown("""
        <div class='scenario-box'>
        <b>시나리오</b>: "왜 6인실이에요? 저는 2인실 달라고 했잖아요!"
        </div>""", unsafe_allow_html=True)
        checklist([
            ("1️⃣","현재 병실 상황 간호부에 즉시 확인"),
            ("2️⃣","'현재 2인실이 모두 사용 중이어서 우선 다인실로 배정됐습니다. 대기 명단에 등록해 드리겠습니다.'"),
            ("3️⃣","대기 순서 안내: '2인실 빌 경우 바로 연락드리겠습니다.'"),
            ("4️⃣","비용 차이 안내: '2인실 이동 시 하루 OO원 차액이 발생합니다.'"),
            ("5️⃣","병실 이동 시 간호부와 협의 후 EMR 즉시 변경"),
        ])

    with tabs[2]:
        checklist([
            ("1️⃣","진료과 현황 파악 후 정확한 예상 시간 안내 (임의로 줄여 말하지 않기)"),
            ("2️⃣","다과 방문 시 과별 대기 순서 명확히 안내"),
            ("3️⃣","검사 대기: '검사실 상황에 따라 대기가 발생할 수 있습니다. 번호 남기시면 연락드릴게요.'"),
            ("4️⃣","반복 민원 → 팀장 보고 후 진료과에 일정 조율 건의"),
        ])

    with tabs[3]:
        checklist([
            ("1️⃣","신청 날짜·서류 종류 EMR 즉시 조회"),
            ("2️⃣","의사 서명 필요 서류: 담당 의사 스케줄 확인"),
            ("3️⃣","법정 기한 (의무기록 14일) 안내"),
            ("4️⃣","완성 예정일 확정 후 연락 약속"),
            ("5️⃣","법원·보험사 제출 기한 있는 경우: 팀장 보고 후 우선 처리"),
        ])

    with tabs[4]:
        st.markdown("""
        <div class='danger-box'>
        <b>🚨 병원급은 보안 인력·CCTV가 있습니다. 혼자 감당하려 하지 마세요.</b>
        </div>""", unsafe_allow_html=True)
        checklist([
            ("1️⃣","낮고 침착한 목소리로: '차분히 말씀해 주시면 최선을 다해 도와드리겠습니다.'"),
            ("2️⃣","반복 폭언 → 즉시 팀장·보안 요원 호출"),
            ("3️⃣","물리적 위협 → 112 신고. 보안 요원에게도 즉시 연락"),
            ("4️⃣","CCTV 녹화 중임을 자연스럽게 인지시키기"),
            ("5️⃣","상황 종료 후 경위서 작성. 의료법 제12조 위반 고소 가능"),
        ])


# ══════════════════════════════════════════════
# STEP 7 — 환자 커뮤니케이션
# ══════════════════════════════════════════════

def page_step7():
    render_hero(
        "STEP 7 · 환자 커뮤니케이션",
        "병원급은 다과 동시 응대·보호자 안내·콜센터 연계 등 커뮤니케이션 채널이 복잡합니다.",
        "상시 업무",
    )

    sh("🗣️ 병원급 커뮤니케이션 특성")
    st.markdown("""
    <div class='card'>
    <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;'>
        <div style='background:#e8f5e9;border-radius:10px;padding:14px;text-align:center;'>
            <div style='font-size:1.5rem;'>👥</div>
            <b style='color:#1b5e20;font-size:0.9rem;'>다과 동시 안내</b>
            <div style='font-size:0.8rem;color:#546e7a;margin-top:6px;line-height:1.7;'>여러 진료과 방문 환자에게 과별 순서·위치·검사 흐름을 명확히 안내</div>
        </div>
        <div style='background:#e3f2fd;border-radius:10px;padding:14px;text-align:center;'>
            <div style='font-size:1.5rem;'>👨‍👩‍👧</div>
            <b style='color:#01579b;font-size:0.9rem;'>보호자 커뮤니케이션</b>
            <div style='font-size:0.8rem;color:#546e7a;margin-top:6px;line-height:1.7;'>입원 비용·중간 정산·병실 배정·퇴원 일정을 보호자와 적극 소통</div>
        </div>
        <div style='background:#fff3e0;border-radius:10px;padding:14px;text-align:center;'>
            <div style='font-size:1.5rem;'>📞</div>
            <b style='color:#e65100;font-size:0.9rem;'>콜센터·창구 병행</b>
            <div style='font-size:0.8rem;color:#546e7a;margin-top:6px;line-height:1.7;'>콜센터 운영 병원은 창구와 전화 응대 역할 분담 파악 필수</div>
        </div>
    </div></div>""", unsafe_allow_html=True)

    sh("📞 병원급 전화 응대 완전 가이드")
    tabs = st.tabs(["📞 기본 전화 응대","📅 예약·변경","💰 수납 문의","🏥 입원 관련","📄 서류 문의"])

    with tabs[0]:
        checklist([
            ("✅","수신 즉시: '안녕하세요, OO병원 원무팀 OOO입니다.'"),
            ("✅","콜센터 연계 여부 확인: 일부 병원은 콜센터→원무 연결 구조. 연결 시 '연결되었습니다' 인사"),
            ("✅","메모 준비: 이름·연락처·내용 메모 후 환자 이름 재확인"),
            ("✅","모르면 확인 후 연락: '확인 후 OO분 이내 연락드리겠습니다.'"),
            ("✅","마무리: '감사합니다. 빠른 쾌유 바랍니다.'"),
        ])
    with tabs[1]:
        checklist([
            ("1️⃣","'예약 도와드리겠습니다. 성함과 생년월일 확인해도 될까요?'"),
            ("2️⃣","'어떤 진료과·어떤 증상으로 오실 예정인가요?'"),
            ("3️⃣","의뢰서 유무 확인: '타 병원 의뢰서 있으신가요? 있으시면 지참해 주세요.'"),
            ("4️⃣","이전 방문 여부 확인: 기존 환자 번호 조회 후 예약 등록"),
            ("5️⃣","'OO일 OO시 OO과 예약되셨습니다. 10분 전 도착해 주세요.'"),
            ("6️⃣","검사 예약 시: '검사 전 금식 여부' 등 주의사항 안내 (간호부 확인 후)"),
        ])
    with tabs[2]:
        checklist([
            ("✅","환자명·생년월일 확인 후 EMR 조회"),
            ("✅","'어떤 날짜 진료 건 문의하세요?' 날짜 특정"),
            ("✅","세부내역서 팩스·이메일 발송 요청: 수령 정보 확인 후 발송"),
            ("⚠️","전화로 정확한 금액만 안내. '대략'이나 '아마도' 표현 금지"),
            ("✅","보험 청구 관련 서류: '어떤 보험 종류인지 먼저 확인해 주시겠어요?' 후 안내"),
        ])
    with tabs[3]:
        checklist([
            ("✅","입원 중 보호자 연락: '현재 입원 중이신 OOO 보호자님 맞으신가요?'"),
            ("✅","중간 정산 연락: '입원 진료비가 OO만원 발생했습니다. 방문하셔서 정산 부탁드립니다.'"),
            ("✅","퇴원 안내: '내일 퇴원 예정이시며 예상 정산 금액은 OO만원입니다.'"),
            ("⚠️","전화로 진료 정보 제공 시 보호자 확인 필수 (개인정보 보호)"),
        ])
    with tabs[4]:
        checklist([
            ("✅","'어떤 서류가 필요하신가요?' 정확한 서류명 확인"),
            ("✅","발급 가능 여부·소요기간 안내"),
            ("✅","'직접 방문하시거나 대리인 신청 시 위임장이 필요합니다.'"),
            ("✅","팩스 발송 가능 여부: '팩스 번호 알려주시면 발송해 드리겠습니다.'"),
        ])

    sh("👴 특수 환자 응대 가이드")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='card'>
        <b style='color:#1b5e20;'>👴 고령 환자</b>
        <div style='font-size:0.83rem;color:#37474f;margin-top:10px;line-height:2.0;'>
        · 말 천천히, 또렷하게<br>
        · 금액 숫자 큰 글씨로 써서 보여주기<br>
        · 다과 방문 시 어디로 가야 하는지 지도·안내 표지 함께 설명<br>
        · 보호자 동반 시 보호자에게도 동일 안내<br>
        · 노인 진찰료 감면 자동 적용 확인<br>
        · 산정특례·장기요양 등록 여부 확인
        </div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <b style='color:#01579b;'>🌍 외국인 환자</b>
        <div style='font-size:0.83rem;color:#37474f;margin-top:10px;line-height:2.0;'>
        · 여권·외국인등록증으로 확인<br>
        · 건강보험 가입 여부 자격 조회<br>
        · 미가입 외국인: 전액 비급여<br>
        · 기본 영어 안내 표현 숙지<br>
        · 통역 앱(파파고) 적극 활용<br>
        · 영문 영수증 발급 가능 여부 확인<br>
        · 지역 외국인지원센터 연락처 비치
        </div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='card'>
        <b style='color:#c62828;'>♿ 장애인·거동 불편</b>
        <div style='font-size:0.83rm;color:#37474f;margin-top:10px;line-height:2.0;'>
        · 장애인 편의시설 위치 안내<br>
        · 장애인 본인부담 감면 여부 확인<br>
        · 청각장애: 필담·수어통역사 요청<br>
        · 시각장애: 소리로 명확히 안내<br>
        · 휠체어: 창구에서 직접 나가서 안내<br>
        · 독거·보호자 없는 환자: 사회복지사 연계
        </div></div>""", unsafe_allow_html=True)

    sh("💆 감정노동 관리")
    checklist([
        ("🛡️","<b>감정 분리</b>: 환자의 화는 나를 향한 것이 아닌 상황에 대한 것. '나는 잘못이 없다' 인식"),
        ("💬","<b>동료 디브리핑</b>: 힘든 상황 후 동료·팀장에게 말하기. 혼자 삭이면 번아웃"),
        ("📋","<b>클레임 기록</b>: 반복 민원 환자 기록 후 팀장 보고. 대응 방침 공유"),
        ("🏥","<b>병원 지원 요청</b>: 감당 안 되면 즉시 상급자에게 지원 요청"),
        ("🧘","<b>퇴근 후 분리</b>: 업무는 퇴근과 함께. 집에서 업무 걱정 최소화"),
        ("📞","<b>EAP 활용</b>: 병원에서 운영하는 직원 상담 프로그램(EAP) 있으면 적극 활용"),
    ])


# ══════════════════════════════════════════════
# 용어 사전
# ══════════════════════════════════════════════

def page_terms():
    render_hero(
        "빠른 참조 — 병원급 필수 용어 사전",
        "병원급 원무 업무에서 반드시 알아야 할 핵심 용어 20개를 검색할 수 있습니다.",
        "상시 참조",
    )
    search = st.text_input("🔍 용어 검색", placeholder="예: DRG, 전원, 중환자실, 응급...")
    filtered = TERMS if not search else [
        t for t in TERMS if search in t[0] or search in t[2]
    ]
    if not filtered:
        st.info("검색 결과가 없습니다. 다른 키워드로 검색해 보세요.")
    else:
        for name,eng,definition in filtered:
            st.markdown(f"""
            <div class='term-card'>
                <div class='term-name'>{name} <span class='term-eng'>({eng})</span></div>
                <div class='term-def'>{definition}</div>
            </div>""", unsafe_allow_html=True)
    st.markdown(f"<div style='color:#9e9e9e;font-size:0.82rem;margin-top:10px;'>총 {len(filtered)}개 용어 표시</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 긴급 상황 대응
# ══════════════════════════════════════════════

def page_emergency():
    render_hero(
        "긴급 상황 대응 매뉴얼",
        "병원급 특유의 긴급 상황 — 전원·응급·야간 대응까지 미리 읽어두고 즉시 행동하세요.",
        "응급 대응",
    )

    sh("🚨 병원급 원무 긴급 상황 대응")
    emergencies = [
        ("🖥️ EMR 시스템 다운",[
            "IT 담당자·원무팀장 즉시 연락 (내선번호 항상 숙지)",
            "수기 접수 용지·수납 장부 즉시 꺼내기 (창구 서랍 항시 비치)",
            "환자에게 '시스템 장애 복구 중, 잠시 대기' 안내",
            "응급 환자는 수기 접수 후 수납은 복구 후 처리",
            "복구 후 수기 처리 내역 전부 EMR 일괄 입력 확인",
        ]),
        ("🔍 건강보험 자격 조회 실패",[
            "주민번호 재확인 후 재조회",
            "공단 고객센터(1577-1000) 전화 자격 확인",
            "조회 불가 → 비급여 임시 수납 후 사후 정산 설명",
            "의료급여 자격 조회 실패: 주민센터·사회보장정보원(1566-0009) 확인",
            "자동차·산재 보험 확인 불가: 보험회사 직접 전화 확인",
        ]),
        ("🚑 원내 응급 상황 (쓰러짐·심정지 등)",[
            "즉시 '원내 코드블루(코드 확인)' 방송 또는 의료진 긴급 호출",
            "119 신고 (필요 시) — 동시에 의료진 알림",
            "원무는 동선 확보, AED 위치 안내, 보호자 연락",
            "응급 처치는 의료진에게. 원무는 절대 의료 행위 하지 않음",
            "응급 이송 결정 시 전원 서류 준비 지원",
        ]),
        ("🔄 긴급 전원 요청",[
            "전원 동의서 즉시 징구 (환자 불가 시 보호자)",
            "현재까지 진료비 신속 정산",
            "진료 요약지·영상 CD 의무기록팀과 즉시 협조",
            "수신 병원 원무팀·응급실에 환자 정보 팩스·전화 전달",
            "구급차 수배 (병원 방침 따름) 및 이송 비용 안내",
        ]),
        ("💰 고액 정산 거부 민원",[
            "환자·보호자를 조용한 상담실로 안내",
            "세부내역서 출력 후 항목별 함께 검토",
            "중간 정산 기납부 내역 확인 및 설명",
            "분할 납부 가능 여부 팀장 확인 (병원 방침)",
            "이의 유지 시 건강보험공단(1577-1000) 또는 의료분쟁조정중재원 안내",
        ]),
        ("🌙 야간 당직 중 응급 입원",[
            "응급실로부터 입원 오더 수령 확인",
            "야간 병실 배정: 당직 간호사와 협의",
            "보호자에게 입원 수속 안내 (동의서는 익일 완비 가능 여부 확인)",
            "응급 보증금 수납 or 익일 납부 병원 방침 확인",
            "야간 인계장에 응급 입원 내용 기록 후 주간 인계",
        ]),
        ("🔒 개인정보 유출 의심",[
            "즉시 원무팀장·원장 보고",
            "유출 범위(이름·주민번호·진료기록 등) 신속 파악",
            "72시간 이내 개인정보보호위원회 신고 의무",
            "해당 환자 개별 통보 의무 (내용증명 권고)",
            "개인정보보호위원회(118) 신고",
        ]),
        ("😡 환자·보호자 폭력·폭언",[
            "침착하게: '차분히 말씀해 주시면 도와드리겠습니다.'",
            "반복 폭언 → 즉시 팀장·보안 요원 호출",
            "물리적 위협 → 112 신고 + 보안 요원 긴급 호출",
            "상황 종료 후 경위서 작성·보관",
            "의료법 제12조 위반 — 고소·고발 가능. 원장과 상의",
        ]),
    ]
    for title,steps in emergencies:
        with st.expander(f"{title}"):
            for i,step in enumerate(steps,1):
                st.markdown(f"""
                <div style='display:flex;gap:12px;padding:9px 0;align-items:flex-start;border-bottom:1px solid #f0f0f0;'>
                    <div style='min-width:26px;height:26px;background:linear-gradient(135deg,#2e7d32,#43a047);color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:700;flex-shrink:0;'>{i}</div>
                    <div style='font-size:0.88rem;color:#37474f;line-height:1.7;'>{step}</div>
                </div>""", unsafe_allow_html=True)

    sh("📞 병원급 원무 필수 연락처")
    contacts = [
        ("🏥","건강보험공단 고객센터","1577-1000","자격 조회·민원·환급"),
        ("🔨","근로복지공단 (산재)","1588-0075","산재 승인·청구"),
        ("🚑","응급의료정보센터","1339","응급환자 이송·병원"),
        ("🔒","개인정보 침해 신고","118","개인정보보호위원회"),
        ("⚖️","의료분쟁조정중재원","1670-2545","의료분쟁 조정"),
        ("🏛️","국민권익위원회","1398","의료 민원·공익신고"),
        ("👮","경찰 (폭력·위협)","112","원내 폭력 상황"),
        ("🚒","소방·응급","119","응급환자·화재"),
    ]
    col1,col2 = st.columns(2)
    for i,(icon,name,number,desc) in enumerate(contacts):
        col = col1 if i%2==0 else col2
        col.markdown(f"""
        <div style='background:white;border-radius:12px;padding:14px 18px;margin-bottom:12px;border:1px solid #e8f5e9;display:flex;gap:12px;align-items:center;'>
            <div style='font-size:1.4rem;'>{icon}</div>
            <div>
                <div style='font-weight:700;color:#1b5e20;font-size:0.9rem;'>{name}</div>
                <div style='color:#2e7d32;font-weight:700;font-size:1.1rem;'>{number}</div>
                <div style='color:#9e9e9e;font-size:0.78rem;'>{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    tip("비상 연락처는 창구 모니터 옆에 라미네이팅해서 붙여두세요. 당직 중 검색할 시간이 없습니다.", "tip")


# ══════════════════════════════════════════════
# 사이드바 & 라우터
# ══════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:20px 0 10px;'>
        <div style='font-size:2.5rem;'>🏨</div>
        <div style='font-family:Gmarket Sans,sans-serif;font-size:1.05rem;font-weight:700;color:#e8f5e9;'>원무 온보딩 가이드</div>
        <div style='font-size:0.8rem;color:#a5d6a7;margin-top:4px;'>병원급 (30~300병상) 전용</div>
    </div>
    <hr style='border-color:rgba(255,255,255,0.15);margin:10px 0 18px;'>
    """, unsafe_allow_html=True)

    selected_label = st.radio("메뉴 선택", list(MENU_ITEMS.keys()), label_visibility="collapsed")
    page = MENU_ITEMS[selected_label]

    st.markdown("""
    <hr style='border-color:rgba(255,255,255,0.15);margin:20px 0 14px;'>
    <div style='font-size:0.78rem;color:#81c784;padding:0 4px;line-height:1.8;'>
    💡 <b style='color:#a5d6a7;'>학습 순서 Tip</b><br>
    STEP 1→7 순서로 따라가면<br>
    병원급 업무 흐름이 잡힙니다.<br><br>
    📌 의원급 가이드와 함께 비교하며<br>
    &nbsp;&nbsp;&nbsp;&nbsp;차이점을 파악하세요.
    </div>""", unsafe_allow_html=True)

PAGE_MAP = {
    "home":      page_home,
    "step1":     page_step1,
    "step2":     page_step2,
    "step3":     page_step3,
    "step4":     page_step4,
    "step5":     page_step5,
    "step6":     page_step6,
    "step7":     page_step7,
    "terms":     page_terms,
    "emergency": page_emergency,
}
PAGE_MAP[page]()

st.markdown("""
<div style='text-align:center;padding:40px 0 20px;color:#a5d6a7;font-size:0.82rem;'>
    🏨 원무 온보딩 가이드 [병원급] · 병원 개원 & 경영 컨설팅 지원 도구<br>
    <span style='font-size:0.75rem;color:#bdbdbd;'>본 가이드는 교육 목적으로 제작되었습니다. 수가 기준은 심평원 고시를 최우선으로 따르세요.</span>
</div>
""", unsafe_allow_html=True)
