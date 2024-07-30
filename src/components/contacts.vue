<script setup></script>
<template>
  <footer class="contacts">
    <div class="contacts_img_1">
      <img src="../assets/photos/contacts.jpg" alt="" />
    </div>
    <div class="contacts_img_2">
      <img src="../assets/photos/contacts.jpg" alt="" />
    </div>
    <div class="contacts_links">
      <p>for more information please reach out through our emails or socials</p>

      <div class="links_wrapper">
        <a href="">instagram</a>
        <a href="">whatsapp channel</a>
        <a href="">twitter</a>
        <a href="">facebook</a>
        <a href="">linked in</a>
      </div>
    </div>
    <div class="contacts_email">
      <h1>info@techedrwanda.com</h1>
    </div>
    <div class="contacts_footer">
      <p>a product of group 2</p>
      <p>all copyrights reserved @2024</p>
    </div>
  </footer>
</template>
<style scoped>
.contacts {
  height: 100vh;
  background-color: black;
  display: flex;
  flex-direction: column;
  padding: 144px 72px 24px 72px;
  position: relative;

  .contacts_img_1 {
    position: absolute;
    left: -10%;
    top: 62%;
    transform: translateY(-50%);
    height: 500px;
    width: 500px;
    border-radius: 50%;

    img {
      height: 450px;
      width: 450px;
      border-radius: 50%;
      object-fit: cover;
    }
  }
  .contacts_img_2 {
    position: absolute;
    left: -15%;
    top: 62%;
    transform: translateY(-50%);
    height: 500px;
    width: 500px;
    border-radius: 50%;

    img {
      height: 450px;
      width: 450px;
      border-radius: 50%;
      object-fit: cover;
      opacity: 0.5;
    }
  }

  .contacts_links {
    display: flex;
    flex-direction: row;
    width: 100%;
    justify-content: space-between;

    p {
      font-size: 12px;
      color: white;
      text-transform: uppercase;
      width: 296px;
    }

    .links_wrapper {
      display: flex;
      flex-direction: row;
      gap: 24px;

      a {
        font-size: 12px;
        color: white;
        text-transform: uppercase;
      }
    }
  }

  .contacts_email {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    h1 {
      font-size: 48px;
      color: white;
      text-transform: uppercase;
    }
  }

  .contacts_footer {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;

    p {
      font-size: 12px;
      text-transform: uppercase;
      color: white;
    }
  }
}
</style>
