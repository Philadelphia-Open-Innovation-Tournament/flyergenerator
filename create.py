from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import textwrap
import random
import qrcode
import io

# Wild business ideas
wild_ideas = [
    # 🌿 GREENTECH
    "GreenPrint: Sustainable 3D-printed housing solutions",
    "SkyFarm: AI-optimized vertical farming systems",
    "EcoPackage: Biodegradable packaging from agricultural waste",
    "SolarSkin: Highly efficient, flexible solar panels",
    "TrashTreasure: AI-powered waste sorting and recycling systems",
    "CarbonCapture: Direct air capture technology for CO2 reduction",
    "OceanClean: Autonomous marine plastic collection systems",
    "BioLight: Engineered bioluminescent plants for lighting",
    "AirHarvest: Efficient atmospheric water generators",
    "EcoFuel: Next-generation biofuel production from algae",
    "EnergyWeb: Blockchain-based renewable energy trading platforms",
    "HydroHarvest: Sustainable deep-sea aquaculture systems",
    "BioReactor: Engineered microorganisms for carbon sequestration",
    "AquaFarm: Sustainable offshore aquaculture platforms",
    "TerraForm: Advanced geoengineering simulation tools",
    "EcoSphere: Closed-loop life support systems for space applications",
    "BioConstruct: Mycelium-based sustainable building materials",
    "EcoLoop: AI-optimized circular economy platforms",
    "WindHarvest: High-altitude wind energy systems",
    "NanoSolar: Nanotech-enhanced solar cell efficiency boosters",

    # 🎓 EDUTECH
    "ARLearn: Augmented reality platforms for immersive education",
    "VRCampus: Virtual reality university campuses",
    "AITutor: Personalized AI-powered tutoring systems",
    "SkillForge: Microlearning platforms for rapid skill acquisition",
    "EduBlock: Blockchain-based academic credential verification",
    "LangAI: AI-powered language learning assistants",
    "MindMap: Cognitive mapping tools for enhanced learning",
    "EduGame: Gamified educational content creation platform",
    "PeerTeach: Peer-to-peer knowledge sharing marketplaces",
    "ClassroomAI: AI teaching assistants for personalized learning",
    "VirtualLab: Remote access scientific laboratory simulations",
    "EduMetrics: AI-driven educational performance analytics",
    "SkillSim: VR-based vocational training simulations",
    "BrainBoost: Personalized cognitive training applications",
    "EduChain: Blockchain for secure sharing of educational records",

    # 🏥 HEALTHCARE
    "NanoMed: Targeted drug delivery using nanoparticles",
    "GenomeGuard: AI-driven genetic risk assessment and prevention",
    "NeuroBoost: Non-invasive cognitive enhancement techniques",
    "EmotiAI: Emotion recognition software for mental health",
    "BioSync: Personalized sleep optimization wearables",
    "SkinPrint: 3D bioprinting for wound healing and grafts",
    "VRTherapy: Virtual reality platforms for mental health treatment",
    "GenePharma: CRISPR-based gene therapy treatments",
    "NeuroLink: Brain-computer interfaces for paralysis patients",
    "BrainTrack: Non-invasive brain activity monitoring devices",
    "MindWellness: AI-driven mental health prediction and support",
    "NanoSensor: Implantable nanodevices for health monitoring",
    "GeneTherapy: Targeted genetic treatments for rare diseases",
    "HoloMed: Mixed reality surgical planning and training",
    "NanoTarget: Targeted cancer therapies using nanoparticles",

    # 🔧 HARDTECH
    "QuantumSecure: Post-quantum cryptography for data protection",
    "NeuroPilot: Advanced brain-computer interfaces for accessibility",
    "HyperLoop: High-speed vacuum tube transportation",
    "SpaceLoom: Microgravity experiments for materials research",
    "AgroBot: Autonomous precision agriculture robots",
    "NeuralNet: Neuromorphic computing chips for AI applications",
    "SkyCharge: Improved wireless charging for electric vehicles",
    "QuantumSense: Quantum sensors for precision measurements",
    "RoboChef: AI-assisted robotic kitchen assistants",
    "NanoCoat: Nanoparticle coatings for improved material properties",
    "FusionEnergy: Compact nuclear fusion reactor research",
    "QuantumClock: Ultra-precise atomic clocks for timing applications",
    "DroneSwarm: Coordinated drone swarms for complex tasks",
    "BionicProsthetics: Advanced neural-integrated artificial limbs",
    "QuantumRadar: Next-generation quantum radar systems",

    # 💻 SOFTWARE
    "MindMeld: AI-enhanced collaborative problem-solving platform",
    "DataDNA: DNA-based data storage prototypes",
    "VoiceAssist: Advanced AI for natural language processing",
    "QuantumAlgo: Quantum algorithm development for specific industries",
    "SynBio: Synthetic biology design tools and databases",
    "QuantumSim: Quantum system simulation software",
    "AIDiplomacy: AI-assisted international negotiation platforms",
    "QuantumML: Quantum-classical hybrid machine learning algorithms",
    "BrainType: Thought-to-text brain-computer interfaces",
    "NeuroMarket: EEG-based neuromarketing research tools",
    "SoundScape: 3D audio environments for productivity",
    "EcoSense: IoT-based environmental monitoring networks",
    "MindWave: EEG-controlled smart home interfaces",
    "NeuroNet: Brain-inspired AI for edge computing",
    "SwarmAI: Distributed AI systems for complex problem-solving",

    # ⚽ SPORTSTECH
    "BioMechCoach: AI-powered biomechanics analysis for athletes",
    "VRTraining: Immersive virtual reality sports training platforms",
    "SmartGear: IoT-enabled smart sports equipment",
    "FanEngage: AR-enhanced stadium experience apps",
    "AthleteDNA: Genetic testing for personalized athletic training",
    "E-SportsPro: Advanced analytics for esports team optimization",
    "ReflexAI: AI-driven reflex and reaction time training systems",
    "SportsBrainTech: Neurofeedback for peak athletic performance",
    "InjuryPredict: AI for injury prediction and prevention in sports",
    "DopingDetect: Advanced anti-doping testing technologies",
    "FanStats: Real-time sports analytics platforms for fans",
    "AquaForm: AI swim technique analysis and optimization",
    "SportsMindset: Mental training apps for athletes",
    "TacticsAR: Augmented reality for sports strategy visualization",
    "AthleteRecovery: Personalized post-performance recovery systems"
]

