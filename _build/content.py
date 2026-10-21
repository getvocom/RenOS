"""RenOS site content.

Routes, titles, H1s and keywords follow the RenOS sitemap and keyword map.
Copy follows the RenOS claims guardrails: no certifications, prices, customer
results, vendor names or roadmap features presented as shipped.
"""
from stars import STARS  # noqa: F401

# Where lead forms post. Leave empty until a form backend is confirmed;
# the forms then tell visitors nothing was sent instead of failing silently.
FORM_ENDPOINT = ""

# Prices from the pricing design are not yet cleared for public use.
# Set to True once they're approved; every card, table and FAQ then shows the figures.
SHOW_PRICES = False

# Single source of truth for facts reused across pages.
FACTS = {
    "tagline": "The AI Operating System for Teams",
    "status": "Design-partner pilots are open",
    "pilot_days": 60,
    "pilot_seats": 15,
    "free_seats": "Admin, auditor and read-only compliance seats are always free.",
    "model_reach": "hundreds of AI models through one workspace",
}

CYAN, VIOLET, GREEN, AMBER, PINK, BLUE = "#5ee0ff", "#8f80f7", "#5fd0a0", "#f2b45a", "#f08bb8", "#6aa8ff"
ACCENTS = [CYAN, VIOLET, GREEN, AMBER, PINK, BLUE]

MODES = [
    ("Chat Mode", "/product/chat", "Ask in plain language. Policy picks the model."),
    ("Builder Mode", "/product/builder", "Work with more than one model side by side."),
    ("Agent Mode", "/product/agents", "Several agents, each with its own identity, on one task."),
]
FEATURES = [
    ("Policy Routing", "/product/routing", "Your rules pick the model before anything is sent."),
    ("Audit Trail", "/product/audit-trail", "Every task writes a record anyone can read."),
    ("Admin Dashboard", "/product/admin", "Spend, policy and access in one place."),
    ("Supported AI Models", "/models", "Hundreds of models, one governed workspace."),
]

# ------------------------------------------------------------------ Teams

TEAMS = [
    {
        "slug": "sales", "name": "Sales", "accent": CYAN,
        "title": "AI for Sales Teams: Faster Outreach, Clear Records",
        "description": "AI for sales teams that drafts and researches on approved models, handles customer data by policy and keeps a record of outreach. Start a pilot.",
        "h1": "AI for Sales Teams, With a Record of Every Message",
        "intro": "Your reps already use AI for sales outreach, account research and call prep. RenOS gives them the same speed on approved models, handles customer data by your rules, and keeps a record of every AI-assisted message.",
        "pains": [
            "My reps each pay for a different AI tool and I have no idea what customer data goes into any of them.",
            "We coach on call notes and emails, but nobody can tell me which ones AI wrote or what it was told.",
            "Every time a rep finds a new tool, it's another subscription and another place our pipeline data lives.",
        ],
        "helps": [
            ("Draft and Research on Approved Models", "Reps describe the task in Chat mode. Policy sends anything with customer data to a model you approved."),
            ("Sales Coaching With Real Context", "Managers see which messages were AI-assisted and the task behind them, so coaching starts from what actually happened."),
            ("One Workspace Instead of Many Tools", "Every rep works in one place across many models, so you stop paying for overlapping subscriptions."),
        ],
        "modes": ["Chat Mode", "Builder Mode"],
        "faq": [
            ("Can reps keep using the AI they like?", "Reps pick a mode and describe the task. RenOS routes it to a model your admin approved, so they get strong results without choosing or managing tools."),
            ("What happens to customer data in a prompt?", "Your policy decides by data sensitivity. Tasks that touch customer data go only to the models you allow, and each decision is logged with its reason."),
            ("Does this add steps for the sales team?", "No. Reps submit a task the way they would in any assistant. Policy, routing and the record happen in the background."),
        ],
    },
    {
        "slug": "compliance", "showcase": "audit", "name": "Compliance", "accent": VIOLET,
        "title": "AI Governance for Compliance Teams, Without Interviews",
        "description": "AI governance for compliance teams: free auditor seats, evidence of every AI task without interviewing staff, and rule changes that apply next task.",
        "h1": "AI Governance for Compliance Teams That Need Evidence",
        "intro": "AI governance for compliance teams usually means a policy document and a lot of trust. RenOS turns the policy into rules that run before any model is called, and writes the evidence as people work.",
        "pains": [
            "We have an AI policy. I couldn't prove anyone follows it.",
            "When someone asks which AI tools touched client data last month, I have to send a survey.",
            "Blocking consumer AI just moved it to personal phones.",
        ],
        "helps": [
            ("Free Auditor and Read-Only Seats", "Compliance reviewers get their own seats at no cost, so review never waits on a license."),
            ("Evidence Without Interviews", "Every task writes an audit entry automatically: who, what task, which model, which policy and any overrides."),
            ("Policy Changes Apply to the Next Task", "Adjust a rule in the admin view and it governs the very next task. No retraining, no memo."),
            ("Exportable Records", "Audit logs export cleanly, so evidence fits into the review process you already run."),
        ],
        "modes": ["Chat Mode", "Agent Mode"],
        "faq": [
            ("Do compliance staff need paid seats?", "No. Admin, auditor and read-only compliance seats are always free."),
            ("Can a non-technical reviewer read the audit trail?", "Yes. Each entry includes a plain-language Routing Rationale written for someone who wasn't in the room."),
            ("How does this relate to the audit trail product page?", "This page covers how compliance teams use RenOS. The AI audit trail page explains what each entry holds."),
        ],
    },
    {
        "slug": "it", "showcase": "signin", "name": "IT and Security", "accent": BLUE,
        "title": "AI System Administration for IT Teams | RenOS",
        "description": "AI system administration for IT teams: approve models and suppliers in one place, add SSO and SCIM on Enterprise, and deploy privately. Book a demo.",
        "h1": "AI System Administration Without the Sprawl",
        "intro": "IT teams end up owning AI whether they planned to or not. RenOS gives you one place for AI system administration: which models and suppliers are allowed, for which data, for which roles.",
        "pains": [
            "Every department brought its own AI tool and now I'm supposed to secure all of them.",
            "I can't answer which vendors have seen our data without opening five admin consoles.",
            "Our security team wants AI on our own infrastructure. Most tools don't offer that.",
        ],
        "helps": [
            ("One Place to Approve Models and Suppliers", "Set which models and suppliers each task may use, by data sensitivity, task type and role."),
            ("Identity on Enterprise", "Enterprise plans include SSO and SCIM so access follows your directory."),
            ("Private or Local Deployment", "Keep sensitive work inside your own environment when policy calls for it."),
        ],
        "modes": ["Agent Mode", "Chat Mode"],
        "faq": [
            ("Can we run RenOS in our own environment?", "Yes. Private or local deployment keeps data inside your environment."),
            ("Does RenOS support single sign-on?", "SSO and SCIM are part of the Enterprise plan."),
            ("Where are routing rules enforced?", "At routing time, before any model is called. A task that breaks policy never reaches the model."),
        ],
    },
    {
        "slug": "operations", "showcase": "workspace", "name": "Operations", "accent": GREEN,
        "title": "AI for Work: Task Automation for Operations Teams",
        "description": "AI for work that operations teams can run: Chat and Builder for daily tasks, agents for repeat workflows, and no extra steps for staff. Start a pilot.",
        "h1": "AI for Work That Your Operations Team Can Run Every Day",
        "intro": "Operations teams want AI for work that just happens: drafting, summarizing, repeatable workflows. RenOS handles the model choice and the record, so your people only describe the task.",
        "pains": [
            "Half my team uses AI daily, the other half doesn't trust it, and nobody shares what works.",
            "We automate a workflow, it breaks quietly, and nobody can see what the AI did.",
            "Every new tool means another login and another training session.",
        ],
        "helps": [
            ("Chat and Builder for Daily Tasks", "Describe the task in plain language. Compare outputs from more than one model when the answer matters."),
            ("Agents for Repeatable Workflows", "Set up agents with their own identities for work that repeats, with every action recorded."),
            ("No Extra Steps for Staff", "Governance is a byproduct of normal use. Nobody fills in a log."),
        ],
        "modes": ["Chat Mode", "Builder Mode", "Agent Mode"],
        "faq": [
            ("Do staff need to know which model to use?", "No. They pick Chat, Builder or Agent and describe the work. Policy picks the model."),
            ("Can we automate recurring tasks?", "Agent mode runs several agents on one task, each with its own identity, and logs every step."),
            ("How long does it take to get going?", "Pilots run 60 days with a written success plan, starting with one real workflow."),
        ],
    },
    {
        "slug": "leadership-coaching", "name": "Leadership and Coaching", "accent": PINK,
        "title": "Leadership Coaching AI With Clear Guardrails | RenOS",
        "description": "Leadership coaching AI for leaders and coaches: governed coaching workflows, private notes kept by policy, and a record of every session. Book a demo.",
        "h1": "Leadership Coaching AI You Can Trust With Real Conversations",
        "intro": "AI in coaching works best when people trust where their words go. RenOS lets leaders and coaches use AI for preparation, reflection and follow-up, with policy deciding which models see sensitive notes.",
        "pains": [
            "I'd use AI to prepare for hard conversations, but not if my notes end up somewhere I can't see.",
            "Our coaches each use different tools, so there's no consistent way of working.",
            "Leaders want AI support, and HR wants to know where personal information goes.",
        ],
        "helps": [
            ("Governed Coaching Workflows", "Build repeatable preparation and follow-up workflows that every coach can use."),
            ("Sensitive Notes Stay on Approved Models", "Policy routes personal or confidential notes only to the models you allow, or to a private deployment."),
            ("A Clear Record for HR", "Every session writes an audit entry, so you can show how personal information was handled."),
        ],
        "modes": ["Chat Mode", "Builder Mode"],
        "faq": [
            ("Is coaching content kept private?", "Your policy decides which models can see sensitive content, and private deployment keeps it inside your environment."),
            ("Can coaches share workflows?", "Yes. Builder mode lets teams compare outputs and settle on approaches that work, all within the same policies."),
            ("Who can see coaching records?", "Access follows roles you set. Audit entries record what happened without exposing content to people who shouldn't see it."),
        ],
    },
    {
        "slug": "finance", "showcase": "budgets", "name": "Finance", "accent": AMBER,
        "title": "AI Spend Control and Cost per Task for Finance Teams",
        "description": "AI spend control for finance teams: one bill instead of many subscriptions, per-team spend caps, and the cost of every AI task in one view. Book a demo.",
        "h1": "AI Spend Control Down to the Cost of Each Task",
        "intro": "AI spend control is hard when every team expenses its own tool. RenOS puts AI on one workspace, caps spend per team, and shows the cost of each task in the admin view.",
        "pains": [
            "We're paying for several AI subscriptions to get the capability of one.",
            "I see the invoices. I can't see what any of it produced.",
            "Budgets for AI live in a spreadsheet, not in the system that spends them.",
        ],
        "helps": [
            ("One Bill Instead of Many", "One workspace across many models replaces overlapping subscriptions."),
            ("Per-Team Spend Caps", "Set caps by team and let the system enforce them."),
            ("Cost per Task", "The admin view shows who ran what, on which model, at what cost."),
            ("Cheaper Models for Low-Stakes Work", "Policy can send routine tasks to lower-cost models and keep approved premium models for sensitive work."),
        ],
        "modes": ["Chat Mode", "Agent Mode"],
        "faq": [
            ("Can we cap AI spend by team?", "Yes. Per-team spend caps are set in the admin view and enforced by the system."),
            ("How do we see what AI costs per task?", "The admin view records the cost of each task alongside who ran it, the model and the policy applied."),
            ("Do auditors need paid seats?", "No. Admin, auditor and read-only compliance seats are always free."),
        ],
    },
]

