#!/bin/bash
#
# Claude Code Starter Kit Setup
# Bulletproof. Elegant. Delightful.
#
# Usage:
#   Interactive:     curl -sSL https://raw.githubusercontent.com/edutone/claude-engineering-excellence/main/STARTER_KIT/setup.sh | bash
#   Non-interactive: curl -sSL ... | bash -s -- --stack=react --edtech
#

set -e

REPO_URL="https://github.com/edutone/claude-engineering-excellence"
BRANCH="main"

# Colors (with fallback for non-color terminals)
if [[ -t 1 ]]; then
    GREEN='\033[0;32m'
    BLUE='\033[0;34m'
    YELLOW='\033[1;33m'
    RED='\033[0;31m'
    BOLD='\033[1m'
    NC='\033[0m'
else
    GREEN='' BLUE='' YELLOW='' RED='' BOLD='' NC=''
fi

# Parse arguments for non-interactive mode
STACK=""
EDTECH=false
NON_INTERACTIVE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --stack=*) STACK="${1#*=}"; NON_INTERACTIVE=true ;;
        --edtech) EDTECH=true; NON_INTERACTIVE=true ;;
        --help)
            echo "Usage: setup.sh [--stack=java|react|dotnet|vue|python] [--edtech]"
            exit 0 ;;
        *) ;;
    esac
    shift
done

# ============================================================================
# HEADER
# ============================================================================
echo ""
echo -e "${BLUE}${BOLD}"
echo "  ╔═══════════════════════════════════════════════════════════════╗"
echo "  ║                                                               ║"
echo "  ║              CLAUDE CODE STARTER KIT                          ║"
echo "  ║                                                               ║"
echo "  ║         60 seconds to your first magic moment                 ║"
echo "  ║                                                               ║"
echo "  ╚═══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# ============================================================================
# PRE-FLIGHT CHECKS
# ============================================================================
echo -e "${BLUE}▸ Running pre-flight checks...${NC}"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}✗ Node.js not found${NC}"
    echo "  Please install Node.js 18+ from https://nodejs.org"
    exit 1
fi
echo -e "${GREEN}  ✓ Node.js $(node --version)${NC}"

# Check npm
if ! command -v npm &> /dev/null; then
    echo -e "${RED}✗ npm not found${NC}"
    exit 1
fi
echo -e "${GREEN}  ✓ npm $(npm --version)${NC}"

# Check git
if ! command -v git &> /dev/null; then
    echo -e "${RED}✗ git not found${NC}"
    echo "  Please install git from https://git-scm.com"
    exit 1
fi
echo -e "${GREEN}  ✓ git $(git --version | cut -d' ' -f3)${NC}"

# Check/install Claude Code
if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}  ⟳ Installing Claude Code...${NC}"
    npm install -g @anthropic-ai/claude-code 2>/dev/null || {
        echo -e "${RED}✗ Failed to install Claude Code${NC}"
        echo "  Try: sudo npm install -g @anthropic-ai/claude-code"
        exit 1
    }
fi
echo -e "${GREEN}  ✓ Claude Code installed${NC}"

# Check authentication
echo -e "${BLUE}▸ Checking authentication...${NC}"
if ! claude --version &> /dev/null; then
    echo -e "${YELLOW}  ! Please authenticate with Claude Code${NC}"
    echo ""
    echo "    Run: ${BOLD}claude auth${NC}"
    echo ""
    echo "    Then run this setup again."
    exit 0
fi
echo -e "${GREEN}  ✓ Authenticated${NC}"

echo ""

# ============================================================================
# INTERACTIVE PROMPTS (if not non-interactive)
# ============================================================================
if [ "$NON_INTERACTIVE" = false ]; then
    echo -e "${BLUE}▸ Quick configuration${NC}"
    echo ""
    echo "  What's your primary stack?"
    echo ""
    echo "    1) Java / Spring Boot"
    echo "    2) React / TypeScript"
    echo "    3) .NET / C#"
    echo "    4) Vue.js"
    echo "    5) Python / FastAPI / Django"
    echo "    6) Other / Skip patterns"
    echo ""
    read -p "  Enter choice [1-6]: " stack_choice

    case $stack_choice in
        1) STACK="java" ;;
        2) STACK="react" ;;
        3) STACK="dotnet" ;;
        4) STACK="vue" ;;
        5) STACK="python" ;;
        *) STACK="none" ;;
    esac

    echo ""
    read -p "  Do you handle student/child data (FERPA/COPPA)? [y/N]: " edtech_choice
    [[ $edtech_choice =~ ^[Yy]$ ]] && EDTECH=true
