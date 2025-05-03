document.addEventListener('DOMContentLoaded', function () {
    const map = L.map('map').setView([30.615, -96.34], 15);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    const categoryFilter = document.getElementById('categoryFilter');
    const travelModeSelect = document.getElementById('travelModeSelect');
    const resourceList = document.getElementById('resourceList');
    let markers = [];
    let routingControl = null;

    function getUserLocation(callback) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                pos => callback([pos.coords.latitude, pos.coords.longitude]),
                () => alert("Could not get your location")
            );
        } else {
            alert("Geolocation not supported.");
        }
    }

    function showRoute(destinationCoords) {
        const mode = travelModeSelect.value;

        getUserLocation(userCoords => {
            if (routingControl) {
                map.removeControl(routingControl);
            }

            routingControl = L.Routing.control({
                waypoints: [
                    L.latLng(userCoords[0], userCoords[1]),
                    L.latLng(destinationCoords[0], destinationCoords[1])
                ],
                router: L.Routing.osrmv1({
                    serviceUrl: 'https://router.project-osrm.org/route/v1',
                    profile: mode === 'car' ? 'driving' : mode === 'bike' ? 'cycling' : 'foot'
                }),
                lineOptions: {
                    styles: [{ color: '#500000', weight: 4 }]
                },
                addWaypoints: false,
                draggableWaypoints: false,
                show: false,
                createMarker: () => null
            }).addTo(map);
        });
    }

    function fetchResources(category = '') {
        const lang = 'en'; // Default language
        let url = `/api/resources?lang=${lang}`;
        if (category) url += `&category=${encodeURIComponent(category)}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                markers.forEach(m => map.removeLayer(m));
                markers = [];
                resourceList.innerHTML = '';

                data.forEach(resource => {
                    const marker = L.marker([resource.latitude, resource.longitude])
                        .addTo(map)
                        .bindPopup(`<b>${resource.name}</b><br>${resource.description}<br>${resource.address}`);
                    markers.push(marker);

                    const li = document.createElement('li');
                    li.innerHTML = `
                        <strong>${resource.name}</strong><br>
                        ${resource.category}<br>
                        <em>${resource.address}</em><br>
                        <button class="route-btn" data-lat="${resource.latitude}" data-lng="${resource.longitude}">
                            Get Directions
                        </button>
                    `;
                    resourceList.appendChild(li);
                });

                document.querySelectorAll('.route-btn').forEach(btn => {
                    btn.addEventListener('click', () => {
                        const lat = parseFloat(btn.getAttribute('data-lat'));
                        const lng = parseFloat(btn.getAttribute('data-lng'));
                        showRoute([lat, lng]);
                    });
                });
            });
    }

    categoryFilter.addEventListener('change', () => {
        fetchResources(categoryFilter.value);
    });

    fetchResources(); // Initial load
});