# ------------------------------------------------------------------ Industries
# Industry keywords ("AI for credit unions" and so on) are not yet validated in Keyword Planner.

INDUSTRIES = [
    {
        "slug": "dental-groups", "name": "Dental Groups", "accent": CYAN,
        "title": "AI for Dental Groups: Governed AI Across Locations",
        "description": "AI for dental groups and multi-location practices: keep patient work on approved models, see every location in one view, and show compliance. Book a demo.",
        "h1": "AI for Dental Groups, Governed Across Every Location",
        "intro": "Front desk, billing and insurance teams are already using AI. RenOS gives dental groups and multi-location practices one governed workspace, so patient-identifiable work stays on approved models and compliance can see what happened.",
        "pains": [
            "Our front desk uses free AI tools to write patient messages and nobody records what went in.",
            "After every breach in the news, the board asks what AI we use. I don't have a good answer.",
            "Ownership wants us to adopt AI faster. Compliance wants it locked down.",
        ],
        "helps": [
            ("Patient Work Stays on Approved Models", "Policy keeps patient-identifiable tasks on the models you approve, or in a private deployment."),
            ("One Admin View Across Locations", "See AI use across every practice without asking each office manager."),
            ("New Practices Inherit the Rules", "Acquired locations get the same policies on day one."),
            ("An Audit Trail Compliance Can Read", "Every task writes a plain-language record your privacy officer can review."),
        ],
        "note": "Private deployment keeps data in your environment, and a BAA is part of the Enterprise plan design. Patient data stays out of pilots until the right agreement is in place.",
        "modes": ["Chat Mode", "Builder Mode"],
        "faq": [
            ("Can patient information go through RenOS?", "Not during a pilot. Regulated data stays out until the right agreement is in place. A BAA is part of the Enterprise plan design, and private deployment keeps data in your environment."),
            ("How does RenOS handle multiple locations?", "One admin view covers every location, and policies apply across the group, including practices you add later."),
            ("Will this slow down the front desk?", "No. Staff describe the task as they would in any assistant. Policy and logging happen in the background."),
        ],
    },
    {
        "slug": "credit-unions", "name": "Credit Unions", "accent": VIOLET,
        "title": "AI for Credit Unions: Inventory, Policy and Evidence",
        "description": "AI for credit unions: one inventory of every AI tool and model, vendor choices set by policy and logged, and exportable evidence for exams. Book a demo.",
        "h1": "AI for Credit Unions That Already Have the Mandate",
        "intro": "Credit unions are being asked to show oversight of AI and the vendors behind it. RenOS gives compliance, risk and lending teams one governed workspace with an inventory, policy and evidence built in.",
        "pains": [
            "We're expected to do due diligence on every AI vendor, and I can't even list them all.",
            "Loan officers and member service reps already use AI tools nobody approved.",
            "Our compliance budget covers a lot. AI governance isn't in it yet.",
        ],
        "helps": [
            ("One Inventory of AI Use", "See every model and supplier your people use, in one place."),
            ("Vendor Choices Set by Policy", "Control which models and suppliers each task may use, and log every choice with its reason."),
            ("Exportable Evidence for Examiners", "Audit entries export cleanly when an examiner asks how AI was used."),
        ],
        "modes": ["Chat Mode", "Agent Mode"],
        "faq": [
            ("Does RenOS help with AI vendor due diligence?", "It gives you the inventory and the record: which models and suppliers were used, for which tasks, under which policy."),
            ("Do rules differ by state?", "Expectations vary by regulator and state. RenOS lets you set policy to match your own obligations rather than one fixed template."),
            ("Can member data go through a pilot?", "No. Regulated data stays out of pilots until the right agreement is in place."),
        ],
    },
    {
        "slug": "real-estate", "name": "Real Estate Brokerages", "accent": AMBER,
        "title": "AI for Real Estate Brokerages, With Proof of Policy",
        "description": "AI for real estate brokerages: one policy across agents and offices, governed buyer messages, and an audit trail for each AI-assisted text. Book a demo.",
        "h1": "AI for Real Estate Brokerages That Want Proof, Not Promises",
        "intro": "Agents use AI for listing copy, lead follow-up and buyer texts. RenOS lets brokerages show that every AI-assisted listing and conversation followed the same policy.",
        "pains": [
            "One AI-written listing with the wrong wording and I'm the one who's liable.",
            "Agents use AI for buyer texts and I have no way to check any of it.",
            "Our insurance covers the risk. Our software doesn't.",
        ],
        "helps": [
            ("Govern More Than Listing Copy", "Lead routing, CRM notes and buyer and tenant messages all run under the same rules."),
            ("Consistent Policy Across Agents and Offices", "One set of rules for the whole brokerage, enforced before any model is called."),
            ("An Audit Trail per Message", "Every AI-assisted message has a record of who asked, what was asked and which policy applied."),
        ],
        "modes": ["Chat Mode", "Builder Mode"],
        "faq": [
            ("Do fair housing rules apply to AI-written ads?", "Advertising rules apply however the copy was written. RenOS helps by applying your policy consistently and keeping a record of every AI-assisted message."),
            ("Can agents keep their own tools?", "Agents work in one workspace across many models, so you get one policy instead of a different tool on every phone."),
            ("How do we roll this out across offices?", "Start with a 60-day pilot in one team, then extend the same policies brokerage-wide."),
        ],
    },
    {
        "slug": "property-management", "name": "Property Management", "accent": GREEN,
        "title": "AI for Property Management: Fair, Documented Messages",
        "description": "AI for property management: policy and an audit trail across tenant and prospect messages, plus private deployment for tenant data. Start a 60-day pilot.",
        "h1": "AI for Property Management That Shows Fair Treatment",
        "intro": "Leasing and maintenance teams send a lot of messages. RenOS lets property managers use AI for that work while keeping a clear record that every tenant and prospect was treated under the same policy.",
        "pains": [
            "Leasing agents are buried in email and I can't see what they're telling prospects.",
            "The same maintenance messages get written by hand a hundred times a week.",
            "If a tenant says they were treated differently, I need to show exactly what happened.",
        ],
        "helps": [
            ("Policy Across Tenant and Prospect Messages", "Every AI-assisted message follows the same rules, set once."),
            ("An Audit Trail for Every Conversation", "Show who asked, what was sent and which policy applied."),
            ("Private Deployment for Tenant Data", "Keep tenant information inside your own environment when policy calls for it."),
        ],
        "modes": ["Chat Mode", "Agent Mode"],
        "faq": [
            ("Can agents handle repetitive maintenance messages?", "Yes. Agent mode can handle repeatable workflows, and every step is recorded."),
            ("How does RenOS help with fair treatment questions?", "Every AI-assisted message is logged with the policy that applied, so you can show what happened."),
            ("Where does tenant data go?", "Your policy decides which models can see it, and private deployment keeps it in your environment."),
        ],
    },
    {
        "slug": "professional-services", "name": "Professional Services", "accent": BLUE,
        "title": "AI for Professional Services Firms: Per-Matter Records",
        "description": "AI for professional services firms: route privileged work to approved models, keep a per-matter audit record, and govern every tool at once. Book a demo.",
        "h1": "AI for Professional Services Firms, Matter by Matter",
        "intro": "Law, accounting and tax firms need to show clients which systems touched their work and under what policy. RenOS routes privileged work to approved models and keeps the record per matter.",
        "pains": [
            "One person pastes a filing into the wrong tool and we have a privilege problem.",
            "Our AI policy means little if I can't see how people actually use AI.",
            "We have cover for the risk. We don't have tooling for it.",
        ],
        "helps": [
            ("Privileged Work on Approved Models", "Route privileged or confidential work only to models you approve, or to a private deployment."),
            ("A Per-Matter Audit Record", "Show a client, in writing, which systems touched their matter and under which policy."),
            ("One Layer Across Every Tool", "Govern every model the firm uses in one place instead of adding another point tool."),
        ],
        "modes": ["Builder Mode", "Chat Mode"],
        "faq": [
            ("Can we keep client work off public models?", "Yes. Policy routes confidential work only to the models you approve, or to a private deployment."),
            ("Can we report AI use to a client?", "Audit entries record who ran each task, on which model and under which policy, and they export cleanly."),
            ("Does this replace our existing tools?", "RenOS sits across the models your firm uses and governs them in one place."),
        ],
    },
    {
        "slug": "insurance", "name": "Insurance and Financial Services", "accent": PINK,
        "title": "AI for Insurance and Financial Services Firms | RenOS",
        "description": "AI for insurance and financial services: model and supplier provenance logged per task, policy by data sensitivity, and exportable records. Book a demo.",
        "h1": "AI for Insurance and Financial Services, Ready for the Question",
        "intro": "Sooner or later, someone will ask where your AI outputs came from. RenOS logs model and supplier provenance for every task, so insurers and financial firms already have the answer.",
        "pains": [
            "If an examiner asks for model provenance, we don't have a clean answer.",
            "Our compliance budget covers surveillance tools. Nothing covers AI.",
            "Nobody knows which advisors use AI on client communications.",
        ],
        "helps": [
            ("Provenance Logged per Task", "Every task records which model and supplier handled it, and why."),
            ("Policy by Data Sensitivity", "Client and financial data goes only where your rules allow."),
            ("Exportable Records", "Audit logs export cleanly for reviews and examinations."),
        ],
        "modes": ["Chat Mode", "Builder Mode"],
        "faq": [
            ("What does RenOS record for each task?", "The user, the task, the model or models used, the policy applied, the output reference and any overrides."),
            ("Can advisors use AI on client messages?", "Yes, under your policy. Each AI-assisted message is logged with the rule that applied."),
            ("Can client financial data go through a pilot?", "No. Regulated data stays out of pilots until the right agreement is in place."),
        ],
    },
    {
        "slug": "fintech", "name": "Fintech", "accent": CYAN,
        "title": "AI for Fintech Teams: Budgets, Reviews and Records",
        "description": "AI for fintech teams: budget caps enforced per agent and team, every human review logged, and vendor-neutral governance across models. Book a demo.",
        "h1": "AI for Fintech Teams Moving Faster Than Their Controls",
        "intro": "Fintech teams adopt AI quickly, and the controls lag behind. RenOS enforces budgets per agent and team, logs who reviewed what, and works across clouds and models.",
        "pains": [
            "Even on one cloud's AI stack, our monitoring is thin.",
            "Agent budgets live in a spreadsheet. The system doesn't enforce them.",
            "When a regulator asks, we rebuild our AI inventory from chat logs.",
        ],
        "helps": [
            ("Budget Caps per Agent and Team", "Spend limits are enforced and recorded by the system, not tracked by hand."),
            ("Every Review Logged", "Who reviewed which output, and what they changed, is part of the record."),
            ("Vendor-Neutral Governance", "One policy layer across clouds and models."),
        ],
        "modes": ["Agent Mode", "Builder Mode"],
        "faq": [
            ("Does RenOS work across cloud providers?", "Yes. RenOS sits across the models and suppliers you use and applies one policy to all of them."),
            ("Can we cap what agents spend?", "Yes. Budget caps apply per team and per agent, and every task's cost is recorded."),
            ("Can we produce an AI inventory on request?", "The admin view and exportable audit logs show which models were used, by whom and for what."),
        ],
    },
    {
        "slug": "telecom", "name": "Telecom", "accent": AMBER,
        "title": "AI for Telecom: Customer Data on Your Infrastructure",
        "description": "AI for telecom care and network teams: keep customer network data in a private deployment, with policy and audit across operations. Book a demo.",
        "h1": "AI for Telecom Teams That Handle Customer Network Data",
        "intro": "Care and network operations teams handle data that carries real obligations. RenOS keeps that data in a private deployment on infrastructure you control, with policy and audit across every team.",
        "pains": [
            "Answering one call-log question means three systems and a compliance sign-off.",
            "Support reps draft replies in consumer AI tools.",
            "I don't want customer data showing up in an audit finding.",
        ],
        "helps": [
            ("Private Deployment on Your Infrastructure", "Keep customer network data inside your own environment."),
            ("Policy Across Care and Network Teams", "One set of rules for every team that touches customer data."),
            ("An Audit Trail for Every Task", "Show who used AI, on what data, under which policy."),
        ],
        "modes": ["Chat Mode", "Agent Mode"],
        "faq": [
            ("Can customer data stay on our infrastructure?", "Yes. Private or local deployment keeps data inside your environment."),
            ("Can support reps use AI for replies?", "Yes, under your policy. Each reply is logged with the rule that applied."),
            ("Can customer network data go through a pilot?", "No. Regulated data stays out of pilots until the right agreement is in place."),
        ],
    },
    {
        "slug": "msps", "menu": "Governed AI as a managed service", "name": "MSPs and IT Partners", "accent": VIOLET,
        "title": "AI for MSPs: Governed AI as a Managed Service",
        "description": "AI for MSPs: add governed AI as a service line next to security and compliance, with one admin view across clients and no mixing of data. Book a demo.",
        "h1": "AI for MSPs Ready to Offer Governed AI",
        "intro": "Your clients' staff are already pasting data into free AI tools. RenOS lets MSPs offer governed AI as a managed service, with one admin view across clients and each client's data kept separate.",
        "pains": [
            "My techs are drowning in tickets across dozens of clients.",
            "Headcount can't scale with client count.",
            "Clients' staff paste data into free AI tools and it lands on us when something goes wrong.",
        ],
        "helps": [
            ("A New Service Line", "Offer governed AI alongside the security and compliance services you already run."),
            ("One Admin View Across Clients", "Manage policy and spend for every client without mixing client data."),
            ("Agents for Repeat Work", "Agent mode handles repeatable tasks with every action recorded."),
        ],
        "modes": ["Agent Mode", "Chat Mode"],
        "faq": [
            ("Is there a partner program?", "Yes. See the partners page for how MSPs and IT consultancies work with RenOS."),
            ("Are client environments kept separate?", "Yes. You get one admin view across clients without mixing their data."),
            ("Can clients run RenOS privately?", "Private or local deployment keeps each client's data inside their environment."),
        ],
    },
]