fi

echo ""
echo -e "${BLUE}▸ Installing with: ${BOLD}stack=$STACK, edtech=$EDTECH${NC}"
echo ""

# ============================================================================
# DOWNLOAD REPOSITORY
# ============================================================================
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo -e "${BLUE}▸ Downloading starter kit...${NC}"
if ! git clone --depth 1 --branch $BRANCH $REPO_URL "$TEMP_DIR" 2>/dev/null; then
    echo -e "${RED}✗ Download failed${NC}"
    exit 1
fi
echo -e "${GREEN}  ✓ Downloaded${NC}"

# ============================================================================
# CREATE DIRECTORY STRUCTURE
# ============================================================================
echo -e "${BLUE}▸ Setting up .claude/ directory...${NC}"

mkdir -p .claude/commands
mkdir -p .claude/patterns
mkdir -p .claude/sessions

# ============================================================================
# ESSENTIAL COMMANDS (THE 5 THAT MATTER)
# ============================================================================

# 1. /code-review - THE essential command
cat > .claude/commands/code-review.md << 'EOF'
---
description: Review staged changes before commit
---

Review my staged changes. Be concise, flag only real issues:

1. **Bugs**: Logic errors, edge cases
2. **Security**: Vulnerabilities, secrets
3. **Style**: Obvious violations only

```bash
git diff --cached
```

If everything looks good, say "✓ Ready to commit" and nothing more.
EOF

# 2. /explain - understand code
cat > .claude/commands/explain.md << 'EOF'
---
description: Explain code (usage: /explain src/file.ts)
---

Explain this code concisely:
- **What**: 1-2 sentences
- **How**: Key logic only
- **Watch out**: Edge cases, gotchas

$ARGUMENTS
EOF

# 3. /help - project-specific help
cat > .claude/commands/help.md << 'EOF'
---
description: Show available commands and quick tips
---

# Claude Code Quick Help

## Essential Commands
| Command | What It Does |
|---------|--------------|
| `/code-review` | Review staged changes (use before every commit!) |
| `/explain [file]` | Explain what code does |
| `/capture` | Save an insight from this session |

## Tips
- **Before committing**: Always run `/code-review`
- **When confused**: `/explain src/whatever.ts`
- **Found something useful?**: `/capture` to save it

## The ONE Habit
```bash
# Before every commit:
/code-review
```

That's it. Everything else is optional.
EOF

# 4. /capture - passive flywheel
cat > .claude/commands/capture.md << 'EOF'
---
description: Save an insight (30 seconds)
---

# Quick Capture

Something worked well? Let's save it.

I'll add to `.claude/sessions/captures.md`:

```markdown
## [DATE] - [TITLE]
**Type**: solution | pattern | gotcha
**Insight**: [2-3 sentences]
```

