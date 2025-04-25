// Seat Selection
document.addEventListener('DOMContentLoaded', function() {
    const seatGrid = document.querySelector('.seat-grid');
    if (seatGrid) {
        const seats = seatGrid.querySelectorAll('.seat');
        let selectedSeats = [];

        seats.forEach(seat => {
            if (!seat.classList.contains('booked')) {
                seat.addEventListener('click', function() {
                    if (this.classList.contains('selected')) {
                        this.classList.remove('selected');
                        selectedSeats = selectedSeats.filter(s => s !== this.dataset.seatNumber);
                    } else {
                        this.classList.add('selected');
                        selectedSeats.push(this.dataset.seatNumber);
                    }
                    updateSelectedSeatsInput();
                });
            }
        });

        function updateSelectedSeatsInput() {
            const input = document.querySelector('input[name="seat_numbers"]');
            if (input) {
                input.value = selectedSeats.join(',');
            }
        }
    }
});

// Form Validation
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.classList.add('is-invalid');
        } else {
            field.classList.remove('is-invalid');
        }
    });

    return isValid;
}

// Show Search
const searchInput = document.querySelector('#show-search');
if (searchInput) {
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const showCards = document.querySelectorAll('.show-card');

        showCards.forEach(card => {
            const title = card.querySelector('.card-title').textContent.toLowerCase();
            const description = card.querySelector('.card-text').textContent.toLowerCase();
            
            if (title.includes(searchTerm) || description.includes(searchTerm)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// Date Formatting
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Initialize tooltips
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
}); 