<template>
    <b-row>
        <b-col>
            <div class="mb-4">
                <b-button :to="{name: 'trouble-create'}" variant="primary" size="md">
                    Добавить
                </b-button>
            </div>
            <b-table hover outlined head-variant="light"
                :items="troubles"
                :fields="fields"
                :filter="filter"
                >
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(image)="data">
                    <table-thumbnail v-if="data.item.image"
                                     :id="data.item.id"
                                     :src="data.item.image"
                    />
                </template>
                <template v-slot:cell(image)="data">
                    <table-thumbnail v-if="data.item.image"
                        :id="data.item.id"
                        :src="data.item.image"
                    />
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'trouble-update', params: {id: data.item.id}}"></b-button>
                        <!--<btn-turn :turn="true"/>-->
                        <b-button class="btn_delete" @click="deleteTrouble(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>
    </b-row>
</template>

<script>
import TroubleMixin from '@/mixins/info/TroubleMixin';

export default {
    name: "TroubleList",
    mixins: [TroubleMixin],
    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: 'id', label: 'ID'},
                { key: 'name', label: 'Название'},
                { key: 'image', label: 'Иконка'},
                { key: 'actions', label: ''},

            ],
            activePage: 1,
            filter: {
                level: null
            },
        }
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Проблемы', to: {name: 'troubles'}},
        ];
        this.getTroubles()
    },
    methods: {
        goFilter(e) {
            e.preventDefault();
            this.troublesSearch = this.filter
            this.getTroubles()
        },
        clearFilter() {
            this.filter = {}
            this.troublesSearch = {}
            this.getTroubles()
        },
    }
}
</script>

<style scoped>

</style>
