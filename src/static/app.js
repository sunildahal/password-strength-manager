// API Base URL
const API_BASE = window.location.origin;

// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Initialize forms
    initializeLoginForm();
    initializeStrengthForm();
    initializeGeneratorForm();
    initializeBreachForm();
    initializeLogs();

    // Check if user is logged in
    checkAuthStatus();
}

// Authentication
function checkAuthStatus() {
    fetch('/auth/status')
        .then(response => response.json())
        .then(data => {
            if (data.logged_in) {
                updateUIForLoggedInUser(data.user);
            }
        })
        .catch(error => console.log('Auth check failed:', error));
}

function updateUIForLoggedInUser(user) {
    // Update navigation if needed
    console.log('User logged in:', user);
}

// Login Form
function initializeLoginForm() {
    const loginForm = document.getElementById('login-form');
    const twofaForm = document.getElementById('2fa-form');

    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            fetch('/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                if (result.message === 'Password OK. Enter 2FA token.') {
                    document.getElementById('login-step').style.display = 'none';
                    document.getElementById('2fa-step').style.display = 'block';
                } else if (result.error) {
                    showAlert(result.error, 'error');
                }
            })
            .catch(error => {
                showAlert('Login failed. Please try again.', 'error');
            });
        });
    }

    if (twofaForm) {
        twofaForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            fetch('/auth/verify-2fa', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                if (result.message === 'Login successful') {
                    showAlert('Login successful! Redirecting...', 'success');
                    setTimeout(() => {
                        window.location.href = '/dashboard';
                    }, 1000);
                } else if (result.error) {
                    showAlert(result.error, 'error');
                }
            })
            .catch(error => {
                showAlert('2FA verification failed. Please try again.', 'error');
            });
        });
    }
}

// Password Strength Form
function initializeStrengthForm() {
    const strengthForm = document.getElementById('strength-form');
    const resultContainer = document.getElementById('strength-result');

    if (strengthForm) {
        strengthForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            fetch('/strength/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                displayStrengthResult(result);
            })
            .catch(error => {
                showAlert('Failed to check password strength.', 'error');
            });
        });
    }
}

function displayStrengthResult(result) {
    const resultContainer = document.getElementById('strength-result');
    let html = '<h4>Analysis Results:</h4>';

    if (result.error) {
        html += `<div class="alert alert-error">${result.error}</div>`;
    } else {
        const scoreColor = result.complexity_score >= 80 ? 'success' :
                          result.complexity_score >= 60 ? 'warning' : 'error';

        html += `
            <div class="result-container ${scoreColor}">
                <strong>Entropy:</strong> ${result.entropy.toFixed(2)} bits<br>
                <strong>Complexity Score:</strong> ${result.complexity_score}/100<br>
                <strong>Patterns Detected:</strong> ${result.patterns.join(', ') || 'None'}<br>
                <strong>Dictionary Attack Risk:</strong> ${result.dictionary_weak ? 'High' : 'Low'}
            </div>
        `;
    }

    resultContainer.innerHTML = html;
    resultContainer.style.display = 'block';
}

// Password Generator Form
function initializeGeneratorForm() {
    const generatorForm = document.getElementById('generator-form');
    const resultContainer = document.getElementById('generator-result');

    if (generatorForm) {
        generatorForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            // Convert checkbox values to boolean
            data.use_upper = data.use_upper === 'on';
            data.use_lower = data.use_lower === 'on';
            data.use_digits = data.use_digits === 'on';
            data.use_symbols = data.use_symbols === 'on';

            fetch('/generator/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                displayGeneratorResult(result);
            })
            .catch(error => {
                showAlert('Failed to generate password.', 'error');
            });
        });
    }
}

function displayGeneratorResult(result) {
    const resultContainer = document.getElementById('generator-result');
    let html = '<h4>Generated Password:</h4>';

    if (result.error) {
        html += `<div class="alert alert-error">${result.error}</div>`;
    } else {
        html += `
            <div class="result-container success">
                <div style="font-family: monospace; font-size: 1.2rem; margin-bottom: 10px;">
                    <strong>${result.generated_password}</strong>
                </div>
                <small>Length: ${result.length} | Options: ${Object.entries(result.options).filter(([k,v]) => v).map(([k,v]) => k.replace('use_', '')).join(', ')}</small>
            </div>
        `;
    }

    resultContainer.innerHTML = html;
    resultContainer.style.display = 'block';
}

// Breach Check Form
function initializeBreachForm() {
    const breachForm = document.getElementById('breach-form');
    const resultContainer = document.getElementById('breach-result');

    if (breachForm) {
        breachForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            fetch('/breach/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                displayBreachResult(result);
            })
            .catch(error => {
                showAlert('Failed to check password breach.', 'error');
            });
        });
    }
}

function displayBreachResult(result) {
    const resultContainer = document.getElementById('breach-result');
    let html = '<h4>Breach Check Results:</h4>';

    if (result.error) {
        html += `<div class="alert alert-error">${result.error}</div>`;
    } else {
        const statusClass = result.breached ? 'error' : 'success';
        const statusText = result.breached ?
            `⚠️ BREACHED: Found in ${result.count.toLocaleString()} breaches` :
            '✅ SAFE: Not found in known breaches';

        html += `
            <div class="result-container ${statusClass}">
                ${statusText}
                ${result.message ? `<br><small>${result.message}</small>` : ''}
            </div>
        `;
    }

    resultContainer.innerHTML = html;
    resultContainer.style.display = 'block';
}

// Activity Logs
function initializeLogs() {
    const refreshBtn = document.getElementById('refresh-logs');
    const logsContainer = document.getElementById('logs-container');

    if (refreshBtn) {
        refreshBtn.addEventListener('click', loadLogs);
        loadLogs(); // Load on page load
    }
}

function loadLogs() {
    const logsContainer = document.getElementById('logs-container');
    logsContainer.innerHTML = '<div class="loading">Loading activity logs...</div>';

    fetch('/dashboard/logs')
        .then(response => response.json())
        .then(logs => {
            displayLogs(logs);
        })
        .catch(error => {
            logsContainer.innerHTML = '<div class="alert alert-error">Failed to load logs.</div>';
        });
}

function displayLogs(logs) {
    const logsContainer = document.getElementById('logs-container');

    if (!logs || logs.length === 0) {
        logsContainer.innerHTML = '<div class="alert alert-info">No activity logs found.</div>';
        return;
    }

    let html = '';
    logs.slice(0, 10).forEach(log => { // Show last 10 logs
        const timestamp = new Date(log.timestamp).toLocaleString();
        html += `
            <div class="log-entry">
                <div>
                    <span class="log-action">${log.action}</span>
                    <span class="log-user">by ${log.user}</span>
                </div>
                <div class="log-time">${timestamp}</div>
            </div>
        `;
    });

    logsContainer.innerHTML = html;
}

// Utility Functions
function showAlert(message, type = 'info') {
    // Remove existing alerts
    const existingAlerts = document.querySelectorAll('.alert');
    existingAlerts.forEach(alert => alert.remove());

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.innerHTML = `<i class="fas fa-info-circle"></i> ${message}`;

    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Password copied to clipboard!', 'success');
    }).catch(() => {
        showAlert('Failed to copy password.', 'error');
    });
}

// Make functions globally available
window.copyToClipboard = copyToClipboard;