import folium

# Départ et arrivée
depart = ("Metz", 49.1193, 6.1757)
actual = (45.8150, 15.9819)
arrivee = ("Oulan-Bator", 47.8864, 106.9057)

# Trajet complet (ajout Baku et Aktau)
trajet_coords = [
    (49.1193, 6.1757),    # Metz
    (45.8992, 6.1294),    # Annecy
    (45.4642, 9.1900),    # Milan
    (45.4408, 12.3155),   # Venise
    (45.8150, 15.9819),   # Zagreb
    (48.3069, 14.2858),   # Linz
    (44.4268, 26.1025),   # Bucarest
    (41.6771, 26.5555),   # Edirne
    (41.0082, 28.9784),   # Istanbul
    (39.9334, 32.8597),   # Ankara
    (40.4093, 49.8671),   # Baku
    (43.6500, 51.2000),   # Aktau
    (41.2995, 69.2401),   # Tachkent
    (42.8746, 74.5698),   # Bichkek
    (48.0000, 79.0000),
    (47.8864, 106.9057)   # Oulan-Bator
]

# Carte centrée
carte = folium.Map(
    location=[50, 50],
    zoom_start=3,
)

# Trajet bleu
# Index de la position actuelle dans le trajet
position_actuelle = 4  # Metz

# Trajet déjà parcouru
folium.PolyLine(
    trajet_coords[:position_actuelle+1],  # jusqu'au point actuel
    color="#0F4C8E",  # vert forêt
    weight=3,
    opacity=0.85
).add_to(carte)

# Trajet futur
folium.PolyLine(
    trajet_coords[position_actuelle:],  # à partir du point actuel
    color="#3D70A7",
    weight=3,
    opacity=0.5,
    dash_array="5, 8"  # pointillé
).add_to(carte)

# Départ maison bleue
folium.Marker(
    location=[depart[1], depart[2]],
    popup="Metz — Départ",
    icon=folium.Icon(icon="home", prefix="fa", color="darkblue")
).add_to(carte)
folium.Marker(
    location=[actual[0], actual[1]],
    icon=folium.DivIcon(
        icon_size=(0, 0),
        icon_anchor=(0, 0),
        html="""
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 35px;
            transform: translate(-50%, -50%) scaleX(-1) rotate(5deg);
            transform-origin: 50% 50%;
            opacity: 0.9;
        ">
            🚲
        </div>
        """
    )
).add_to(carte)
# Arrivée
ville, lat, lon = arrivee
folium.CircleMarker(
    location=[lat, lon],
    radius=8,
    color="#0f5ebeff",
    fill=True,
    fill_color="#0f5ebe",
    fill_opacity=1,
    popup=ville
).add_to(carte)

# Sauvegarde

carte.save("MAPS/trajet_en_cours.html")