<script>
export default {
    name: "SexMixin",
    data () {
        return {
            levels: [],
            level: {
                id: null,
                name: null,
            },
            filter: null,
        }
    },
    methods: {
        getLevels() {
            return new Promise((resolve, reject) => {
                const self = this;
                this.$axios
                    .get(process.env.VUE_APP_HOST + '/api/workout/get-level-list/')
                    .then(function (response) {
                        console.log(response);
                        self.levels = response.data.results
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
