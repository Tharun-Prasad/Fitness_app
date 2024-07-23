function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function handleClick(planType, userProgressJson) {
    const csrftoken = getCookie('csrftoken');

    // Parse the userProgressJson string to JSON object
    let userProgress;
    try {
        userProgress = JSON.parse(userProgressJson);
    } catch (error) {
        console.error('Failed to parse userProgress JSON:', error);
        alert('Failed to update: Invalid userProgress object');
        return;
    }

    // Ensure userProgress is defined and has necessary properties
    if ( userProgress.length === 0 || !userProgress[0].fields) {
        console.error('Invalid userProgress object:', userProgress);
        alert('Failed to update: Invalid userProgress object');
        return;
    }

    const progressData = userProgress[0].fields;

    // Update the planType of userProgress
    progressData.plan = planType;

    fetch(`/update-progress/${userProgress[0].pk}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            user: progressData.user,
            plan: progressData.plan,
            no_days: progressData.no_days
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            alert('Plan updated successfully!');
            // Handle success scenario (e.g., update UI)
        } else {
            alert('Failed to update plan');
        }
    })
    .catch(error => {
        alert('Failed to update: ' + error.message);
        console.error('Error:', error);
    });
}