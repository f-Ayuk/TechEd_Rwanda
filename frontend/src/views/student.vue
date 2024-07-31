<script setup>
import navigation from '@/components/navigationdash.vue';
import course from '@/components/course.vue';
import resourse from '@/components/resourse.vue';
import contacts from "@/components/contacts.vue";
</script>

<template>
  <section class="student">
    <navigation class="nav" />
    <div class="content">
      <img src="../assets/photos/student&teacher.jpg" alt="Background Image" class="student_img" />
      <div class="avatar_wrapper">
        <div class="avatar">
          <img src="../assets/photos/student.png" alt="Avatar" />
          <p>Vanessa Mdee</p>
        </div>
        <p class="grades">Overall Grades: 89%</p>
      </div>
      <div class="dashboard_wrapper">
        <div class="current_courses">
          <h1>Current Enrolled Courses</h1>
          <div class="current_courses_wrapper">
            <course class="course">
              <template #course_name>Basic Computer Literacy</template>
              <template #course_img>
                <img src="../assets/photos/Basic Computer Literacy.png" alt="Basic Computer Literacy" />
              </template>
            </course>
            <course>
            <template #course_name>Introduction to Coding</template>
            <template #course_img>
              <img src="../assets/photos/Introduction to Coding.png" alt="Introduction to Coding" />
            </template>
          </course>
          </div>
        </div>
        <div class="resources">
          <h1>Resources</h1>
          <div class="resources_wrapper">
            <resourse class="resource">
              <template #re_name>Basic Computer Literacy</template>
              <template #re_info_time>2 weeks</template>
              <template #re_info_title>English, French, Swahili, Kinyarwanda</template>
            </resourse>
            <resourse class="resource">
              <template #re_name>Introduction to Programming</template>
              <template #re_info_time>3 weeks</template>
              <template #re_info_title>English, French, Swahili, Kinyarwanda</template>
            </resourse>
            <resourse class="resource">
              <template #re_name>Advanced Mathematics</template>
              <template #re_info_time>4 weeks</template>
              <template #re_info_title>English, French, Swahili, Kinyarwanda</template>
            </resourse>
            <resourse class="resource">
              <template #re_name>Digital Literacy</template>
              <template #re_info_time>2 weeks</template>
              <template #re_info_title>English, French, Swahili, Kinyarwanda</template>
            </resourse>
          </div>
        </div>
      </div>
    </div>
  </section>
  <contacts class="footer" />
</template>

<style scoped>
.student {
  background-color: #10123b;
  min-height: 100vh;
  padding: 80px 2rem;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
}

.nav {
  position: absolute;
  top: 0;
  width: 100%;
  z-index: 10;
}

.student_img {
  position: absolute;
  border-radius: 50%;
  height: 50vh;
  width: 50vh;
  object-fit: cover;
  bottom: -10%;
  right: 0;
  z-index: 1;
  opacity: 0.1;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2;
  width: 100%;
  max-width: 1200px;
}

.avatar_wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;

  .avatar {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1rem;

    img {
      width: 80px;
      height: 80px;
      border-radius: 50%;
    }

    p {
      font-size: 1.2rem;
      font-weight: bold;
    }
  }

  .grades {
    font-size: 1.1rem;
    font-weight: bold;
  }
}

.dashboard_wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.current_courses, .resources {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;

  h1 {
    font-size: 1.5rem;
    border-bottom: 2px solid white;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
    text-transform: uppercase;
  }
}

.current_courses_wrapper, .resources_wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}

.course, .resource {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 1rem;
  width: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.course img, .resource img {
  width: 100%;
  height: auto;
  border-radius: 4px;
}

@media (max-width: 1024px) {
  .student_img {
    height: 40vh;
    width: 40vh;
  }

  .avatar_wrapper {
    flex-direction: column;
    gap: 0.5rem;
  }

  .avatar img {
    width: 60px;
    height: 60px;
  }

  .dashboard_wrapper {
    gap: 1rem;
  }

  .current_courses_wrapper, .resources_wrapper {
    gap: 1rem;
  }

  .course, .resource {
    width: 180px;
  }
}

@media (max-width: 768px) {
  .student_img {
    height: 30vh;
    width: 30vh;
  }

  .avatar_wrapper {
    gap: 0.5rem;
  }

  .avatar img {
    width: 50px;
    height: 50px;
  }

  .current_courses_wrapper, .resources_wrapper {
    gap: 0.5rem;
  }

  .course, .resource {
    width: 160px;
  }
}

@media (max-width: 480px) {
  .student_img {
    height: 20vh;
    width: 20vh;
  }

  .avatar_wrapper {
    gap: 0.5rem;
  }

  .avatar img {
    width: 40px;
    height: 40px;
  }

  .current_courses_wrapper, .resources_wrapper {
    gap: 0.5rem;
  }

  .course, .resource {
    width: 140px;
  }
}
</style>
