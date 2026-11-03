"""RenOS site content.

Routes, titles, H1s and keywords follow the RenOS sitemap and keyword map.
Copy follows the RenOS claims guardrails: no certifications, prices, customer
results, vendor names or roadmap features presented as shipped.
"""
from stars import STARS  # noqa: F401

# Where lead forms post. Leave empty until a form backend is confirmed;
# the forms then tell visitors nothing was sent instead of failing silently.
FORM_ENDPOINT = ""

# Prices and dollar figures from the Atlas design. Set to False to hide every
# price on the site (cards, tables, receipts and FAQs fall back to "Talk to Sales").
SHOW_PRICES = True

# Where the RenOS app lives. The website's Sign In page hands off to {APP_URL}/login.
# Planned address once DNS and HTTPS (nginx) are set up on the app server.
APP_URL = "https://app.rengroup.ai"

# Single source of truth for facts reused across pages.
FACTS = {
    "tagline": "The Governance Layer for AI at Work",
    "footer": "The governance layer for AI at work. Use every model, and prove what each one did.",
    "status": "Pilots are open",
    "pilot_days": 60,
    "pilot_seats": 15,
    "free_seats": "Admin, auditor and read-only compliance seats are always free.",
    "model_reach": "hundreds of AI models through one workspace",
}

CYAN, VIOLET, GREEN, AMBER, PINK, BLUE = "#5ee0ff", "#8f80f7", "#5fd0a0", "#f2b45a", "#f08bb8", "#6aa8ff"
ACCENTS = [CYAN, VIOLET, GREEN, AMBER, PINK, BLUE]

MODES = [
    ("Chat Mode", "/product/chat", "An answer, a draft or a thinking partner. Lowest cost."),
    ("Builder Mode", "/product/builder", "A finished thing: a doc, app, report or workflow. Plan first."),
    ("Agent Mode", "/product/agents", "Something done or watched in other systems. Always capped."),
]
FEATURES = [
    ("Policy Routing", "/product/routing", "Your rules pick the model before anything is sent."),
    ("Audit Trail", "/product/audit-trail", "Every task writes a record anyone can read."),
    ("Admin Dashboard", "/product/admin", "Sessions, cost and policy activity in one place."),
    ("Supported AI Models", "/models", "Hundreds of models, one governed workspace."),
    ("How Credits Work", "/product/credits", "From top-up to audit record, step by step."),
]

# ------------------------------------------------------------------ Teams

TEAMS = [
    {
        "slug": "sales", "menu": "Faster outreach, clear records", "name": "Sales", "accent": CYAN,
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
        "slug": "compliance", "menu": "Evidence without interviews", "showcase": "audit", "name": "Compliance", "accent": VIOLET,
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
        "slug": "it", "menu": "Models, access and SSO in one place", "showcase": "signin", "name": "IT and Security", "accent": BLUE,
        "title": "AI System Administration for IT Teams | RenOS",
        "description": "AI system administration for IT teams: approve models and suppliers in one place, add SSO and SCIM on Enterprise, and deploy privately. Book a pilot.",
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
        "slug": "operations", "menu": "Everyday work your team can run", "showcase": "workspace", "name": "Operations", "accent": GREEN,
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
        "slug": "leadership-coaching", "menu": "Coaching AI with guardrails", "name": "Leadership and Coaching", "accent": PINK,
        "title": "Leadership Coaching AI With Clear Guardrails | RenOS",
        "description": "Leadership coaching AI for leaders and coaches: governed coaching workflows, private notes kept by policy, and a record of every session. Book a pilot.",
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
        "slug": "finance", "menu": "Spend control down to the task", "showcase": "budgets", "name": "Finance", "accent": AMBER,
        "title": "AI Spend Control and Cost per Task for Finance Teams",
        "description": "AI spend control for finance teams: one bill instead of many subscriptions, per-team spend caps, and the cost of every AI task in one view. Book a pilot.",
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
        "slug": "dental-groups", "name": "Dental Groups",
        "rule": ("Patient Records Stay Approved", "Source is the patient-records drive", "Allow approved or local models only. Log every override."), "accent": CYAN,
        "title": "AI for Dental Groups: Governed AI Across Locations",
        "description": "AI for dental groups and multi-location practices: keep patient work on approved models, see every location in one view, and show compliance. Book a pilot.",
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
        "slug": "credit-unions", "name": "Credit Unions",
        "rule": ("Lending Answers Cite the Policy", "Topic is lending policy", "Answer only from the current policy document, and cite the section."), "accent": VIOLET,
        "title": "AI for Credit Unions: Inventory, Policy and Evidence",
        "description": "AI for credit unions: one inventory of every AI tool and model, vendor choices set by policy and logged, and exportable evidence for exams. Book a pilot.",
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
        "description": "AI for real estate brokerages: one policy across agents and offices, governed buyer messages, and an audit trail for each AI-assisted text. Book a pilot.",
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
        "slug": "property-management", "name": "Property Management",
        "rule": ("Rent Notices Need a Manager", "Draft is a rent-increase notice", "Require manager approval before sending."), "accent": GREEN,
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
        "description": "AI for professional services firms: route privileged work to approved models, keep a per-matter audit record, and govern every tool at once. Book a pilot.",
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
        "description": "AI for insurance and financial services: model and supplier provenance logged per task, policy by data sensitivity, and exportable records. Book a pilot.",
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
        "description": "AI for fintech teams: budget caps enforced per agent and team, every human review logged, and vendor-neutral governance across models. Book a pilot.",
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
        "description": "AI for telecom care and network teams: keep customer network data in a private deployment, with policy and audit across operations. Book a pilot.",
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
        "description": "AI for MSPs: add governed AI as a service line next to security and compliance, with one admin view across clients and no mixing of data. Book a pilot.",
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
        ("Platform", [("Product Overview", "/product", "One workspace for every model, agent and task")] +
         [(t, h, d) for t, h, d in FEATURES]),
        ("Modes", [(t, h, d) for t, h, d in MODES] +
         [("Security and Trust", "/security", "Controls you can point to")]),
    ]),
    ("Governance", "/governance"),
    ("Solutions", [
        ("By Industry", [("All Solutions", "/solutions", "Policy packs for regulated, people-heavy work")] +
         [(i["name"], f"/industries/{i['slug']}", i.get("menu", "AI for " + i["name"].lower())) for i in INDUSTRIES[:4]]),
        ("", [(i["name"], f"/industries/{i['slug']}", i.get("menu", "AI for " + i["name"].lower())) for i in INDUSTRIES[4:]]),
        ("By Team", [("All Teams", "/teams", "How RenOS fits each team")] +
         [(t["name"], f"/teams/{t['slug']}", t["menu"]) for t in TEAMS]),
    ]),
    ("Credits", "/credits"),
    ("Pricing", "/pricing"),
    ("Partners", "/partners"),
    ("About", "/about"),
]

FOOTER = [
    ("Product", [("How It Works", "/product"), ("Governance", "/governance"), ("Security", "/security"),
                 ("Pricing", "/pricing"), ("Vocom Credits", "/credits")]),
    ("Solutions", [("Healthcare", "/industries/dental-groups"), ("Property Management", "/industries/property-management"),
                   ("Credit Unions", "/industries/credit-unions"), ("MSPs and IT Partners", "/industries/msps"),
                   ("All Solutions", "/solutions")]),
    ("Company", [("About", "/about"), ("Partners", "/partners"), ("Resources", "/resources"), ("Contact", "/contact"),
                 ("Book a Pilot", "/pilot"), ("Sign In", "/login")]),
]

# ------------------------------------------------------------------ Page helpers

def mode_cards(exclude=None, h2="How It Fits With the Other Modes", lede=None):
    return {"type": "cards", "h2": h2, "lede": lede, "items": [
        {"title": t, "text": d, "href": h, "more": f"See {t}"} for t, h, d in MODES if t != exclude]}


TIMELINE = [("12:44:02", "Policy Evaluated", "Data residency matched"),
            ("12:44:03", "Model Executed", "Approved frontier model" + (" · $0.012" if SHOW_PRICES else " · cost logged")),
            ("12:44:31", "Accepted by User", "Sealed · chain intact")]
SESSION_BULLETS = ["Plain-language summary of what happened and why that model was chosen.",
                   "Step-by-step timeline from request to accepted result.",
                   "Tamper-evident chain so records can be verified later."]
PILOT_CTA = {"h2": "Start With One Pilot Team",
             "text": 'Sixty days, one team, one real workflow. You\'ll see governed sessions, receipts and cost on your own work. <a href="/pilot">How the pilot works</a>.'}


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
    if item.get("rule"):
        sections.append({"type": "cards", "eyebrow": "What a Rule Looks Like", "h2": "A Policy Pack Rule for " + item["name"],
                         "lede": 'Packs are starting points you edit and simulate before publishing. See <a href="/governance">how policies work</a>.',
                         "cols": 2, "items": [{"title": item["rule"][0], "plain": True, "rule": [("When", item["rule"][1]), ("Then", item["rule"][2])]},
                                              {"title": "Tested Before It Goes Live", "plain": True,
                                               "text": "Lint and simulation run against the last 30 days of sessions, so you see conflicts, gaps and how much traffic a rule would block before anyone is affected."}],
                         "foot": "Examples are illustrative."})
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
                 "buttons": [("Book a Pilot", "/pilot"), ("See Pricing", "/pricing", "ghost")],
                 "visual": {"shot": f"{kind}-{item['slug']}", "fallback": item.get("showcase") or [
                     ("label", "ROUTING RATIONALE"),
                     ("note", "Sensitive data detected, so policy sent this task to an approved model."),
                     ("kv", "Team", name), ("kv", "Policy", "Data sensitivity"), ("ok", "Audit entry written")]}},
        "sections": sections,
        "cta": PILOT_CTA,
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
                     "buttons": [("Book a Pilot", "/pilot"), ("See a Governed Session", "/governance", "ghost")],
                     "visual": {"shot": shot, "fallback": hero_visual or rows_[0].get("visual")}},
            "sections": sections}


