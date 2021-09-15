<script>
export default {
    name: "SexMixin",
    data () {
        return {
            sexes: [],
            sex: {
                id: null,
                name: null,
            },
            filter: null,
        }
    },
    methods: {
        getSexes() {
            return new Promise((resolve, reject) => {
                const self = this;
                this.$axios
                    .get(process.env.VUE_APP_HOST + '/api/workout/get-sex-list/')
                    .then(function (response) {
                        console.log(response);
                        self.sexes = response.data.results
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
