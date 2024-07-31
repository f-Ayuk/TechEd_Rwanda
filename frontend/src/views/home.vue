<script setup>
import navigation from "@/components/navigation.vue";
import course from "@/components/course.vue";
import contacts from "@/components/contacts.vue";
import { RouterLink } from "vue-router";
</script>

<template>
  <navigation />
  <section class="home">
    <div class="home_index">
      <img
        src="../assets/photos/student&teacher.jpg"
        alt="Students and Teacher"
        class="index_img img_1"
      />
      <img
        src="../assets/photos/home_1.jpg"
        alt="Home Image 1"
        class="index_img img_2"
      />
      <img
        src="../assets/photos/home_3.jpg"
        alt="Home Image 2"
        class="index_img img_3"
      />
      <img
        src="../assets/photos/home_4.jpg"
        alt="Home Image 3"
        class="index_img img_4"
      />

      <div class="index_heading">
        <h1>TechEd Rwanda</h1>
        <h2>Create Your Future in Tech and Coding</h2>
        <p>
          Deliver dynamic learning experiences to every student, everywhere.
          Take teaching and learning to the next level with TechEd, the #1
          educational software, and the foundation of the Instructure Learning
          Platform.
        </p>
        <RouterLink to="/signup" class="cta-button">Get Started</RouterLink>
      </div>
    </div>

    <div class="courses">
      <h1 class="courses_title">Most Popular Courses</h1>
      <div class="courses_trusted">
        <h2 class="course_title">Trusted By</h2>
        <div class="courses_trusted_imgs">
          <img src="../assets/photos/alu.png" alt="ALU Logo" />
          <img src="../assets/photos/reb.png" alt="REB Logo" />
          <img
            src="../assets/photos/imbuto.jpeg"
            alt="Imbuto Foundation Logo"
          />
          <img src="../assets/photos/mastercard.jpeg" alt="Mastercard Logo" />
        </div>
      </div>
      <div class="courses_wrapper_course">
        <div class="course_wrapper">
          <course>
            <template #course_name>Basic Computer Literacy</template>
            <template #course_img>
              <img
                src="../assets/photos/Basic Computer Literacy.png"
                alt="Basic Computer Literacy"
              />
            </template>
          </course>
          <course>
            <template #course_name
              >Internet Safety and Digital Citizenship</template
            >
            <template #course_img>
              <img
                src="../assets/photos/Internet Safety and Digital Citizenship.png"
                alt="Internet Safety and Digital Citizenship"
              />
            </template>
          </course>
          <course>
            <template #course_name>Introduction to Coding</template>
            <template #course_img>
              <img
                src="../assets/photos/Introduction to Coding.png"
                alt="Introduction to Coding"
              />
            </template>
          </course>
          <course>
            <template #course_name>Microsoft Office Suite</template>
            <template #course_img>
              <img
                src="../assets/photos/Microsoft Office Suite_.png"
                alt="Microsoft Office Suite"
              />
            </template>
          </course>
        </div>
        <div class="course_wrapper">
          <course>
            <template #course_name>Multimedia Skills</template>
            <template #course_img>
              <img
                src="../assets/photos/Multimedia Skills.png"
                alt="Multimedia Skills"
              />
            </template>
          </course>
          <course>
            <template #course_name>Robotics and STEM Activities</template>
            <template #course_img>
              <img
                src="../assets/photos/Robotics and STEM Activities.png"
                alt="Robotics and STEM Activities"
              />
            </template>
          </course>
          <course>
            <template #course_name>Typing Skills</template>
            <template #course_img>
              <img
                src="../assets/photos/Typing Skills.png"
                alt="Typing Skills"
              />
            </template>
          </course>
          <course>
            <template #course_name>Collaborative Projects</template>
            <template #course_img>
              <img
                src="../assets/photos/Collaborative Projects.png"
                alt="Collaborative Projects"
              />
            </template>
          </course>
        </div>
      </div>
    </div>

    <div class="aboutus">
      <div class="aboutus_img">
        <img src="../assets/photos/about.jpg" alt="About Us" />
      </div>
      <div class="aboutus_wrapper">
        <div class="aboutus_heading">
          <h1>About Us</h1>
        </div>
        <p class="aboutus_mission">
          TechEd Rwanda is dedicated to transforming education through
          technology. Our mission is to provide high-quality, accessible, and
          dynamic learning experiences to students across Rwanda. We are
          committed to leveraging the power of technology to bridge educational
          gaps and prepare learners for the future.
        </p>
        <p class="aboutus_values">
          Our core values include innovation, inclusivity, and excellence. We
          strive to foster a learning environment where every student has the
          opportunity to thrive, and where educators are empowered with the
          tools and resources they need to succeed.
        </p>
      </div>
    </div>

    <contacts />
  </section>
</template>

<style scoped>
.home {
  background-color: #10123b;
  display: flex;
  flex-direction: column;
  gap: 144px;
  color: #fff;
}

.home_index {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-start;
  height: 100vh;
  padding: 0 72px;
  position: relative;
  overflow: hidden;
}

.index_img {
  position: absolute;
  border-radius: 50%;
  width: 600px;
  height: 600px;
  object-fit: cover;
  transition: all 0.5s ease-in-out;
  opacity: 0.8;
}