# ------------------------------------------------------------------ Navigation

NAV = [
    ("Product", [
        ("Platform", [("Product Overview", "/product", "One workspace for every AI tool")] +
         [(t, h, d) for t, h, d in FEATURES]),
        ("Modes", [(t, h, d) for t, h, d in MODES]),
    ]),
    ("Teams", [
        ("By Team", [("All Teams", "/teams", "How RenOS fits each team")] +
         [(t["name"], f"/teams/{t['slug']}", t["h1"]) for t in TEAMS[:3]]),
        ("", [(t["name"], f"/teams/{t['slug']}", t["h1"]) for t in TEAMS[3:]]),
    ]),
    ("Industries", [
        ("By Industry", [("All Industries", "/industries", "Governed AI for your sector")] +
         [(i["name"], f"/industries/{i['slug']}", i.get("menu", "AI for " + i["name"].lower())) for i in INDUSTRIES[:4]]),
        ("", [(i["name"], f"/industries/{i['slug']}", i.get("menu", "AI for " + i["name"].lower())) for i in INDUSTRIES[4:]]),
    ]),
    ("Resources", [
        ("Learn", [
            ("Resources", "/resources", "Guides for using AI at work"),
            ("What Is an AI Operating System", "/ai-operating-system", "A plain guide"),
            ("Security and Data", "/security", "Where your data goes"),
        ]),
        ("Company", [
            ("About RenOS", "/about", "Why we built it"),
            ("Partners", "/partners", "For MSPs and IT consultancies"),
            ("60-Day Pilot", "/pilot", "How a pilot works"),
        ]),
    ]),
    ("Pricing", "/pricing"),
]

FOOTER = [
    ("Product", [("Overview", "/product")] + [(t, h) for t, h, _ in MODES] + [(t, h) for t, h, _ in FEATURES]),
    ("Teams", [("All Teams", "/teams")] + [(t["name"], f"/teams/{t['slug']}") for t in TEAMS]),
    ("Industries", [("All Industries", "/industries")] + [(i["name"], f"/industries/{i['slug']}") for i in INDUSTRIES]),
    ("Resources", [("Resources", "/resources"), ("AI Operating System Guide", "/ai-operating-system"),
                   ("Security and Data", "/security")]),
    ("Company", [("About", "/about"), ("Partners", "/partners"), ("Pricing", "/pricing"),
                 ("60-Day Pilot", "/pilot"), ("Contact", "/contact"), ("Vocom AI", "https://www.vocom.ai")]),
]

# ------------------------------------------------------------------ Page helpers

def mode_cards(exclude=None, h2="How It Fits With the Other Modes", lede=None):
    return {"type": "cards", "h2": h2, "lede": lede, "items": [
        {"title": t, "text": d, "href": h, "more": f"See {t}"} for t, h, d in MODES if t != exclude]}


TIMELINE = [("09:14:02", "Policy Evaluated", "Confidential data matched"),
            ("09:14:03", "Model Executed", "Approved model · cost logged"),
            ("09:16:31", "Accepted by User", "Audit entry written")]


def collection_page(item, kind):
    base = "/teams" if kind == "teams" else "/industries"
    hub = "Teams" if kind == "teams" else "Industries"
    mode_lookup = {t: (h, d) for t, h, d in MODES}
    sections = [
        {"type": "cards", "eyebrow": "Sound Familiar?", "h2": "What We Hear From " + item["name"] + " Leaders",
         "icons": False, "items": [{"title": f"Problem {i + 1}", "quote": q, "text": ""} for i, q in enumerate(item["pains"])]},
        {"type": "cards", "eyebrow": "How RenOS Helps", "h2": "How RenOS Helps " + item["name"] + " Teams",
         "cols": 2 if len(item["helps"]) == 4 else 3,
         "items": [{"title": t, "text": d} for t, d in item["helps"]]},
    ]
    if item.get("note"):
        sections.append({"type": "prose", "html": f'<p class="callout">{item["note"]}</p>', "tight": True})
    sections += [
        {"type": "cards", "eyebrow": "Recommended Modes", "h2": "Where to Start",
         "lede": 'Every mode runs under the same <a href="/product/routing">policy routing</a> and writes to the same <a href="/product/audit-trail">AI audit trail</a>.',
         "items": [{"title": m, "text": mode_lookup[m][1], "href": mode_lookup[m][0], "more": f"See {m}"} for m in item["modes"]]},
        {"type": "faq", "h2": "Frequently Asked Questions", "items": item["faq"]},
    ]
    name = item["name"]
    return {
        "route": f"{base}/{item['slug']}", "crumb": name, "crumbs": [(hub, base)],
        "title": item["title"], "description": item["description"],
        "hero": {"eyebrow": f"RenOS for {name}", "h1": item["h1"], "lede": item["intro"],
                 "buttons": [("Start a Pilot", "/pilot"), ("Book a Demo", "/contact", "ghost")],
                 "visual": {"shot": f"{kind}-{item['slug']}", "fallback": item.get("showcase") or [
                     ("label", "ROUTING RATIONALE"),
                     ("note", "Sensitive data detected, so policy sent this task to an approved model."),
                     ("kv", "Team", name), ("kv", "Policy", "Data sensitivity"), ("ok", "Audit entry written")]}},
        "sections": sections,
        "cta": {"h2": "Start a 60-Day Pilot With Your " + ("Team" if kind == "teams" else "Organization"),
                "text": 'Bring one real workflow. We\'ll set up policy together and you\'ll see the routing rationale and audit trail on your own work. <a href="/pilot">How the pilot works</a>.'},
    }


def feature_page(route, crumb, title, desc, eyebrow, h1, lede, rows_, related, faq_, shot, extra=None, h1_accent=None, hero_visual=None):
    sections = [{"type": "rows", "h2": "How It Works", "items": rows_}]
    if extra:
        sections += extra
    sections += [
        {"type": "cards", "h2": "Related Pages", "items": related},
        {"type": "faq", "h2": "Frequently Asked Questions", "items": faq_},
    ]
    return {"route": route, "crumb": crumb, "crumbs": [("Product", "/product")], "software": True,
            "software_name": f"RenOS {crumb}", "title": title, "description": desc,
            "hero": {"eyebrow": eyebrow, "h1": h1, "h1_accent": h1_accent, "lede": lede,
                     "buttons": [("Start a Pilot", "/pilot"), ("Book a Demo", "/contact", "ghost")],
                     "visual": {"shot": shot, "fallback": hero_visual or rows_[0].get("visual")}},
            "sections": sections}


# ------------------------------------------------------------------ Pages

