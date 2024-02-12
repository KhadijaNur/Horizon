document.addEventListener('DOMContentLoaded', function() {
    const paginationButtons = document.querySelectorAll('.pagination button');
    const contentContainer = document.getElementById('content');
  
    paginationButtons.forEach(button => {
      button.addEventListener('click', function() {
        goToPage(parseInt(button.textContent));
      });
    });
  
    function goToPage(page) {
      const contentItems = Array.from({ length: 30 }, (_, index) => `Item ${index + 1}`);
      const itemsPerPage = 5;
      const start = (page - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      const currentPageItems = contentItems.slice(start, end);
  
      contentContainer.innerHTML = currentPageItems.join(', ');
  
      paginationButtons.forEach(button => {
        button.classList.remove('active');
      });
      paginationButtons[page - 1].classList.add('active');
    }
  });
  
  
  function openModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
}

// Function to close the modal popup
function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

// Function to handle deletion confirmation
function confirmDelete(postId) {
    openModal(); // Display the modal popup
    var deleteBtn = document.getElementById("deleteBtn");
    deleteBtn.onclick = function() {
        window.location.href = postId + "/delete";
    };
}