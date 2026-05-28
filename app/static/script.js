document.getElementById('docForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const generateBtn = document.getElementById('generateBtn');
    const previewArea = document.getElementById('preview');
    
    // UI Feedback
    generateBtn.textContent = 'Generating...';
    generateBtn.disabled = true;
    
    const formData = new FormData(e.target);
    
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Update Official Letterhead & Branding
            const companyNameInput = document.getElementById('company').value;
            document.getElementById('header_company_name').textContent = companyNameInput || 'Prakriti Enterprise';
            
            // Sync Recipient Header
            document.getElementById('preview_name').textContent = formData.get('name');
            document.getElementById('preview_date').textContent = data.date;
            document.getElementById('doc_title').textContent = formData.get('document_type');
            
            // Update Signatory based on company
            if (companyNameInput.includes('Prakriti')) {
                document.getElementById('signatory_name').textContent = 'Pooja Maru';
                document.querySelector('#signature_area p:last-child').textContent = 'Director, Prakriti Enterprise';
            } else {
                document.getElementById('signatory_name').textContent = 'Authorized Signatory';
                document.querySelector('#signature_area p:last-child').textContent = `HR Department, ${companyNameInput}`;
            }

            // Generate unique Doc ID
            const randomID = Math.floor(1000 + Math.random() * 9000);
            document.getElementById('doc_id').textContent = `PRK-${new Date().getFullYear()}-${randomID}`;

            // Convert Markdown to HTML (Bold and Line breaks)
            let content = data.document
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\n/g, '<br>');
            
            previewArea.innerHTML = `<div class="animate-in">${content}</div>`;
        } else {
            previewArea.innerHTML = `<div style="color: #ef4444; padding: 2rem; border: 1px solid currentColor; border-radius: 8px;">Error: ${data.error}</div>`;
        }
    } catch (err) {
        previewArea.innerHTML = `<div style="color: #ef4444;">Network Error: Could not connect to the backend.</div>`;
    } finally {
        generateBtn.textContent = 'Generate Professional Document';
        generateBtn.disabled = false;
    }
});

// Live Date Initialization for inputs
document.addEventListener('DOMContentLoaded', () => {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('start_date').value = today;
});