def pages():
    P = []

    # ---------------- Home
    P.append({
        "route": "/", "title": "RenOS: The AI Operating System for Teams",
        "description": "RenOS is the AI operating system for teams. Run AI agents on any model, routed by your rules, explained in plain language and logged. Start a pilot.",
        "hero": {
            "eyebrow": "AI Operating System", "h1": "The AI Operating System", "h1_accent": "for Your Team",
            "lede": "Run AI agents across any model your team uses. RenOS picks the model for each task under your rules, explains why in plain language, and logs everything automatically.",
            "buttons": [("Start a Pilot", "/pilot"), ("Book a Demo", "/contact", "ghost")],
            "proof": ["Every task policy-checked", "Every task logged", "Hundreds of models, one workspace"],
            "visual": {"shot": "home-hero", "fallback": "globe", "alt": "The RenOS workspace showing a task routed to an approved model with its routing rationale"},
        },
        "sections": [
            {"type": "cards", "eyebrow": "The Problem", "h2": "Your Team Already Uses AI. Can You Prove What It Did?",
             "lede": "AI arrives one subscription at a time. Separate bills, separate tools, and nobody able to show who ran what, on which model, with what data.",
             "icons": False, "items": [
                 {"title": "Shadow AI", "text": "Staff paste client and customer data into consumer chatbots, with no agreement in place."},
                 {"title": "Subscription Sprawl", "text": "You pay for several AI tools and can't see how any of them are used."},
                 {"title": "No Answer for the Auditor", "text": "When someone asks what the AI did with that data, nobody can say."}]},
            {"type": "cards", "id": "how-it-works", "eyebrow": "How It Works", "h2": "How RenOS Works",
             "lede": "People pick a mode and describe the task. Policy and routing happen in the background, and the record writes itself.",
             "cols": 4, "items": [
                 {"num": "01", "title": "Submit a Task", "text": "Pick Chat, Builder or Agent mode and describe the work. No model to choose.", "demo": ("Chat · Builder · Agent", "Draft a renewal notice for our Maple Court tenants")},
                 {"num": "02", "title": "Policy Decides", "text": 'Your rules by data sensitivity, task type and role pick the model before anything is sent. See <a href="/product/routing">policy routing</a>.', "demo": ("Policy checked", "Confidential · approved model")},
                 {"num": "03", "title": "Routing Rationale", "text": "A plain-language reason comes with every decision.", "demo": ("Rationale", "Tenant data, so an approved model")},
                 {"num": "04", "title": "Audit Trail", "text": 'An entry is written automatically, readable by someone who wasn\'t in the room. See the <a href="/product/audit-trail">AI audit trail</a>.', "demo": ("Logged", "Result accepted · no overrides")}]},
            mode_cards(h2="Chat, Builder and Agent Modes",
                       lede="Three ways to work, one set of rules. Every mode is an AI assistant your admin can govern."),
            {"type": "split", "eyebrow": "Cost and Independence", "h2": "Spend Less on Every AI Task",
             "lede": "Stop paying for several subscriptions to get the capability of one, and stop being locked into the vendor you started with.",
             "bullets": ["One workspace across hundreds of AI models.", "Per-team spend caps, enforced by the system.",
                         'Cheaper models for low-stakes work, set by <a href="/product/admin">company AI controls</a>.'],
             "visual": [("label", "SPEND THIS MONTH"), ("bar", "Sales", "72%"), ("bar", "Operations", "48%"),
                        ("bar", "Finance", "30%"), ("kv", "Low-stakes tasks", "Routed to lower-cost models")]},
            {"type": "split", "eyebrow": "Risk and Accountability", "h2": "Govern and Audit Every Agent",
             "lede": "Every task is one governed record: who ran it, on which model, under which policy, with what outcome.",
             "bullets": ["Plain-language summary of what happened and why that model was chosen.",
                         "Step-by-step timeline from request to accepted result.",
                         "Exportable logs your compliance team can review."],
             "summary": "A property manager asked for a renewal notice. Because it involved confidential tenant data, policy required an approved model. It ran in seconds and was accepted with no overrides.",
             "timeline": TIMELINE},
            {"type": "cards", "eyebrow": "Teams", "h2": "Built for the Teams That Answer for Their AI",
             "lede": 'See how RenOS fits <a href="/teams">every team</a> that uses AI at work.',
             "items": [{"title": t["name"], "text": t["intro"].split(". ")[0] + ".", "href": f"/teams/{t['slug']}", "accent": t["accent"], "more": f"RenOS for {t['name']}"} for t in TEAMS]},
            {"type": "chips", "eyebrow": "Industries", "h2": "Governed AI for Regulated Industries",
             "lede": 'Organizations with a compliance duty, client confidentiality, or a growing AI bill. <a href="/industries">See all industries</a>.',
             "items": [(i["name"], f"/industries/{i['slug']}") for i in INDUSTRIES]},
            {"type": "split", "eyebrow": "60-Day Pilot", "h2": "Start With a 60-Day Pilot",
             "lede": "Up to 15 seats, Pro features, usage credits and a written success plan. Bring one real workflow and see governed AI on your own work.",
             "bullets": ["Kickoff and a written success plan in week one.", "Your first real workflow live early.",
                         "Review the audit trail with your compliance contact."],
             "buttons": [("See How the Pilot Works", "/pilot")],
             "visual": [("label", "PILOT PLAN"), ("kv", "Length", "60 days"), ("kv", "Seats", "Up to 15"),
                        ("kv", "Includes", "Pro features, usage credits"), ("ok", "Written success plan")]},
            {"type": "faq", "h2": "RenOS Frequently Asked Questions", "items": [
                ("What is RenOS?", 'RenOS is an AI operating system for teams. It gives your people one workspace across many AI models, routes each task by your rules, explains every decision in plain language and writes an audit entry automatically. Read <a href="/ai-operating-system">what an AI operating system is</a>.'),
                ("How is it different from a single AI assistant?", "An assistant answers questions. RenOS sits across every assistant and model your team uses and adds the policy layer, audit trail and admin view across all of them."),
                ("Which AI models does it work with?", 'RenOS reaches hundreds of models through one workspace, across text and reasoning, image, audio and video. See <a href="/models">supported AI models</a>.'),
                ("Where does our data go?", "You choose which models and suppliers each task may use, by data sensitivity, task type or role. Every choice is logged with its reason."),
                ("Can it run in our own environment?", "Yes. Private or local deployment keeps data inside your environment."),
                ("How do we get started?", 'Start with a <a href="/pilot">60-day pilot</a>: up to 15 seats, a written success plan and one real workflow.'),
            ]},
        ],
    })

    # ---------------- Product Overview
    P.append({
        "route": "/product", "crumb": "Product", "software": True,
        "title": "RenOS Product: AI Tools Your Team Can Govern",
        "description": "RenOS brings the AI tools your team uses into one governed workspace: policy routing, an audit trail, cost control and three modes. Book a live demo.",
        "hero": {"eyebrow": "Product", "h1": "One Workspace for Every", "h1_accent": "AI Tool Your Team Uses",
                 "lede": "Your team doesn't need more AI tools. It needs one place to use them, with rules that run before any model is called and a record that writes itself.",
                 "buttons": [("Book a Demo", "/contact"), ("Start a Pilot", "/pilot", "ghost")],
                 "visual": {"shot": "product-hero", "fallback": "workspace"}},
        "sections": [
            {"type": "cards", "eyebrow": "The Problem", "h2": "AI Tools Arrive One Subscription at a Time",
             "lede": "Each team picks its own AI tools. Soon there are several bills, several places your data lives, and no single view of any of it.",
             "icons": False, "items": [
                 {"title": "Scattered Tools", "text": "Every department has its own assistant, login and settings."},
                 {"title": "Scattered Data", "text": "Customer and company data ends up in places nobody approved."},
                 {"title": "Scattered Bills", "text": "Overlapping subscriptions with no view of what they produce."}]},
            {"type": "cards", "eyebrow": "Four Jobs", "h2": "What RenOS Does for Company AI", "cols": 2, "items": [
                {"title": "Routing", "text": "Every task goes to the right model under your rules.", "href": "/product/routing", "more": "See policy routing"},
                {"title": "Governance", "text": "Rules by data sensitivity, task type and role, enforced before any model is called.", "href": "/security", "more": "See security and data"},
                {"title": "Audit", "text": "An entry for every task, readable by someone who wasn't in the room.", "href": "/product/audit-trail", "more": "See the AI audit trail"},
                {"title": "Cost Control", "text": "Per-team spend caps and the cost of every task in one view.", "href": "/product/admin", "more": "See the admin dashboard"}]},
            {"type": "flow", "eyebrow": "Product Flow", "h2": "Follow One Task Through RenOS",
             "lede": "From the admin's first budget to the record an auditor reads. This is what your team and your admin actually see.",
             "steps": [
                 ("Sign In", "signin", "People sign in with their company account. Their role and policies are already set."),
                 ("Set Budgets and Caps", "budgets", 'The admin sets monthly budgets per team, with alerts and a hard ceiling for each agent task. See the <a href="/product/admin">admin dashboard</a>.'),
                 ("Choose Allowed Models", "supply", 'Each data class gets its own list of allowed models. Regulated data stays on approved models or your own keys.'),
                 ("Run a Task", "task", 'Policy picks the model, explains why in plain language and checks the budget before anything runs. See <a href="/product/routing">policy routing</a>.'),
                 ("Read the Audit Record", "audit", 'Who ran what, on which model, under which policy and at what cost. See the <a href="/product/audit-trail">AI audit trail</a>.'),
                 ("Hit a Budget Limit", "limit", "When a team reaches its cap, work pauses instead of overspending. The user picks a cheaper route or asks an owner to approve more."),
             ]},
            mode_cards(h2="Three Modes, One Set of Rules", lede="People choose how they want to work. Policy, routing and the record stay the same."),
            {"type": "split", "eyebrow": "The Admin Loop", "h2": "See What Happened, Change a Rule, Done",
             "lede": "The admin sees what happened across the team without interviewing anyone, adjusts a rule, and it applies to the next task.",
             "bullets": ["Who ran what, on which model, under which policy, at what cost.", "Rule changes take effect on the next task.",
                         'Free admin, auditor and read-only seats. See <a href="/pricing">RenOS pricing</a>.'],
             "visual": [("label", "ADMIN VIEW"), ("kv", "Tasks this week", "All logged"), ("kv", "Policy changes", "Applied to next task"),
                        ("kv", "Spend", "Within team caps"), ("ok", "No interviews needed")]},
            {"type": "faq", "h2": "Frequently Asked Questions", "items": [
                ("Is RenOS another AI assistant?", "No. RenOS is the layer across the AI tools your team uses: one workspace, one policy, one audit trail."),
                ("Do people have to learn which model to use?", "No. They pick a mode and describe the task. Policy picks the model and explains why."),
                ("Can we see a demo on our own work?", 'Yes. <a href="/contact">Book a demo</a> and bring one real task.'),
            ]},
        ],
    })

    # ---------------- Mode and feature pages
    P.append(feature_page(
        "/product/chat", "Chat Mode", "AI Assistant for Teams, Routed to the Right Model",
        "Chat mode is an AI assistant for everyday work: ask in plain language, policy picks the model, and every chat is logged without extra steps. Start a pilot.",
        "Chat Mode", "An AI Assistant That Picks", "Ask in plain language. RenOS sends each request to the right model under your rules, shows you why, and logs the chat without anyone lifting a finger.",
        [
            {"title": "Ask in Plain Language", "text": "Your AI assistant works the way people already do: describe the task and get to work. No model menu, no settings.",
             "visual": "workspace"},
            {"title": "The Right Model, With the Reason Shown", "text": 'Policy picks the model for each request and shows a plain-language reason. Learn how <a href="/product/routing">policy routing</a> decides.',
             "visual": "task"},
            {"title": "Every Chat Logged Without Extra Steps", "text": 'Each chat writes an entry to the <a href="/product/audit-trail">AI audit trail</a>. Nobody fills in a form.',
             "visual": "audit"},
        ],
        [{"title": "Builder Mode", "text": "Work with more than one model side by side.", "href": "/product/builder", "more": "See Builder Mode"},
         {"title": "Agent Mode", "text": "Several AI agents on one task, each with its own identity.", "href": "/product/agents", "more": "See Agent Mode"},
         {"title": "RenOS for Operations", "text": "AI for work that operations teams run every day.", "href": "/teams/operations", "more": "See the operations page"}],
        [("Is Chat mode my AI or the company's?", "It's your AI assistant inside the company's rules. You use it like any assistant; your admin decides which models it may use."),
         ("Can I choose the model myself?", "You don't need to. Policy picks the right model for each task and explains why."),
         ("Is every chat recorded?", "Yes. Each chat writes an audit entry automatically, with the policy that applied.")],
        "product-chat", h1_accent="the Right Model for You"))

    P.append(feature_page(
        "/product/builder", "Builder Mode", "Builder Mode: Run AI Tasks Across Models",
        "Builder mode lets your team run AI tasks across more than one model side by side, compare the results, iterate and accept, with every version recorded.",
        "Builder Mode", "Build With More Than One", "Working with AI is better when you can compare. Builder mode runs the same task on more than one model in split view, so you pick the best result and keep the record.",
        [
            {"title": "Split View", "text": "Run one AI task on several approved models at once and see the outputs side by side.",
             "visual": [("pill", "Builder · Split view"), ("split", [("MODEL A", "Clear, formal draft"), ("MODEL B", "Shorter, friendlier draft")])]},
            {"title": "Compare and Pick", "text": "Iterate on the version that works, and accept it when it's ready.",
             "visual": [("kv", "Versions", "3"), ("kv", "Accepted", "Model B, version 2"), ("ok", "Choice recorded")]},
            {"title": "Every Version Recorded", "text": 'Each version, model and acceptance is written to the <a href="/product/audit-trail">AI audit trail</a>.',
             "visual": [("label", "AUDIT ENTRY"), ("kv", "Models used", "2"), ("kv", "Policy", "Internal documents"), ("ok", "Written automatically")]},
        ],
        [{"title": "Chat Mode", "text": "An AI assistant that picks the right model.", "href": "/product/chat", "more": "See Chat Mode"},
         {"title": "Agent Mode", "text": "AI agents that work together on one task.", "href": "/product/agents", "more": "See Agent Mode"},
         {"title": "RenOS for Operations", "text": "Use AI for work your team repeats every day.", "href": "/teams/operations", "more": "See the operations page"}],
        [("Which models can Builder mode compare?", "Any models your admin approves for that kind of task."),
         ("Does comparing models cost more?", "Each model run is a task with a cost, shown in the admin view and covered by team spend caps."),
         ("Is the rejected output kept?", "The record shows every version and which one was accepted.")],
        "product-builder", h1_accent="AI Model Side by Side"))

    P.append(feature_page(
        "/product/agents", "Agent Mode", "AI Agents That Work Together, With Rules",
        "Agent mode runs several AI agents on one task, each with its own identity and role, with handoffs, review and every action in one audit trail. Book a demo.",
        "Agent Mode", "AI Agents That Work", "An AI agent is useful. A few working together under rules is better. Agent mode runs several agents on one task, each with its own identity, and keeps every step in one trail.",
        [
            {"title": "Agents With Roles", "text": "Each AI agent has its own identity and role, so you always know which agent did what.",
             "visual": [("pill", "Agent mode"), ("kv", "Researcher", "Gathers sources"), ("kv", "Writer", "Drafts the brief"), ("kv", "Reviewer", "Checks against policy")]},
            {"title": "Handoffs and Review", "text": "Agents pass work to each other and to a person for review before anything is accepted.",
             "visual": [("label", "HANDOFF"), ("note", "Writer passed the draft to Reviewer"), ("ok", "Sent to a person for review")]},
            {"title": "Every Agent's Actions in One Trail", "text": 'One <a href="/product/audit-trail">AI audit trail</a> covers every agent, model and handoff in the task.',
             "visual": [("label", "AUDIT ENTRY"), ("kv", "Agents", "3"), ("kv", "Models used", "2"), ("ok", "Every step logged")]},
        ],
        [{"title": "Chat Mode", "text": "An AI assistant for everyday work.", "href": "/product/chat", "more": "See Chat Mode"},
         {"title": "Builder Mode", "text": "Compare more than one model side by side.", "href": "/product/builder", "more": "See Builder Mode"},
         {"title": "RenOS for IT", "text": "AI system administration without the sprawl.", "href": "/teams/it", "more": "See the IT page"}],
        [("What is an AI agent in RenOS?", "An agent is an AI worker with its own identity and role. Several can work on one task under the same rules."),
         ("Can AI agents talk to each other?", "Yes. Agents hand work to each other, and every handoff is recorded."),
         ("Who checks the agents' work?", "You decide where a person reviews the work before it's accepted, and the review is part of the record.")],
        "product-agents", h1_accent="Together on One Task", hero_visual="workspace"))

    P.append(feature_page(
        "/product/routing", "Policy Routing", "Policy Routing: Use Any AI Model by the Rules",
        "Policy routing lets your team use any AI model under rules for data sensitivity, task type and role, enforced before a model is called. Book a live demo.",
        "Policy Routing", "Use Any Model.", "Different AI models are good at different things. RenOS lets your team run AI on any model you approve, and your rules decide which one each task uses.",
        [
            {"title": "Rules by Sensitivity, Task and Role", "text": "Set rules by data sensitivity, task type and user role. They run at routing time, before any model sees the task.",
             "visual": "supply"},
            {"title": "A Plain-Language Routing Rationale", "text": "Every decision comes with a reason anyone can read.",
             "visual": [("label", "ROUTING RATIONALE"), ("note", "Contains tenant data, so policy sent this to an approved model.")]},
            {"title": "The Right Model for the Stakes", "text": 'Cheaper models for low-stakes work, approved models for sensitive work. Track it in the <a href="/product/admin">admin dashboard</a>.',
             "visual": [("kv", "Low-stakes task", "Lower-cost model"), ("kv", "Sensitive task", "Approved model"), ("ok", "Choice logged with reason")]},
        ],
        [{"title": "AI Audit Trail", "text": "Every routing decision lands in the record.", "href": "/product/audit-trail", "more": "See the audit trail"},
         {"title": "Supported AI Models", "text": "Hundreds of models, one governed workspace.", "href": "/models", "more": "See supported models"},
         {"title": "RenOS for Compliance", "text": "AI governance for compliance teams.", "href": "/teams/compliance", "more": "See the compliance page"}],
        [("Can we really use any model?", "You can use any model your admin approves. Policy decides which one each task may use."),
         ("When are rules enforced?", "At routing time, before any model is called."),
         ("Why do different AI models matter?", "Models differ in strength and cost. Routing lets you match each task to the right one without asking people to choose.")],
        "product-routing", h1_accent="Your Rules Decide Which.", hero_visual="task"))

    P.append(feature_page(
        "/product/audit-trail", "Audit Trail", "AI Audit Trail for Every Agent and Model",
        "The RenOS AI audit trail records every task: user, model, policy, output and overrides, readable by a non-technical reviewer and exportable. Book a demo.",
        "Audit Trail", "An AI Audit Trail Your Admin", "AI and audit don't usually mix well. RenOS writes an audit entry for every task automatically, in language a reviewer can follow without help.",
        [
            {"title": "What Each Entry Holds", "text": "The user, the task, the model or models used, the policy applied, the output reference and any overrides.",
             "visual": [("label", "AUDIT ENTRY"), ("kv", "User", "Leasing team"), ("kv", "Models", "1 approved model"), ("kv", "Policy", "Tenant data"), ("kv", "Overrides", "None")]},
            {"title": "Readable by a Non-Technical Reviewer", "text": "Each entry starts with a plain-language summary of what happened and why that model was chosen.",
             "visual": [("label", "IN PLAIN LANGUAGE"), ("note", "A leasing agent asked for a renewal notice. Policy required an approved model. Accepted with no overrides.")]},
            {"title": "Exportable", "text": 'Audit logs export cleanly for reviews. See <a href="/security">security and data</a> for how logs are kept.',
             "visual": [("kv", "Export", "Ready"), ("kv", "Retention", "Set by plan"), ("ok", "Written automatically")]},
        ],
        [{"title": "Policy Routing", "text": "The rules behind every entry.", "href": "/product/routing", "more": "See policy routing"},
         {"title": "Admin Dashboard", "text": "Company AI controls for spend, policy and access.", "href": "/product/admin", "more": "See the admin dashboard"},
         {"title": "RenOS for Compliance", "text": "Evidence without interviews.", "href": "/teams/compliance", "more": "See the compliance page"}],
        [("Is the audit trail automatic?", "Yes. Every task writes an entry with no extra step for the person doing the work."),
         ("How long are audit logs kept?", "Pro keeps 90 days. Enterprise keeps one year or more, with export."),
         ("Can we use AI for audit work itself?", "Yes. Audit teams use RenOS like any team, and their own tasks are logged the same way.")],
        "product-audit-trail", h1_accent="Can Actually Read", hero_visual="audit"))

    P.append(feature_page(
        "/product/admin", "Admin Dashboard", "Company AI Controls: Spend, Policy and Access",
        "Company AI controls in one dashboard: who ran what, on which model, under which policy and at what cost, with per-team spend caps and free admin seats.",
        "Admin Dashboard", "Company AI,", "Company AI shouldn't need a survey to understand. The admin dashboard shows AI at work across your organization, and lets you change the rules in one place.",
        [
            {"title": "Who Ran What", "text": "Who ran each task, on which model, under which policy, at what cost.",
             "visual": [("label", "THIS WEEK"), ("kv", "Tasks", "All logged"), ("kv", "Teams", "6"), ("kv", "Policy exceptions", "None")]},
            {"title": "Per-Team Spend Caps", "text": "Set caps by team and let the system enforce them.",
             "visual": "budgets"},
            {"title": "Work Pauses at the Cap", "text": "When a team reaches its cap, work pauses instead of overspending. People can pick a cheaper model or ask an owner to approve more, and agent runs stop at their per-task ceiling.",
             "visual": "limit"},
            {"title": "Free Admin, Auditor and Compliance Seats", "text": 'Admin, auditor and read-only compliance seats are always free. See <a href="/pricing">RenOS pricing</a>.',
             "visual": [("kv", "Admin seats", "Free"), ("kv", "Auditor seats", "Free"), ("kv", "Read-only seats", "Free")]},
        ],
        [{"title": "Policy Routing", "text": "Change a rule and it applies to the next task.", "href": "/product/routing", "more": "See policy routing"},
         {"title": "AI Audit Trail", "text": "Every task, readable by a reviewer.", "href": "/product/audit-trail", "more": "See the audit trail"},
         {"title": "RenOS for Finance", "text": "AI spend control down to the task.", "href": "/teams/finance", "more": "See the finance page"}],
        [("What can admins change?", "Which models and suppliers each task may use, rules by data sensitivity, task type and role, and spend caps per team."),
         ("Do admin seats cost extra?", "No. Admin, auditor and read-only compliance seats are always free."),
         ("When do rule changes take effect?", "On the next task.")],
        "product-admin", h1_accent="Under Your Control", hero_visual="oversight"))

    # ---------------- Models
    P.append({
        "route": "/models", "crumb": "Supported AI Models", "software": True,
        "title": "AI Models in RenOS: Hundreds, One Workspace",
        "description": "RenOS gives your team hundreds of AI models in one governed workspace, across text, image, audio and video, with the admin deciding which may be used.",
        "hero": {"eyebrow": "Supported AI Models", "h1": "Hundreds of AI Models,", "h1_accent": "One Governed Workspace",
                 "lede": "RenOS reaches hundreds of AI models through one workspace. Your admin decides which models and suppliers each task may use, and every choice is logged.",
                 "buttons": [("Book a Demo", "/contact"), ("See Policy Routing", "/product/routing", "ghost")],
                 "visual": {"shot": "models-hero", "fallback": [("label", "APPROVED FOR THIS TASK"), ("kv", "Text and reasoning", "Approved"),
                            ("kv", "Image", "Approved"), ("kv", "Audio", "Not for this role"), ("ok", "Choice logged with reason")]}},
        "sections": [
            {"type": "cards", "eyebrow": "By Capability", "h2": "AI Models for Every Kind of Work", "cols": 4, "items": [
                {"title": "Text and Reasoning", "text": "Drafting, summarizing, analysis and planning."},
                {"title": "Image", "text": "Creating and editing images under the same rules."},
                {"title": "Audio", "text": "Transcription and voice work, governed like any task."},
                {"title": "Video", "text": "Video tasks routed to the models you approve."}]},
            {"type": "cards", "h2": "You Decide Which Models Are Used", "items": [
                {"title": "Approve Models and Suppliers", "text": "Set which agent models and suppliers each task may use, by data sensitivity, task type and role."},
                {"title": "Switch Without Retraining", "text": "People keep working the same way when you change suppliers."},
                {"title": "Every Choice Logged", "text": 'Each routing choice and its reason lands in the <a href="/product/audit-trail">AI audit trail</a>.'}]},
            {"type": "faq", "h2": "Frequently Asked Questions", "items": [
                ("How many AI models does RenOS support?", "Hundreds, through one workspace, across text and reasoning, image, audio and video."),
                ("Can we restrict which models are used?", 'Yes. Your admin approves models and suppliers, and <a href="/product/routing">policy routing</a> enforces it.'),
                ("Why use more than one model?", 'Different models are good at different things. <a href="/product/builder">Builder mode</a> lets you compare them side by side.')]},
        ],
    })

    # ---------------- AI operating system guide
    P.append({
        "route": "/ai-operating-system", "crumb": "What Is an AI Operating System",
        "title": "What Is an AI Operating System? A Plain Guide",
        "description": "What is an AI operating system? A plain guide to how it works, how it differs from an AI assistant, who needs one and how to evaluate one for your team.",
        "hero": {"eyebrow": "Guide", "h1": "What Is an AI Operating System?",
                 "lede": "A plain-English guide for people who run teams: what an AI operating system is, how AI works inside one, and how to tell whether your organization needs one."},
        "sections": [
            {"type": "toc", "tight": True, "items": [
                ("what-it-is", "What an AI Operating System Is"), ("vs-assistant", "How It Differs From an AI Assistant"),
                ("four-jobs", "The Four Jobs"), ("who-needs-one", "Who Needs One"), ("mistakes", "Mistakes to Avoid"),
                ("evaluate", "How to Evaluate One"), ("renos", "Where RenOS Fits")]},
            {"type": "prose", "html": GUIDE_HTML},
        ],
    })

    # ---------------- Teams hub and items
    P.append({
        "route": "/teams", "crumb": "Teams",
        "title": "RenOS for Every Team: Sales, IT, Compliance",
        "description": "RenOS is AI for every team: sales, compliance, IT, operations, coaching and finance, all on one governed workspace with one audit trail. Book a demo.",
        "hero": {"eyebrow": "Teams", "h1": "RenOS for Every Team",
                 "lede": "Every AI team looks different. Sales wants speed, compliance wants evidence, finance wants a single bill. RenOS gives each team AI at work under one set of rules.",
                 "buttons": [("Start a Pilot", "/pilot"), ("Book a Demo", "/contact", "ghost")]},
        "sections": [
            {"type": "cards", "h2": "Choose Your Team", "items": [
                {"title": t["name"], "text": t["intro"].split(". ")[0] + ".", "href": f"/teams/{t['slug']}", "accent": t["accent"], "more": f"RenOS for {t['name']}"} for t in TEAMS]},
            {"type": "cards", "h2": "How RenOS Adapts to Each Team", "items": [
                {"title": "Rules by Role", "text": 'Policy routing applies different rules to different roles. See <a href="/product/routing">policy routing</a>.'},
                {"title": "Modes for Each Way of Working", "text": 'Chat, Builder and Agent modes suit different work. See <a href="/product">the product overview</a>.'},
                {"title": "One Record for Everyone", "text": 'Every team writes to the same <a href="/product/audit-trail">AI audit trail</a>.'}]},
            {"type": "faq", "h2": "Frequently Asked Questions", "items": [
                ("Can different teams have different rules?", "Yes. Rules can vary by user role, data sensitivity and task type."),
                ("Do we need a separate tool per team?", "No. Every team works in one workspace with policies that fit it."),
                ("Which team should start the pilot?", "The team with one real, repeatable workflow and someone who'll own the success plan.")]},
        ],
    })
    P += [collection_page(t, "teams") for t in TEAMS]

    # ---------------- Industries hub and items
    P.append({
        "route": "/industries", "crumb": "Industries",
        "title": "RenOS by Industry: Governed AI for Your Sector",
        "description": "Governed AI built around your industry, from dental groups and credit unions to real estate, insurance, fintech and MSPs. Book a live demo of RenOS today.",
        "hero": {"eyebrow": "Industries", "h1": "Governed AI, Built Around", "h1_accent": "Your Industry",
                 "lede": "Organizations with a compliance duty, client confidentiality or a growing AI bill need company AI they can prove. RenOS adapts its policy and records to your sector.",
                 "buttons": [("Book a Demo", "/contact"), ("Start a Pilot", "/pilot", "ghost")]},
        "sections": [
            {"type": "cards", "h2": "Choose Your Industry", "items": [
                {"title": i["name"], "text": i["intro"].split(". ")[0] + ".", "href": f"/industries/{i['slug']}", "accent": i["accent"], "more": f"AI for {i['name']}"} for i in INDUSTRIES]},
            {"type": "cards", "h2": "How RenOS Adapts to Your Industry", "items": [
                {"title": "Policy for Your Obligations", "text": 'Set rules to match your own obligations. See <a href="/product/routing">policy routing</a>.'},
                {"title": "Data Where You Decide", "text": 'Private deployment keeps data in your environment. See <a href="/security">security and data</a>.'},
                {"title": "Evidence on Request", "text": 'Exportable entries from the <a href="/product/audit-trail">AI audit trail</a>.'}]},
            {"type": "faq", "h2": "Frequently Asked Questions", "items": [
                ("Is RenOS certified for regulated industries?", "Not yet. SOC 2 preparation is planned. Today you get policy enforced before any model is called, exportable audit logs and a private deployment option."),
                ("Can regulated data go through a pilot?", "No. Regulated data stays out of pilots until the right agreement is in place."),
                ("Is my industry missing?", 'RenOS works for any organization that has to answer for its AI. <a href="/contact">Get in touch</a>.')]},
        ],
    })
    P += [collection_page(i, "industries") for i in INDUSTRIES]

    # ---------------- Pricing
    P.append({
        "route": "/pricing", "crumb": "Pricing",
        "title": "RenOS Pricing: Pilot, Pro and Enterprise",
        "description": "RenOS pricing for the Pilot, Pro and Enterprise plans, with free admin, auditor and compliance seats. Talk to sales for a quote, or book a live demo today.",
        "hero": {"eyebrow": "Pricing", "h1": "Simple Pricing for Governed AI",
                 "lede": "Pay for governed seats. One subscription covers governance: policy routing, the audit trail and admin oversight. Model usage runs on RenOS Credits, and every task shows exactly what it cost."},
        "sections": [
            {"type": "pricing", "eyebrow": "Plans", "h2": "Choose a Plan", "plans": [
                {"name": "Pilot", "blurb": "Prove it on one team before you commit.", "cta": ("Start a Pilot", "/pilot"),
                 "price": "$1,500", "unit": "flat, 60 days", "terms": "Fully credited to your first annual plan",
                 "features": ["Up to 15 seats, all Pro features", "Usage credits included",
                              "A written success plan with weekly governed-task reports"],
                 "features_priced": ["Up to 15 seats, all Pro features", "$150 of RenOS Credits included",
                                     "A written success plan with weekly governed-task reports", "Your fee credited to year one if you continue"]},
                {"name": "Pro", "tag": "Most Teams Start Here", "blurb": "Governed AI for teams of 5 to 100.", "featured": True,
                 "cta": ("Talk to Sales", "/contact"), "cta_priced": ("Start With Pro", "/contact"),
                 "price": "$35", "price_monthly": "$42", "unit": "per seat / month", "terms": "5-seat minimum",
                 "features": ["Chat, Builder and Agent modes, split view", "Every approved model through RenOS Credits",
                              "Policy routing with plain-language reasons", "Audit trail with 90-day retention",
                              "Admin dashboard and team spend caps", "Usage credits per seat, pooled monthly"],
                 "features_priced": ["Chat, Builder and Agent modes, split view", "Every approved model through RenOS Credits",
                                     "Policy routing with plain-language reasons", "Audit trail with 90-day retention",
                                     "Admin dashboard and team spend caps", "$5 of credits per seat, pooled monthly"]},
                {"name": "Enterprise", "blurb": "For regulated organizations and existing AI contracts.", "cta": ("Talk to Sales", "/contact"),
                 "price": "From $60", "unit": "per seat / month", "terms": "Billed annually · 25-seat minimum",
                 "features": ["Everything in Pro", "Bring your own model keys", "SSO and SCIM provisioning",
                              "Audit retention of one year or more, with export", "Custom policies, data residency and supply controls",
                              "DPA, BAA and an uptime SLA as part of the plan design"]}],
             "extras": [
                 {"title": "Private Deployment", "text": 'Run RenOS on your own infrastructure. Available as an add-on. See <a href="/security">security and data</a>.',
                  "text_priced": 'From $1,500 per environment per month. Run RenOS on your own infrastructure. See <a href="/security">security and data</a>.'},
                 {"title": "Free Admin Seats", "text": "Admins, auditors and read-only compliance reviewers never count as paid seats."}]},
            {"type": "cards", "eyebrow": "RenOS Credits", "h2": "Model Usage, Priced the Way Models Are Priced", "cols": 4,
             "lede": 'You see exactly what every task cost, in the same record that shows why it ran. See the <a href="/product/audit-trail">AI audit trail</a>.',
             "items": [
                 {"title": "Credits Track Real Usage", "text": "Each task spends credits at its model's published rate, so cost follows the work."},
                 {"title": "Cost in the Audit Trail", "text": "Every governed task records the model, the credits spent and the policy that chose it."},
                 {"title": "Budgets You Control", "text": 'Set caps per team and per user, with alerts as they fill up. Agent tasks get a hard ceiling. See the <a href="/product/admin">admin dashboard</a>.'},
                 {"title": "Cheaper Models for Routine Work", "text": 'Policy can send low-stakes tasks to lower-cost models. See <a href="/product/routing">policy routing</a>.'}]},
            {"type": "compare", "eyebrow": "Compare Plans", "h2": "What Changes Between Pro and Enterprise", "cols": ["Pro", "Enterprise"], "rows": [
                ("Governed seats", {"cells": ["Talk to Sales", "Talk to Sales"], "cells_priced": ["$35 / month, annual", "From $60 / month, annual"]}),
                ("Minimum seats", "5", "25"),
                ("Credits included", "Pooled per seat", "Pay as you go"),
                ("Bring your own model keys", None, "Included"),
                ("Audit retention", "90 days", "One year or more, with export"),
                ("Single sign-on and SCIM", None, "Included"),
                ("Model supply controls", "Standard", "Per data class"),
                ("Private or local deployment", None, "Add-on"),
                ("DPA, BAA and SLA", "DPA", "DPA, BAA and uptime SLA")]},
            {"type": "faq", "eyebrow": "Questions", "h2": "Pricing Questions", "items": [
                ("Is there a free plan?", 'No. RenOS governs teams, so a solo free seat wouldn\'t show you what it does. Start with a <a href="/pilot">60-day pilot</a> instead.'),
                ("What happens to unused credits?", "Pro's included credits pool across your team each month. Talk to us about purchased credits."),
                ("Where do the models come from?", 'Through RenOS, or through your own keys on Enterprise. Admins can restrict sensitive data to approved models only. See <a href="/models">supported AI models</a>.'),
                ("Do admins and auditors need a paid seat?", "No. Admin, auditor and read-only compliance seats are always free."),
                ("Can we use our existing AI contracts?", "Yes, on Enterprise. Bring your own keys and RenOS still applies policy and writes the audit trail."),
                ("Can partners offer RenOS to their clients?", 'Yes. MSPs and IT partners can offer RenOS to the organizations they support. See the <a href="/partners">partner program</a>.')]},
        ],
        "cta": {"h2": "Talk to Sales About Your Team", "text": "Tell us about your team and the work you'd test first, and we'll recommend a plan."},
    })

    # ---------------- Pilot
    P.append({
        "route": "/pilot", "crumb": "60-Day Pilot",
        "title": "Get Started With AI: The RenOS 60-Day Pilot",
        "description": "Get started with AI the governed way. The RenOS 60-day pilot covers up to 15 seats, Pro features and a written success plan. Apply for a pilot today.",
        "hero": {"eyebrow": "Design-Partner Pilots Are Open", "h1": "Get Started With", "h1_accent": "a 60-Day Pilot",
                 "lede": "The easiest way to start AI with rules in place. Up to 15 seats, Pro features, usage credits and a written success plan, run on one real workflow.",
                 "buttons": [("Apply for a Pilot", "#apply"), ("Book a Demo First", "/contact", "ghost")],
                 "visual": {"shot": "pilot-hero", "fallback": [("label", "PILOT PLAN"), ("kv", "Length", "60 days"), ("kv", "Seats", "Up to 15"),
                            ("kv", "Includes", "Pro features, usage credits"), ("ok", "Written success plan")]}},
        "sections": [
            {"type": "cards", "eyebrow": "What Happens", "h2": "How the Pilot Runs", "cols": 4, "items": [
                {"num": "01", "title": "Kickoff and Success Plan", "text": "Agree on the workflow, the people and what success means, in writing."},
                {"num": "02", "title": "First Workflow Live", "text": 'Your team starts using <a href="/product/chat">Chat</a>, <a href="/product/builder">Builder</a> or <a href="/product/agents">Agent</a> mode on real work.'},
                {"num": "03", "title": "Review the Audit Trail", "text": 'Walk through the <a href="/product/audit-trail">AI audit trail</a> with your compliance contact.'},
                {"num": "04", "title": "Results and Decision", "text": "Review results against the written plan and decide what's next."}]},
            {"type": "cards", "eyebrow": "What You Bring", "h2": "What Your Team Brings", "items": [
                {"title": "One Real Workflow", "text": "Something your team does often, where AI could help."},
                {"title": "An Admin", "text": "Someone to set policy and watch the admin view."},
                {"title": "A Compliance or Risk Contact", "text": "Someone to review the record with us."}]},
            {"type": "prose", "tight": True, "html": '<h2>What Success Looks Like</h2><p>Success is measured against the written plan you agree to at kickoff, not against someone else\'s numbers. Regulated data stays out of the pilot until the right agreement is in place.</p>'},
            {"type": "form", "id": "apply", "eyebrow": "Apply", "h2": "Apply for a 60-Day Pilot",
             "lede": "Tell us about your team and the task you'd test first.", "submit": "Apply for a Pilot", "fields": [
                 ("name", "Name", "text"), ("email", "Work email", "email"), ("company", "Company", "text"),
                 ("team_size", "Team size", "select", True, [("", "Choose one"), ("1-15", "1 to 15"), ("16-50", "16 to 50"), ("51-200", "51 to 200"), ("200+", "More than 200")]),
                 ("task", "The task you'd test first", "textarea")]},
        ],
        "cta": False,
    })

    # ---------------- Security
    P.append({
        "route": "/security", "crumb": "Security and Data",
        "title": "RenOS Security: Your Data, Your Environment",
        "description": "How RenOS handles your data: policy enforced before any model is called, private deployment for your own AI, and exportable audit logs. Book a live demo.",
        "hero": {"eyebrow": "Security and Data", "h1": "Your Data Stays", "h1_accent": "Where You Decide",
                 "lede": "Running your own AI shouldn't mean giving up control of your data. RenOS enforces policy before any model is called and can run inside your own environment.",
                 "buttons": [("Ask a Security Question", "/contact?type=security"), ("Book a Demo", "/contact", "ghost")]},
        "sections": [
            {"type": "cards", "h2": "How RenOS Handles Your Data", "cols": 3, "items": [
                {"title": "Where Data Goes", "text": "You choose which models and suppliers each task may use, by sensitivity, task type or role."},
                {"title": "Private or Local Deployment", "text": "Keep data inside your own environment when policy calls for it."},
                {"title": "Policy Before Any Model", "text": 'Rules are enforced at routing time. See <a href="/product/routing">policy routing</a>.'},
                {"title": "Admin Control of Suppliers", "text": 'Approve models and suppliers in the <a href="/product/admin">admin dashboard</a>.'},
                {"title": "Exportable Audit Logs", "text": 'Every task is recorded in the <a href="/product/audit-trail">AI audit trail</a> and exports cleanly.'},
                {"title": "SOC 2 Preparation", "text": "SOC 2 preparation is planned. We'll say so here when it's done."}]},
            {"type": "split", "eyebrow": "Supply Policy", "h2": "Decide Which Models See Which Data",
             "lede": "Every data class gets its own list of allowed models. Regulated data stays on approved models, your own keys or a private deployment.",
             "bullets": ["Set by data sensitivity, task type and role.", "Enforced before any model is called.",
                         'Every choice logged with its reason in the <a href="/product/audit-trail">AI audit trail</a>.'],
             "visual": "supply"},
            {"type": "faq", "h2": "Security Questions", "items": [
                ("What is your security posture today?", "SOC 2 preparation is planned. Today you get exportable audit logs, policy enforced before any model is called, a private or local deployment option, and regulated data kept out of pilots until the right agreement is in place."),
                ("Can we run our own AI on our own infrastructure?", "Yes. Private or local deployment keeps data inside your environment."),
                ("Are BAA and DPA available?", "BAA and DPA are part of the Enterprise plan design. Talk to us about your requirements.")]},
        ],
    })

    # ---------------- Partners
    P.append({
        "route": "/partners", "crumb": "Partners",
        "title": "RenOS for MSPs and IT Partners",
        "description": "RenOS for MSPs and IT consultancies: offer governed AI services to every client, manage them all from one admin view, and register deals. Become a partner.",
        "hero": {"eyebrow": "Partners", "h1": "Offer Governed AI", "h1_accent": "to Every Client",
                 "lede": "Your clients want AI services they can trust. RenOS lets MSPs and IT consultancies offer governed AI alongside the security and compliance work you already do.",
                 "buttons": [("Become a Partner", "/contact?type=partner"), ("See AI for MSPs", "/industries/msps", "ghost")]},
        "sections": [
            {"type": "cards", "h2": "Why Partners Work With RenOS", "items": [
                {"title": "A New Service Line", "text": 'Add governed AI next to your security and compliance services. See <a href="/industries/msps">AI for MSPs</a>.'},
                {"title": "One Admin View Across Clients", "text": 'Manage policy and spend for every client from the <a href="/product/admin">admin dashboard</a>, without mixing data.'},
                {"title": "Deal Registration", "text": "Register opportunities so the work you bring stays yours."}]},
            {"type": "faq", "h2": "Partner Questions", "items": [
                ("Who is the partner program for?", "MSPs and IT consultancies that support organizations with security and compliance needs."),
                ("Can we pilot with a client first?", 'Yes. Start with a <a href="/pilot">60-day pilot</a> for one client.'),
                ("How do we apply?", 'Use the <a href="/contact?type=partner">partner contact form</a> and tell us about your clients.')]},
        ],
        "cta": {"h2": "Become a RenOS Partner", "text": 'Tell us about your clients and services. <a href="/contact?type=partner">Contact the partner team</a>.'},
    })

    # ---------------- About
    P.append({
        "route": "/about", "crumb": "About",
        "title": "About RenOS: The Team Behind Governed AI",
        "description": "Why we built RenOS: AI spreads through organizations faster than anyone can track it. RenOS is governed AI from Vocom AI. Read our story, then say hello.",
        "hero": {"eyebrow": "About", "h1": "Why We Built RenOS",
                 "lede": "AI is spreading through organizations one subscription at a time, and almost nobody can prove what it did. We built RenOS to fix that."},
        "sections": [
            {"type": "prose", "html": '''<h2>The Problem We Kept Seeing</h2>
<p>Every team we spoke with was already using AI. Sales had one tool, operations another, and a few people had their own. Data went into all of them. When someone asked what the AI had done with a client's information, nobody could answer.</p>
<h2>Our Approach</h2>
<p>We think governance should come first and stay invisible. People should be able to use any model that suits the task, while the organization decides the rules and gets a record it can trust. That's why RenOS puts <a href="/product/routing">policy routing</a> before every model call and writes an <a href="/product/audit-trail">AI audit trail</a> automatically.</p>
<h2>Where We Are</h2>
<p>Design-partner pilots are open. Multi-agent identities, access to hundreds of models and audit logging have been demoed live, and our design partners help shape what comes next. <a href="/pilot">Join the pilot</a>.</p>
<h2>Who We Are</h2>
<p>RenOS is from <a href="https://www.vocom.ai">Vocom AI</a>.</p>'''},
        ],
    })

    # ---------------- Contact
    P.append({
        "route": "/contact", "crumb": "Contact",
        "title": "Book a RenOS Demo",
        "description": "Book a RenOS demo: in 15 minutes, see one real task routed without picking a model, the routing rationale, the audit entry and the admin view. Book now.",
        "hero": {"eyebrow": "Book a Demo", "h1": "See RenOS Run", "h1_accent": "on Your Own Work",
                 "lede": "A 15-minute demo on one real task from your world. No slides about the future."},
        "sections": [
            {"type": "cards", "eyebrow": "The 15-Minute Demo", "h2": "What You'll See", "cols": 4, "items": [
                {"num": "01", "title": "Your Task", "text": "One real task from your world, submitted without choosing a model."},
                {"num": "02", "title": "The Decision", "text": 'The policy decision and its plain-language <a href="/product/routing">Routing Rationale</a>.'},
                {"num": "03", "title": "The Record", "text": 'The <a href="/product/audit-trail">audit trail</a> entry, written automatically.'},
                {"num": "04", "title": "The Admin View", "text": 'Who ran what, on which model, under which policy, at what cost. See the <a href="/product/admin">admin dashboard</a>.'}]},
            {"type": "form", "id": "form", "h2": "Get in Touch", "submit": "Send Request", "fields": [
                ("name", "Name", "text"), ("email", "Work email", "email"), ("company", "Company", "text"),
                ("team_size", "Team size", "select", True, [("", "Choose one"), ("1-15", "1 to 15"), ("16-50", "16 to 50"), ("51-200", "51 to 200"), ("200+", "More than 200")]),
                ("type", "What can we help with?", "select", True, [("demo", "Book a demo"), ("partner", "Partnership"), ("security", "Security question"), ("other", "Something else")]),
                ("message", "Message", "textarea", False)]},
        ],
        "cta": False,
    })

    # ---------------- Resources
    P.append({
        "route": "/resources", "crumb": "Resources",
        "title": "How to Use AI at Work: RenOS Resources",
        "description": "Guides on how to use AI at work: what an AI operating system is, how teams and industries use governed AI, and how to get started. Read the guides.",
        "hero": {"eyebrow": "Resources", "h1": "Guides for Using AI at Work",
                 "lede": "Plain guides for people who want to use AI at work without losing track of what it does."},
        "sections": [
            {"type": "cards", "h2": "Start Here", "items": [
                {"title": "What Is an AI Operating System?", "text": "How AI works across a team, and when you need one layer across every tool.", "href": "/ai-operating-system", "more": "Read the guide"},
                {"title": "AI Tools for Teams", "text": "How one governed workspace replaces scattered AI tools.", "href": "/product", "more": "See the product"},
                {"title": "Get Started With a Pilot", "text": "How to start AI with rules in place, in 60 days.", "href": "/pilot", "more": "See the pilot"}]},
            {"type": "cards", "h2": "Use AI by Team", "items": [
                {"title": t["name"], "text": t["h1"] + ".", "href": f"/teams/{t['slug']}", "accent": t["accent"], "more": "Read more"} for t in TEAMS]},
            {"type": "chips", "h2": "Use AI by Industry", "items": [(i["name"], f"/industries/{i['slug']}") for i in INDUSTRIES]},
        ],
    })

    # ---------------- 404
    P.append({
        "route": "/404", "crumb": "Page Not Found", "noindex": True,
        "title": "Page Not Found, RenOS", "description": "This page doesn't exist.",
        "hero": {"eyebrow": "404", "h1": "This Page Isn't Here",
                 "lede": 'Try the <a href="/">home page</a>, the <a href="/product">product overview</a>, <a href="/pricing">pricing</a> or <a href="/contact">contact us</a>.',
                 "buttons": [("Go Home", "/"), ("Book a Demo", "/contact", "ghost")]},
        "sections": [], "cta": False,
    })
    return P


