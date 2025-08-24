function stuDirect() {
    console.log("Redirecting...");
    window.location.href = "/stulogin";
}
function staffLogin() {
    console.log("Redirecting...");
    window.location.href = "/stafflog";
}

const standardCleaningToggle = document.getElementById('standardCleaningToggle');
const deepCleaningToggle = document.getElementById('deepCleaningToggle');
const placeRequestButton = document.getElementById('placeRequestButton');
const messageBox = document.getElementById('messageBox');

function handleToggleChange(changedToggle) {
    messageBox.style.display = 'none'; 

    if (changedToggle === standardCleaningToggle && standardCleaningToggle.checked) {
        deepCleaningToggle.checked = false;
    } else if (changedToggle === deepCleaningToggle && deepCleaningToggle.checked) {
        standardCleaningToggle.checked = false;
    }
}

standardCleaningToggle.addEventListener('change', function() {
    handleToggleChange(this);
});
deepCleaningToggle.addEventListener('change', function() {
    handleToggleChange(this);
});

placeRequestButton.addEventListener('click', function() {
    const requestData = {
        selectedOption: standardCleaningToggle.checked ? 'Standard Cleaning' : (deepCleaningToggle.checked ? 'Deep Cleaning' : 'None'),
        timestamp: new Date().toISOString() 
    };

    if (!standardCleaningToggle.checked && !deepCleaningToggle.checked) {
        messageBox.textContent = '⚠️ Please select one cleaning option to place a request.';
        messageBox.className = 'mt-6 p-4 rounded-md text-center bg-yellow-200 text-yellow-800';
        messageBox.style.display = 'block';
        return; 
    }

    console.log('Cleaning request placed with options:', requestData);

    messageBox.textContent = `🎉 Your request for ${requestData.selectedOption} has been placed!`;
    messageBox.className = 'mt-6 p-4 rounded-md text-center bg-green-200 text-green-800';
    messageBox.style.display = 'block';

    standardCleaningToggle.checked = false;
    deepCleaningToggle.checked = false;
});

function sntDashDirect() {
    if (document.getElementById("email"))
    console.log("Redirecting...");
    window.location.href = "/studash";
}

function goBack() {
    console.log("Going Back....");
    window.location.href = '/'
}