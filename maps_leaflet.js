var map = L.map('.map').setView([33.749, -84.388], 13);

L.tileLayer('tiles/{z}/{x}/{y}.png', {
    minZoom: 1,
    maxZoom: 18,
    attribution: 'Offline Map Data'
}).addTo(map);

L.marker([33.749, -84.388]).addTo(map).bindPopup('Offline in Atlanta');