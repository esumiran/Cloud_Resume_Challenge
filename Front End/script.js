window.addEventListener("DOMContentLoaded", (event) => {
    GetVisitCount();
});


const AzureFunctionApi = 'http://localhost:7071/api/GetResumeCount';

const GetVisitCount = () => {
    let count = 100;
    fetch(AzureFunctionApi).then(response => {
        return response.json()
    }).then(response => {
        console.log("website called the azure function Api");
        count = response.visitor_count;
        document.getElementById("visitor_count").innerText = count;
    }).catch(function(error){
        console.log(error);
    })
    return count;
}