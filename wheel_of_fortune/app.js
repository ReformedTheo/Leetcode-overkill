const canvas = document.getElementById('wheel');
const ctx = canvas.getContext('2d');
const spinBtn = document.getElementById('spin-btn');
const logoDisplay = document.getElementById('logo-display');

const segments = [
    'C',
    'JS',
    'C++',
    'C#',
    'Py',
    'Rust',
    'Go',
    'Java'
];

// Map of segment to its logo image path
const segmentImages = {
    'C': './images/C.png',
    'JS': './images/js.png',
    'C++': './images/Cpp.png',
    'C#': './images/csharp.png',
    'Py': './images/python.png',
    'Rust': './images/rust.png',
    'Go': './images/go.png',
    'Java': './images/java.png'
};

// Draw the wheel
function drawWheel() {
    const segmentAngle = 2 * Math.PI / segments.length;
    
    segments.forEach((segment, index) => {
        ctx.beginPath();
        ctx.arc(150, 150, 150, index * segmentAngle, (index + 1) * segmentAngle);
        ctx.lineTo(150, 150);
        ctx.closePath();
        ctx.fillStyle = index % 2 === 0 ? '#FFD700' : '#FF6347';
        ctx.fill();
        ctx.stroke();
        
        // Draw text 
        ctx.fillStyle = 'black';
        ctx.textAlign = 'right';
        ctx.font = '16px Arial';
        const angle = index * segmentAngle + segmentAngle / 2;
        ctx.fillText(segment, 150 + 110 * Math.cos(angle), 150 + 110 * Math.sin(angle));
    });
}

spinBtn.addEventListener('click', () => {
    const spins = Math.floor(Math.random() * (4 - 3 + 1)) + 3; // 3 to 4 spins
    const targetSegment = Math.floor(Math.random() * segments.length);
    const totalRotation = 2 * Math.PI * spins + targetSegment * (2 * Math.PI / segments.length);
    
    let rotation = 0;
    const step = totalRotation / 300;

    function animate() {
        ctx.clearRect(0, 0, 300, 300);
        ctx.save();
        ctx.translate(150, 150);
        ctx.rotate(rotation);
        ctx.translate(-150, -150);
        drawWheel();
        ctx.restore();

        rotation += step;

        if (rotation < totalRotation) {
            requestAnimationFrame(animate);
        } else {
            // Find out which segment is at the top
            let normalizedRotation = rotation % (2 * Math.PI); // Normalize to 0 to 2*PI
            let segmentIndex = Math.floor(normalizedRotation / (2 * Math.PI / segments.length));
            segmentIndex = segments.length - segmentIndex - 1; // Invert the index since the canvas coordinates are inverted
            if (segmentIndex < 0) segmentIndex = 0; // Ensure non-negative

            // Display the chosen logo
            logoDisplay.src = segmentImages[segments[segmentIndex]];
            logoDisplay.style.display = 'block';
        }
    }
    animate();
});

drawWheel();
