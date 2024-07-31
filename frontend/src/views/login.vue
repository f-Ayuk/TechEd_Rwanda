<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router"; // Import useRouter
import navigation from "@/components/navigation.vue";
import contacts from "@/components/contacts.vue";

const email = ref("");
const password = ref("");
const router = useRouter(); // Initialize router

const handleSubmit = async (e) => {
  e.preventDefault();

  const response = await fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: email.value,
      password: password.value,
    }),
  });

  if (response.ok) {
    // Handle successful login (e.g., redirect to the student dashboard)
    console.log("Login successful");
    router.push({ name: "student" }); // Navigate to student dashboard route
  } else {
    // Handle error (e.g., show an error message)
    console.error("Login failed");
  }
};
</script>

<template>
  <section class="signup">
    <navigation class="z" />

    <img src="../assets/photos/student&teacher.jpg" alt="" class="signup_img" />
    <div class="signup_wrapper">
      <h1>Sign up and start learning</h1>
      <form @submit="handleSubmit">
        <input
          v-model="email"
          type="text"
          id="email"
          name="email"
          required
          placeholder="email"
        />

        <input
          v-model="password"
          type="password"
          id="password"
          name="password"
          required
          placeholder="password"
        />

        <button type="submit">login</button>
      </form>
    </div>
  </section>
  <contacts />
</template>

<style scoped>
.signup {
  height: 100vh;
  background-color: #10123b;
  padding: 0 72px;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  position: relative;
  overflow: hidden;
}

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
</style>
