document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".programme-item");
  const contentBox = document.getElementById("programme-content");
  const programmes = window.programmeDescriptions;

  items.forEach(item => {
    item.addEventListener("click", () => {
      // Reset styles
      items.forEach(i => i.classList.remove("bg-green-100", "font-semibold"));
      item.classList.add("bg-green-100", "font-semibold");

      const title = item.dataset.title;
      const content = programmes[title] || "No details available.";
      contentBox.innerHTML = `
        <h2 class="text-2xl font-bold mb-2">${title}</h2>
        <p class="text-gray-700">${content}</p>
      `;
    });
  });

  // Trigger click on the first item by default
  if (items.length > 0) {
    items[0].click();
  }
});
