<script setup></script>

<template>
  <div class="resource_wrapper">
    <div class="re_header">
      <div class="re_header_h1"><h1>career path</h1></div>
      <h3>
        <slot name="re_name"></slot>
      </h3>
    </div>

    <div class="re_info">
      <div class="re_info_wp">
        <p>time</p>
        <p>
          <slot name="re_info_time"> </slot>
        </p>
      </div>
      <div class="re_info_wp">
        <p>language</p>
        <p>
          <slot name="re_info_title"></slot>
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.resource_wrapper {
  width: 230px;
  height: 230px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 12px;
  background-color: transparent;
  border-radius: 8px;
  border: 1px solid white;

  .re_header {
    display: flex;
    flex-direction: column;
    gap: 12px;

    .re_header_h1 {
      background-color: rgb(255, 255, 255);
      padding: 1.6px;
      h1 {
        font-size: 13px;
        text-transform: uppercase;
      }
    }

    h3 {
      font-size: 12px;
      text-transform: uppercase;
      color: white;
    }
  }

  .re_info {
    display: flex;
    flex-direction: column;
    gap: 8px;

    .re_info_wp {
      display: flex;
      flex-direction: row;
      width: 100%;
      justify-content: space-between;
      padding-bottom: 6px;
      border-bottom: 1px dotted white;

      p {
        text-transform: uppercase;
        font-size: 13px;
        color: white;
      }
    }
  }
}
</style>
