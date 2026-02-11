async function analyze() {
    const resumeText = document.getElementById("resume").value;
    const jdText = document.getElementById("jd").value;

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            resume_text: resumeText,
            job_description: jdText
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Match Percentage: ${data.match_percentage}%</h3>
        <p><strong>Matched Keywords:</strong> ${data.matched_keywords.join(", ")}</p>
        <p><strong>Missing Keywords:</strong> ${data.missing_keywords.join(", ")}</p>
    `;
}
