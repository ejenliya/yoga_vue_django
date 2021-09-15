<template>
    <b-row>
        <b-col>
            <div class="mb-4">
                <b-button class='mr-4' :to="{name: 'workout-create'}" variant="primary" size="md">
                    Добавить
                </b-button>
                <b-button v-b-toggle.sidebar-filter variant="info">Фильтр</b-button>
            </div>
            <b-table hover outlined head-variant="light"
                :items="workouts"
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
                        <b-button class="btn_edit" :to="{name: 'workout-update', params: {id: data.item.id}}"></b-button>
                        <!--<btn-turn :turn="true"/>-->
                        <b-button class="btn_delete" @click="deleteWorkout(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>
        <b-sidebar
            id="sidebar-filter"
            :backdrop-variant="'dark'"
            backdrop
            title="Фильтр"
        >
            <b-form @submit="goFilter($event)">
                <div class="px-3 py-2">
                    <label>Тренировка:</label>

                    <b-form-select
                        v-model="filter"
                        :options="workoutLevels"
                        value-field="name"
                        text-field="name"
                    />
                </div>
                <div class="px-3 py-2">
                    <b-button type="submit" @click="goFilter" variant="success">Фильтровать</b-button>
                    &nbsp;
                    <b-button type="submit" @click="clearFilter" variant="warning">Очистить</b-button>
                    <br>
                    <br>
                </div>

            </b-form>
        </b-sidebar>
    </b-row>
</template>

<script>
import WorkoutMixin from '@/mixins/info/WorkoutMixin';

export default {
    name: "WorkoutList",
    mixins: [WorkoutMixin],
    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: 'id', label: 'ID'},
                { key: 'name', label: 'Название'},
                { key: 'image', label: 'Иконка'},
                { key: 'level', label: 'Сложность'},
                { key: 'duration', label: 'Длительность'},
                { key: 'actions', label: ''},
            ],
            activePage: 1,
            filter: {
                level: null
            },
            workoutLevels:[
                'Простой',
                'Средний',
                'Продвинутый'
            ]
        }
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Тренировки', to: {name: 'workouts'}},
        ];
        this.getWorkouts()
    },
    methods: {
        goFilter(e) {
            e.preventDefault();
            this.workoutSearch = this.filter
            this.getWorkouts()
        },
        clearFilter() {
            this.filter = {}
            this.workoutSearch = {}
            this.getWorkouts()
        },
    }
}
</script>

<style scoped>

</style>