GUIDE_HTML = '''
<h2 id="what-it-is">What an AI Operating System Is</h2>
<p>An AI operating system is the layer that sits between the people in your organization and the AI models they use. It doesn't replace those models. It decides which model handles each task, applies your rules before anything is sent, and records what happened.</p>
<p>Think about how a computer's operating system works. Applications don't talk to the hardware directly. The operating system schedules the work, controls access and keeps track of what each program did. An AI based operating system does the same job for AI: people describe the work, and the system handles which model, under which rules, with which record.</p>
<p>That matters because most organizations no longer use one AI tool. They use several, often picked by different teams at different times. Each comes with its own settings, its own bill and its own idea of what gets logged. An operating system for AI brings them under one set of rules.</p>

<h2 id="vs-assistant">How It Differs From an AI Assistant</h2>
<p>An AI assistant answers questions and completes tasks. It's the thing people type into. Most assistants are built around one supplier's models, and their admin tools govern that supplier's stack well.</p>
<p>An AI operating system works one level up. It doesn't compete with assistants; it sits across them. If your team uses more than one AI supplier, and most do, the gap between those suppliers is where the risk sits. Nobody logs across them, nobody applies one policy to all of them, and nobody can answer simple questions like which AI tools touched customer data last week.</p>
<p>To explain AI governance in one line: an assistant helps a person do a task, while an AI operating system helps an organization control and prove how every task was done.</p>

<h2 id="four-jobs">The Four Jobs</h2>
<p>Strip away the jargon and an AI operating system does four jobs.</p>
<h3>Routing</h3>
<p>Every task goes to a model. Routing decides which one, based on what the task is and what data it involves. Good routing means people never have to choose a model themselves, and cheaper models handle low-stakes work while approved models handle sensitive work.</p>
<h3>Governance</h3>
<p>Rules decide what is allowed: which models and suppliers may see which data, for which roles and which kinds of task. The important part is when those rules run. If they run before any model is called, a task that breaks policy never leaves the building.</p>
<h3>Audit</h3>
<p>Every task should leave a record: who ran it, what they asked for, which model or models handled it, which policy applied, what came back and whether anyone overrode the decision. The record should be readable by someone who wasn't in the room, not only by an engineer.</p>
<h3>Cost Control</h3>
<p>When AI runs through one layer, spend becomes visible. You can see the cost of each task, set caps by team, and stop paying for several overlapping subscriptions to get the capability of one.</p>

<h2 id="who-needs-one">Who Needs One</h2>
<p>Not every organization needs an AI operating system. A single person using one assistant for personal productivity doesn't. The need shows up when a few things are true at once:</p>
<ul>
<li>More than a handful of people use AI for work.</li>
<li>They use more than one tool or supplier.</li>
<li>Someone in the organization has to answer for how client, customer or patient data is handled.</li>
<li>The AI bill is growing and nobody can say what it buys.</li>
</ul>
<p>That describes most multi-person organizations with a compliance duty, client confidentiality or a budget owner who asks questions. Healthcare groups, financial institutions, law and accounting firms, property managers and the IT partners who support them tend to feel it first.</p>

<h2 id="mistakes">Mistakes to Avoid</h2>
<h3>Blocking Instead of Governing</h3>
<p>Blocking consumer AI feels safe, but it usually moves usage onto personal devices where you can see even less. People adopt AI because it helps them. Give them a governed way to use it.</p>
<h3>A Policy You Can't Evidence</h3>
<p>A written AI policy is a good start. If you can't show that people followed it, it won't hold up when someone asks.</p>
<h3>Picking One Vendor's Admin Tools and Stopping There</h3>
<p>Vendor admin tools are often strong inside their own walls. The risk sits between vendors, which no single vendor's tools can see.</p>
<h3>Adding Steps for Users</h3>
<p>If governance means extra forms, people will route around it. The record should be a byproduct of normal work.</p>

<h2 id="evaluate">How to Evaluate One</h2>
<p>When you look at any AI operating system, ask these questions:</p>
<ol>
<li>Are rules enforced before a model is called, or only reported afterward?</li>
<li>Can a non-technical reviewer read the audit record without help?</li>
<li>Does it work across the models and suppliers you already use?</li>
<li>Can you keep sensitive work inside your own environment?</li>
<li>Can you see cost per task and cap spend by team?</li>
<li>Does it add any steps for the people doing the work?</li>
<li>Can you export the records?</li>
</ol>
<p>Ask for a demo on one of your real tasks, not a scripted one. You'll learn more in fifteen minutes than from any feature list.</p>

<h2 id="renos">Where RenOS Fits</h2>
<p>RenOS is an AI operating system for teams. People pick <a href="/product/chat">Chat</a>, <a href="/product/builder">Builder</a> or <a href="/product/agents">Agent</a> mode and describe the task. <a href="/product/routing">Policy routing</a> picks the model under your rules and explains why in plain language. Every task writes an entry to the <a href="/product/audit-trail">AI audit trail</a>, and the <a href="/product/admin">admin dashboard</a> shows who ran what, on which model, at what cost. It reaches <a href="/models">hundreds of AI models</a> through one workspace.</p>
<p>Design-partner pilots are open. <a href="/pilot">Start with a 60-day pilot</a> or <a href="/contact">book a demo</a>.</p>
'''
