document.addEventListener('DOMContentLoaded', () => {
    const movieInput = document.getElementById('movie-input');
    const recommendBtn = document.getElementById('recommend-btn');
    const recommendationsContainer = document.getElementById('recommendations-container');

    recommendBtn.addEventListener('click', async () => {
        const movieTitle = movieInput.value.trim();
        
        if (!movieTitle) {
            alert('Please enter a movie title');
            return;
        }

        try {
            const response = await fetch('/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ movie: movieTitle })
            });

            const recommendations = await response.json();

            // Clear previous recommendations
            recommendationsContainer.innerHTML = '';

            if (recommendations.length === 0) {
                recommendationsContainer.innerHTML = '<p>No recommendations found.</p>';
                return;
            }

            recommendations.forEach(movie => {
                const recommendationEl = document.createElement('div');
                recommendationEl.classList.add('recommendation');
                recommendationEl.innerHTML = `
                    <h3>${movie.title}</h3>
                    <p>Genres: ${movie.genres}</p>
                    <p>Rating: ${movie.vote_average}/10</p>
                `;
                recommendationsContainer.appendChild(recommendationEl);
            });
        } catch (error) {
            console.error('Error:', error);
            recommendationsContainer.innerHTML = '<p>An error occurred while fetching recommendations.</p>';
        }
    });
});