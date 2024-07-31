<script setup>
import navigation from '@/components/navigationdash.vue';
import contacts from "@/components/contacts.vue";
import { RouterLink } from "vue-router";
</script>

<template>
  <section class="admin">
    <navigation />
    <div class="admin_content">
      <img src="../assets/photos/student&teacher.jpg" alt="Student and Teacher" class="student_img" />
      <div class="avatar">
        <img src="../assets/photos/M3N.jpg" alt="Avatar" />
        <p>Hello, Administrator</p>
      </div>
      <div class="admin_wrapper">
        <!-- Reach -->
        <div class="admin_wrapper_reach">
          <h1>Registered Users</h1>
          <div class="admin_wrapper_reach_wrapper">
            <div class="reach_numbers">
              <p class="title">Current Teachers</p>
              <p class="number">12</p>
            </div>
            <div class="reach_numbers">
              <p class="title">Current Students</p>
              <p class="number">129</p>
            </div>
          </div>
        </div>
        <!-- Teachers Curriculum -->
        <div class="admin_wrapper_re">
          <h1>Online Resourses</h1>
          <div class="admin_wrapper_reach_wrapper">
            <div class="reach_numbers">
              <p>Typing Skills</p>
              <img src="../assets/photos/Polygon 1.svg" alt="Video Icon" />
                          <p><a href="https://youtu.be/8Ic2L7ZyFC8" class="cta-button"><button>Open Video </button></a></p>
              
            </div>
            <div class="reach_numbers">
              <p>Computer Literacy</p>
              <img src="../assets/photos/Polygon 1.svg" alt="Video Icon" />
<p><a href="https://www.youtube.com/watch?v=5h9NHPh9mrw&list=PLG4CGP1xLFmkg-8ghWUFuik3eGm_-aCAu" class="cta-button"><button>Open Video </button></a></p>
              
            </div>
            <div class="reach_numbers">
              <p>Digital Literacy</p>
              <img src="../assets/photos/Polygon 1.svg" alt="Video Icon" />
              <p><a href="https://youtu.be/_LElWqXi7Ag" class="cta-button" target="_self"><button>Open Video </button></a></p>
            </div>
            <div class="reach_numbers">
              <p>Robotics</p>
              <img src="../assets/photos/Polygon 1.svg" alt="Video Icon" />
              <p><a href="https://www.youtube.com/watch?v=NRj6gzah7JA&list=PL4g1oAdmuCfqmYvURLzVFkMMUI7839biN" class="cta-button"><button>Open Video </button></a></p>
            </div>
          </div>
        </div>
        <!-- Current Students -->
        <div class="admin_students">
          <h1>Current Managing Students</h1>
          <studentavatar>
            <template #student_name>MUKIZA EMA</template>
            <template #student_grade>97%</template>
            <template #student_course>Microsoft Office Suite</template>
          </studentavatar>
          <studentavatar>
            <template #student_name>MUKIZA EMA</template>
            <template #student_grade>97%</template>
            <template #student_course>Microsoft Office Suite</template>
          </studentavatar>
          <studentavatar>
            <template #student_name>MUKIZA EMA</template>
            <template #student_grade>97%</template>
            <template #student_course>Microsoft Office Suite</template>
          </studentavatar>
          <studentavatar>
            <template #student_name>MUKIZA EMA</template>
            <template #student_grade>97%</template>
            <template #student_course>Microsoft Office Suite</template>
          </studentavatar>
        </div>
      </div>
    </div>
    <contacts />
  </section>
</template>

<style scoped>
.admin {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  background-color: #10123b;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  padding: 72px 1rem 0;
  gap: 2rem;
}

.student_img {
  position: absolute;
  border-radius: 50%;
  height: 40vw;
  width: 40vw;
  max-width: 620px;
  max-height: 620px;
  object-fit: cover;
  bottom: -15%;
  right: -5%;
  z-index: 1;
}

.avatar {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  width: 100%;
  position: relative;
  z-index: 2;
}

.avatar img {
  width: 3.5rem;
  height: 3.5rem;
  border-radius: 50%;
}

.avatar p {
  font-size: 1.25rem;
  color: white;
  text-transform: uppercase;
}

.admin_content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  z-index: 2;
}

.admin_wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  width: 100%;
  max-width: 1200px;
}

.admin_wrapper_reach,
.admin_wrapper_re {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.admin_wrapper_reach h1,
.admin_wrapper_re h1 {
  font-size: 1.5rem;
  text-transform: uppercase;
  color: white;
  border-bottom: 1px solid white;
  padding-bottom: 0.5rem;
}

.admin_wrapper_reach_wrapper,
.admin_wrapper_reach_wrapper {
  display: flex;
  flex-direction: row;
  gap: 1.5rem;
}

.reach_numbers {
  background-color: white;
  padding: 1rem;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  width: 230px;
  height: 200px;
}

.reach_numbers .title {
  font-size: 1rem;
  text-transform: uppercase;
}

.reach_numbers .number {
  font-size: 2.5rem;
  text-transform: uppercase;
}

.admin_students {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding-top: 1rem;
  border-top: 1px solid white;
}

.admin_students h1 {
  font-size: 1.5rem;
  color: white;
  text-transform: uppercase;
}

/* Media Queries for Responsiveness */
@media (max-width: 1200px) {
  .student_img {
    height: 30vw;
    width: 30vw;
  }
}

@media (max-width: 992px) {
  .student_img {
    height: 35vw;
    width: 35vw;
  }

  .admin_wrapper {
    padding: 0 1rem;
  }
}

@media (max-width: 768px) {
  .student_img {
    height: 40vw;
    width: 40vw;
  }

  .admin_wrapper {
    padding: 0 0.5rem;
  }

  .admin_wrapper_reach_wrapper,
  .admin_wrapper_reach_wrapper {
    flex-direction: column;
    gap: 1rem;
  }

  .reach_numbers {
    width: 100%;
    height: auto;
  }
}

@media (max-width: 576px) {
  .student_img {
    height: 50vw;
    width: 50vw;
  }

  .avatar p {
    font-size: 1rem;
  }

  .admin_wrapper {
    padding: 0.5rem;
  }
}
</style>
