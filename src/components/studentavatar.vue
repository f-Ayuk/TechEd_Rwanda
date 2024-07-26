<script setup></script>

<template>
  <div class="student_avatar">
    <div class="student_profile">
      <img src="../assets/photos/student.png" alt="" />
      <p>
        <slot name="student_name"></slot>
      </p>
    </div>
    <p>
      <slot name="student_grade"></slot>
    </p>

    <p>
      <slot name="student_course"></slot>
    </p>
  </div>
</template>

<style scoped>
.student_avatar {
  display: flex;
  flex-direction: row;
  gap: 72px;

  .student_profile {
    display: flex;
    flex-direction: row;
    gap: 16px;

    img {
      border-radius: 50%;
      height: 16px;
      width: 16px;
      object-fit: cover;
    }

    p {
      color: white;
      font-size: 13px;
      text-transform: uppercase;
      width: 106px;
    }
  }
  p {
    color: white;
    font-size: 13px;
    text-transform: uppercase;
    width: 240px;
  }
}
</style>
