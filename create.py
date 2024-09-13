from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import textwrap
import random
import qrcode
import io

# Improved wild business ideas with corresponding questions
improved_ideas_and_questions = [
    ("GreenPrint: AI-optimized sustainable 3D-printed housing solutions", "Could this revolutionize eco-friendly urban development?"),
    ("SkyFarm: AI-driven vertical farming systems with IoT integration", "Is this the future of sustainable urban agriculture?"),
    ("EcoPackage: Biodegradable packaging from agricultural waste and mycelium", "Will this innovation end our reliance on plastic packaging?"),
    ("SolarSkin: Highly efficient, flexible solar panels with nanotech enhancements", "Could this technology turn any surface into a power source?"),
    ("TrashTreasure: AI-powered waste sorting and upcycling systems", "Is this the key to achieving a zero-waste society?"),
    ("CarbonCapture: Direct air capture technology with enhanced CO2 conversion", "Could this be the breakthrough we need to reverse climate change?"),
    ("OceanClean: Autonomous marine plastic collection and recycling drones", "Will this innovation save our oceans from plastic pollution?"),
    ("BioLight: Genetically engineered bioluminescent plants for sustainable lighting", "Is this nature's answer to our lighting needs?"),
    ("AirHarvest: Smart atmospheric water generators with AI-optimized distribution", "Could this technology end water scarcity in arid regions?"),
    ("EcoFuel: Next-generation biofuel production from algae and waste biomass", "Is this the sustainable fuel solution for the transportation sector?"),
    ("EnergyWeb: Decentralized blockchain-based renewable energy trading platforms", "Will this democratize the energy market and boost renewable adoption?"),
    ("HydroHarvest: Sustainable deep-sea aquaculture systems with AI monitoring", "Could this be the future of sustainable seafood production?"),
    ("BioReactor: Engineered microorganisms for enhanced carbon sequestration", "Is this the biological solution to our carbon problem?"),
    ("AquaFarm: AI-managed sustainable offshore aquaculture platforms", "Will this revolutionize fish farming and protect wild fish stocks?"),
    ("TerraForm: Advanced geoengineering simulation tools with quantum computing", "Could this help us safely test climate intervention strategies?"),
    ("EcoSphere: AI-optimized closed-loop life support systems for space habitats", "Is this the key to long-term space exploration and colonization?"),
    ("BioConstruct: Mycelium-based sustainable building materials with enhanced properties", "Will fungi be the foundation of future eco-friendly architecture?"),
    ("EcoLoop: AI-driven circular economy platforms for industry-wide resource optimization", "Could this end waste in manufacturing and consumption?"),
    ("WindHarvest: High-altitude wind energy systems with autonomous drones", "Is this the untapped renewable energy source we've been looking for?"),
    ("NanoSolar: Quantum dot-enhanced solar cell efficiency boosters", "Will this make solar energy the dominant power source worldwide?"),
    ("ARLearn: Cross-platform augmented reality for immersive, adaptive education", "Could this transform how we learn and interact with information?"),
    ("VRCampus: Global virtual reality university campuses with haptic feedback", "Is this the future of higher education and international collaboration?"),
    ("AITutor: Personalized AI-powered tutoring systems with emotional intelligence", "Will this revolutionize personalized learning and student support?"),
    ("SkillForge: Microlearning platforms with AI-curated content for rapid skill acquisition", "Could this be the solution to lifelong learning and reskilling?"),
    ("EduBlock: Blockchain-based academic credential verification with smart contracts", "Will this end credential fraud and streamline hiring processes?"),
    ("LangAI: AI-powered language learning assistants with real-time translation", "Is this the key to breaking down global language barriers?"),
    ("MindMap: AI-enhanced cognitive mapping tools for optimized learning and memory", "Could this dramatically improve how we process and retain information?"),
    ("EduGame: AI-driven gamified educational content creation and adaptation platform", "Will this make learning as engaging as playing video games?"),
    ("PeerTeach: Blockchain-incentivized peer-to-peer knowledge sharing marketplaces", "Is this the future of collaborative, decentralized education?"),
    ("ClassroomAI: AI teaching assistants for personalized learning and classroom management", "Could this provide every student with a personal tutor?"),
    ("VirtualLab: Photorealistic remote access scientific laboratory simulations", "Will this democratize access to advanced scientific equipment?"),
    ("EduMetrics: AI-driven educational performance analytics with predictive insights", "Could this help identify and address learning gaps before they widen?"),
    ("SkillSim: Haptic feedback-enabled VR vocational training simulations", "Is this the safest and most effective way to train for high-risk jobs?"),
    ("BrainBoost: Personalized cognitive training applications with neurofeedback", "Will this help us unlock our full cognitive potential?"),
    ("EduChain: Quantum-secure blockchain for lifelong learning record management", "Could this create a universal, tamper-proof educational passport?"),
    ("NanoMed: AI-guided targeted drug delivery using programmable nanoparticles", "Will this revolutionize how we treat diseases at the cellular level?"),
    ("GenomeGuard: AI-driven genetic risk assessment and CRISPR-based prevention", "Could this be the key to personalized preventive medicine?"),
    ("NeuroBoost: Non-invasive cognitive enhancement techniques using focused ultrasound", "Is this the future of mental performance optimization?"),
    ("EmotiAI: Emotion recognition software for mental health monitoring and intervention", "Will this transform how we diagnose and treat mental health issues?"),
    ("BioSync: Personalized sleep optimization wearables with circadian rhythm adjustment", "Could this end sleep disorders and boost global productivity?"),
    ("SkinPrint: 3D bioprinting for personalized wound healing and organ transplants", "Is this the solution to the organ donation shortage?"),
    ("VRTherapy: Immersive virtual reality platforms for phobia and PTSD treatment", "Will this make mental health treatment more effective and accessible?"),
    ("GenePharma: CRISPR-based gene therapy treatments for genetic disorders", "Could this be the end of hereditary diseases?"),
    ("NeuroLink: Brain-computer interfaces for paralysis patients and enhanced communication", "Is this the future of human-computer interaction?"),
    ("BrainTrack: Non-invasive brain activity monitoring devices for early diagnosis", "Will this allow us to catch neurological issues before symptoms appear?"),
    ("MindWellness: AI-driven mental health prediction and personalized support systems", "Could this make mental health care proactive rather than reactive?"),
    ("NanoSensor: Implantable nanodevices for continuous health monitoring and drug delivery", "Is this the key to predictive and preventive healthcare?"),
    ("GeneTherapy: Targeted genetic treatments for rare diseases using viral vectors", "Will this offer hope for patients with previously untreatable conditions?"),
    ("HoloMed: Mixed reality surgical planning and training with haptic feedback", "Could this dramatically improve surgical outcomes and training?"),
    ("NanoTarget: Targeted cancer therapies using AI-guided nanoparticles", "Is this the breakthrough we need in the fight against cancer?"),
    ("QuantumSecure: Post-quantum cryptography for future-proof data protection", "Will this keep our data safe in the age of quantum computers?"),
    ("NeuroPilot: Advanced brain-computer interfaces for full-body mobility assistance", "Could this give complete autonomy back to paralyzed individuals?"),
    ("HyperLoop: High-speed vacuum tube transportation with magnetic levitation", "Is this the future of intercity travel and logistics?"),
    ("SpaceLoom: Microgravity experiments for novel materials research and production", "Will this usher in a new era of space-based manufacturing?"),
    ("AgroBot: Autonomous precision agriculture robots with AI crop management", "Could this solve global food security challenges?"),
    ("NeuralNet: Neuromorphic computing chips for ultra-efficient AI applications", "Is this the key to creating truly intelligent machines?"),
    ("SkyCharge: Long-range wireless charging for electric vehicles and drones", "Will this eliminate 'range anxiety' for electric vehicle owners?"),
    ("QuantumSense: Quantum sensors for ultra-precise measurements in various fields", "Could this lead to breakthroughs in navigation, medical imaging, and more?"),
    ("RoboChef: AI-assisted robotic kitchen assistants with advanced sensory capabilities", "Is this the future of food preparation and culinary innovation?"),
    ("NanoCoat: Self-healing nanoparticle coatings for improved material durability", "Will this dramatically extend the lifespan of consumer products?"),
    ("FusionEnergy: Compact nuclear fusion reactor research for limitless clean energy", "Could this solve our energy needs for centuries to come?"),
    ("QuantumClock: Ultra-precise atomic clocks for next-gen GPS and time-keeping", "Is this the key to centimeter-level GPS accuracy and beyond?"),
    ("DroneSwarm: Coordinated autonomous drone swarms for complex tasks and emergencies", "Will this revolutionize search and rescue, delivery, and more?"),
    ("BionicProsthetics: Advanced neural-integrated artificial limbs with sensory feedback", "Could this provide amputees with fully functional replacement limbs?"),
    ("QuantumRadar: Next-generation quantum radar systems for stealth detection", "Is this the end of stealth technology as we know it?"),
    ("MindMeld: AI-enhanced collaborative problem-solving platform with brain-computer interfaces", "Will this unlock unprecedented levels of human collaboration?"),
    ("DataDNA: High-density DNA-based data storage with rapid read/write capabilities", "Could this be the ultimate solution to our data storage needs?"),
    ("VoiceAssist: Advanced AI for natural language processing with emotional understanding", "Is this the key to truly natural human-computer interaction?"),
    ("QuantumAlgo: Quantum algorithm development for optimization in specific industries", "Will this solve currently intractable problems in logistics, finance, and more?"),
    ("SynBio: Synthetic biology design tools and databases for custom organism creation", "Could this usher in a new era of biological engineering?"),
    ("QuantumSim: Quantum system simulation software for material and drug discovery", "Is this the fast-track to revolutionary new materials and medicines?"),
    ("AIDiplomacy: AI-assisted international negotiation platforms for conflict resolution", "Will this lead to more peaceful and equitable global relations?"),
    ("QuantumML: Quantum-classical hybrid machine learning algorithms for complex modeling", "Could this dramatically accelerate scientific discoveries?"),
    ("BrainType: Thought-to-text brain-computer interfaces for seamless communication", "Is this the future of human communication and accessibility?"),
    ("NeuroMarket: EEG-based neuromarketing research tools for ethical consumer insights", "Will this transform how products are designed and marketed?"),
    ("SoundScape: Personalized 3D audio environments for enhanced productivity and wellbeing", "Could this revolutionize how we work and relax?"),
    ("EcoSense: Global IoT-based environmental monitoring networks for climate action", "Is this the key to understanding and mitigating climate change?"),
    ("MindWave: EEG-controlled smart home interfaces for accessibility and convenience", "Will this make smart homes accessible to everyone?"),
    ("NeuroNet: Brain-inspired AI architectures for efficient edge computing", "Could this bring human-like reasoning to our devices?"),
    ("SwarmAI: Distributed AI systems for complex global problem-solving", "Is this how we'll tackle the world's most challenging issues?"),
    ("BioMechCoach: AI-powered biomechanics analysis for injury prevention and performance", "Will this create a new generation of safer, better athletes?"),
    ("VRTraining: Immersive virtual reality sports training with real-time feedback", "Could this democratize access to elite-level coaching?"),
    ("SmartGear: IoT-enabled smart sports equipment with performance tracking", "Is this the key to unlocking every athlete's potential?"),
    ("FanEngage: AR-enhanced stadium experience apps with real-time stats and replays", "Will this transform how we experience live sports?"),
    ("AthleteDNA: Genetic testing and AI for personalized athletic training and nutrition", "Could this be the future of tailored sports performance?"),
    ("E-SportsPro: Advanced analytics and AI coaching for esports team optimization", "Is this how esports will overtake traditional sports in popularity?"),
    ("ReflexAI: AI-driven reflex and reaction time training systems for various sports", "Will this create a new breed of super-fast athletes?"),
    ("SportsBrainTech: Neurofeedback systems for mental training in high-pressure sports", "Could this be the key to consistent peak performance?"),
    ("InjuryPredict: AI and wearable tech for injury prediction and prevention in sports", "Is this the end of season-ending injuries for athletes?"),
    ("DopingDetect: Advanced AI-driven anti-doping testing technologies", "Will this ensure fair play in sports once and for all?"),
    ("FanStats: Augmented reality sports analytics platforms for enhanced fan engagement", "Could this turn every fan into a sports analyst?"),
    ("AquaForm: AI swim technique analysis and optimization with underwater sensors", "Is this how we'll break every swimming world record?"),
    ("SportsMindset: Mental training apps with AI-guided meditation for athletes", "Will this make mental toughness as trainable as physical strength?"),
    ("TacticsAR: Augmented reality for real-time sports strategy visualization and planning", "Could this revolutionize how teams strategize during games?"),
    ("AthleteRecovery: Personalized post-performance recovery systems with AI optimization", "Is this the key to extending athletes' careers and health?"),
    ("NeuroPlay: Brain-computer interfaces for thought-controlled gaming experiences", "Will this create a new dimension of immersive gaming?"),
    ("EcoGym: Energy-generating gym equipment powering sustainable fitness centers", "Could this turn every workout into clean energy production?"),
    ("GenomeEdit: Precision CRISPR tools for ethical genetic enhancement in humans", "Is this the next step in human evolution?"),
    ("QubitCloud: Quantum cloud computing services for on-demand quantum processing", "Will this make quantum computing accessible to everyone?"),
    ("NanoAssembly: Molecular-scale 3D printing for custom nanomaterial creation", "Could this usher in a new era of material science?")
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

def create_flyer(c, page_num, idea_and_question):
    idea, question = idea_and_question
    y_start = 750

    # Title
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(300, y_start, "Philadelphia Open")
    c.drawCentredString(300, y_start - 50, "Innovation Tournament")

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(300, y_start - 80, "October 26-27, 2024")

    c.setFont("Helvetica", 14)
    c.drawCentredString(300, y_start - 100, "Netrality Data Center - 401 North Broad St, Philadelphia, PA")

    # QR code
    qr = create_qr_code("https://innovationphilly.com")
    c.drawImage(qr, 225, 490, width=150, height=150)

    c.setFont("Helvetica", 18)
    c.drawCentredString(300, 475, "Scan to register")

    c.setFont("Courier", 18)
    idea = f"Idea #{random.randint(100000, 999999)}: {idea}"
    wrapped_idea = textwrap.wrap(idea, width=50)
    for i, line in enumerate(wrapped_idea):
        c.drawCentredString(300, 425 - i*25, line)

    c.setFont("Courier", 18)
    wrapped_question = textwrap.wrap(question, width=50)
    for i, line in enumerate(wrapped_question):
        c.drawCentredString(300, 350 - i*25, line)

    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(300, 260, "Your vote could change everything!")
    c.drawCentredString(300, 230, "Register now to drive the next wave of innovation.")

    # Leagues
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 180, "Innovation Leagues")

    c.setFont("Helvetica", 16)
    for i, league in enumerate(leagues):
        c.drawString(100 if i < 3 else 350, 140 - (i % 3) * 30, league)

    # Event details
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 45, "2 Days of Innovation!")

    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 20, "Collaborate, Compete, Create the Future.")

# Generate flyers
for i, idea_and_question in enumerate(improved_ideas_and_questions):
    c = canvas.Canvas(f"philly_innovation_tournament_flyer_{i+1}.pdf", pagesize=letter)
    create_flyer(c, i+1, idea_and_question)
    c.showPage()
    c.save()

print("Flyers have been generated!")

