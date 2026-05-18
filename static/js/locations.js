document.addEventListener("DOMContentLoaded", () => {

  const mapElement = document.getElementById("locations-map");

  const venues = JSON.parse(
    mapElement.dataset.venues
  );

  const map = L.map("locations-map", {
    scrollWheelZoom: false
  }).setView(
    [52.3676, 4.9041],
    12
  );

  L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
      attribution: "&copy; OpenStreetMap contributors"
    }
  ).addTo(map);

  venues.forEach((venue) => {

    L.marker([
      venue.latitude,
      venue.longitude
    ])
      .addTo(map)
      .bindPopup(`
        <strong>${venue.name}</strong><br>
        ${venue.city}
      `);

  });

});