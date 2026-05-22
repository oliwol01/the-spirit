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

  // FILTERING

  const filterButtons = document.querySelectorAll(
    ".filter-trigger"
  );

  const venueCards = document.querySelectorAll(
    ".venue-card-wrapper"
  );

  const searchInput = document.getElementById(
    "venue-search"
  );

  filterButtons.forEach((button) => {

    button.addEventListener("click", () => {

      const selectedCategory = button.dataset.category;

      const resultsLabel = document.getElementById(
        "locations-results-label"
      );

      if (selectedCategory === "All") {

        resultsLabel.textContent = "All venues";

      } else {

        resultsLabel.textContent = `${selectedCategory}s`;

      }

      // ACTIVE BUTTON

      filterButtons.forEach((btn) => {
        btn.classList.remove("active-filter-btn");
      });

      button.classList.add("active-filter-btn");

      // FILTER VENUES

      let visibleCount = 0;

      venueCards.forEach((card) => {

        const venueCategory = card.dataset.category;

        const venueName = card
          .innerText
          .toLowerCase();

        const searchValue = searchInput.value
          .toLowerCase()
          .trim();

        const matchesCategory =
          selectedCategory === "All" ||
          venueCategory === selectedCategory;

        const matchesSearch =
          venueName.includes(searchValue);

        if (
          matchesCategory &&
          matchesSearch
        ) {

          card.style.display = "block";

          visibleCount++;

        } else {

          card.style.display = "none";

        }

      });

      // NO RESULTS MESSAGE

      const noResultsMessage = document.getElementById(
        "no-results-message"
      );

      if (
        visibleCount === 0 &&
        selectedCategory !== "All"
      ) {

        noResultsMessage.classList.remove("d-none");

      } else {

        noResultsMessage.classList.add("d-none");

      }

    });

  });

  // SEARCH

  searchInput.addEventListener("input", () => {

    const activeButton = document.querySelector(
      ".active-filter-btn"
    );

    activeButton.click();

  });

});