document.getElementById('generateBtn').addEventListener('click', async () => {
    const prompt = document.getElementById('prompt').value;
    const output = document.getElementById('output');
    
    output.innerText = 'Generating script...';
  
    try {
      const response = await fetch('http://127.0.0.1:8000/api/scripts/generate/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });
  
      const data = await response.json();
  
      if (response.ok) {
        output.innerText = data.content || 'No content generated.';
      } else {
        output.innerText = `Error: ${data.error}`;
      }
    } catch (error) {
      output.innerText = `Error: ${error.message}`;
    }
  });
  