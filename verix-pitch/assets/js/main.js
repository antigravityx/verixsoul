// ==========================================
// VERIX SOUL - TECHNICAL PITCH DECK
// JavaScript Interactivo
// ==========================================

// ========== Inicialización ==========
document.addEventListener('DOMContentLoaded', () => {
    initParticles();
    initSmoothScroll();
    initMermaid();
    initFormHandler();
    initScrollAnimations();
});

// ========== Particles.js Background ==========
function initParticles() {
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            particles: {
                number: {
                    value: 80,
                    density: {
                        enable: true,
                        value_area: 800
                    }
                },
                color: {
                    value: '#8b5cf6'
                },
                shape: {
                    type: 'circle'
                },
                opacity: {
                    value: 0.5,
                    random: true,
                    anim: {
                        enable: true,
                        speed: 1,
                        opacity_min: 0.1,
                        sync: false
                    }
                },
                size: {
                    value: 3,
                    random: true,
                    anim: {
                        enable: true,
                        speed: 2,
                        size_min: 0.1,
                        sync: false
                    }
                },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#8b5cf6',
                    opacity: 0.4,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 2,
                    direction: 'none',
                    random: false,
                    straight: false,
                    out_mode: 'out',
                    bounce: false
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: {
                        enable: true,
                        mode: 'repulse'
                    },
                    onclick: {
                        enable: true,
                        mode: 'push'
                    },
                    resize: true
                },
                modes: {
                    repulse: {
                        distance: 100,
                        duration: 0.4
                    },
                    push: {
                        particles_nb: 4
                    }
                }
            },
            retina_detect: true
        });
    }
}

// ========== Smooth Scroll ==========
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ========== Mermaid Diagrams ==========
function initMermaid() {
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({
            startOnLoad: true,
            theme: 'dark',
            themeVariables: {
                primaryColor: '#8b5cf6',
                primaryTextColor: '#f8fafc',
                primaryBorderColor: '#8b5cf6',
                lineColor: '#3b82f6',
                secondaryColor: '#3b82f6',
                tertiaryColor: '#06b6d4',
                background: '#11111b',
                mainBkg: '#11111b',
                secondBkg: '#1a1a2e',
                tertiaryBkg: '#0a0a0f',
                textColor: '#f8fafc',
                fontSize: '16px'
            }
        });
    }
}

// ========== Form Handler ==========
function initFormHandler() {
    const form = document.getElementById('collaborateForm');
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                interest: document.getElementById('interest').value,
                message: document.getElementById('message').value
            };
            
            // Aquí se puede integrar con un servicio de email
            // Por ahora, mostramos un alert
            alert(`¡Gracias por tu interés, ${formData.name}!\n\nTe contactaremos pronto a ${formData.email}.\n\nTipo de colaboración: ${formData.interest}`);
            
            // Limpiar formulario
            form.reset();
            
            // En producción, aquí iría la llamada a la API
            // await fetch('/api/contact', {
            //     method: 'POST',
            //     headers: { 'Content-Type': 'application/json' },
            //     body: JSON.stringify(formData)
            // });
        });
    }
}

// ========== Scroll Animations ==========
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Animar cards al hacer scroll
    const animatedElements = document.querySelectorAll(
        '.problem-card, .ecosystem-card, .philosophy-card, .funding-category, .timeline-item'
    );
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// ========== Navbar Scroll Effect ==========
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(10, 10, 15, 0.98)';
        navbar.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.5)';
    } else {
        navbar.style.background = 'rgba(10, 10, 15, 0.95)';
        navbar.style.boxShadow = 'none';
    }
});

// ========== Active Nav Link ==========
const sections = document.querySelectorAll('.section');
const navLinks = document.querySelectorAll('.nav-menu a');

window.addEventListener('scroll', () => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// ========== Typing Effect for Hero ==========
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Opcional: activar efecto de escritura en el tagline
// const tagline = document.querySelector('.tagline');
// if (tagline) {
//     const originalText = tagline.textContent;
//     typeWriter(tagline, originalText, 50);
// }

// ========== Console Easter Egg ==========
console.log('%c🌌 VERIX SOUL', 'font-size: 24px; font-weight: bold; background: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;');
console.log('%c¿Eres un desarrollador curioso? 👀', 'font-size: 14px; color: #06b6d4;');
console.log('%cÚnete al proyecto: https://github.com/antigravityx/vris', 'font-size: 12px; color: #94a3b8;');
console.log('%cLicencia de Existencia Universal - 100% Open Source', 'font-size: 10px; color: #8b5cf6; font-style: italic;');
