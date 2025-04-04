document.addEventListener("DOMContentLoaded", function () {
    const apiUrl = "https://33cfivi7di2up7i43jdihvrwre0urcxn.lambda-url.us-east-2.on.aws/";

    fetch(apiUrl)
        .then(response => response.json()) 
        .then(data => {
            const visitorElement = document.getElementById("visitor_count");

            if (data?.Visitor_Count !== undefined) {
                visitorElement.innerText = data.Visitor_Count;
            } else {
                throw new Error("Visitor_Count not found in API response.");
            }
        })
        .catch(error => {
            console.error("Error fetching visitor count:", error);

            
        });
});
