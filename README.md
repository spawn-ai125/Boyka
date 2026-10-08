<!-- PROJECT LOGO & BANNER -->
<p align="center">
  <img src="https://shields.io" alt="Python Version" />
  <img src="https://shields.io" alt="License" />
  <img src="https://shields.io" alt="Stage" />
</p>

<h1 align="center">⚡ BOYKA VULNERABILITY SCANNER ⚡</h1>

<p align="center">
  <strong>A Lightweight, Fast, and Intelligent Network Vulnerability Scanner Written in Python.</strong>
  <br />
  Designed with a minimalist CLI, Boyka maps network ports, banners services, and instantly cross-references known security flaws via authoritative vulnerability databases.
</p>

<hr />

<h2>📋 Table of Contents</h2>
<ul>
  <li><a href="#key-features">Key Features</a></li>
  <li><a href="#how-it-works">How It Works</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#smart-reporting-logic">Smart Reporting Logic</a></li>
  <li><a href="#roadmap">Roadmap</a></li>
  <li><a href="#license">License</a></li>
</ul>

<hr />

<h2 id="key-features">✨ Key Features</h2>
<ul>
  <li><strong>Modern & Clean UI:</strong> Responsive ASCII art header with real-time colored terminal outputs powered by <code>colorama</code>.</li>
  <li><strong>Banner Grabbing:</strong> Establishes socket connections to interactively extract running service versions.</li>
  <li><strong>Live API Integration:</strong> Queries the CIRCL Vulnerability-Lookup API dynamically using intelligent keyword parsing.</li>
  <li><strong>Smart Reporting:</strong> Adapts output based on finding results (compact mode for clean targets, verbose mode for critical issues).</li>
  <li><strong>Code Quality:</strong> Optimized structure adhering to strict formatting guidelines, fully compliant with modern linters like Ruff.</li>
</ul>

<hr />

<h2 id="how-it-works">🧠 How It Works</h2>
<ol>
  <li><strong>Port Scanning:</strong> Boyka checks the most critical network ports utilizing Python's built-in <code>socket</code> library.</li>
  <li><strong>Banner Extraction:</strong> Sends standardized probes (<code>\r\n</code>) to determine exact software configurations.</li>
  <li><strong>Threat Intelligence Loop:</strong> Sanitizes service strings and forwards requests to threat databases.</li>
  <li><strong>Conditional Output:</strong> Aggregates responses to generate instant visual summaries for security enthusiasts and administrators.</li>
</ol>

<hr />

<h2 id="installation">🚀 Installation</h2>

<p>Ensure you have Python 3.8+ installed on your system. Clone or download the single-file script, then install dependencies:</p>

```bash
# Install required third-party libraries
pip install colorama requests
```

<hr />

<h2 id="usage">💻 Usage</h2>

<p>Run the single-file script directly from your terminal environment:</p>

```bash
python boyka.py
```

<h3>Interactive Menu Overview:</h3>
<ul>
  <li><code>[1] Start Network Vulnerability Scanner</code>: Launches target input prompt and scanning matrix.</li>
  <li><code>[2] Help</code>: Provides tool capability and framework overview.</li>
  <li><code>[3] Exit</code>: Terminates the interactive CLI loop safely.</li>
</ul>

<hr />

<h2 id="smart-reporting-logic">📊 Smart Reporting Logic</h2>

<blockquote>
  📌 <strong>Boyka's Smart Architecture Policy:</strong>
  <br />
  If <strong>no vulnerabilities</strong> are found, Boyka respects your terminal space and generates a clean list of active ports and versions. If <strong>vulnerabilities exist</strong>, it highlights critical warnings and appends direct CVE IDs with descriptive threat summaries.
</blockquote>

<hr />

<h2 id="roadmap">🗺️ Roadmap (Upcoming Features)</h2>
<ul>
  <li>[ ] Implement Multi-threading for hyper-fast asynchronous scanning.</li>
  <li>[ ] Export clean scan logs directly to local <code>report.txt</code> files.</li>
  <li>[ ] Add support for custom port ranges specified by the user.</li>
</ul>

<hr />

<h2>👨‍💻 Author</h2>
<p>
  <strong>Coded By 4B2A</strong><br />
  <em>Built with passion, guided by precision, optimized for reliability.</em>
</p>
