<script>
export default {
    name: "TroubleMixin",
    troublesSearch: [],
    data () {
        return {
            troubles: [],
            trouble: {
                id: null,
                name: null,
                image: null
            },
            image: null,
            filter: null,
        }
    },
    methods: {
        getTroubles() {
            return new Promise((resolve, reject) => {
                const self = this;
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/workout/get-trouble-list/', {
                                params: this.troublesSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response);
                                self.troubles = response.data.results
                                
                                resolve(response)
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                                reject(response)
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            })
        },
        getTrouble(id) {
            const self = this;
            return new Promise((resolve, reject) => {
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/workout/get-trouble/' + id + '/', {
                                params: this.troublesSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response);
                                self.trouble = response.data;
                                self.image = response.data.image;
                                self.trouble.image = null;
                                resolve(response)
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                                reject(response)
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            })
        },
        deleteTrouble(id) {
            if (this.deleteRequest('/api/workout/delete-trouble/' , id))
                this.troubles = this.troubles.filter(element => element.id !== id);
        },
        saveTrouble(obj, id = null) {
            const self = this;
            if (typeof(obj.image) == 'string')
                delete obj.image;

            if (obj.image === [])
                obj.image = null;

            let formData = new FormData();
            Object.keys(obj).map(function(key) {
                if (obj[key])
                    formData.append(key, obj[key]);
            });

            if (id){
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .put(
                                process.env.VUE_APP_HOST + '/api/workout/update-trouble/' + id + '/',
                                formData,
                                {
                                    headers: {
                                        'Content-Type': 'multipart/form-data',
                                        Authorization: token
                                    },
        
                                }
                            )
                            .then(function (response) {
                                self.templateShowSuccess(response);
                                self.getTrouble(id)
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            }else{
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .post(
                                process.env.VUE_APP_HOST + '/api/workout/create-trouble/',
                                formData,
                                {
                                    headers: {
                                        'Content-Type': 'multipart/form-data',
                                        Authorization: token
                                    },
        
                                }
                            )
                            .then(function (response) {
                                console.log(response);
                                self.goBack()
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            }
        },
    }
}
</script>

<style scoped>

</style>
