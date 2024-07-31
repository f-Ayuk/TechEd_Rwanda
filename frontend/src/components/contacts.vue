<script setup></script>

<template>
  <footer class="contacts">
    <div class="contacts_content">
      <h1>Get In Touch</h1>
      <p>Connect with us through our social media channels:</p>
      <div class="links_wrapper">
        <a href="#" aria-label="Instagram" class="social-icon"><i class="fab fa-instagram"></i></a>
        <a href="#" aria-label="WhatsApp" class="social-icon"><i class="fab fa-whatsapp"></i></a>
        <a href="#" aria-label="Twitter" class="social-icon"><i class="fab fa-twitter"></i></a>
        <a href="#" aria-label="Facebook" class="social-icon"><i class="fab fa-facebook-f"></i></a>
        <a href="#" aria-label="LinkedIn" class="social-icon"><i class="fab fa-linkedin-in"></i></a>
      </div>
    </div>
    <div class="contacts_email">
      <h2>Contact Us</h2>
      <p><a href="mailto:info@techedrwanda.com">info@techedrwanda.com</a></p>
    </div>
    <div class="contacts_footer">
      <p>A product of Group 2</p>
      <p>All copyrights reserved ©2024</p>
    </div>
  </footer>
</template>

<style scoped>
.contacts {
  background-color: #212121;
  color: #e0e0e0;
  padding: 40px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border-top: 5px solid #ff5722;
}

.contacts_content {
  max-width: 800px;
  margin-bottom: 30px;
}

.contacts_content h1 {
  font-size: 28px;
  margin-bottom: 10px;
  font-weight: bold;
}

.contacts_content p {
  font-size: 16px;
  margin-bottom: 20px;
}

.links_wrapper {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-bottom: 30px;
}

.social-icon {
  font-size: 32px;
  color: #e0e0e0;
  text-decoration: none;
  transition: color 0.3s ease, transform 0.3s ease;
}

.social-icon:hover {
  color: #ff5722;
  transform: scale(1.1);
}

.contacts_email {
  margin-bottom: 30px;
}

.contacts_email h2 {
  font-size: 22px;
  margin-bottom: 10px;
  font-weight: bold;
}

.contacts_email p {
  font-size: 16px;
}

.contacts_email a {
  color: #ff5722;
  text-decoration: none;
  transition: color 0.3s ease;
}

.contacts_email a:hover {
  color: #e0e0e0;
}

.contacts_footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  font-size: 14px;
}

.contacts_footer p {
  margin: 0;
}

@media (max-width: 600px) {
  .contacts_content h1 {
    font-size: 24px;
  }

  .contacts_content p {
    font-size: 14px;
  }

  .links_wrapper {
    gap: 15px;
  }

  .social-icon {
    font-size: 28px;
  }

  .contacts_email h2 {
    font-size: 20px;
  }

  .contacts_email p {
    font-size: 14px;
  }

  .contacts_footer p {
    font-size: 12px;
  }
}
</style>
