<script setup></script>

<template>
  <nav class="navigation">
    <div class="nav_links">
      <p>techEd Rwanda</p>
      <div class="nav_links_wrapper">
        <a href="">all courses</a>
        <a href="">about us</a>
        <a href="">reach out</a>
      </div>
    </div>
    <div class="nav_register">
      <RouterLink to="/signup" class="nav_signup">signup</RouterLink>
      <RouterLink to="/login" class="nav_login">log in</RouterLink>
    </div>
  </nav>
</template>

<style>
.navigation {
  display: flex;
  flex-direction: row;
  background-color: white;
  padding: 8px 32px;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  margin: 12px 0;
  width: 96vw;
  border-radius: 36px;
  z-index: 10000;
  .nav_links {
    width: 40vw;
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    p {
      font-size: 16px;
    }

    .nav_links_wrapper {
      display: flex;
      flex-direction: row;
      gap: 24px;

      a {
        text-transform: uppercase;
        font-size: 14px;
      }
    }
  }

  .nav_register {
    display: flex;
    flex-direction: row;
    gap: 24px;

    a {
      font-size: 12px;
      text-transform: uppercase;
      padding: 6px 12px;
      border-radius: 24px;
    }

    .nav_login {
      background-color: #10123b;
      color: white;
    }

    .nav_signup {
      border: 1px solid #10123b;
      color: #10123b;
    }
  }
}
</style>
