document.getElementById('analyze-btn').addEventListener('click', async () => {
    const fileInput = document.getElementById('csv-file');
    const btn = document.getElementById('analyze-btn');
    const spinner = document.getElementById('loading-spinner');
    const dashboard = document.getElementById('results-dashboard');
    
    const file = fileInput.files[0];
    if (!file) {
        alert("ACCESS DENIED: Please upload a CSV dataset first.");
        return;
    }

    btn.classList.add('hidden');
    spinner.classList.remove('hidden');
    dashboard.classList.add('hidden');

    const formData = new FormData();
    formData.append('dataset', file);

    try {
        const response = await fetch('http://127.0.0.1:5000/analyze', { method: 'POST', body: formData });
        const jsonResponse = await response.json();
        
        if (jsonResponse.status === "success") {
            const data = jsonResponse.data;
            
            // 1. Populate EDA (Data Overview)
            document.getElementById('row-count').textContent = data.eda.total_rows;
            document.getElementById('feature-count').textContent = data.eda.total_features;
            
            let distHtml = "";
            for (const [className, count] of Object.entries(data.eda.class_distribution)) {
                distHtml += `<div class="dist-item"><span>${className}</span> <span>${count}</span></div>`;
            }
            document.getElementById('class-dist-box').innerHTML = distHtml;

            // 2. Populate Extended Metrics
            document.getElementById('f1-display').textContent = data.metrics.f1_score;
            document.getElementById('acc-display').textContent = data.metrics.accuracy;
            document.getElementById('prec-display').textContent = data.metrics.precision;
            document.getElementById('rec-display').textContent = data.metrics.recall;
            
            // 3. Populate Matrix
            let matrixHtml = "";
            data.confusion_matrix.forEach(row => {
                matrixHtml += `[ ${row.join(" \t ")} ]\n`;
            });
            document.getElementById('matrix-display').textContent = matrixHtml;

            spinner.classList.add('hidden');
            dashboard.classList.remove('hidden');
        } else {
            alert("Backend Error: " + jsonResponse.message);
            btn.classList.remove('hidden');
            spinner.classList.add('hidden');
        }
    } catch (error) {
        console.error("Fetch error: ", error);
        alert("Network Error: Could not connect to the backend server.");
        btn.classList.remove('hidden');
        spinner.classList.add('hidden');
    }
});