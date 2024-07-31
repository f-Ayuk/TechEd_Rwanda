<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <div class="course">
    <p>
      <slot name="course_name"></slot>
    </p>
    <slot name="course_img"></slot>
    <RouterLink to="/signup" class="nav_login"><a href="">Enroll now</a></RouterLink>
  </div>
</template>

<style scoped>
.course {
  width: 332px;
  height: 320px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 12px;
  background-color: #f8f9fb;
  padding: 12px;

  a {
    font-size: 16px;
    background-color: black;
    padding: 6px 12px;
    color: white;
    cursor: pointer;
    width: fit-content;
    border-radius: 24px;
  }
}
</style>
