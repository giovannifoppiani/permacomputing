
# Create a complete, optimized index.html file
# Based on permacomputing principles and low-tech design

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Giovanni Foppiani - Communication designer & PhD researcher exploring techno-social ecosystems, digital sustainability, and regenerative mobility">
  <meta name="author" content="Giovanni Foppiani">
  <title>Giovanni Foppiani</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Giovanni→Foppiani</h1>
    <p class="subtitle">Communication designer & PhD researcher</p>
  </header>

  <main>
    <section id="about">
      <h2>About</h2>
      <p>Through his design practice, he collaborates with public institutions, conscious brands and collectives to foster sustainable, social and digital innovation – reflecting a consistent commitment to <strong>Communication for the Common Good</strong>.</p>
      
      <p>He leverages his design background to steer the energy transition toward socially desirable scenarios by bridging industry and research, using data visualization as a navigational tool for climate-positive synergies.</p>

      <h3>2024 — 25</h3>
      <p>While working as a researcher at the <strong>University Iuav of Venice</strong>, he explored social initiatives as drivers of social and digital innovation. As an assistant professor, he organised the <em>Amplify Social Initiatives</em> and <em>Welcome Day</em> workshops, as well as Prof. Gianni Sinni's course titled <em>Public Futures. Data, rights, design</em> with Irene Sgarro. During his fellowship, he collaborated with research groups such as CTRL+JUNK and the University Digital Ecosystems project to promote communication through sustainable innovation.</p>

      <h3>2023 — 24</h3>
      <p>As a designer, he developed a <a href="https://criticity.com">low-carbon digital platform</a> designed to minimize carbon emissions related to web usage while amplifying the impact of the dissemination. He holds a Master's degree in Communication Design and Digital Product from <strong>ISIA Firenze</strong>, and his graduation project investigated <em>The Impact of the Internet</em> focusing on its energy consumption, sustainable practices, and the implications for users and the planet.</p>
    </section>

    <section id="publications">
      <h2>Publications</h2>
      <ul class="pub-list" id="publications-list">
        <!-- Publications loaded from JSON -->
      </ul>
    </section>

    <section id="projects">
      <h2>Selected Projects</h2>
      <div class="table-container">
        <table id="projects-table">
          <thead>
            <tr>
              <th>Year</th>
              <th>Title</th>
              <th>Discipline</th>
              <th>Collaboration</th>
            </tr>
          </thead>
          <tbody>
            <!-- Projects loaded from JSON -->
          </tbody>
        </table>
      </div>
    </section>

    <section id="bio">
      <h2>Bio</h2>
      <p><strong>Giovanni Foppiani</strong> is a communication designer and PhD researcher at <strong>LUT</strong> and <strong>RMIT University</strong> whose work explores techno-social ecosystems. With a master's degree in Communication Design from ISIA Firenze, and previously served as research fellow at University Iuav of Venice, his practice focuses on digital sustainability, social innovation, and regenerative mobility. His collaborations with public institutions and non-profit organisations reflect a consistent commitment to Communication for the Common Good.</p>
      
      <p class="pronunciation">/ˈjo.ʋɑn.ni fopːiɑni/</p>
      
      <p class="contact">
        <a href="mailto:giovanni.foppiani@lut.fi">giovanni.foppiani@lut.fi</a><br>
        <a href="https://orcid.org/0009-0008-3784-2451" target="_blank" rel="noopener">ORCID 0009-0008-3784-2451</a>
      </p>
      
      <p class="social">
        <a href="https://instagram.com/giovannifoppiani" target="_blank" rel="noopener">Instagram</a> • 
        <a href="https://linkedin.com/in/giovannifoppiani" target="_blank" rel="noopener">LinkedIn</a>
      </p>
    </section>
  </main>

  <footer>
    <p class="note"><strong>Note:</strong> This is not my official portfolio but rather a web-repository of lost-and-found links of my work.</p>
    <p class="metrics">
      Page weight: <span id="page-weight">calculating...</span> • 
      Estimated CO₂: <span id="page-carbon">calculating...</span>
    </p>
    <p class="sustainability">This page uses system fonts, no JavaScript frameworks, and minimal CSS following <a href="https://permacomputing.net" target="_blank" rel="noopener">permacomputing principles</a>.</p>
    <p class="update">Last update: October 2025</p>
  </footer>

  <script>
    // Minimal JavaScript - only for loading data and calculating page weight
    // This could be removed and data embedded directly in HTML for zero-JS version
    
    // Load publications
    fetch('publications.json')
      .then(response => response.json())
      .then(data => {
        const list = document.getElementById('publications-list');
        data.publications.forEach(pub => {
          const li = document.createElement('li');
          li.innerHTML = `<strong>${pub.authors}</strong> (${pub.year}). <em>${pub.title}</em>. ${pub.venue}${pub.pages ? ', pp. ' + pub.pages : ''}. ${pub.publisher || ''} ${pub.status ? '<span class="status">[' + pub.status + ']</span>' : ''}`;
          list.appendChild(li);
        });
      })
      .catch(err => console.error('Error loading publications:', err));
    
    // Load projects
    fetch('projects.json')
      .then(response => response.json())
      .then(data => {
        const tbody = document.querySelector('#projects-table tbody');
        data.projects.forEach(project => {
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td>${project.year}</td>
            <td>${project.title}</td>
            <td>${project.discipline}</td>
            <td>${project.collaboration}</td>
          `;
          tbody.appendChild(tr);
        });
      })
      .catch(err => console.error('Error loading projects:', err));
    
    // Calculate page weight (approximate)
    window.addEventListener('load', function() {
      // Get all resources
      const resources = performance.getEntriesByType('resource');
      let totalSize = 0;
      
      resources.forEach(resource => {
        totalSize += resource.transferSize || 0;
      });
      
      // Add document size
      const navigation = performance.getEntriesByType('navigation')[0];
      if (navigation) {
        totalSize += navigation.transferSize || 0;
      }
      
      const kb = (totalSize / 1024).toFixed(2);
      document.getElementById('page-weight').textContent = kb + ' KB';
      
      // Rough CO2 calculation: 0.81 kWh per GB transferred, 0.5 kg CO2 per kWh
      const gb = totalSize / (1024 * 1024 * 1024);
      const co2 = (gb * 0.81 * 0.5).toFixed(2);
      document.getElementById('page-carbon').textContent = co2 + 'g CO₂';
    });
  </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ Created index.html")
print("  - Semantic HTML5 structure")
print("  - System fonts via CSS")
print("  - Minimal JavaScript (only for data loading & metrics)")
print("  - Page weight calculator in footer")
print("  - Accessible markup")
