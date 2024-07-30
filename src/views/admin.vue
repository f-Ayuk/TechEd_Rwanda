<script setup>
import navigation from "@/components/navigation.vue";
import studentavatar from "@/components/studentavatar.vue";
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
            <p class="title">current teachers</p>
            <p class="number">x12</p>
          </div>
          <div class="reach_numbers">
            <p class="title">current students</p>
            <p class="number">x129</p>
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

      <!-- students -->
      <div class="admin_students">
        <h1>current managing students</h1>
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

  /*  */
  .admin_wrapper {
    display: flex;
    flex-direction: column;
    gap: 12px;

    .admin_wrapper_reach {
      display: flex;
      flex-direction: column;
      gap: 12px;

      h1 {
        font-size: 14px;
        text-transform: uppercase;
        color: white;
        padding-bottom: 4px;
        border-bottom: 1px solid white;
      }

      .admin_wrapper_reach_wrapper {
        display: flex;
        flex-direction: row;
        gap: 12px;

        .reach_numbers {
          width: 230px;
          height: 210px;
          background-color: white;
          padding: 12px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;

          .title {
            font-size: 14px;
            text-transform: uppercase;
          }

          .number {
            font-size: 56px;
            text-transform: uppercase;
          }
        }
      }
    }

    /*  */
    .admin_wrapper_re {
      display: flex;
      flex-direction: column;
      gap: 12px;

      h1 {
        font-size: 14px;
        text-transform: uppercase;
        color: white;
        padding-bottom: 4px;
        border-bottom: 1px solid white;
      }

      .admin_wrapper_reach_wrapper {
        display: flex;
        flex-direction: row;
        gap: 12px;

        .reach_numbers {
          width: 230px;
          height: 210px;
          background-color: white;
          padding: 12px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;

          p {
            font-size: 14px;
            color: black;
            text-transform: uppercase;
          }
        }
      }
    }
    /*  */
  }

  /*  */
  .admin_students {
    display: flex;
    flex-direction: column;
    gap: 4px;
    padding-top: 4px;
    border-top: 1px solid white;
    h1 {
      text-transform: uppercase;
      font-size: 14px;
      color: white;
    }
  }
  /*  */
}
</style>
