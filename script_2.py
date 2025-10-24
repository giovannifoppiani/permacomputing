
import json

# Create publications.json with your actual publications
publications_data = {
    "publications": [
        {
            "year": "2025",
            "authors": "Foppiani, G., Sgarro, I., & Sinni, G.",
            "title": "Public Futures. Data, rights, design",
            "venue": "Design@Work. Sources & Resources",
            "pages": "70-75",
            "publisher": "Anteferma Edizioni"
        },
        {
            "year": "2025",
            "authors": "Fagnoni, R., Foppiani, G., & Leonardi, C.",
            "title": "Soluzioni low-tech per l'adattamento al cambiamento climatico nello spazio urbano",
            "venue": "Design@Work. Sources & Resources",
            "pages": "166-169",
            "publisher": "Anteferma Edizioni"
        },
        {
            "year": "2025",
            "authors": "Costa, P., Fagnoni, R., Foppiani, G., Lodovini, A., Manfroni, M., & Sinni, G.",
            "title": "Sopravvivere al digitale: Design e Terzo settore",
            "venue": "Design for Survival (Vol. X)",
            "publisher": "",
            "status": "In progress"
        },
        {
            "year": "2025",
            "authors": "Costa, P., Fagnoni, R., Foppiani, G., Lodovini, A., Manfroni, M., & Sinni, G.",
            "title": "Amplifying social initiatives in a located landscape",
            "venue": "Cumulus 2025",
            "publisher": "",
            "status": "In progress"
        },
        {
            "year": "2025",
            "authors": "Fagnoni, R., Foppiani, G., Lodovini, A., Manfroni, M., & Sinni, G.",
            "title": "Amplifying social initiatives: un framework di design per il Terzo settore",
            "venue": "SID 2025",
            "publisher": "",
            "status": "In progress"
        },
        {
            "year": "2025",
            "authors": "Leonardi, C., Foppiani, G., Soffietti, F., & Artioli, L.",
            "title": "Design per l'emergenza: piattaforme low-tech diffuse come strumenti di co-design per la mitigazione del cambiamento climatico e la resilienza comunitaria",
            "venue": "SID. Design Plurale 2025",
            "publisher": "",
            "status": "In progress"
        },
        {
            "year": "2024",
            "authors": "Foppiani, G., & Zerial, E.",
            "title": "E[arth]rosion: Satellite views are points of view",
            "venue": "2CO-Communicating Complexity 4: Selected contributions to the Conference July 3-5, 2024, Barcelona",
            "publisher": "FrancoAngeli"
        },
        {
            "year": "2024",
            "authors": "Foppiani, G.",
            "title": "Nessi. Appunti per l'ecosistema digitale dell'università",
            "venue": "Arcipelaghi digitali. Cartografia dei servizi Iuav",
            "pages": "132-141",
            "publisher": "Società Editrice Anteferma"
        },
        {
            "year": "2020",
            "authors": "Cheri, S., Deganello, P., Foppiani, G., et al.",
            "title": "Cibo e design – la conversione ecologica delle merci",
            "venue": "",
            "publisher": "Società Editrice Il Mulino"
        },
        {
            "year": "2020",
            "authors": "Foppiani, G.",
            "title": "There is no plan bee",
            "venue": "AND Rivista Di Architetture, Città e Architetti",
            "pages": "37(1)",
            "publisher": ""
        }
    ]
}

with open('publications.json', 'w', encoding='utf-8') as f:
    json.dump(publications_data, f, ensure_ascii=False, indent=2)

print("✓ Created publications.json")
print(f"  - {len(publications_data['publications'])} publications included")
print("  - Properly formatted JSON")
print("  - UTF-8 encoding for special characters")
