#!/usr/bin/env python3
"""Build the website's current academic CV PDF."""

from pathlib import Path
import shutil

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    CondPageBreak,
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Yulong_Liu_CV_2026.pdf"
WEB_PDF = ROOT / "assets" / "pdf" / "Yulong_CV2026_V2.pdf"
ROOT_PDF = ROOT / "Yulong_CV2026_V2.pdf"

INK = colors.HexColor("#1D201B")
MUTED = colors.HexColor("#62665E")
ACCENT = colors.HexColor("#A63F2C")
LIGHT = colors.HexColor("#DDD7CD")
PAPER = colors.HexColor("#FFFDFC")


def styles():
    sheet = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=sheet["Normal"],
            fontName="Times-Bold",
            fontSize=27,
            leading=27,
            textColor=INK,
            spaceAfter=3,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=sheet["Normal"],
            fontName="Helvetica",
            fontSize=8.3,
            leading=11,
            textColor=MUTED,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=sheet["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=10,
            textColor=ACCENT,
            spaceBefore=9,
            spaceAfter=5,
            keepWithNext=True,
            uppercase=True,
        ),
        "entry": ParagraphStyle(
            "Entry",
            parent=sheet["Normal"],
            fontName="Helvetica",
            fontSize=8.7,
            leading=11.5,
            textColor=INK,
            spaceAfter=2.5,
        ),
        "entry_small": ParagraphStyle(
            "EntrySmall",
            parent=sheet["Normal"],
            fontName="Helvetica",
            fontSize=8.1,
            leading=10.4,
            textColor=INK,
            spaceAfter=2.2,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=sheet["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10.5,
            textColor=MUTED,
        ),
        "date": ParagraphStyle(
            "Date",
            parent=sheet["Normal"],
            fontName="Helvetica-Bold",
            fontSize=7.7,
            leading=10,
            textColor=MUTED,
            alignment=TA_RIGHT,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=sheet["Normal"],
            fontName="Helvetica",
            fontSize=8.15,
            leading=10.6,
            leftIndent=10,
            firstLineIndent=-7,
            textColor=INK,
            spaceAfter=1.8,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=sheet["Normal"],
            fontName="Helvetica",
            fontSize=7,
            leading=8,
            textColor=MUTED,
        ),
    }


STYLES = styles()


def p(text, style="entry"):
    return Paragraph(text, STYLES[style])


def section(title):
    return [
        CondPageBreak(0.58 * inch),
        Paragraph(title.upper(), STYLES["section"]),
        HRFlowable(width="100%", thickness=0.55, color=LIGHT, spaceAfter=5),
    ]


