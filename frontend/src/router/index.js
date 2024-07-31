import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/home.vue"),
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/signup.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/login.vue"),
    },
    {
      path: "/student",
      name: "student",
      component: () => import("../views/student.vue"),
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("../views/admin.vue"),
    },
  ],
});

export default router;
