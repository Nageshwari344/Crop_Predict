document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll("section");
  const navLinks = document.querySelectorAll(".nav-link");
  const startDetectionBtn = document.getElementById('startDetectionBtn');

  const loginModal = document.getElementById('loginModal');
  const registerModal = document.getElementById('registerModal');

  const loginBtn = document.querySelector('a[href="#login"]');
  const closeLoginBtn = document.getElementById('closeModal');
  const closeRegisterBtn = document.getElementById('closeRegisterModal');

  const openRegisterLink = document.querySelector('#loginModal a[href="#"]');
  const openLoginFromRegisterBtn = document.getElementById('openLoginFromRegister');
  document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-link");
    const startDetectionBtn = document.getElementById('startDetectionBtn');
  
    const loginModal = document.getElementById('loginModal');
    const registerModal = document.getElementById('registerModal');
  
    const loginBtn = document.querySelector('a[href="#login"]');
    const closeLoginBtn = document.getElementById('closeModal');
    const closeRegisterBtn = document.getElementById('closeRegisterModal');
  
    const openRegisterLink = document.querySelector('#loginModal a[href="#"]');
    const openLoginFromRegisterBtn = document.getElementById('openLoginFromRegister');
  
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");
  
    // Highlight navigation links on scroll
    window.addEventListener("scroll", () => {
      let currentSectionId = "";
      sections.forEach(section => {
        const offset = section.offsetTop - 130;
        if (window.pageYOffset >= offset) {
          currentSectionId = section.id;
        }
      });
  
      navLinks.forEach(link => {
        const href = link.getAttribute("href");
        link.classList.remove("border-b-2", "border-green-700", "text-green-900");
        if (href.includes(currentSectionId)) {
          link.classList.add("border-b-2", "border-green-700", "text-green-900");
        }
      });
    });
  
    // Show login modal when detection starts
    startDetectionBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      loginModal?.classList.remove('hidden');
    });
  
    // Open login modal
    loginBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      loginModal?.classList.remove('hidden');
    });
  
    // Close login modal
    closeLoginBtn?.addEventListener('click', () => {
      loginModal?.classList.add('hidden');
    });
  
    // Close register modal
    closeRegisterBtn?.addEventListener('click', () => {
      registerModal?.classList.add('hidden');
    });
  
    // Switch to register modal
    openRegisterLink?.addEventListener('click', (e) => {
      e.preventDefault();
      loginModal?.classList.add('hidden');
      registerModal?.classList.remove('hidden');
    });
  
    // Switch back to login modal
    openLoginFromRegisterBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      registerModal?.classList.add('hidden');
      loginModal?.classList.remove('hidden');
    });
  
    // Hide modals on outside click
    window.addEventListener('click', (e) => {
      if (e.target === loginModal) loginModal.classList.add('hidden');
      if (e.target === registerModal) registerModal.classList.add('hidden');
    });
  
    // Handle login form submission
    loginForm?.addEventListener("submit", (e) => {
      const email = document.getElementById("loginEmail").value.trim();
      const password = document.getElementById("loginPassword").value.trim();
  
      if (!email || !password) {
        e.preventDefault();
        alert("Please fill in all login fields.");
      }
      // Else allow form to submit normally
    });
  
    // Handle registration form submission
    registerForm?.addEventListener("submit", (e) => {
      const name = document.getElementById("registerName").value.trim();
      const email = document.getElementById("registerEmail").value.trim();
      const password = document.getElementById("registerPassword").value.trim();
  
      if (!name || !email || !password) {
        e.preventDefault();
        alert("Please fill in all registration fields.");
      }
      // Else allow form to submit normally
    });
  
  });
  
  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");

  // Highlight navigation links on scroll
  window.addEventListener("scroll", () => {
    let currentSectionId = "";
    sections.forEach(section => {
      const offset = section.offsetTop - 130;
      if (window.pageYOffset >= offset) {
        currentSectionId = section.id;
      }
    });

    navLinks.forEach(link => {
      const href = link.getAttribute("href");
      link.classList.remove("border-b-2", "border-green-700", "text-green-900");
      if (href.includes(currentSectionId)) {
        link.classList.add("border-b-2", "border-green-700", "text-green-900");
      }
    });
  });

  // Show login modal when detection starts
  startDetectionBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    loginModal?.classList.remove('hidden');
  });

  // Open login modal
  loginBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    loginModal?.classList.remove('hidden');
  });

  // Close login modal
  closeLoginBtn?.addEventListener('click', () => {
    loginModal?.classList.add('hidden');
  });

  // Close register modal
  closeRegisterBtn?.addEventListener('click', () => {
    registerModal?.classList.add('hidden');
  });

  // Switch to register modal
  openRegisterLink?.addEventListener('click', (e) => {
    e.preventDefault();
    loginModal?.classList.add('hidden');
    registerModal?.classList.remove('hidden');
  });

  // Switch back to login modal
  openLoginFromRegisterBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    registerModal?.classList.add('hidden');
    loginModal?.classList.remove('hidden');
  });

  // Hide modals on outside click
  window.addEventListener('click', (e) => {
    if (e.target === loginModal) loginModal.classList.add('hidden');
    if (e.target === registerModal) registerModal.classList.add('hidden');
  });

  // Handle login form submission
  loginForm?.addEventListener("submit", (e) => {
    e.preventDefault();
    const email = document.getElementById("loginEmail").value.trim();
    const password = document.getElementById("loginPassword").value.trim();

    if (email && password) {
      window.location.href = "/login";
    } else {
      alert("Please fill in all login fields.");
    }
  });

  // Handle registration form submission
  registerForm?.addEventListener("button", (e) => {
    e.preventDefault();
    const name = document.getElementById("registerName").value.trim();
    const email = document.getElementById("registerEmail").value.trim();
    const password = document.getElementById("registerPassword").value.trim();

    if (name && email && password) {
      window.location.href = "/dashboard";
    } else {
      alert("Please fill in all registration fields.");
    }
  });
  
});
