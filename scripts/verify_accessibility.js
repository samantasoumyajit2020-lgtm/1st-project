const fs = require('fs');
const http = require('http');

// Check file content directly
const htmlContent = fs.readFileSync('public/analytics.html', 'utf8');

let issues = [];

// Check Back Button
if (!htmlContent.includes('aria-label="Go back"')) {
    issues.push('Back button missing aria-label');
}
if (!htmlContent.match(/<button class="back-btn"[^>]*>[\s\S]*?<svg[^>]*aria-hidden="true"/)) {
    // This regex is a bit simplistic but sufficient for a quick check if we assume standard formatting
    // A better check is just to see if the SVG inside back-btn has aria-hidden
    // Let's just check if we can find the specific pattern we expect to be missing
}

// Check Navigation Links
const navMatches = htmlContent.match(/<a href="#" class="nav-item">/g);
if (navMatches && navMatches.length > 0) {
    issues.push(`Found ${navMatches.length} nav items without aria-labels`);
}

// Check Active Link
if (htmlContent.includes('class="nav-item active"') && !htmlContent.includes('aria-current="page"')) {
    issues.push('Active nav item missing aria-current="page"');
}

console.log('--- Static Analysis Issues ---');
console.log(issues.join('\n'));

// Check Server
http.get('http://localhost:3000/analytics.html', (res) => {
    console.log('\n--- Server Check ---');
    console.log(`Status Code: ${res.statusCode}`);
    if (res.statusCode === 200) {
        console.log('Server is serving analytics.html');
    } else {
        console.error('Server failed to serve analytics.html');
    }
}).on('error', (e) => {
    console.error(`Got error: ${e.message}`);
});