leagues = [
    "🌿 GREENTECH", "🎓 EDUTECH", "🏥 HEALTHCARE",
    "🔧 HARDTECH", "💻 SOFTWARE", "⚽ SPORTSTECH"
]

def create_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    return ImageReader(img_buffer)

def create_flyer(c, page_num, idea):
    # Adjust the starting y-coordinate to prevent bleeding off the top edge
    y_start = 750  # Reduced from 780

    # Title
    c.setFont("Courier-Bold", 44)
    c.drawCentredString(300, y_start, "Philadelphia Open")
    c.drawCentredString(300, y_start - 50, "Innovation Tournament")

    c.setFont("Courier-Bold", 18)
    c.drawCentredString(300, y_start - 80, "October 26-27, 2024")

    c.setFont("Courier", 14)
    c.drawCentredString(300, y_start - 100, "Netrality Data Center")
    c.drawCentredString(300, y_start - 120, "401 North Broad St, Philadelphia, PA")

    # QR code
    qr = create_qr_code("https://innovationphilly.com")
    # Move the QR code up by adjusting its y-coordinate
    c.drawImage(qr, 225, 480, width=150, height=150)  # Increased from 480

    c.setFont("Courier-Bold", 18)
    c.drawCentredString(300, 460, "Scan to register!")  # Increased from 460

    # Wild business idea
    c.setFont("Courier-Bold", 24)
    c.drawCentredString(300, 420, "Can you do better than this?")  # Increased from 420

    c.setFont("Courier", 20)
    wrapped_idea = textwrap.wrap(idea, width=35)
    for i, line in enumerate(wrapped_idea):
        c.drawCentredString(300, 380 - i*25, line)  # Increased from 380

    c.setFont("Courier-Bold", 24)
    c.drawCentredString(300, 300, "If so, prove it! Register now!")  # Increased from 300

    # Leagues
    c.setFont("Courier-Bold", 20)
    c.drawCentredString(300, 240, "Innovation Leagues")  # Increased from 240

    c.setFont("Courier", 16)
    for i, league in enumerate(leagues):
        c.drawString(100 if i < 3 else 350, 200 - (i % 3) * 30, league)  # Increased from 200

    # Event details
    c.setFont("Courier-Bold", 24)
    c.drawString(50, 60, "2 Days of Innovation!")

    c.setFont("Courier", 18)
    c.drawString(50, 30, "Collaborate, Compete, Create the Future")

    # Page number
    c.setFont("Courier", 10)
    c.drawString(500, 30, f"#{page_num}")

for i,item in enumerate(wild_ideas):
    c = canvas.Canvas(f"philly_innovation_tournament_flyer_{i+1}.pdf", pagesize=letter)
    create_flyer(c, i+1, item)
    c.showPage()
    c.save()

print("flyers have been generated!")
