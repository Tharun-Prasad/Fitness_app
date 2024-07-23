document.getElementById('bmiForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);
    const age = parseInt(document.getElementById('age').value);
    
    if (isNaN(height) || isNaN(weight) || isNaN(age)) {
        alert("Please enter valid values");
        return;
    }
    
    const bmi = weight / (height * height);
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML =` Your BMI is ${bmi.toFixed(2)}`;
});