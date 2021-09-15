<script>
export default {
    name: "DayMixin",
    data () {
        return {
            days: [],
            day: {
                id: null,
                name: null,
            },
            filter: null,
        }
    },
    methods: {
        getDays() {
            return new Promise((resolve, reject) => {
                const self = this;
                this.$axios
                    .get(process.env.VUE_APP_HOST + '/api/workout/get-day-list/')
                    .then(function (response) {
                        console.log(response);
                        self.days = response.data.results
                        resolve(response)
                    })
                    .catch(function (response) {
                        console.log(response);
                        reject(response)
                    })
            })
            .catch(response => {
                console.log(response)
            })
        },
    }
}
</script>

<style scoped>

</style>
