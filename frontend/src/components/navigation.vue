<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <nav class="navigation">
    <div class="nav_links">
      <RouterLink to="/"><img src="../assets/photos/logo.jpeg" alt="Logo" class="nav_logo" /></RouterLink>
      <div class="nav_links_wrapper">
        <RouterLink to="/" class="nav_link">Home</RouterLink>
        <RouterLink to="/" class="nav_link">About Us</RouterLink>
        <RouterLink to="/" class="nav_link">Support</RouterLink>
        <RouterLink to="/" class="nav_link">Contact Us</RouterLink>
      </div>
    </div>
    <div class="nav_register">
      <RouterLink to="/signup" class="nav_signup">Sign Up</RouterLink>
      <RouterLink to="/login" class="nav_login">Log In</RouterLink>
    </div>
  </nav>
</template>

<style scoped>
.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 32px;
  background-color: white;
  position: fixed;
  top: 0;
  width: 100%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.nav_logo {
  height: 40px;
  object-fit: contain;
}

.nav_links {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.nav_links_wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  flex: 1;
  cursor: pointer;
}

.nav_link {
  text-transform: uppercase;
  font-size: 14px;
  color: #10123b;
  text-decoration: none;
  padding: 8px 16px;
  transition: color 0.3s ease;
  cursor: pointer;
}

.nav_link:hover {
  color: #ff6f61;
  cursor: pointer;
}

.nav_register {
  display: flex;
  align-items: center;
  gap: 24px;
  cursor: pointer;
}

.nav_signup, .nav_login {
  text-transform: uppercase;
  font-size: 12px;
  padding: 6px 12px;
  border-radius: 24px;
  cursor: pointer;
  text-decoration: none;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.nav_signup {
  border: 1px solid #10123b;
  color: #10123b;
  cursor: pointer;
  background-color: transparent;
}

.nav_signup:hover {
  background-color: #10123b;
  color: white;
  cursor: pointer;
}

.nav_login {
  background-color: #10123b;
  color: white;
  cursor: pointer;
}

.nav_login:hover {
  cursor: pointer;
  background-color: #ff6f61;
}

@media (max-width: 768px) {
  .nav_links_wrapper {
    display: none;
  }

  .nav_links {
    flex: 1;
    display: flex;
    justify-content: center;
  }

  .nav_links_wrapper_mobile {
    display: flex;
    flex-direction: column;
    gap: 12px;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background-color: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 16px;
  }

  .nav_toggle {
    display: block;
  }

  .nav_toggle_icon {
    font-size: 24px;
    cursor: pointer;
  }
}

@media (min-width: 769px) {
  .nav_toggle {
    display: none;
  }
}
</style>
