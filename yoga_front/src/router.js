import Vue from 'vue'
import Router from 'vue-router'

import TheContainer from './containers/TheContainer.vue';
import Login from './components/Login.vue';
import ChangePassword from "./views/ChangePassword";
import Home from "./views/Home";

import StudentList from "./views/user/student/StudentList";
import StudentForm from "./views/user/student/StudentForm";

import WorkoutList from "@/views/info/workout/WorkoutList";
import WorkoutForm from "@/views/info/workout/WorkoutForm";

import TroubleList from "@/views/info/trouble/TroubleList";
import TroubleForm from "@/views/info/trouble/TroubleForm";

Vue.use(Router);

export default new Router({
	mode: 'history',
	// mode: 'hash',
	linkActiveClass: 'active',
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/login',
			name: 'login',
			component: Login,
			meta: {
				requiresAuth: false
			},
		},
		{
			path: '/',
			name: 'main',
			component: TheContainer,
			redirect: 'home',
			meta: {
				requiresAuth: true
			},
			children: [
				{
					path: 'home',
					name: 'home',
					component: Home,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'change-password',
					name: 'change-password',
					component: ChangePassword,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'user/student',
					name: 'students',
					component: StudentList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'user/student/update/:id',
					name: 'student-update',
					component: StudentForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'user/student/create',
					name: 'student-create',
					component: StudentForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'workout',
					name: 'workouts',
					component: WorkoutList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'workout/update/:id',
					name: 'workout-update',
					component: WorkoutForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'workout/create',
					name: 'workout-create',
					component: WorkoutForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'trouble',
					name: 'troubles',
					component: TroubleList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'trouble/update/:id',
					name: 'trouble-update',
					component: TroubleForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'trouble/create',
					name: 'trouble-create',
					component: TroubleForm,
					meta: {
						requiresAuth: true
					}
				},
			]
		},
	],
})