What was useful? (I'll format it)

$ARGUMENTS
EOF

# 5. /review-sessions - weekly flywheel review
cat > .claude/commands/review-sessions.md << 'EOF'
---
description: Review captured insights (5 min weekly)
---

# Weekly Review

Let me check `.claude/sessions/captures.md` and surface patterns.

I'll identify:
- Solutions used multiple times → candidates for team patterns
- Common gotchas → should be documented
- Stale entries → can be cleaned up

This takes 5 minutes and compounds your team's knowledge.
EOF

echo -e "${GREEN}  ✓ 5 essential commands installed${NC}"

# ============================================================================
# CLAUDE.MD (Project Instructions)
# ============================================================================

if [ "$EDTECH" = true ]; then
cat > .claude/CLAUDE.md << 'EOF'
# Project Instructions for Claude

## Three Rules
1. **I review everything** before committing
2. **No secrets** in prompts (API keys, passwords)
3. **No student PII** in prompts (FERPA/COPPA required)

## EdTech Compliance
- NEVER log student names, emails, grades, or IDs
- NEVER include student data in error messages
- ALL student data access requires authorization
- Encrypt student data at rest and in transit

## Code Style
- Follow existing patterns
- Keep it simple
- Write tests for new features
EOF
else
cat > .claude/CLAUDE.md << 'EOF'
# Project Instructions for Claude

## Three Rules
1. **I review everything** before committing
2. **No secrets** in prompts (API keys, passwords)
3. **Iteration is normal** - this is collaboration

## Code Style
- Follow existing patterns
- Keep it simple
- Write tests for new features
EOF
fi

echo -e "${GREEN}  ✓ CLAUDE.md created${NC}"

# ============================================================================
# STACK PATTERNS (only if selected)
# ============================================================================

if [ "$STACK" != "none" ] && [ -n "$STACK" ]; then
    PATTERN_FILE="$TEMP_DIR/STARTER_KIT/.claude/patterns/${STACK}-patterns.md"
    if [ -f "$PATTERN_FILE" ]; then
        cp "$PATTERN_FILE" .claude/patterns/
        echo -e "${GREEN}  ✓ ${STACK} patterns added${NC}"
    fi
fi

# ============================================================================
# SESSIONS DIRECTORY (for flywheel)
# ============================================================================

cat > .claude/sessions/captures.md << 'EOF'
# Captured Insights

> Run `/capture` to add insights. Run `/review-sessions` weekly.

---

EOF

echo -e "${GREEN}  ✓ Sessions directory initialized${NC}"

# ============================================================================
# PRE-COMMIT HOOK (passive security)
# ============================================================================

mkdir -p .hooks
cat > .hooks/pre-commit << 'HOOK'
#!/bin/bash
# Blocks commits containing obvious secrets

PATTERNS=(
    'AKIA[0-9A-Z]{16}'           # AWS Access Key
    'ghp_[a-zA-Z0-9]{36}'        # GitHub Token
    'sk-[a-zA-Z0-9]{48}'         # OpenAI Key
    'xox[baprs]-[a-zA-Z0-9-]+'   # Slack Token
)

for pattern in "${PATTERNS[@]}"; do
    if git diff --cached | grep -qE "$pattern"; then
        echo "❌ Potential secret detected matching: $pattern"
        echo "   Please remove before committing."
        exit 1
    fi
done

exit 0
HOOK
chmod +x .hooks/pre-commit

if [ -d ".git" ]; then
    git config core.hooksPath .hooks 2>/dev/null || true
    echo -e "${GREEN}  ✓ Pre-commit hook enabled${NC}"
else
    echo -e "${YELLOW}  ! Pre-commit hook ready (activate with: git config core.hooksPath .hooks)${NC}"
fi

# ============================================================================
# SUCCESS!
# ============================================================================

echo ""
echo -e "${GREEN}${BOLD}"
echo "  ╔═══════════════════════════════════════════════════════════════╗"
echo "  ║                                                               ║"
echo "  ║                    ✓ SETUP COMPLETE                           ║"
echo "  ║                                                               ║"
echo "  ╚═══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# ============================================================================
# MAGIC MOMENT
# ============================================================================

# Detect if we're in a real codebase
FILE_COUNT=$(find . -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.java" -o -name "*.cs" -o -name "*.vue" 2>/dev/null | head -20 | wc -l)

echo -e "${BLUE}${BOLD}  YOUR FIRST MAGIC MOMENT${NC}"
echo ""

if [ "$FILE_COUNT" -gt 0 ]; then
    # Real codebase - suggest exploration
    echo "  You're in a codebase! Try this now:"
    echo ""
    echo -e "    ${YELLOW}claude \"What does this codebase do? Give me a 3-sentence summary.\"${NC}"
else
    # Empty/new directory - suggest help
    echo "  This looks like a new project. Try:"
    echo ""
    echo -e "    ${YELLOW}claude \"/help\"${NC}"
    echo ""
    echo "  Or start with any question about your code."
fi

echo ""
echo -e "${BLUE}${BOLD}  THE ONE HABIT${NC}"
echo ""
echo "  Before every commit, run:"
echo ""
echo -e "    ${YELLOW}claude \"/code-review\"${NC}"
echo ""
echo -e "  ${GREEN}That's it. You're ready to build.${NC}"
echo ""