# ------------------------------------------------------------------ Pages

def pages():
    P = []

    # ---------------- Home
    P.append({
        "route": "/", "title": "RenOS: The AI Operating System for Teams",
        "description": "RenOS is the AI operating system for teams: use every AI model under your policies, with an audit trail that writes itself. Book a 60-day pilot.",
        "hero": {
            "eyebrow": "The Governance Layer for AI at Work", "h1": "Use Every AI Model.", "h1_accent": "Prove What Each One Did.",
            "lede": "RenOS sends each task to the right model under your organization's policies, and writes an audit trail automatically. Your team just asks. Your admin sees everything without asking anyone.",
            "buttons": [("Book a Pilot", "/pilot"), ("See a Governed Session", "/governance", "ghost")],
            "proof": ["Every session policy-checked", "Every session logged", "Local and offline models"],
            "visual": {"shot": "home-hero", "fallback": "globe", "alt": "The RenOS workspace showing a task routed to an approved model with its routing rationale"},
        },
        "sections": [
            {"type": "problems", "sr_h2": "The Problem", "items": [
                {"title": "Shadow AI", "text": "Staff paste client and patient data into consumer chatbots, with no agreement in place."},
                {"title": "Subscription Sprawl", "text": "You pay for several AI tools and can't see how any of them are used."},
                {"title": "No Answer for the Auditor", "text": "When someone asks what the AI did with that data, nobody can say."}]},
            {"type": "cards", "id": "how-it-works", "eyebrow": "How It Works", "h2": "Governance That Adds No Work for Your Team",
             "lede": "People pick a mode and describe the task. Policy and routing happen in the background, and the record writes itself.",
             "items": [
                 {"num": "01", "title": "Ask in Plain Language", "text": 'Sign in with your company account. Your role is already set. Choose <a href="/product/chat">Chat</a>, <a href="/product/builder">Builder</a> or <a href="/product/agents">Agent</a> and describe the work.', "demo": ("Chat · Builder · Agent", "Draft a rent-increase notice for Maple Court...")},
                 {"num": "02", "title": "Policy Picks the Model", "text": 'Rules by data sensitivity, task type and role run before any model sees the task. You get a plain-language reason. See <a href="/product/routing">policy routing</a>.', "demo": ("Policy checked · Confidential", "Approved frontier model")},
                 {"num": "03", "title": "The Record Writes Itself", "text": 'Every step lands in a tamper-evident <a href="/product/audit-trail">audit trail</a>. Accept the result and the session closes. Nothing to export.', "demo": ("Logged · GS-20418", "Result accepted · no overrides")}]},
            {"type": "split", "eyebrow": "The Governed Session", "h2": "A Record a Stranger Can Read",
             "lede": 'Each task is one governed session: who ran it, on which model, under which policy, with what outcome. See <a href="/governance">how governance works</a>.',
             "bullets": SESSION_BULLETS,
             "summary": "Kevin asked for a rent-increase notice. Because it involved confidential tenant data, policy required an approved frontier model. It ran in 4.2 seconds. Kevin accepted it. No overrides.",
             "timeline": TIMELINE},
            {"type": "cards", "eyebrow": "Capabilities", "h2": "Everything an Admin Needs, and Nothing Users Notice",
             "lede": "The wedge is governance. The rest makes it usable every day.", "items": [
                 {"title": "Routing Under Policy", "text": "Rules by data sensitivity, task type and role, enforced before a task reaches any model.", "href": "/product/routing", "more": "See policy routing"},
                 {"title": "Automatic Audit Trail", "text": "Every governed task writes an entry. Nobody has to remember to document anything.", "href": "/product/audit-trail", "more": "See the audit trail"},
                 {"title": "Admin Oversight", "text": "One place to see sessions, cost and policy activity, and to change a rule that applies to the next task.", "href": "/product/admin", "more": "See the admin dashboard"},
                 {"title": "Hundreds of Models", "text": "Frontier and open models behind one interface, so you can switch suppliers without retraining your team.", "href": "/models", "more": "See supported models"},
                 {"title": "Local and Offline", "text": "Keep sensitive work on your own machines when policy calls for it.", "href": "/security", "more": "See security"},
                 {"title": "Multi-Agent, Side by Side", "text": "Run several models or agents at once and compare results, with policy applied to each.", "href": "/product/agents", "more": "See Agent mode"}]},
            {"type": "chips", "eyebrow": "Who It's For", "h2": "Teams Where Someone Has to Answer for AI Use",
             "lede": 'Multi-user organizations with a compliance duty, client confidentiality, or a growing AI bill. <a href="/solutions">See all solutions</a>.',
             "items": [("Multi-Location Healthcare", "/industries/dental-groups"), ("Property Management", "/industries/property-management"),
                       ("Credit Unions", "/industries/credit-unions"), ("Professional Services", "/industries/professional-services"),
                       ("MSPs and IT Partners", "/industries/msps"), ("Real Estate Brokerages", "/industries/real-estate")]},
            {"type": "faq", "h2": "RenOS Frequently Asked Questions", "items": [
                ("What is RenOS?", 'RenOS is an AI operating system for teams, and the governance layer for AI at work. It gives your people one workspace across many AI models, routes each task by your rules, explains every decision in plain language and writes an audit entry automatically. Read <a href="/ai-operating-system">what an AI operating system is</a>.'),
                ("How is it different from a single AI assistant?", "An assistant answers questions. RenOS sits across every model your team uses and adds the policy layer, audit trail and admin view across all of them."),
                ("Which AI models does it work with?", 'Frontier and open models through one workspace, plus your own keys on Enterprise and local models on your own hardware. See <a href="/models">supported AI models</a>.'),
                ("Where does our data go?", "You choose which models and suppliers each task may use, by data sensitivity, task type or role. Every choice is logged with its reason."),
                ("Can it run in our own environment?", 'Yes. Private deployment runs RenOS on your own infrastructure with local models. See <a href="/security">security</a>.'),
                ("How do we get started?", 'Start with a <a href="/pilot">60-day pilot</a>: one team, one real workflow, up to 15 seats and a written success plan.'),
            ]},
        ],
    })

    # ---------------- Product Overview
    crew_budget = "$2.00" if SHOW_PRICES else "Hard cap"
    P.append({
        "route": "/product", "crumb": "Product", "software": True,
        "title": "RenOS Product: AI Tools Your Team Can Govern",
        "description": "RenOS brings every AI model your team uses into one governed workspace: Chat, Builder and Agent modes, policy routing and an audit trail. Book a pilot.",
        "hero": {"eyebrow": "Chat · Builder · Agent", "h1": "One Workspace for Every", "h1_accent": "Model, Agent and Task.",
                 "lede": "RenOS runs on a server, so your whole team signs in from any device. Every task is routed by policy, every result carries a receipt, and every action has a tier.",
                 "buttons": [("Book a Pilot", "/pilot"), ("See a Governed Session", "/governance", "ghost")],
                 "visual": {"shot": "product-hero", "fallback": "globe-labels"}},
        "sections": [
            {"type": "cards", "eyebrow": "Three Modes, One Composer", "h2": "Ask Yourself: An Answer, a Thing Made, or a Thing Done?",
             "lede": "A mode belongs to a run, so one project thread can hold all three. Chat is suggested up to Builder or Agent, never forced.",
             "items": [
                 {"title": "Chat", "tag": "Lowest Cost", "plain": True, "text": "You want an answer, a draft, or a thinking partner.",
                  "example": "Draft a reply to the carrier about the Manila outage.",
                  "dl": [("Authority", "Read-only"), ("Cost", "Lowest · about 2 s"), ("Ends when", "Reply sent")],
                  "href": "/product/chat", "more": "See Chat Mode"},
                 {"title": "Builder", "tag": "Plan First", "plain": True, "text": "You want a finished thing: a doc, app, report or workflow.",
                  "example": "Plan · editable: Triage playbook, Credit calculator, Root-cause template.",
                  "dl": [("Authority", "Creates files inside the project sandbox"), ("Cost", "Medium · plan + N units"), ("Ends when", "Artifact delivered")],
                  "href": "/product/builder", "more": "See Builder Mode"},
                 {"title": "Agent", "tag": "Always Capped", "plain": True, "text": "You want something done or watched in other systems.",
                  "example": "Watch Manila-route latency. If it stays above 200 ms, open a task and email the carrier.",
                  "dl": [("Authority", "Acts through connectors, by tier"), ("Cost", "Highest · always capped"), ("Ends when", "Goal met, cap hit, or stopped")],
                  "href": "/product/agents", "more": "See Agent Mode"}]},
            {"type": "split", "eyebrow": "Routing Under Policy", "h2": "The Right Model for the Task, Inside the Rules",
             "lede": 'Auto is the default. Rules by data sensitivity, task type and role run before any model sees the task, and manual model choice is a governed override. See <a href="/product/routing">policy routing</a>.',
             "bullets": ["Locked models explain themselves, with the rule that blocked them.",
                         "Route profiles: Economy, Balanced, Max quality and Private.",
                         "Monthly caps with alerts, and a downshift to Economy at the cap."],
             "visual": "routing"},
            {"type": "cards", "eyebrow": "Multi-Agent Crews", "h2": "Patterns You Can Run, With Caps You Set",
             "lede": "A crew is named roles, one objective and hard caps, and it runs as one governed session. Reviewers never grade their own work.",
             "items": [
                 {"title": "Planner, Then Executors", "text": "A planner makes the plan; executors build the units in parallel. Better control and observability for long workflows."},
                 {"title": "Visionary and Integrator", "text": "A second vendor re-runs the proof independently. Verdicts: Same page, Revise, Reject, or Escalate to you as referee."},
                 {"title": "Verifier-Gated Actions", "text": "An independent verifier checks rules before anything leaves the building. Tier-3 actions always wait for a human."}],
             "after": {"type": "stats", "items": [("3", "review rounds"), ("5", "scope units"), (crew_budget, "budget per crew run"), ("Tier 3", "needs human sign-off")]}},
            {"type": "cards", "eyebrow": "Around the Workspace", "h2": "Everything a Team Needs to Work With AI Day to Day", "items": [
                {"title": "Projects", "text": "Workspaces with a brief, an alignment gate and a morning brief, shared across the team."},
                {"title": "Connectors and Plug-Ins", "text": "One hub for connectors, skills and models, with plain-language permission review at least authority."},
                {"title": "Approvals Inbox", "text": "Only Tier-3 actions interrupt you. Everything else is checked by rules and logged."},
                {"title": "Split View", "text": "Run up to four models side by side and compare, with policy applied to each."},
                {"title": "Local and Offline", "text": "Keep sensitive work on your own machines when policy calls for it."},
                {"title": "Intranet", "text": "An organization home with a permission-aware assistant: same question, different answers for different people."}]},
            {"type": "flow", "eyebrow": "Product Flow", "h2": "Follow One Task Through RenOS",
             "lede": "From the admin's first budget to the record an auditor reads. This is what your team and your admin actually see.",
             "steps": [
                 ("Sign In", "signin", "People sign in with their company account. Their role and policies are already set."),
                 ("Set Budgets and Caps", "budgets", 'The admin sets monthly caps per team and user, with alerts at 50, 80 and 100% and a hard ceiling for each agent task. See the <a href="/product/admin">admin dashboard</a>.'),
                 ("Choose Allowed Models", "supply", 'Each data class gets its own list of allowed models. Regulated data stays on approved models or your own keys.'),
                 ("Run a Task", "task", 'Policy picks the model, explains why in plain language and checks the budget before anything runs. See <a href="/product/routing">policy routing</a>.'),
                 ("Read the Audit Record", "audit", 'Who ran what, on which model, under which policy and at what cost. See the <a href="/product/audit-trail">AI audit trail</a>.'),
                 ("Hit a Budget Limit", "limit", "When a team reaches its cap, work pauses instead of overspending. The user picks a cheaper route or asks an owner to approve more."),
             ]},
            {"type": "faq", "h2": "Frequently Asked Questions", "items": [
                ("Is RenOS another AI assistant?", "No. RenOS is the layer across the AI models your team uses: one workspace, one policy, one audit trail."),
                ("Do people have to learn which model to use?", "No. Auto is the default. They pick a mode and describe the task, and policy picks the model and explains why. Choosing a model by hand is a governed override."),
                ("Does it run on our laptops?", "RenOS runs on a server, so your whole team signs in from any device. Local models can run on your own hardware when policy calls for it."),
                ("Can we see it on our own work?", 'Yes. <a href="/pilot">Book a pilot</a> and bring one real workflow.'),
            ]},
        ],
    })

    # ---------------- Mode and feature pages
    P.append(feature_page(
        "/product/chat", "Chat Mode", "AI Assistant for Teams, Routed to the Right Model",
        "Chat mode is an AI assistant for everyday work: ask in plain language, policy picks the model, and every chat is logged without extra steps. Start a pilot.",
        "Chat Mode", "An AI Assistant That Picks", "You want an answer, a draft or a thinking partner. Chat is the lowest-cost mode: read-only, a reply in about two seconds, routed to the right model under your rules and logged without anyone lifting a finger.",
        [
            {"title": "Ask in Plain Language", "text": "Your AI assistant works the way people already do: describe the task and get to work. No model menu, no settings.",
             "visual": "workspace"},
            {"title": "The Right Model, With the Reason Shown", "text": 'Auto is the default. Policy picks the model for each request and shows a plain-language reason. Learn how <a href="/product/routing">policy routing</a> decides.',
             "visual": "task"},
            {"title": "Read-Only, Lowest Cost", "text": "Chat answers and drafts. It doesn't create files or act in other systems, so it's the cheapest way to work. The run ends when the reply is sent.",
             "visual": [("label", "CHAT MODE"), ("kv", "Authority", "Read-only"), ("kv", "Cost", "Lowest · about 2 s"), ("kv", "Ends when", "Reply sent")]},
            {"title": "Every Chat Logged Without Extra Steps", "text": 'Each chat writes an entry to the <a href="/product/audit-trail">AI audit trail</a>. Nobody fills in a form.',
             "visual": "audit"},
        ],
        [{"title": "Builder Mode", "text": "A finished thing: a doc, app, report or workflow.", "href": "/product/builder", "more": "See Builder Mode"},
         {"title": "Agent Mode", "text": "Something done or watched in other systems, always capped.", "href": "/product/agents", "more": "See Agent Mode"},
         {"title": "RenOS for Operations", "text": "AI for work that operations teams run every day.", "href": "/teams/operations", "more": "See the operations page"}],
        [("Is Chat mode my AI or the company's?", "It's your AI assistant inside the company's rules. You use it like any assistant; your admin decides which models it may use."),
         ("Can I choose the model myself?", "You don't need to. Auto picks the right model for each task and explains why. A manual choice is a governed override, and locked models show the rule that blocked them."),
         ("What if my question turns into real work?", "Chat suggests moving up to Builder or Agent when a task needs a finished file or an action. It's a suggestion, never forced, and one project thread can hold all three modes."),
         ("Is every chat recorded?", "Yes. Each chat writes an audit entry automatically, with the policy that applied.")],
        "product-chat", h1_accent="the Right Model for You"))

    P.append(feature_page(
        "/product/builder", "Builder Mode", "Builder Mode: Run AI Tasks From Plan to Finished Work",
        "Builder mode runs AI tasks that end in a finished thing: a doc, app, report or workflow. It plans first, builds in a sandbox and records every version.",
        "Builder Mode", "Build the Finished Thing,", "You want a finished thing: a doc, app, report or workflow. Builder mode shows you an editable plan first, builds each unit inside the project sandbox, and delivers the artifact with a full record.",
        [
            {"title": "An Editable Plan First", "text": "Before anything is built, Builder shows the plan and what it will cost. Edit it, drop a unit or add one, then start.",
             "visual": [("pill", "Builder · Plan first"), ("label", "PLAN · EDITABLE"), ("kv", "Unit 1", "Triage playbook"), ("kv", "Unit 2", "Credit calculator"), ("kv", "Unit 3", "Root-cause template"), ("kv", "Cost", "Medium · plan + 3 units")]},
            {"title": "Built Inside the Project Sandbox", "text": "Builder creates files inside the project sandbox. Nothing acts on other systems; that's what Agent mode and its approval tiers are for.",
             "visual": [("label", "AUTHORITY"), ("note", "Creates files inside the project sandbox"), ("ok", "Ends when the artifact is delivered")]},
            {"title": "Compare Models in Split View", "text": "Run up to four models side by side on the same unit and keep the best result, with policy applied to each.",
             "visual": [("pill", "Split view"), ("split", [("MODEL A", "Clear, formal draft"), ("MODEL B", "Shorter, friendlier draft")])]},
            {"title": "Every Version Recorded", "text": 'Each plan, version, model and acceptance is written to the <a href="/product/audit-trail">AI audit trail</a>.',
             "visual": [("label", "AUDIT ENTRY"), ("kv", "Units", "3 delivered"), ("kv", "Policy", "Internal documents"), ("ok", "Written automatically")]},
        ],
        [{"title": "Chat Mode", "text": "An answer, a draft or a thinking partner.", "href": "/product/chat", "more": "See Chat Mode"},
         {"title": "Agent Mode", "text": "Something done or watched in other systems.", "href": "/product/agents", "more": "See Agent Mode"},
         {"title": "RenOS for Operations", "text": "Use AI for work your team repeats every day.", "href": "/teams/operations", "more": "See the operations page"}],
        [("What can Builder mode make?", "A finished thing: a document, a small app, a report or a workflow, delivered as an artifact in your project."),
         ("What does it cost?", "Medium: the plan plus one charge per unit built. You see the estimate on the plan before anything runs."),
         ("Can Builder compare models?", "Yes. Split view runs up to four approved models side by side so you can keep the best result."),
         ("Is the rejected output kept?", "The record shows every version and which one was accepted.")],
        "product-builder", h1_accent="Plan First"))

    P.append(feature_page(
        "/product/agents", "Agent Mode", "AI Agents That Work Together, With Rules",
        "Agent mode gets work done in other systems through connectors, by approval tier and always capped. Crews run several AI agents as one governed session.",
        "Agent Mode", "AI Agents That Act,", "You want something done or watched in other systems. Agent mode acts through connectors by approval tier, always runs under a hard cap, and ends when the goal is met, the cap is hit or you stop it.",
        [
            {"title": "Acts Through Connectors, by Tier", "text": "Agents work in your other systems through connectors with the least authority they need. Every action carries an approval tier.",
             "visual": [("pill", "Agent · Always capped"), ("note", "Watch Manila-route latency. If it stays above 200 ms, open a task and email the carrier."), ("kv", "Authority", "Connectors, by tier"), ("kv", "Ends when", "Goal met, cap hit, or stopped")]},
            {"title": "Always Capped", "text": 'Agent tasks and crews always carry a hard limit, so a runaway job can\'t spend your month. See <a href="/credits">RenOS Credits</a>.',
             "visual": "limit"},
            {"title": "Crews: Agents That Work Together", "text": "A crew is named roles, one objective and hard caps, and it runs as one governed session. Planner and executors, a second vendor that re-runs the proof, or a verifier that checks rules before anything leaves the building. Reviewers never grade their own work.",
             "visual": [("label", "CREW · ONE GOVERNED SESSION"), ("kv", "Planner", "Makes the plan"), ("kv", "Executors", "Build units in parallel"), ("kv", "Verifier", "Checks rules before release"), ("kv", "Review rounds", "3")]},
            {"title": "Tier-3 Actions Wait for a Human", "text": 'Only Tier-3 actions interrupt you, in the approvals inbox. Everything else is checked by rules and logged in one <a href="/product/audit-trail">AI audit trail</a>.',
             "visual": [("label", "APPROVALS INBOX"), ("note", "Email the carrier about route latency"), ("kv", "Tier", "3 · needs human sign-off"), ("ok", "Every step logged")]},
        ],
        [{"title": "Chat Mode", "text": "An answer, a draft or a thinking partner.", "href": "/product/chat", "more": "See Chat Mode"},
         {"title": "Builder Mode", "text": "A finished thing, planned first.", "href": "/product/builder", "more": "See Builder Mode"},
         {"title": "RenOS for IT", "text": "AI system administration without the sprawl.", "href": "/teams/it", "more": "See the IT page"}],
        [("What is an AI agent in RenOS?", "An agent is an AI worker that does or watches something in your other systems, through connectors, under an approval tier and a hard cap."),
         ("Can AI agents work together?", "Yes. A crew runs several agents with named roles on one objective, as one governed session, and every handoff is recorded."),
         ("Who checks the agents' work?", "Reviewers never grade their own work. An independent verifier checks rules, and Tier-3 actions always wait for a human."),
         ("Can an agent run up a big bill?", "No. Agent tasks and crews always carry a hard ceiling, and the run stops when it reaches it.")],
        "product-agents", h1_accent="Always Capped", hero_visual="workspace"))

    P.append(feature_page(
        "/product/routing", "Policy Routing", "Policy Routing: Use Any AI Model by the Rules",
        "Policy routing lets your team use any AI model under rules for data sensitivity, task type and role, enforced before a model is called. Book a pilot today.",
        "Policy Routing", "Use Any Model.", "Different AI models are good at different things. RenOS lets your team run AI on any model you approve, and your rules decide which one each task uses.",
        [
            {"title": "Rules by Sensitivity, Task and Role", "text": "Set rules by data sensitivity, task type and user role. They run at routing time, before any model sees the task.",
             "visual": "supply"},
            {"title": "A Plain-Language Routing Rationale", "text": "Every decision comes with a reason anyone can read.",
             "visual": [("label", "ROUTING RATIONALE"), ("note", "Contains tenant data, so policy sent this to an approved model.")]},
            {"title": "Locked Models Explain Themselves", "text": "Only models your policy allows for a task are selectable. Locked rows show the rule that blocked them, so nobody has to guess.",
             "visual": "routing"},
            {"title": "Route Profiles and Caps", "text": 'Pick Economy, Balanced, Max quality or Private. Monthly caps send alerts at 50, 80 and 100%, and routing downshifts to Economy at the cap. Track it in the <a href="/product/admin">admin dashboard</a>.',
             "visual": [("label", "ROUTE PROFILE"), ("kv", "Profile", "Balanced"), ("kv", "At the cap", "Downshift to Economy"), ("ok", "Choice logged with reason")]},
        ],
        [{"title": "AI Audit Trail", "text": "Every routing decision lands in the record.", "href": "/product/audit-trail", "more": "See the audit trail"},
         {"title": "Supported AI Models", "text": "Hundreds of models, one governed workspace.", "href": "/models", "more": "See supported models"},
         {"title": "RenOS for Compliance", "text": "AI governance for compliance teams.", "href": "/teams/compliance", "more": "See the compliance page"}],
        [("Can we really use any model?", "You can use any model your admin approves. Policy decides which one each task may use."),
         ("Can people pick a model by hand?", "Yes. Auto is the default, and a manual choice is a governed override that's logged like everything else."),
         ("When are rules enforced?", "At routing time, before any model is called."),
         ("Why do different AI models matter?", "Models differ in strength and cost. Routing lets you match each task to the right one without asking people to choose.")],
        "product-routing", h1_accent="Your Rules Decide Which.", hero_visual="task"))

    P.append(feature_page(
        "/product/audit-trail", "Audit Trail", "AI Audit Trail for Every Agent and Model",
        "The RenOS AI audit trail records every task: user, model, policy, output and overrides, readable by a non-technical reviewer and exportable. Book a pilot.",
        "Audit Trail", "An AI Audit Trail Your Admin", "AI and audit don't usually mix well. RenOS writes an audit entry for every task automatically, in language a reviewer can follow without help.",
        [
            {"title": "What Each Entry Holds", "text": "The user, the task, the model or models used, the policy applied, the output reference and any overrides.",
             "visual": [("label", "AUDIT ENTRY"), ("kv", "User", "Leasing team"), ("kv", "Models", "1 approved model"), ("kv", "Policy", "Tenant data"), ("kv", "Overrides", "None")]},
            {"title": "Readable by a Non-Technical Reviewer", "text": "Each entry starts with a plain-language summary of what happened and why that model was chosen.",
             "visual": [("label", "IN PLAIN LANGUAGE"), ("note", "A leasing agent asked for a renewal notice. Policy required an approved model. Accepted with no overrides.")]},
            {"title": "Tamper-Evident by Design", "text": "Each record is chained to the one before it. Any change breaks the chain and shows up on verification.",
             "visual": [("label", "CHAIN"), ("kv", "GS-20417", "Sealed"), ("kv", "GS-20418", "Sealed"), ("ok", "Chain intact")]},
            {"title": "Exportable", "text": 'Audit logs export cleanly for reviews. See <a href="/security">security and data</a> for how logs are kept.',
             "visual": [("kv", "Export", "Ready"), ("kv", "Retention", "90 days Pro · 1 year+ Enterprise"), ("ok", "Written automatically")]},
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
            {"title": "Per-Team Spend Caps", "text": "Set caps per team and per user, with alerts at 50, 80 and 100%. Agent tasks get a hard ceiling.",
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
         ("When do rule changes take effect?", "On the next task. Every rule is simulated before it's published."),
         ("When do budget alerts fire?", "At 50, 80 and 100% of each cap.")],
        "product-admin", h1_accent="Under Your Control", hero_visual="oversight"))

    # ---------------- Models
    P.append({
        "route": "/models", "crumb": "Supported AI Models", "software": True,
        "title": "AI Models in RenOS: Hundreds, One Workspace",
        "description": "RenOS gives your team hundreds of AI models in one governed workspace, across text, image, audio and video, with the admin deciding which may be used.",
        "hero": {"eyebrow": "Supported AI Models", "h1": "Hundreds of AI Models,", "h1_accent": "One Governed Workspace",
                 "lede": "RenOS reaches hundreds of AI models through one workspace. Your admin decides which models and suppliers each task may use, and every choice is logged.",
                 "buttons": [("Book a Pilot", "/pilot"), ("See Policy Routing", "/product/routing", "ghost")],
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
                {"title": "Switch Without Retraining", "text": "Frontier and open models behind one interface, so people keep working the same way when you change suppliers."},
                {"title": "Three Ways to Supply a Model", "text": 'Vocom credits, your own keys or local models on your own hardware. See <a href="/credits">RenOS Credits</a>.'},
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
        "description": "RenOS is AI for every team: sales, compliance, IT, operations, coaching and finance, all on one governed workspace with one audit trail. Book a pilot.",
        "hero": {"eyebrow": "Teams", "h1": "RenOS for Every Team",
                 "lede": "Every AI team looks different. Sales wants speed, compliance wants evidence, finance wants a single bill. RenOS gives each team AI at work under one set of rules.",
                 "buttons": [("Book a Pilot", "/pilot"), ("See Solutions", "/solutions", "ghost")]},
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
        "description": "Governed AI built around your industry, from dental groups and credit unions to real estate, insurance, fintech and MSPs. Book a 60-day RenOS pilot.",
        "hero": {"eyebrow": "Industries", "h1": "Governed AI, Built Around", "h1_accent": "Your Industry",
                 "lede": "Organizations with a compliance duty, client confidentiality or a growing AI bill need company AI they can prove. RenOS adapts its policy and records to your sector.",
                 "buttons": [("Book a Pilot", "/pilot"), ("See Solutions", "/solutions", "ghost")]},
        "sections": [
            {"type": "cards", "h2": "Choose Your Industry", "items": [
                {"title": i["name"], "text": i["intro"].split(". ")[0] + ".", "href": f"/industries/{i['slug']}", "accent": i["accent"], "more": f"AI for {i['name']}"} for i in INDUSTRIES]},
            {"type": "cards", "h2": "How RenOS Adapts to Your Industry", "items": [
                {"title": "Policy for Your Obligations", "text": 'Set rules to match your own obligations. See <a href="/product/routing">policy routing</a>.'},
                {"title": "Data Where You Decide", "text": 'Private deployment keeps data in your environment. See <a href="/security">security and data</a>.'},
                {"title": "Evidence on Request", "text": 'Exportable entries from the <a href="/product/audit-trail">AI audit trail</a>.'}]},
            {"type": "faq", "h2": "Frequently Asked Questions", "items": [
                ("Is RenOS certified for regulated industries?", 'We won\'t claim a certification until it is in hand. Today you get policy enforced before any model is called, a tamper-evident audit trail and a private deployment option. See <a href="/security">security</a>.'),
                ("Can regulated data go through a pilot?", "No. Regulated data stays out of pilots until the right agreement is in place."),
                ("Is my industry missing?", 'RenOS works for any organization that has to answer for its AI. <a href="/contact">Get in touch</a>.')]},
        ],
    })
    P += [collection_page(i, "industries") for i in INDUSTRIES]

    # ---------------- Governance
    P.append({
        "route": "/governance", "crumb": "Governance", "software": True, "software_name": "RenOS Governance",
        "title": "AI Governance Platform: A Record a Stranger Can Read",
        "description": "RenOS is the AI governance layer for your team: plain-English policies tested before they go live, a tamper-evident audit trail and admin oversight.",
        "hero": {"eyebrow": "The Governance Layer for AI at Work", "h1": "A Record a Stranger", "h1_accent": "Can Read.",
                 "lede": "Each task is one governed session: who ran it, on which model, under which policy, with what outcome. It writes itself, so nobody has to remember to document anything.",
                 "buttons": [("Book a Pilot", "/pilot"), ("Read the Security Overview", "/security", "ghost")]},
        "sections": [
            {"type": "split", "eyebrow": "The Governed Session", "h2": "The Audit Trail Is the Product",
             "lede": 'Not a log you export at the end of the quarter, but a record written as the work happens. See the <a href="/product/audit-trail">AI audit trail</a>.',
             "bullets": SESSION_BULLETS,
             "summary": "A team member asked for a rent-increase notice. Because it involved confidential tenant data, policy required an approved frontier model. It ran in 4.2 seconds. The result was accepted. No overrides.",
             "timeline": TIMELINE},
            {"type": "visual", "eyebrow": "Policies", "h2": "Rules in Plain English, Tested Before They Go Live",
             "lede": 'Start from an industry pack, describe the rule in plain English, or build a WHEN / THEN rule from scratch. Nothing is live until you simulate and publish. See <a href="/solutions">industry packs</a>.',
             "visual": "rule"},
            {"type": "stats", "eyebrow": "Admin Oversight", "h2": "Is Governance Working, and Is It Worth Renewing?",
             "lede": 'One place to see sessions, cost and policy activity, and to change a rule that applies to the next task. See the <a href="/product/admin">admin dashboard</a>.',
             "items": [("1,284", "governed sessions this month"), ("214 / wk", "hits on the busiest rule"), ("0", "unlogged overrides"),
                       ("$38 / $100" if SHOW_PRICES else "38%", "org monthly budget used" if not SHOW_PRICES else "org monthly budget")],
             "foot": "Illustrative sample data.",
             "after": {"type": "cards", "items": [
                 {"title": "Audit Export", "text": "Evidence a regulator or auditor can open, with retention of 90 days on Pro and a year or more on Enterprise."},
                 {"title": "Approval Tiers", "text": "Every action has a tier. Tier-3 actions need a human before they run, and every override is logged."},
                 {"title": "Budgets and Caps", "text": 'Caps per team and per user with alerts at 50, 80 and 100%. Agent tasks get a hard ceiling. See <a href="/credits">RenOS Credits</a>.'}]}},
            {"type": "faq", "h2": "Governance Questions", "items": [
                ("What is a governed session?", "One task from request to accepted result: who ran it, on which model, under which policy, with what outcome, written as the work happens."),
                ("Can a record be changed after the fact?", "Each record is chained to the one before it. Any change breaks the chain and shows up on verification."),
                ("How are new rules tested?", "Every rule is linted and simulated against the last 30 days of sessions before it's published. Lint and simulation are deterministic; no model grades its own policy."),
                ("How long are records kept?", "90 days on Pro, and a year or more with export on Enterprise.")]},
        ],
        "cta": {"h2": "See the Record for Yourself", "text": "Book a pilot and open a governed session from your own workflow."},
    })

    # ---------------- Solutions
    P.append({
        "route": "/solutions", "crumb": "Solutions",
        "title": "AI Solutions for Regulated, People-Heavy Teams",
        "description": "Governed AI for healthcare, property management, credit unions, professional services, real estate and MSPs, with policy packs for each. Book a pilot.",
        "hero": {"eyebrow": "Built for Regulated, People-Heavy Work", "h1": "Governed AI for the Teams", "h1_accent": "That Can't Afford a Guess.",
                 "lede": "Healthcare, property, credit unions, professional services and the MSPs who serve them. Same layer, with policy packs shaped to how each one actually works.",
                 "buttons": [("Book a Pilot", "/pilot"), ("See Pricing", "/pricing", "ghost")]},
        "sections": [
            {"type": "cards", "eyebrow": "Who It's For", "h2": "Pick Your World",
             "lede": "Each pack starts with sensible rules, connectors and sample workflows, so a pilot team is productive on day one.", "items": [
                 {"title": "Healthcare Practices", "text": "Patient records stay on approved or local models. Every draft that touches PHI has a receipt, a model and a reviewer.", "href": "/industries/dental-groups", "more": "AI for dental groups"},
                 {"title": "Property Management", "text": "Tenant notices, maintenance triage and owner reports with a record of who approved what.", "href": "/industries/property-management", "more": "AI for property management"},
                 {"title": "Credit Unions", "text": "Member communications and policy answers under rules your examiners can read.", "href": "/industries/credit-unions", "more": "AI for credit unions"},
                 {"title": "Professional Services", "text": "Client work stays inside client boundaries. Time, cost and model use roll up per matter.", "href": "/industries/professional-services", "more": "AI for professional services"},
                 {"title": "Managed Service Providers", "text": "Run one governed workspace per client from a single admin view, alongside the services you already provide.", "href": "/industries/msps", "more": "AI for MSPs"},
                 {"title": "Real Estate Teams", "text": "Listings, disclosures and follow-ups drafted fast, with approvals before anything goes out.", "href": "/industries/real-estate", "more": "AI for real estate"}]},
            {"type": "cards", "eyebrow": "What a Rule Looks Like", "h2": "Same Engine, Different Vocabulary", "foot": "Examples are illustrative. Packs are starting points you edit and simulate before publishing.", "items": [
                {"title": "Healthcare", "plain": True, "rule": [("When", "Source is the patient-records drive"), ("Then", "Allow approved or local models only. Log every override.")]},
                {"title": "Property Management", "plain": True, "rule": [("When", "Draft is a rent-increase notice"), ("Then", "Require manager approval before sending.")]},
                {"title": "Credit Union", "plain": True, "rule": [("When", "Topic is lending policy"), ("Then", "Answer only from the current policy document, and cite the section.")]}]},
            {"type": "chips", "eyebrow": "More Industries", "h2": "Every Industry We Serve",
             "lede": 'See every <a href="/industries">industry page</a>, or how RenOS fits each <a href="/teams">team</a>.',
             "items": [(i["name"], f"/industries/{i['slug']}") for i in INDUSTRIES]},
            {"type": "cards", "eyebrow": "By Team", "h2": "Governed AI for Every Team", "items": [
                {"title": t["name"], "text": t["menu"] + ".", "href": f"/teams/{t['slug']}", "accent": t["accent"], "more": f"RenOS for {t['name']}"} for t in TEAMS]},
        ],
        "cta": {"h2": "Tell Us Your Industry", "text": "We'll set up the matching pack for your pilot team."},
    })

    # ---------------- Credits
    P.append({
        "route": "/credits", "crumb": "Credits", "software": True, "software_name": "RenOS Credits",
        "title": "RenOS Credits: One Balance for Every AI Model",
        "description": "RenOS Credits pay for AI model use across providers with no markup. Every call is metered, receipted and tied to a governed session, with hard caps.",
        "hero": {"eyebrow": "Model Credits Supplied by Vocom", "h1": "One Balance for Every Model.", "h1_accent": "No Markup on Usage.",
                 "lede": 'Credits pay for model use across providers. Every call is metered, receipted and tied to a governed session, so cost is as auditable as the work. See <a href="/product/credits">how credits work, step by step</a>.',
                 "buttons": [("Book a Pilot", "/pilot"), ("See Plans", "/pricing", "ghost")]},
        "sections": [
            {"type": "stats", "tight": True, "items": [
                ("1 credit", "= $0.01" if SHOW_PRICES else "of model usage"), ("0%", "markup on model usage"),
                ("Per call", "metered and receipted"), ("Hard caps", "per user, team and agent run")]},
            {"type": "split", "eyebrow": "Every Call, Accounted For", "h2": "Cost Lives Next to the Proof",
             "lede": 'Each receipt links usage to the session, the policy and the person. Finance sees spend by team. Compliance sees the same record in the <a href="/product/audit-trail">audit trail</a>.',
             "visual": "receipt"},
            {"type": "cards", "eyebrow": "Where Models Come From", "h2": "Three Ways to Supply a Model",
             "lede": 'Policy decides which are allowed for each task. Locked options always say why. See <a href="/product/routing">policy routing</a>.', "items": [
                 {"title": "Vocom Credits", "text": "Pay as you go across approved cloud models with one balance and one invoice."},
                 {"title": "Bring Your Own Key", "text": "Use your own provider account. Keys are stored encrypted and never placed in prompts."},
                 {"title": "Local Models", "text": "Run on your own hardware at zero credit cost for work that must stay on-premises."}]},
            {"type": "cards", "eyebrow": "Stay in Budget", "h2": "Caps That Act Before the Bill Does", "items": [
                {"title": "Budgets", "text": "Set monthly caps per org, team and user. Alerts at 50, 80 and 100%."},
                {"title": "Route Profiles", "text": "Economy, Balanced, Max quality and Private. Downshift to Economy automatically at the cap."},
                {"title": "Agent Ceilings", "text": "Agent tasks and crews always carry a hard limit, so a runaway job can't spend your month."}]},
            {"type": "cards", "eyebrow": "How Topping Up Works", "h2": "From Balance to Back to Work in Four Steps", "cols": 4,
             "lede": 'Want the full picture, from budgets to the audit record? Read <a href="/product/credits">how RenOS credits work</a>.', "items": [
                 {"num": "1", "title": "Check Balance", "text": "See credits, spend and caps in one view."},
                 {"num": "2", "title": "Choose an Amount", "text": "Preset packs or a custom amount."},
                 {"num": "3", "title": "Confirm Payment", "text": "Card, or invoice for teams."},
                 {"num": "4", "title": "Back to Work", "text": "Balance updates and sessions resume."}]},
            {"type": "faq", "h2": "Credit Questions", "items": [
                ("What is a RenOS credit?", "One credit is one cent of model usage" + (", so 1 credit = $0.01" if SHOW_PRICES else "") + ". A task that costs 31 cents at the provider uses 31 credits."),
                ("Do you mark up model usage?", "No. Credits are spent at each model's published rate. When a provider cuts prices, your cost drops the same day."),
                ("Who supplies the credits?", "Credits are supplied through our carrier partner Vocom. You can also bring your own keys on Enterprise, or run local models at zero credit cost."),
                ("Do credits expire?", "Pro's included credits pool across your team each month. Purchased credits stay valid for 12 months.")]},
        ],
        "cta": {"h2": "Start With Credits Included", "text": "Pilots come with a starter balance and caps already set."},
    })

    # ---------------- Pricing
    P.append({
        "route": "/pricing", "crumb": "Pricing",
        "title": "RenOS Pricing: Pilot, Pro and Enterprise",
        "description": "RenOS pricing: pay for governed seats and use every AI model at its list price with no markup. Pilot, Pro and Enterprise plans, with free admin seats.",
        "hero": {"eyebrow": "Pricing", "h1": "Pay for Governed Seats.", "h1_accent": "Use Every Model at Its List Price.",
                 "lede": 'One subscription covers governance: policy routing, the audit trail and admin oversight. Model usage runs on <a href="/credits">RenOS Credits</a>, billed at each provider\'s published rate with no markup.'},
        "sections": [
            {"type": "pricing", "tight": True, "sr_h2": "Plans", "plans": [
                {"name": "Pilot", "blurb": "Prove it on one team before you commit.", "cta": ("Book a Pilot", "/pilot"),
                 "price": "$1,500", "unit": "flat, 60 days", "terms": "Fully credited to your first annual plan",
                 "features": ["Up to 15 seats, all Pro features", "Usage credits included",
                              "A written success plan with weekly governed-session reports", "Your fee credited to year one if you continue"],
                 "features_priced": ["Up to 15 seats, all Pro features", "$150 of RenOS Credits included",
                                     "A written success plan with weekly governed-session reports", "Your fee credited to year one if you continue"]},
                {"name": "Pro", "tag": "Most Teams Start Here", "blurb": "Governed AI for teams of 5 to 100.", "featured": True,
                 "cta": ("Talk to Sales", "/contact?type=pricing"), "cta_priced": ("Start With Pro", "/contact?type=pricing"),
                 "price": "$35", "price_monthly": "$42", "unit": "per seat / month", "terms": "$42 month-to-month · 5-seat minimum",
                 "features": ["Chat, Builder and Agent modes, split view", "Every model through RenOS Credits",
                              "Policy routing with plain-language reasons", "Audit trail with 90-day retention",
                              "Admin dashboard and team spend caps", "Usage credits per seat, pooled monthly"],
                 "features_priced": ["Chat, Builder and Agent modes, split view", "Every model through RenOS Credits",
                                     "Policy routing with plain-language reasons", "Audit trail with 90-day retention",
                                     "Admin dashboard and team spend caps", "$5 of credits per seat, pooled monthly"]},
                {"name": "Enterprise", "blurb": "For regulated orgs and existing AI contracts.", "cta": ("Talk to Sales", "/contact?type=pricing"),
                 "price": "From $60", "unit": "per seat / month", "terms": "Billed annually · 25-seat minimum",
                 "features": ["Everything in Pro", "Bring your own model keys", "SSO and SCIM provisioning",
                              "Audit retention of 1 year or more, with export", "Custom policies, data residency and supply controls",
                              "DPA, BAA and an uptime SLA"]}],
             "extras": [
                 {"title": "Private Deployment", "text": 'Run RenOS on your own infrastructure with local models. Available as an add-on. See <a href="/security">security</a>.',
                  "text_priced": 'From $1,500 per environment per month. Run RenOS on your own infrastructure with local models. See <a href="/security">security</a>.'},
                 {"title": "Free Admin Seats", "text": "Admins, auditors and read-only compliance reviewers never count as paid seats."}]},
            {"type": "cards", "eyebrow": "RenOS Credits", "h2": "Model Usage, Priced the Way the Providers Price It", "cols": 4,
             "lede": 'Credits are supplied through our carrier partner Vocom and spent at each model\'s published rate. You see exactly what every task cost, in the same record that shows why it ran. See <a href="/product/credits">how RenOS credits work</a>.',
             "items": [
                 {"title": "1 Credit = $0.01" if SHOW_PRICES else "Credits Track Real Usage",
                  "text": "Credits are dollars, not an abstract token. A task that costs $0.31 at the provider uses 31 credits." if SHOW_PRICES else "Each task spends credits at its model's published rate, so cost follows the work."},
                 {"title": "No Markup, Ever", "text": "We charge the provider's list price. When a provider cuts prices, your cost drops the same day."},
                 {"title": "Cost in the Audit Trail", "text": 'Every governed session records the model, the credits spent and the policy that chose it. See the <a href="/product/audit-trail">audit trail</a>.'},
                 {"title": "Budgets You Control", "text": 'Set caps per team and per user, with alerts at 50, 80 and 100%. Agent tasks get a hard ceiling. See the <a href="/product/admin">admin dashboard</a>.'}]},
            {"type": "compare", "eyebrow": "Compare Plans", "h2": "What Changes Between Pro and Enterprise", "cols": ["Pro", "Enterprise"], "rows": [
                ("Governed seats", {"cells": ["Talk to Sales", "Talk to Sales"], "cells_priced": ["$35 / month, annual", "From $60 / month, annual"]}),
                ("Minimum seats", "5", "25"),
                ("Credits included", {"cells": ["Pooled per seat", "Pay as you go"], "cells_priced": ["$5 per seat, pooled", "Pay as you go"]}),
                ("Bring your own model keys", None, "Included"),
                ("Audit retention", "90 days", "1 year or more, with export"),
                ("Single sign-on and SCIM", None, "Included"),
                ("Model supply controls", "Standard", "Verified-only or Exchange, per data class"),
                ("Private or local deployment", None, "Add-on"),
                ("DPA, BAA and SLA", "DPA", "DPA, BAA and 99.5% SLA")]},
            {"type": "faq", "eyebrow": "Questions", "h2": "Pricing Questions", "items": [
                ("Is there a free plan?", 'No. RenOS governs teams, so a solo free seat wouldn\'t show you what it does. Start with a <a href="/pilot">pilot</a> instead: its fee is credited to your first year.'),
                ("What happens to unused credits?", "Pro's included credits pool across your team each month. Purchased credits stay valid for 12 months."),
                ("Where do the models come from?", 'Through our carrier partner Vocom, or your own keys. Admins can restrict sensitive data to verified supply only. See <a href="/credits">RenOS Credits</a>.'),
                ("Do admins and auditors need a paid seat?", "No. Admin, auditor and read-only compliance seats are always free."),
                ("Can we use our own model provider contract?", "Yes, on Enterprise. Bring your own keys and RenOS still applies policy and writes the audit trail."),
                ("Can a partner resell RenOS?", 'Yes. Carriers, MSPs and IT partners can resell RenOS to the organizations they support. See the <a href="/partners">partner program</a>.')]},
        ],
    })

    # ---------------- Pilot
    P.append({
        "route": "/pilot", "crumb": "Book a Pilot",
        "title": "Get Started With AI: The RenOS 60-Day Pilot",
        "description": "Get started with AI the governed way. The RenOS 60-day pilot covers one team, one real workflow, up to 15 seats and a written success plan. Book a pilot.",
        "hero": {"eyebrow": "Pilots Are Open", "h1": "Start With One Pilot Team.",
                 "lede": "Sixty days, one team, one real workflow. You'll see governed sessions, receipts and cost on your own work.",
                 "aside": [("Week 1", "Kickoff, sign-in setup and your first policy pack."),
                           ("Weeks 2 to 6", "Team uses it daily. We tune rules from real sessions."),
                           ("Day 60", "Review the record together and decide what comes next.")],
                 "form": {"submit": "Request a Pilot", "stack": True, "fields": [
                     ("name", "Full name", "text", True, None, "Jane Rivera"), ("email", "Work email", "email", True, None, "jane@company.com"),
                     ("company", "Company", "text", True, None, "Company name"), ("team_size", "Team size", "number", True, None, "e.g. 8"),
                     ("task", "What would you like to try first?", "text", True, None, "e.g. tenant notices")]}},
        "sections": [
            {"type": "cards", "eyebrow": "What's Included", "h2": "What the Pilot Includes", "items": [
                {"title": "Up to 15 Seats", "text": 'All Pro features, including Chat, Builder and Agent modes. See <a href="/pricing">pricing</a>.'},
                {"title": "Credits Included", "text": ("$150 of RenOS Credits" if SHOW_PRICES else "A starter balance of RenOS Credits") + ' and caps already set. See <a href="/credits">RenOS Credits</a>.'},
                {"title": "A Written Success Plan", "text": "Agreed at kickoff, with weekly governed-session reports."}]},
            {"type": "faq", "h2": "Pilot Questions", "items": [
                ("How much does a pilot cost?", ("$1,500 flat for 60 days, " if SHOW_PRICES else "A flat fee for 60 days, ") + "fully credited to your first annual plan if you continue."),
                ("What does our team need to bring?", "One real, repeatable workflow, an admin to set policy, and a compliance or risk contact to review the record with us."),
                ("Can regulated data go through a pilot?", "Regulated data stays out of the pilot until the right agreement is in place.")]},
        ],
        "cta": False,
    })

    # ---------------- Security
    P.append({
        "route": "/security", "crumb": "Security",
        "title": "RenOS Security: Your Data, Your Environment",
        "description": "RenOS security: a tamper-evident audit trail, SSO and SCIM, data residency options, local models and keys kept out of prompts. Request the security pack.",
        "hero": {"eyebrow": "Security and Trust", "h1": "Built So You Can Show", "h1_accent": "Your Work to an Auditor.",
                 "lede": "Records are sealed as they are written, access follows your identity provider, and sensitive work can stay on your own machines.",
                 "buttons": [("Request the Security Pack", "/contact?type=security"), ("Book a Pilot", "/pilot", "ghost")]},
        "sections": [
            {"type": "cards", "eyebrow": "What We Do", "h2": "Controls You Can Point To", "items": [
                {"title": "Tamper-Evident Audit Trail", "text": 'Each record is chained to the one before it. Any change breaks the chain and shows up on verification. See the <a href="/product/audit-trail">audit trail</a>.'},
                {"title": "Identity and Access", "text": "Single sign-on, SCIM provisioning, roles and per-project permissions."},
                {"title": "Data Handling", "text": "Data residency options, configurable retention, and export or deletion on request."},
                {"title": "Local and Offline Models", "text": "Keep confidential work on your own hardware. Policy can require it for chosen data."},
                {"title": "Keys Never in Prompts", "text": "Provider keys and connector secrets are stored encrypted and never placed in model context."},
                {"title": "Least-Authority Actions", "text": "Connectors get the minimum scope, and every action carries an approval tier."}]},
            {"type": "split", "eyebrow": "Supply Policy", "h2": "Decide Which Models See Which Data",
             "lede": 'Every data class gets its own list of allowed models. Regulated data stays on approved models, your own keys or local models. See <a href="/product/routing">policy routing</a>.',
             "bullets": ["Set by data sensitivity, task type and role.", "Enforced before any model is called.",
                         "Locked models show the rule that blocked them."],
             "visual": "supply"},
            {"type": "cards", "eyebrow": "For Your Review", "h2": "Documents We Can Provide",
             "lede": "We'll share what applies to your review under NDA. We won't claim a certification until it is in hand.", "items": [
                 {"title": "Data Processing Agreement", "text": "Standard DPA for customers, with subprocessor list."},
                 {"title": "Business Associate Agreement", "text": "Part of the Enterprise plan design for healthcare customers. Ask us about your requirements."},
                 {"title": "Security Questionnaire", "text": "We'll complete yours or share our standard responses."}]},
            {"type": "faq", "h2": "Security Questions", "items": [
                ("Do you hold a security certification?", "We won't claim a certification until it is in hand. Today you get a tamper-evident audit trail, SSO and SCIM, local and private deployment options, and the documents above under NDA."),
                ("Can we run RenOS on our own infrastructure?", 'Yes. Private deployment runs RenOS on your own infrastructure with local models. See <a href="/pricing">pricing</a>.'),
                ("Are BAA and DPA available?", "A DPA is standard for customers. BAA and DPA are part of the Enterprise plan design. Talk to us about your requirements.")]},
        ],
        "cta": {"h2": "Questions From Your Security Team?", "text": "Send them our way. We'd rather answer early than late.", "button": ("Contact Us", "/contact?type=security")},
    })

    # ---------------- Partners
    P.append({
        "route": "/partners", "crumb": "Partners",
        "title": "RenOS for MSPs and IT Partners",
        "description": "RenOS for MSPs, carriers and consultancies: resell or deliver governed AI to every client, with one admin view across clients and credits metered.",
        "hero": {"eyebrow": "For MSPs, Carriers and Consultancies", "h1": "Bring Governed AI to the", "h1_accent": "Clients You Already Serve.",
                 "lede": "Offer RenOS alongside your services. One admin view across clients, with the audit trail each of them will ask for.",
                 "buttons": [("Become a Partner", "/contact?type=partner"), ("Talk to Us", "/contact", "ghost")]},
        "sections": [
            {"type": "cards", "eyebrow": "Partner Models", "h2": "Three Ways to Work Together", "items": [
                {"title": "Resell", "text": "Sell RenOS and credits to your clients with your own pricing and billing relationship."},
                {"title": "Deliver", "text": "Run each client's workspace yourself, with your own library of policy packs and one admin view."},
                {"title": "Refer", "text": "Introduce clients and we handle onboarding. Simple and low-touch."}]},
            {"type": "cards", "eyebrow": "What You Get", "h2": "Everything to Deliver and Support It", "items": [
                {"title": "Multi-Client Admin", "text": "One console, separate workspaces. Roll up usage and policy activity across all clients."},
                {"title": "Policy Packs", "text": 'Start every client from an industry pack and keep your own library of rules. See <a href="/solutions">solutions</a>.'},
                {"title": "Enablement", "text": "Onboarding playbooks, demo scripts and sales material so your team is ready quickly."},
                {"title": "Shared Roadmap", "text": "Partners shape what ships. Tell us what your clients keep asking for."},
                {"title": "Usage-Based Economics", "text": 'Credits are metered per client, so margins stay clear and predictable. See <a href="/credits">RenOS Credits</a>.'},
                {"title": "Co-Selling", "text": "Joint calls and case studies once your first clients are live."}]},
            {"type": "cards", "eyebrow": "How It Starts", "h2": "From Intro to First Client in Three Steps", "items": [
                {"num": "1", "title": "Intro Call", "text": "We learn your client base and the use cases you see most."},
                {"num": "2", "title": "Pilot Workspace", "text": "You get a partner workspace and one client pilot to prove it out."},
                {"num": "3", "title": "Launch", "text": "Agree terms, brand the workspace and roll out to more clients."}]},
            {"type": "faq", "h2": "Partner Questions", "items": [
                ("Who is the partner program for?", 'MSPs, carriers and IT consultancies that support organizations with security and compliance needs. See <a href="/industries/msps">AI for MSPs</a>.'),
                ("Are client environments kept separate?", "Yes. One console with separate workspaces, so you see every client without mixing their data."),
                ("How do we apply?", 'Use the <a href="/contact?type=partner">partner contact form</a> and tell us about your clients.')]},
        ],
        "cta": {"h2": "Let's Build This Together", "text": "Tell us about your clients and the services you offer today.", "button": ("Become a Partner", "/contact?type=partner")},
    })

    # ---------------- About
    P.append({
        "route": "/about", "crumb": "About",
        "title": "About RenOS: The Team Behind Governed AI",
        "description": "RenOS by Ren Group gives teams one place to use every AI model, with rules they set and a record they can prove. Meet the team behind the governance layer.",
        "hero": {"eyebrow": "About RenOS", "h1": "We Build the Layer That Makes", "h1_accent": "AI at Work Accountable.",
                 "lede": "RenOS by Ren Group gives teams one place to use every model, with rules they set and a record they can prove. Our view: the work should be trusted because it can be shown, not because someone said so.",
                 "buttons": [("Book a Pilot", "/pilot"), ("Contact Us", "/contact", "ghost")]},
        "sections": [
            {"type": "cards", "eyebrow": "What We Believe", "h2": "Things We Won't Compromise On", "items": [
                {"title": "Proof Over Promises", "text": "Every claim a model makes should come with a record of how it was produced."},
                {"title": "Your Rules, Your Data", "text": "Policy belongs to the customer and so does the data. Always."},
                {"title": "Plain Language", "text": "Rules, receipts and summaries a non-engineer can read and act on."}]},
            {"type": "cards", "eyebrow": "The Team", "h2": "The People Behind It", "items": [
                {"title": "Troy", "avatar": True, "meta": "Tech Lead", "text": "Leads architecture and engineering, from the governed session core to the model router."},
                {"title": "Kevin", "avatar": True, "meta": "Product Manager · Marketing Manager · Sales", "text": "Owns product direction, go-to-market and customer conversations."},
                {"title": "Cole", "avatar": True, "meta": "Delivery Manager · Product Owner", "text": "Keeps delivery on track and turns customer needs into a clear backlog."}]},
        ],
        "cta": {"h2": "Work With Us", "text": "Start with one pilot team and see for yourself."},
    })

    # ---------------- Contact
    P.append({
        "route": "/contact", "crumb": "Contact",
        "title": "Contact RenOS: Book a Demo or Talk to a Human",
        "description": "Contact RenOS about pricing, security, partnerships or anything else. Tell us a bit and we'll route it to the right person within one business day.",
        "hero": {"eyebrow": "Contact", "h1": "Talk to a Human.",
                 "lede": "Questions about pricing, security, partnerships or anything else. Tell us a bit and we'll route it to the right person.",
                 "aside": [("Security Review", 'Ask for the security pack or send your questionnaire. See <a href="/security">security</a>.'),
                           ("Partnerships", 'MSPs and consultancies: tell us about your clients. See <a href="/partners">partners</a>.')],
                 "form": {"submit": "Send Message", "stack": True, "fields": [
                     ("name", "Full name", "text", True, None, "Jane Rivera"), ("email", "Work email", "email", True, None, "jane@company.com"),
                     ("company", "Company", "text", True, None, "Company name"),
                     ("type", "Topic", "select", True, [("", "Pricing, security, partnership, other"), ("pricing", "Pricing"), ("security", "Security"), ("partner", "Partnership"), ("demo", "A demo on our own work"), ("other", "Other")]),
                     ("message", "Message", "textarea", False, None, "How can we help?")]}},
        "sections": [],
        "cta": False,
    })

    # ---------------- Thanks (form confirmation)
    P.append({
        "route": "/thanks", "crumb": "Thanks", "noindex": True,
        "title": "Thanks, We've Got It | RenOS", "description": "Your message reached RenOS.",
        "hero": {"center": True, "h1": "Thanks. We've Got It.",
                 "lede": "Expect a reply within one business day. In the meantime, here is what to look at next.",
                 "buttons": [("Explore the Product", "/product"), ("Back to Home", "/", "ghost")]},
        "sections": [], "cta": False,
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

    # ---------------- How credits work
    P.append({
        "route": "/product/credits", "crumb": "How Credits Work", "crumbs": [("Product", "/product")], "software": True,
        "software_name": "RenOS Credits",
        "title": "How RenOS Credits Work, From Top-Up to Audit",
        "description": "How RenOS credits work, step by step: top up, set team budgets, run a task with a hold, settle actual usage and see the cost in the audit trail.",
        "hero": {"eyebrow": "RenOS Credits", "h1": "How RenOS Credits Work",
                 "lede": "Every task spends credits for the model usage it actually needs. Here's how a credit moves through RenOS, from the admin's first top-up to the record an auditor reads.",
                 "buttons": [("Book a Pilot", "/pilot"), ("See RenOS Credits", "/credits", "ghost")],
                 "visual": {"shot": "credits-hero", "fallback": "buy"}},
        "sections": [
            {"type": "flow", "id": "steps", "eyebrow": "Step by Step", "h2": "Follow a Credit Through RenOS",
             "lede": "Seven steps, from the admin's billing page to the moment a team hits its cap. These are the screens your admin and your team actually see.",
             "steps": [
                 ("Buy Credits", "buy", "The admin checks the balance, picks a preset pack or a custom amount, and pays by card, or by invoice for teams. Auto top-up keeps the balance from running dry."),
                 ("Set Budgets and Caps", "budgets", 'The admin sets monthly caps per org, team and user, with alerts at 50, 80 and 100%. Agent tasks get a hard ceiling so a runaway loop can\'t drain the balance. See the <a href="/product/admin">admin dashboard</a>.'),
                 ("Choose Allowed Models", "supply", 'Every data class gets its own list of allowed models. Regulated data stays on approved models or your own keys. See <a href="/product/routing">policy routing</a>.'),
                 ("Run a Task", "task-hold", "A team member runs a task. Policy picks the model, explains why in plain language, and places a hold for the estimated cost before anything runs."),
                 ("Meter and Settle", "settle", "When the task finishes, RenOS charges for the tokens actually used, releases the rest of the hold, and updates team and organization balances."),
                 ("Read the Audit Record", "audit-credits", 'Cost becomes part of the record: who ran what, on which model, under which policy, and what it cost. See the <a href="/product/audit-trail">AI audit trail</a>.'),
                 ("Hit a Budget Limit", "limit", "When a team reaches its cap, work pauses instead of overspending. People can pick a lower-cost model or ask the budget owner to approve more."),
             ]},
            {"type": "cards", "eyebrow": "Key Ideas", "h2": "What Makes Credits Predictable", "cols": 4, "items": [
                {"title": "No Markup on Usage", "text": "Each task is charged for the tokens it actually used, at its model's published rate."},
                {"title": "A Hold Before Anything Runs", "text": "The estimated cost is reserved first, so a task never starts without budget to finish."},
                {"title": "Cost Lives in the Record", "text": "Every task's credits sit next to the model and policy that chose it."},
                {"title": "Work Pauses at the Cap", "text": "Teams can't overspend. Owners approve increases, and agent runs stop at their ceiling."}]},
            {"type": "faq", "h2": "Frequently Asked Questions", "items": [
                ("What is a RenOS credit?", 'One credit is one cent of model usage' + (', so 1 credit = $0.01' if SHOW_PRICES else '') + '. Each task spends credits for the tokens it actually used, at the model\'s published rate with no markup. See <a href="/pricing">RenOS pricing</a> for plans.'),
                ("Why does RenOS place a hold before a task runs?", "The hold reserves the estimated cost so the task can finish within budget. When it's done, RenOS charges actual usage and releases the rest."),
                ("What happens when a team runs out of budget?", "Work pauses instead of overspending. The person can switch to a lower-cost model or ask the budget owner to approve a one-time increase."),
                ("Can an agent run up a big bill?", "No. Each agent task has a hard ceiling, and the run stops when it reaches it."),
                ("Where can we see what each task cost?", 'In the admin view and in every audit entry. See the <a href="/product/admin">admin dashboard</a>.'),
                ("Who can top up credits?", "Org admins, by card or by invoice for teams. Auto top-up can refill the balance when it runs low."),
                ("Do purchased credits expire?", "Purchased credits stay valid for 12 months. Pro's included credits pool across your team each month.")]},
        ],
    })

    # ---------------- Log in portal (noindex: a door to the app, not a page to rank)
    P.append({
        "route": "/login", "crumb": "Sign In", "noindex": True,
        "title": "Sign In to RenOS",
        "description": "Sign in to your RenOS workspace with your work account.",
        "hero": {"eyebrow": "Sign In", "h1": "Sign In to RenOS",
                 "lede": 'Use your work account. Your role and policies come with it, and we\'ll never post anything. Trouble signing in? <a href="/contact">Contact us</a>.',
                 "visual": "portal"},
        "sections": [
            {"type": "cards", "tight": True, "cols": 2, "sr_h2": "Signing In", "items": [
                {"title": "Check Your Second Factor", "plain": True, "text": "After you sign in, the app asks for the 6-digit code from your authenticator app."},
                {"title": "Lost Your Device?", "plain": True, "text": 'Use a recovery code or contact your admin. New here? <a href="/pilot">Book a pilot</a> to get started.'}]}],
        "cta": False,
    })

    # ---------------- 404
    P.append({
        "route": "/404", "crumb": "Page Not Found", "noindex": True,
        "title": "Page Not Found, RenOS", "description": "This page doesn't exist.",
        "hero": {"eyebrow": "404", "h1": "This Page Isn't Here",
                 "lede": 'Try the <a href="/">home page</a>, the <a href="/product">product overview</a>, <a href="/pricing">pricing</a> or <a href="/contact">contact us</a>.',
                 "buttons": [("Go Home", "/"), ("Book a Pilot", "/pilot", "ghost")]},
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
<p>Pilots are open. <a href="/pilot">Start with a 60-day pilot</a> or <a href="/contact">talk to a human</a>.</p>
'''
