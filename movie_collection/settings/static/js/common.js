// scripts.js

const BASE_URL = 'http://localhost:8000'; // Update with your Django server URL

// Function to fetch collections from the Django API
async function fetchCollections() {
    try {
        const response = await fetch(`${BASE_URL}/movies/collections/`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        displayCollections(data);
    } catch (error) {
        console.error('Error fetching collections:', error);
    }
}

// Function to display collections in the HTML
function displayCollections(collections) {
    const collectionsList = document.getElementById('collections-list');
    collectionsList.innerHTML = ''; // Clear previous content

    collections.forEach(collection => {
        const collectionElement = document.createElement('div');
        collectionElement.classList.add('collection');
        collectionElement.innerHTML = `
            <h2>${collection.title}</h2>
            <p>${collection.description}</p>
            <ul>
                ${collection.movies.map(movie => `<li>${movie.title}</li>`).join('')}
            </ul>
            <button onclick="deleteCollection('${collection.uuid}')">Delete</button>
        `;
        collectionsList.appendChild(collectionElement);
    });
}

// Function to handle form submission for creating a new collection
async function createCollection(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const title = formData.get('title');
    const description = formData.get('description');
    // Fetch movies if needed or provide a way to select movies

    try {
        const response = await fetch(`${BASE_URL}/collections/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, description })
        });
        if (!response.ok) {
            throw new Error('Failed to create collection');
        }
        form.reset(); // Clear form fields after successful creation
        fetchCollections(); // Refresh collection list after creation
    } catch (error) {
        console.error('Error creating collection:', error);
    }
}

// Function to delete a collection via DELETE request
async function deleteCollection(collectionUuid) {
    try {
        const response = await fetch(`${BASE_URL}/collections/${collectionUuid}/`, {
            method: 'DELETE'
        });
        if (!response.ok) {
            throw new Error('Failed to delete collection');
        }
        fetchCollections(); // Refresh collection list after deletion
    } catch (error) {
        console.error('Error deleting collection:', error);
    }
}

// Event listener for form submission
const createCollectionForm = document.getElementById('create-collection-form');
createCollectionForm.addEventListener('submit', createCollection);

// Initial fetch of collections when the page loads
fetchCollections();
