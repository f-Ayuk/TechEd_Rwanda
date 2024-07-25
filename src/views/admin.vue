<script setup>
import navigation from "@/components/navigation.vue";
</script>

<template>
  <section class="admin">
    <navigation />
    <img
      src="../assets/photos/student&teacher.jpg"
      alt=""
      class="student_img"
    />
    <div class="avatar">
      <img src="../assets/photos/student.png" alt="" />
      <p>john doe</p>
    </div>

    <!--  -->
    <div class="admin_wrapper">
      <!--  -->
      <div class="admin_wrapper_reach">
        <h1>our numbers</h1>
        <div class="admin_wrapper_reach_wrapper">
          <div class="reach_numbers">
            <p>current teachers</p>
            <p>x12</p>
          </div>
          <div class="reach_numbers">
            <p>current students</p>
            <p>x129</p>
          </div>
        </div>
      </div>
      <!--  -->

      <!-- teach re -->
      <div class="admin_wrapper_re">
        <h1>teachers curriculum</h1>
        <div class="admin_wrapper_reach_wrapper">
          <div class="reach_numbers">
            <p>typing skills syllabus</p>
            <img src="../assets/photos/Polygon 1.svg" alt="" />
            <p>open video</p>
          </div>
          <div class="reach_numbers">
            <p>typing skills syllabus</p>
            <img src="../assets/photos/Polygon 1.svg" alt="" />
            <p>open video</p>
          </div>
          <div class="reach_numbers">
            <p>typing skills syllabus</p>
            <img src="../assets/photos/Polygon 1.svg" alt="" />
            <p>open video</p>
          </div>
          <div class="reach_numbers">
            <p>Robotics</p>
            <img src="../assets/photos/Polygon 1.svg" alt="" />
            <p>open video</p>
          </div>
        </div>
      </div>
      <!--  -->
    </div>
    <!--  -->
  </section>
</template>

<style scoped>
.admin {
  display: flex;
  flex-direction: column;
  background-color: #10123b;
  height: 100vh;
  position: relative;
  overflow: hidden;
  padding: 72px 48px 0px 48px;
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

  .avatar {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 32px;
    width: 100%;

    img {
      width: 54px;
      height: 54px;
      border-radius: 50%;
    }

    p {
      font-size: 20px;
      color: white;
      text-transform: uppercase;
    }
  }
}
</style>
