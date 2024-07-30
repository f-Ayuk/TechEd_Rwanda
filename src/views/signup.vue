<script setup>
import navigation from "@/components/navigation.vue";
import contacts from "@/components/contacts.vue";
</script>

<template>
  <section class="signup">
    <navigation class="z" />

    <img src="../assets/photos/student&teacher.jpg" alt="" class="signup_img" />
    <div class="signup_wrapper">
      <h1>Sign up and start learning</h1>
      <form>
        <input
          type="text"
          id="name"
          name="name"
          required
          placeholder="full name"
        />

        <input
          type="email"
          id="email"
          name="email"
          required
          placeholder="email"
        />

        <input
          type="password"
          id="password"
          name="password"
          required
          placeholder="password"
        />

        <button type="submit">Sign Up</button>
      </form>
    </div>
  </section>
  <contacts />
</template>

<style scoped>
.signup {
  /* display: flex; */
  /* fle */
  height: 100vh;
  background-color: #10123b;
  padding: 0 72px;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  position: relative;
  overflow: hidden;
  .z {
    z-index: 100000;
  }
  .signup_img {
    position: absolute;
    border-radius: 50%;
    width: 600px;
    height: 600px;
    object-fit: cover;
    bottom: -100px;
    left: -100px;
    z-index: 10000;
  }

  .signup_wrapper {
    display: flex;
    flex-direction: column;
    width: 50vw;
    gap: 16px;

    h1 {
      font-size: 16px;
      color: white;
      text-transform: uppercase;
    }

    form {
      display: flex;
      flex-direction: column;
      gap: 12px;

      input {
        padding: 24px 12px;
        border: 1px solid white;
        color: white;
      }

      button {
        padding: 24px 12px;
        text-align: center;
        background-color: #a435f0;
        color: white;
        text-transform: uppercase;
      }
    }
  }
}
</style>
