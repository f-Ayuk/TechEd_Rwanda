<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router"; // Import useRouter
import navigation from "@/components/navigation.vue";
import course from "@/components/course.vue";
import contacts from "@/components/contacts.vue";
import { RouterLink } from "vue-router";

const email = ref("");
const password = ref("");
const router = useRouter(); // Initialize router

const handleSubmit = async (e) => {
  e.preventDefault();

  const response = await fetch("https://teched-rwanda.onrender.com/login", {
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
    const data = await response.json(); // Assuming the backend returns user data

    // Check the user's email and redirect accordingly
    if (data.email === "j.mugisha1@super.com") {
      this.$router.push("admin"); // Redirects to /new-route
    } else {
      router.push({ name: "student" }); // Navigate to student dashboard route
    }
  } else {
    // Handle error (e.g., show an error message)
    console.error("Login failed");
  }
};
</script>

<template>
  <section class="signup">
    <navigation class="z" />
    <div class="signup_content">
      <img src="../assets/photos/student&teacher.jpg" alt="Students and Teacher" class="signup_img" />
      <div class="signup_wrapper">
        <h5>Welcome again, login to access the dashboard</h5>
        <form @submit="handleSubmit">
          <input v-model="email" type="text" id="email" name="email" required placeholder="Enter your email" />
          <input v-model="password" type="password" id="password" name="password" required placeholder="Enter your Password" />
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  </section>
  <contacts class="footer" />
</template>

<style scoped>
.signup {
  height: calc(100vh - 70px); /* Adjusted for space below the navigation bar */
  max-width: 100%;
  background-color: #10123b;
  padding: 0 2rem; /* Responsive padding */
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  margin-top: 80px; /* Space from the navigation bar */
}

.z {
  z-index: 100000;
}

.signup_content {
  display: flex;
  margin-top: 300px;
  margin-bottom: 330px;
  justify-content: center;
  flex-direction: row;
  align-items: center;
  gap: 9rem; /* Space between image and form */
}

.signup_img {
  border-radius: 50%;
  width: 40vw;
  height: 40vw;
  max-width: 600px;
  max-height: 600px;
  object-fit: cover;
  z-index: 10001;
}

.signup_wrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 800px;
  padding: 1rem;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.1);
  z-index: 10001;
}

.signup_wrapper h5 {
  font-size: 1.2rem;
  font-weight: 700;
  color: #c67ff5;
  text-transform: uppercase;
  text-align: center;
  margin-bottom: 1rem;
}

.signup_wrapper form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.signup_wrapper p {
  color: white;
  font-size: 1rem;
  margin: 0;
}

.signup_wrapper input {
  padding: 15px;
  border: 1px solid white;
  color: white;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  font-size: 1rem;
}

.signup_wrapper button {
  padding: 12px;
  text-align: center;
  background-color: #a435f0;
  color: white;
  text-transform: uppercase;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.signup_wrapper button:hover {
  background-color: #9334d7;
  transform: translateY(-2px);
}

/* Media Queries for Responsiveness */
@media (max-width: 1024px) {
  .signup {
    padding: 0 1.5rem;
    margin-top: 80px; /* Increased space for larger screens */
  }

  .signup_img {
    width: 45vw;
    height: 45vw;
  }

  .signup_wrapper {
    width: 80%;
    padding: 1.5rem;
    margin-bottom: 2rem; /* Adjusted space for larger screens */
  }

  .signup_wrapper h5 {
    font-size: 1.25rem;
  }
}

@media (max-width: 768px) {
  .signup {
    padding: 0 1rem;
    margin-top: 90px; /* Increased space for medium screens */
  }

  .signup_img {
    width: 50vw;
    height: 50vw;
  }

  .signup_wrapper {
    width: 85%;
    padding: 1rem;
    margin-bottom: 2rem; /* Adjusted space for medium screens */
  }

  .signup_wrapper h5 {
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .signup {
    padding: 0 0.5rem;
    margin-top: 100px; /* Increased space for smaller screens */
  }

  .signup_img {
    width: 60vw;
    height: 60vw;
  }

  .signup_wrapper {
    width: 95%;
    padding: 0.5rem;
    margin-bottom: 1rem; /* Adjusted space for smaller screens */
  }

  .signup_wrapper h5 {
    font-size: 0.875rem;
  }

  .signup_wrapper input {
    font-size: 0.875rem;
    padding: 10px;
  }

  .signup_wrapper button {
    font-size: 0.875rem;
    padding: 10px;
  }
}
</style>
