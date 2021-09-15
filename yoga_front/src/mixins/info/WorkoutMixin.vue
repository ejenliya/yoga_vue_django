<script>
export default {
	name: "WorkoutMixin",
	workoutSearch: [],
	data() {
		return {
			workouts: [],
			image: null,
			workout: {
				id: null,
				image: null,
				video: null,
				name: null,
				level: null,
				periodicity: null,
				duration: null,
				description: null,
				value: null,
				sex: null,
				troubles: null,
			},
			filter: null,
		};
	},
	methods: {
		getWorkouts() {
			return new Promise((resolve, reject) => {
				const self = this;
				this.$store
					.dispatch("token")
					.then((token) => {
						this.$axios
							.get(
								process.env.VUE_APP_HOST +
									"/api/workout/get-workout-list/",
								{
									params: this.workoutSearch,
									headers: {
										Authorization: token,
									},
								}
							)
							.then(function(response) {
								console.log(response);
								self.workouts = response.data.results;
								resolve(response);
							})
							.catch(function(response) {
								console.log(response);
								self.templateShowError(response);
								reject(response);
							});
					})
					.catch((response) => {
						console.log(response);
					});
			});
		},
		getWorkout(id) {
			const self = this;
			return new Promise((resolve, reject) => {
				this.$store
					.dispatch("token")
					.then((token) => {
						this.$axios
							.get(
								process.env.VUE_APP_HOST +
									"/api/workout/get-workout/" +
									id +
									"/",
								{
									params: this.workoutSearch,
									headers: {
										Authorization: token,
									},
								}
							)
							.then(function(response) {
								console.log(response);
								self.workout = response.data;
								self.image = response.data.image;
								self.video = response.data.video;
								console.log(
									"Workout: " + self.workout.troubles
								);
								resolve(response);
							})
							.catch(function(response) {
								console.log(response);
								self.templateShowError(response);
								reject(response);
							});
					})
					.catch((response) => {
						console.log(response);
					});
			});
		},
		deleteWorkout(id) {
			if (this.deleteRequest("/api/workout/delete-workout/", id))
				this.workouts = this.workouts.filter(
					(element) => element.id !== id
				);
		},
		saveWorkout(obj, id = null) {
			const self = this;
			console.log("Obj " + obj.image + obj.video);
			if (typeof obj.image == "string") delete obj.image;

			if (typeof obj.video == "string") delete obj.video;

			if (obj.image === []) obj.image = null;

			if (obj.video === []) obj.video = null;

			let formData = new FormData();
			Object.keys(obj).map(function(key) {
				if (obj[key]) {
                    obj[key] = JSON.parse(obj[key])
                    console.log(obj[key])
					if (Array.isArray(obj[key])) {
						for (let el of obj[key]) formData.append(key, el);
					} else {
						formData.append(key, obj[key]);
					}
				}
			});
			console.warn(formData.values);
			if (id) {
				this.$axios
					.put(
						process.env.VUE_APP_HOST +
							"/api/workout/update-workout/" +
							id +
							"/",
						formData,
						{
							headers: {
								"Content-Type": "multipart/form-data",
							},
						}
					)
					.then(function(response) {
						self.templateShowSuccess(response);
						self.getWorkout(id);
					})
					.catch(function(response) {
						console.log(response);
						self.templateShowError(response);
					});
			} else {
				this.$axios
					.post(
						process.env.VUE_APP_HOST +
							"/api/workout/create-workout/",
						formData,
						{
							headers: {
								"Content-Type": "multipart/form-data",
							},
						}
					)
					.then(function(response) {
						console.log(response);
						self.goBack();
					})
					.catch(function(response) {
						console.log(response);
						self.templateShowError(response);
					});
			}
		},
	},
};
</script>

<style scoped></style>
