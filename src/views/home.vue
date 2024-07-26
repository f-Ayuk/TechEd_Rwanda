<script setup>
import navigation from "@/components/navigation.vue";
import course from "@/components/course.vue";
import contacts from "@/components/contacts.vue";
</script>

<template>
  <navigation />
  <section class="home">
    <div class="home_index">
      <img
        src="../assets/photos/student&teacher.jpg"
        alt=""
        class="index_img img_1"
      />
      <img src="../assets/photos/home_1.jpg" alt="" class="index_img img_2" />
      <img src="../assets/photos/home_3.jpg" alt="" class="index_img img_3" />
      <img src="../assets/photos/home_4.jpg" alt="" class="index_img img_4" />

      <div class="index_heading">
        <h1>techEd Rwanda</h1>
        <h1>create your future in tech and coding</h1>
        <p>
          Deliver dynamic learning experiences to every student, everywhere.
          Take teaching and learning to the next level with teched, the #1
          educational software, and the foundation of the Instructure Learning
          Platform.
        </p>
        <RouterLink to="/signup">get started</RouterLink>
      </div>
    </div>

    <!--  -->
    <div class="courses">
      <h1 class="courses_title">most popular courses</h1>
      <div class="courses_trusted">
        <h1 class="course_title">trusted by</h1>
        <div class="courses_trusted_imgs">
          <img src="../assets/photos/alu.png" alt="" />
          <img src="../assets/photos/reb.png" alt="" />
          <img src="../assets/photos/imbuto.jpeg" alt="" />
          <img src="../assets/photos/mastercard.jpeg" alt="" />
        </div>
      </div>
      <div class="courses_wrapper_course">
        <div class="course_wrapper">
          <course>
            <template #course_name> Basic Computer Literacy </template>
            <template #course_img>
              <img src="../assets/photos/Basic Computer Literacy.png" alt="" />
            </template>
          </course>
          <course>
            <template #course_name>
              Internet Safety and Digital Citizenship</template
            >
            <template #course_img>
              <img src="../assets/photos/Basic Computer Literacy.png" alt="" />
            </template>
          </course>
          <course>
            <template #course_name> Introduction to Coding </template>
            <template #course_img>
              <img src="../assets/photos/Basic Computer Literacy.png" alt="" />
            </template>
          </course>
          <course>
            <template #course_name> Microsoft Office Suite: </template>
            <template #course_img>
              <img src="../assets/photos/Basic Computer Literacy.png" alt="" />
            </template>
          </course>
        </div>
        <div class="course_wrapper">
          <course>
            <template #course_name> Multimedia Skills </template>
            <template #course_img>
              <img src="../assets/photos/Multimedia Skills.png" alt="" />
            </template>
          </course>
          <course>
            <template #course_name> Robotics and STEM Activities</template>
            <template #course_img>
              <img
                src="../assets/photos/Robotics and STEM Activities.png"
                alt=""
              />
            </template>
          </course>
          <course>
            <template #course_name> Typing Skills </template>
            <template #course_img>
              <img src="../assets/photos/Typing Skills.png" alt="" />
            </template>
          </course>
          <course>
            <template #course_name> Educational Games and Simulations</template>
            <template #course_img>
              <img
                src="../assets/photos/Educational Games and Simulations.png"
                alt=""
              />
            </template>
          </course>
        </div>
        <div class="course_wrapper_1">
          <course>
            <template #course_name> Collaborative Projects</template>
            <template #course_img>
              <img src="../assets/photos/Collaborative Projects.png" alt="" />
            </template>
          </course>
          <course>
            <template #course_name> Introduction to Data Handling</template>
            <template #course_img>
              <img
                src="../assets/photos/Introduction to Data Handling.png"
                alt=""
              />
            </template>
          </course>
        </div>
      </div>
    </div>
    <!--  -->

    <!--  -->
    <div class="aboutus">
      <div class="aboutus_img">
        <img src="../assets/photos/about.jpg" alt="" />
      </div>
      <div class="aboutus_wrapper">
        <div class="aboutus_heading">
          <h1>about us</h1>
          <p>#our mission #our values</p>
        </div>
        <p class="aboutus_mission">
          s simply dummy text of the printing and typesetting industry. Lorem
          Ipsum has been the industry's standard dummy text ever since the
          1500s, when an unknown printer took a galley of type and scrambled it
          to make a type specimen book. It has survived not only five centuries,
          but also the leap into electronic typesetting, remaining essentially
          unchanged. It was popularised in the 1960s with the release of
          Letraset
        </p>
        <p class="aboutus_values">
          s simply dummy text of the printing and typesetting industry. Lorem
          Ipsum has been the industry's standard dummy text ever since the
          1500s, when an unknown printer took a galley of type and scrambled it
          to make a type specimen book. It has survived no
        </p>
      </div>
    </div>
    <!--  -->
    <contacts />
    <!--  -->
  </section>
</template>

<style>
.home {
  background-color: #10123b;
  /* height: 100vh; */
  display: flex;
  flex-direction: column;
  gap: 144px;

  /*  */
  .home_index {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-start;
    height: 100vh;
    padding: 0 72px;
    position: relative;
    overflow: hidden;

    .index_img {
      position: absolute;
      border-radius: 50%;
      width: 600px;
      height: 600px;
      object-fit: cover;
    }
    .img_1 {
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      /* z-index: -1000; */
      opacity: 0.9;
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
      background-color: white;
      height: 420px;
      width: 568px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 24px 48px;
      z-index: 10000;
    }
    /*  */
  }
  .courses {
    display: flex;
    flex-direction: column;
    gap: 72px;
    justify-content: center;
    align-items: center;
    padding: 0 72px;

    .courses_title {
      text-transform: uppercase;
      font-size: 48px;
      color: white;
    }
    /*  */
    .courses_trusted {
      display: flex;
      flex-direction: column;
      gap: 16px;
      justify-content: center;
      align-items: center;

      h1 {
        text-transform: uppercase;
        font-size: 20px;
        color: white;
      }

      .courses_trusted_imgs {
        display: flex;
        font-size: row;
        gap: 12px;

        img {
          width: 48px;
          height: 24px;
          object-fit: cover;
        }
      }
    }
    /*  */

    /*  */

    .courses_wrapper_course {
      display: flex;
      flex-direction: column;
      gap: 24px;
      width: 100%;

      .course_wrapper {
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;

        img {
          flex-grow: 1;
          height: 70%;
          /* width: 100%; */
          object-fit: cover;
        }
      }
    }

    .course_wrapper_1 {
      display: flex;
      flex-direction: row;
      gap: 24px;

      img {
        flex-grow: 1;
        height: 70%;
        /* width: 100%; */
        object-fit: cover;
      }
    }
  }

  /*  */
  .aboutus {
    display: flex;
    flex-direction: row;
    /* justify-content: s; */
    height: 100vh;
    .aboutus_img {
      width: 50vw;
      img {
        border-top-right-radius: 300px;
        height: 100vh;
        width: 100%;
        object-fit: cover;
      }
    }
    .aboutus_wrapper {
      width: 50vw;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 72px;
      padding: 0px 96px;

      .aboutus_heading {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 12px;

        h1 {
          font-size: 48px;
          color: white;
          text-transform: uppercase;
        }

        p {
          font-size: 12px;
          text-transform: uppercase;
          color: rgb(255, 255, 255, 0.5);
        }
      }

      .aboutus_mission {
        width: 385px;
        color: white;
        text-transform: capitalize;
      }
      .aboutus_values {
        width: 385px;
        color: white;
        text-transform: capitalize;
        margin: 0 48px;
      }
    }
  }
}
</style>
