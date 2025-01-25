window.onload = () => {
    // Fetch the JSON data
    fetch('data/video_data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            return response.json(); // Parse JSON
        })
        .then(data => {
            console.log(data); // Log the data to verify it's correct
            renderTable(data); // Pass data to the render function
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
};

// Function to render data in the table
function renderTable(data) {
    const tableBody = document.getElementById('video-list');
    
    // Clear the table before inserting new rows
    tableBody.innerHTML = '';

    data.forEach(video => {
        const row = tableBody.insertRow();
        
        // Insert new cells and populate with the video data
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);
        const cell4 = row.insertCell(3);

        // Map data to table cells
        cell1.textContent = video["Title"] || 'N/A';       // Video Title
        cell2.textContent = video["Views"] || 'N/A';       // View Count
        cell3.textContent = video["Likes"] || 'N/A';       // Likes
        cell4.textContent = video["Comments"] || 'N/A';    // Comments
    });
}