.img_1 {
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.img_2 {
  top: -300px;
  right: -200px;
}

.img_3 {
  bottom: -245px;
  left: -315px;
}

.img_4 {
  bottom: -245px;
  right: -315px;
}

.index_heading {
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  padding: 24px 48px;
  width: 568px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  z-index: 1;
  animation: fadeInUp 1s ease;
}

.index_heading h1 {
  font-size: 48px;
  margin: 0;
  color: #10123b;
}

.index_heading h2 {
  font-size: 24px;
  margin: 16px 0;
  color: #10123b;
}

.index_heading p {
  font-size: 16px;
  margin: 16px 0;
  color: #333;
}

.cta-button {
  background-color: #ff6f61;
  color: #fff;
  cursor: pointer;
  padding: 12px 24px;
  border-radius: 4px;
  text-transform: uppercase;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.cta-button:hover {
  background-color: #e65c50;
}

.courses {
  display: flex;
  flex-direction: column;
  gap: 72px;
  justify-content: center;
  align-items: center;
  padding: 0 72px;
}

.courses_title {
  text-transform: uppercase;
  font-size: 48px;
  color: #ffffff;
  margin-bottom: 24px;
  animation: fadeIn 1s ease;
}

.courses_trusted {
  display: flex;
  flex-direction: column;
  gap: 16px;
  justify-content: center;
  align-items: center;
}

.course_title {
  text-transform: uppercase;
  font-size: 24px;
  color: #ffffff;
}

.courses_trusted_imgs {
  display: flex;
  gap: 12px;
}

.courses_trusted_imgs img {
  width: 300px;
  height: 200px;
  object-fit: cover;
  transition: filter 0.3s ease;
}

.courses_trusted_imgs img:hover {
  filter: grayscale(0%);
}

.courses_wrapper_course {
  display: flex;
  flex-direction: column;
  gap: 24px;
  width: 100%;
}

.course_wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 24px;
}

.course {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  padding: 16px;
  transition: transform 0.3s ease;
}

.course:hover {
  transform: translateY(-10px);
}

.course p {
  font-size: 1.2rem;
  font-weight: bold;
  color: #10123b;
}

.course a {
  font-size: 1rem;
  background-color: #10123b;
  padding: 10px 20px;
  color: white;
  cursor: pointer;
  width: fit-content;
  border-radius: 24px;
  text-decoration: none;
  transition:
    background-color 0.3s ease,
    transform 0.3s ease;
}

.course a:hover {
  background-color: #ff6f61;
  transform: translateY(-2px);
}

.course img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.course img:hover {
  transform: scale(1.05);
}

.aboutus {
  display: flex;
  flex-direction: row;
  height: 100vh;
}

.aboutus_img {
  width: 50vw;
}

.aboutus_img img {
  border-top-right-radius: 300px;
  height: 100vh;
  width: 100%;
  object-fit: cover;
  filter: brightness(70%);
  transition: filter 0.3s ease;
}

.aboutus_img img:hover {
  filter: brightness(80%);
}

.aboutus_wrapper {
  width: 50vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 48px;
  padding: 0px 96px;
}

.aboutus_heading {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 12px;
  animation: fadeIn 1s ease;
}

.aboutus_heading h1 {
  font-size: 48px;
  color: white;
  text-transform: uppercase;
}

.aboutus_mission,
.aboutus_values {
  width: 385px;
  color: white;
  text-transform: capitalize;
  font-size: 16px;
  line-height: 1.6;
  animation: fadeIn 1s ease;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Media Queries */
@media (max-width: 480px) {
  .home_index {
    padding: 0 12px;
  }

  .index_heading {
    padding: 12px 16px;
  }

  .index_img {
    width: 200px;
    height: 200px;
  }

  .courses {
    padding: 0 12px;
  }

  .courses_title {
    font-size: 24px;
  }

  .courses_wrapper_course .course_wrapper {
    flex-direction: column;
    gap: 12px;
  }

  .aboutus_img img {
    height: 30vh;
  }
}

@media (min-width: 481px) and (max-width: 768px) {
  .home_index {
    padding: 0 24px;
  }

  .index_heading {
    padding: 16px 24px;
  }

  .index_img {
    width: 300px;
    height: 300px;
  }

  .courses {
    padding: 0 24px;
  }

  .courses_title {
    font-size: 32px;
  }

  .courses_wrapper_course {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .course_wrapper {
    width: calc(50% - 12px);
    flex-direction: column;
    gap: 16px;
  }

  .aboutus_img img {
    height: 40vh;
  }
}

@media (min-width: 769px) and (max-width: 1200px) {
  .home_index {
    padding: 0 48px;
  }

  .index_heading {
    width: 100%;
  }

  .courses {
    padding: 0 48px;
  }

  .courses_wrapper_course {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .course_wrapper {
    width: calc(50% - 24px);
  }

  .aboutus {
    flex-direction: column;
  }

  .aboutus_img,
  .aboutus_wrapper {
    width: 100%;
  }

  .aboutus_img img {
    height: 50vh;
    border-top-right-radius: 0;
  }

  .aboutus_wrapper {
    padding: 24px;
  }
}
</style>