def dated_entry(title, date, meta=None):
    left = [p(title)]
    if meta:
        left.append(p(meta, "meta"))
    table = Table(
        [[left, p(date, "date")]],
        colWidths=[6.02 * inch, 0.95 * inch],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return table


def bullet(text):
    return Paragraph(f"- {text}", STYLES["bullet"])


def page_decor(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.45)
    canvas.line(doc.leftMargin, 0.39 * inch, LETTER[0] - doc.rightMargin, 0.39 * inch)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.24 * inch, "Yulong Liu - Curriculum Vitae")
    page = str(doc.page)
    canvas.drawRightString(LETTER[0] - doc.rightMargin, 0.24 * inch, page)
    canvas.restoreState()


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.52 * inch,
        title="Yulong Liu - Curriculum Vitae",
        author="Yulong Liu",
        subject="Academic curriculum vitae",
    )

    story = []

    header = Table(
        [
            [
                Paragraph("Yulong Liu", STYLES["name"]),
                Paragraph(
                    '<a href="mailto:yl3825@cornell.edu" color="#A63F2C">yl3825@cornell.edu</a><br/>'
                    '<a href="https://yulongggggg.github.io/yulong_website/" color="#A63F2C">Personal website</a>  |  '
                    '<a href="https://www.linkedin.com/in/yulong-liu-19451a322/" color="#A63F2C">LinkedIn</a>',
                    ParagraphStyle("ContactRight", parent=STYLES["contact"], alignment=TA_RIGHT),
                ),
            ]
        ],
        colWidths=[3.4 * inch, 3.57 * inch],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.extend([header, Spacer(1, 5), HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=4)])

    story.extend(section("Research Interests"))
    story.append(p("Computational Geomechanics  |  Poromechanics  |  Reservoir Simulation  |  Scientific Machine Learning"))

    story.extend(section("Education"))
    story.append(
        dated_entry(
            "<b>Ph.D. in Earth Science</b> - Cornell University",
            "2024 - Present",
            "Minors: Computer Science and Scientific Computing",
        )
    )
    story.append(dated_entry("<b>B.S. in Mining Engineering</b> - Northeastern University (China)", "2024"))

    story.extend(section("Research Experience"))
    story.append(
        dated_entry(
            "<b>Ph.D. Student</b> - Department of Earth and Atmospheric Sciences, Cornell University",
            "Aug. 2024 - Present",
            "Advisor: Chloé Arson | Ithaca, New York",
        )
    )
    story.append(
        p(
            "<i>Computational geomechanics and poromechanics for coupled multiphysics problems in subsurface and reservoir systems, supported by physics-based and machine-learning surrogate modeling.</i>",
            "entry_small",
        )
    )
    for text in [
        "Develop coupled poromechanics and computational geomechanics models of subsurface and reservoir systems in the MOOSE finite element framework, including hydraulic fracturing and geothermal injection-production.",
        "Build physics-informed neural networks, implicit neural representations, and operator-learning surrogates for geometry-aware and physics-aware prediction at a fraction of full simulation cost.",
        "Study multiscale transport in porous media through homogenization theory and investigate AI-driven discovery of interpretable upscaled permeability laws.",
        "Lead cross-institution work on PDE-grounded verification of the physical correctness of LLM-generated multiphysics simulation code.",
    ]:
        story.append(bullet(text))

    story.append(Spacer(1, 3))
    story.append(
        dated_entry(
            "<b>Undergraduate Researcher</b> - Northeastern University (China)",
            "Sep. 2020 - Jun. 2024",
            "B.S. in Mining Engineering | Shenyang, China",
        )
    )
    for text in [
        "Conducted research in mining geomechanics spanning hydraulic fracturing, triaxial rock testing, tunnel boring machines, and AI-driven microseismic processing.",
        "Developed a unified deep-learning model for microseismic signal classification and arrival-time picking; received the Outstanding Thesis Award.",
    ]:
        story.append(bullet(text))

    story.extend(section("Research Support and Computational Allocations"))
    support_entries = [
        (
            "<b>Learned Uncertainty-Propagation and World Models for Enhanced Geothermal Reservoirs</b>",
            "2026",
            "National Science Foundation (NSF), ACCESS program - Awarded. Student lead: Y. Liu; Advisor: C. Arson. Total allocation and Arson group share: 1.5M CPU hours.",
        ),
        (
            "<b>AI-aided Computational Geomechanics</b>",
            "2026",
            "Empire AI Alpha+Beta - Awarded. PIs: Y.C. Han, Y. Liu, A. Tristani, C. Arson. Total allocation and Arson group share: 5.5K GPU hours.",
        ),
        (
            "<b>A Physics-Guided Subsurface Earth-System Model for Uncertainty-Aware Prediction of Geothermal Reservoir Evolution</b>",
            "2026",
            "NASA ROSES-25 F.5 FINESST - Under review. Future Investigator: Y. Liu; PI / faculty mentor: C. Arson.",
        ),
    ]
    for title, date, meta in support_entries:
        story.append(dated_entry(title, date, meta))
        story.append(Spacer(1, 2))

    story.extend(section("Publications"))
    publications = [
        "<b>Yulong Liu</b>, Chloé Arson. <i>A Physics-Informed Neural Network for Modeling Pressurized Cavities of Arbitrary Smooth Shape Embedded in Heterogeneous Rock.</i> <b>Accepted in Rock Mechanics and Rock Engineering</b>, 2026. Research Square preprint: <a href='https://doi.org/10.21203/rs.3.rs-8492281/v1' color='#A63F2C'>doi:10.21203/rs.3.rs-8492281/v1</a>.",
        "<b>Yulong Liu</b>, Jonah Botvinick-Greenhouse, Yunan Yang, Chloé Arson. <i>Operator Learning Surrogate Modeling of Hydraulically Fractured Geothermal Injection-Production Systems: A Cornell Case Study.</i> ARMA US Rock Mechanics/Geomechanics Symposium, Tucson, 2026.",
        "M. Belachew, <b>Yulong Liu</b>, J. D. Frost, Chloé Arson. <i>Numerical Assessment of Plasticity Development and Energy Expenditure of Ant-Like Microtunnelling.</i> Tunnelling and Underground Space Technology, 172, 107501, 2026.",
        "<b>Yulong Liu</b>, Chloé Arson. <i>Physics-Informed Neural Network Surrogate Modeling of Pressurized Cavity in Homogeneous and Bilayered Media.</i> ARMA US Rock Mechanics/Geomechanics Symposium, D022S018R006, 2025.",
        "<b>Yulong Liu</b>, Zhenghan Song, et al. <i>Your Simulation Runs but Solves the Wrong Physics: PDE-Grounded Intent Verification for LLM-Generated Multiphysics Simulation Code.</i> arXiv preprint; under review at NeurIPS 2026.",
        "Zhenghan Song, Yunyi Li, <b>Yulong Liu</b>. <i>Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability: Separating Calibration from Ranking.</i> Under review at ACL ARR 2026.",
    ]
    for item in publications:
        story.append(bullet(item))

    story.extend(section("Thesis"))
    story.append(
        bullet(
            "<b>Yulong Liu.</b> <i>A Unified Model for Microseismic Signal Classification and Arrival-Time Picking Based on Deep Learning.</i> Undergraduate thesis, Northeastern University, 2024."
        )
    )

    story.extend(section("Conferences and Presentations"))
    talks = [
        ("<b>Oral presentation</b>, 60th US Rock Mechanics/Geomechanics Symposium (ARMA), Tucson, AZ", "Jun. 2026"),
        ("<b>Invited speaker and panelist</b>, 20th Phase Field Methods Workshop, Northwestern University", "May 2026"),
        ("<b>Poster presentation</b>, Cornell CEE Graduate Research Symposium, Ithaca, NY", "Apr. 2026"),
        ("<b>Invited seminar</b>, Physics-Informed AI Optimization of Heterogeneous Rock Systems, Southwest Petroleum University", "Dec. 2025"),
        ("<b>Poster presentation</b>, 59th US Rock Mechanics/Geomechanics Symposium (ARMA), Santa Fe, NM", "Jun. 2025"),
    ]
    for title, date in talks:
        story.append(dated_entry(title, date))

    story.extend(section("Fellowships and Awards"))
    awards = [
        ("Estwing Hammer Award - Outstanding EAS Graduate Student of 2024, Cornell University", "2025"),
        ("Cornell University Travel Grant", "2025, 2026"),
        ("Outstanding Thesis, Northeastern University", "2024"),
        ("National Scholarship, Ministry of Education, China", "2024"),
        ("First Class Scholarship, Northeastern University", "2023"),
        ("Autumn Scholarship; Golden Seed Scholarship, Northeastern University", "2022"),
    ]
    for title, date in awards:
        story.append(dated_entry(title, date))

    story.extend(section("Academic Service"))
    for item in [
        "Reviewer, Rock Mechanics and Rock Engineering",
        "Reviewer, Underground Space",
        "Reviewer, International Conference on Artificial Neural Networks",
        "Reviewer, Geothermal Rising Conference",
    ]:
        story.append(bullet(item))

    story.extend(section("Skills"))
    skill_rows = [
        ("Programming & Scientific Computing", "Python, C++, R, MOOSE finite element framework"),
        ("Modeling & Simulation", "Finite element modeling, coupled multiphysics simulation, poromechanics, computational geomechanics, CAD"),
        ("Subsurface & Reservoir", "Hydraulic fracturing, geothermal injection-production, multiscale transport in porous media"),
        ("Scientific Machine Learning", "ML for PDEs, PINNs, operator learning, implicit neural representations, surrogate modeling"),
        ("LLMs for Simulation", "Simulation-software workflows and physical-intent verification of generated code"),
        ("Experimental Methods", "Rock mechanics testing, triaxial compression, laboratory instrumentation"),
        ("Scientific Writing", "LaTeX / Overleaf"),
    ]
    skill_table = Table(
        [[p(f"<b>{a}</b>", "entry_small"), p(b, "entry_small")] for a, b in skill_rows],
        colWidths=[1.75 * inch, 5.22 * inch],
    )
    skill_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEBELOW", (0, 0), (-1, -2), 0.3, LIGHT),
            ]
        )
    )
    story.append(skill_table)

    story.extend(section("Professional Memberships"))
    for item in [
        "American Rock Mechanics Association (ARMA), 2025-Present",
        "International Society for Rock Mechanics and Rock Engineering (ISRM), 2025-Present",
        "Chinese Society for Rock Mechanics and Engineering (CSRME), 2024-Present",
        "Geothermal Rising, 2025-Present",
    ]:
        story.append(bullet(item))

    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    WEB_PDF.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUTPUT, WEB_PDF)
    shutil.copy2(OUTPUT, ROOT_PDF)
    print(OUTPUT)


if __name__ == "__main__":
    build()
