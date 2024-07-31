<script setup>
import { ref, onMounted } from "vue";
import navigation from "@/components/navigation.vue";
import course from "@/components/course.vue";
import resourse from "@/components/resourse.vue";
const userName = ref("John Doe");

// Fetch user data from Django backend
const fetchUserData = async () => {
  try {
    const response = await fetch("http://localhost:8000/api/current-user/", {
      credentials: "include", // include cookies if needed
    });
    if (response.ok) {
      const data = await response.json();
      userName.value = data.name; // assuming the response contains a 'name' field
    } else {
      console.error("Failed to fetch user data:", response.statusText);
    }
  } catch (error) {
    console.error("Error fetching user data:", error);
  }
};

// Fetch the data when component mounts
onMounted(fetchUserData);
</script>
<template>
  <section class="student">
    <img
      src="../assets/photos/student&teacher.jpg"
      alt=""
      class="student_img"
    />
    <navigation />
    <div class="avatar_wrapper">
      <div class="avatar">
        <img src="../assets/photos/student.png" alt="" />
        <p>{{ userName }}</p>
      </div>
      <p>overall grades: 89%</p>
    </div>
    <div class="dashboard_wrapper">
      <div class="current_courses">
        <h1>current enrolled courses</h1>
        <div class="current_courses_wrapper">
          <course class="current_courses_wrapper_course">
            <template #course_name> Basic Computer Literacy </template>
            <template #course_img>
              <img src="../assets/photos/Basic Computer Literacy.png" alt="" />
            </template>
          </course>
          <course class="current_courses_wrapper_course">
            <template #course_name>
              Internet Safety and Digital Citizenship</template
            >
            <template #course_img>
              <img src="../assets/photos/Basic Computer Literacy.png" alt="" />
            </template>
          </course>
        </div>
      </div>
      <div class="current_re_wrapper">
        <h1>resources</h1>
        <div class="current_re">
          <resourse>
            <template #re_name> Basic Computer Literacy </template>
            <template #re_info_time> 2 weeks </template>
            <template #re_info_title>n/a</template>
          </resourse>
          <resourse>
            <template #re_name> Basic Computer Literacy </template>
            <template #re_info_time> 2 weeks </template>
            <template #re_info_title>n/a</template>
          </resourse>
          <resourse>
            <template #re_name> Basic Computer Literacy </template>
            <template #re_info_time> 2 weeks </template>
            <template #re_info_title>n/a</template>
          </resourse>
          <resourse>
            <template #re_name> Basic Computer Literacy </template>
            <template #re_info_time> 2 weeks </template>
            <template #re_info_title>n/a</template>
          </resourse>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.student {
  background-color: #10123b;
  height: 100vh;
  padding: 72px 48px 0px 48px;
  display: flex;
  flex-direction: column;
  /* gap: 24px; */
  /* justify-content: space-between; */
  position: relative;
  overflow: hidden;

  .student_img {
    position: absolute;
    border-radius: 50%;
    height: 620px;
    width: 620px;
    object-fit: cover;
    bottom: -40%;
    right: -10%;
    z-index: 1000000;
  }
  .avatar_wrapper {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;

    .avatar {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      gap: 32px;

      img {
        width: 54px;
        height: 54px;
        border-radius: 50%;
      }

      h4 {
        font-size: 20px;
        color: white;
        text-transform: uppercase;
      }
    }

    p {
      font-size: 20px;
      color: white;
      text-transform: uppercase;
    }
  }

  /*  */
  .dashboard_wrapper {
    display: flex;
    flex-direction: column;
    gap: 12px;
    height: 100%;

    .current_courses {
      display: flex;
      flex-direction: column;
      gap: 12px;

      h1 {
        font-size: 16px;
        color: white;
        padding: 14px 0;
        width: 100%;
        border-bottom: 1px solid white;
        text-transform: uppercase;
      }

      .current_courses_wrapper {
        display: flex;
        flex-direction: row;
        gap: 24px;

        .current_courses_wrapper_course {
          width: 230px;
          height: 230px;

          img {
            height: 140px;
            object-fit: cover;
          }
        }
      }
    }

    .current_re_wrapper {
      display: flex;
      flex-direction: column;
      gap: 12px;

      h1 {
        font-size: 16px;
        color: white;
        padding: 14px 0;
        width: 100%;
        border-bottom: 1px solid white;
        text-transform: uppercase;
      }
    }

    .current_re {
      display: flex;
      flex-direction: row;
      gap: 24px;
    }
  }
  /*  */
}
</style>
