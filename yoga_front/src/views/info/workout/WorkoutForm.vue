<template>
    <b-form @submit="goSave($event)">
        <b-tabs content-class="mt-3">
            <b-tab title="Основное" active>
            <div class="form__item">
                <span class="form__label">Название</span>
                <div class="form__control">
                    <div class="row">
                        <div class="col-12">
                            <b-form-input class="short"
                                          type="text"
                                          required
                                          placeholder="ru"
                                          v-model="workout.name"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div class="form__item">
                <span class="form__label">Описание</span>
                <div class="form__control">
                    <div class="row">
                        <div class="col-12">
                            <b-form-textarea class="short"
                                        required
                                        placeholder="ru"
                                        v-model="workout.description"
                            />
                        </div>
                        
                    </div>
                </div>
            </div>
            <div class="form__item">
                <span class="form__label">Польза</span>
                <div class="form__control">
                    <div class="row">
                        <div class="col-12">
                            <b-form-textarea class="short"
                                        required
                                        placeholder="ru"
                                        v-model="workout.value"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div class="form__item">
                <span class="form__label">Длительность</span>
                <div class="form__control">
                    <div class="row">
                        <div class="col-12">
                            <b-form-input class="short"
                                          type="text"
                                          required
                                          placeholder="ru"
                                          v-model="workout.duration"
                            />
                        </div>
                    </div>
                </div>
            </div>
           <div class="form__item">
                <span class="form__label">Изображение</span>
                <div class="form__control">
                    <template v-if="image">
                        <div class="img__thumbnail">
                            <div class="img__thumbnail-img">
                                <b-img :id="`field-${workout.id}`"
                                       :src="image" width="80"
                                       v-b-modal="'modal__thumbnail' + workout.id"
                                />
                            </div>
                            <b-modal :id="'modal__thumbnail' + workout.id" scrollable hide-footer centered class="modal-dialog-auto">
                                <b-img :src="image" fluid/>
                            </b-modal>
                            <b-button type="button" class="media-delete" variant="link" @click="deleteImg">Удалить</b-button>
                        </div>
                    </template>
                    <template v-else>
                        <b-form-file
                            :id="`field-${workout.image}`"
                            v-model="workout.image"
                            plain
                        />
                    </template>
                </div>
            </div>
            <div class="form__item">
                <span class="form__label">Видео</span>
                <div class="form__control">
                    <template v-if="video">
                        <!-- <div class="img__thumbnail"> -->
                            <!-- <div class="img__thumbnail-img"> -->
                                <video
                                        :id="`field-video-${workout.id}`"
                                        controls
                                       :src="workout.video" width="400"
                                ></video>
                            <!-- </div> -->
                            <!-- <b-modal :id="'modal__thumbnail' + workout.id" scrollable hide-footer centered class="modal-dialog-auto">
                                <b-video :src="video" fluid/>
                            </b-modal> -->
                            <b-button type="button" class="media-delete" variant="link" @click="deleteVideo">Удалить</b-button>
                        <!-- </div> -->
                    </template>
                    <template v-else>
                        <b-form-file
                            :id="`field-${workout.video}`"
                            v-model="workout.video"
                            plain
                        />
                    </template>
                </div>
            </div>


            </b-tab>
            <b-tab title="Проблемы">
                <div class="form__item" v-for="trouble in troubles" v-bind:key="trouble.id">
                    <!-- <span class="form__label" v-if="trouble_id !== trouble.id" :set="trouble_id = trouble.id">{{trouble.name}}</span> -->
                    <div class="img__thumbnail">
                            <div class="img__thumbnail-img">
                                <b-img :id="`field-${trouble.id}`"
                                       :src="trouble.image" width="80"
                                       v-b-modal="'modal__thumbnail' + trouble.id"
                                />
                            </div>
                            <b-modal :id="'modal__thumbnail' + trouble.id" scrollable hide-footer centered class="modal-dialog-auto">
                                <b-img :src="trouble.image" fluid/>
                            </b-modal>
                        </div>
                    <div class="form__control">

                        <b-form-checkbox
                            v-model="troublesList"
                            name="checkbox-1"

                            :value="trouble.id"
                            :unchecked-value="null"
                        >
                            {{ trouble.name }}
                        </b-form-checkbox>
                    </div>
                </div>
            </b-tab>
            <b-tab title="Дни">
                <div class="form__item" v-for="day in days" v-bind:key="day.id">
                    <!-- <span class="form__label" v-if="trouble_id !== trouble.id" :set="trouble_id = trouble.id">{{trouble.name}}</span> -->
                    <div class="form__control">

                        <b-form-checkbox
                            v-model="dayList"
                            name="checkbox-1"

                            :value="day.id"
                            :unchecked-value="null"
                        >
                            {{ day.name }}
                        </b-form-checkbox>
                    </div>
                </div>
            </b-tab>
            <b-tab title="Уровни">
                <div class="form__item" v-for="level in levels" v-bind:key="level.id">
                    <!-- <span class="form__label" v-if="trouble_id !== trouble.id" :set="trouble_id = trouble.id">{{trouble.name}}</span> -->
                    <div class="form__control">

                        <b-form-checkbox
                            v-model="levelList"
                            name="checkbox-1"

                            :value="level.id"
                            :unchecked-value="null"
                        >
                            {{ level.name }}
                        </b-form-checkbox>
                    </div>
                </div>
            </b-tab>
            <b-tab title="Пол">
                <div class="form__item" v-for="sex in sexes" v-bind:key="sex.id">
                    <!-- <span class="form__label" v-if="trouble_id !== trouble.id" :set="trouble_id = trouble.id">{{trouble.name}}</span> -->
                    <div class="form__control">

                        <b-form-checkbox
                            v-model="sexList"
                            name="checkbox-1"

                            :value="sex.id"
                            :unchecked-value="null"
                        >
                            {{ sex.name }}
                        </b-form-checkbox>
                    </div>
                </div>
            </b-tab>

        </b-tabs>

        <div class="form__item form__item_submit">
            <div class="form__control">
                <b-button type="submit" variant="primary">Сохранить</b-button>
            </div>
        </div>
    </b-form>
</template>

<script>
import WorkoutMixin from '@/mixins/info/WorkoutMixin';
import TroubleMixin from '@/mixins/info/TroubleMixin';
import DayMixin from '@/mixins/info/DayMixin';
import LevelMixin from '@/mixins/info/LevelMixin';
import SexMixin from '@/mixins/info/SexMixin';


export default {
    name: 'WorkoutForm',
    mixins: [
        WorkoutMixin, 
        TroubleMixin,
        DayMixin,
        LevelMixin,
        SexMixin
    ],
    components: {
        
    },
    data () {
        return {
            id: null,
            alert: false,
            troublesList: [],
            levelList: [],
            dayList: [],
            sexList: [],
        }
    },
   
    created() {
        this.id = this.$route.params.id;
        if (this.id){
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Тренировка', to: {name: 'workouts'}},
                {text: 'Редактировать', to: {name: 'workout-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Тренировка', to: {name: 'workouts'}},
                {text: 'Создать', to: {name: 'workout-create'}}
            ];
        }
        this.getSexes();
        this.getDays();
        this.getLevels();
        this.getTroubles();

        if (this.$route.params.id)
            this.getWorkout(this.$route.params.id).then((response) => {
                response.data.troubles.forEach((trouble) => {
                    this.troublesList.push(trouble.id)
                })
                response.data.level.forEach((level) => {
                    this.levelList.push(level.id)
                })
                response.data.periodicity.forEach((periodicity) => {
                    this.dayList.push(periodicity.id)
                })
                response.data.sex.forEach((sex) => {
                    this.sexList.push(sex.id)
                })
                
                console.log(this.troublesList)
        });

    },
    methods: {
        goSave($event){
            $event.preventDefault();
            let data = Object.assign({}, this.workout);
            data.troubles = this.troublesList;
            if (data.troubles.length === 0)
                data.troubles = []
            else
                data.troubles = JSON.stringify(this.troublesList)

            data.level = this.levelList;
            if (data.level.length === 0)
                data.level = []
            else
                data.level = JSON.stringify(this.levelList)

            data.periodicity = this.dayList;
            if (data.periodicity.length === 0)
                data.periodicity = []
            else
                data.periodicity = JSON.stringify(this.dayList)

            data.sex = this.sexList;
            if (data.sex.length === 0)
                data.sex = []
            else
                data.sex = JSON.stringify(this.sexList)

            console.log(data);
            this.saveWorkout(data, this.$route.params.id);
            this.alert = true;
        },
        processFile(event) {
            console.log('Event: ', event);
            this.workout.image = event[0]
            this.workout.video = event[1]
        },
        deleteImg() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.image = null;
                this.workout.image = [];
            }
        },
        deleteVideo() {
            let confirmDelete = confirm('Удалить видео?');
            if (confirmDelete) {
                this.video = null;
                this.workout.video = [];
            }
        }
    },
}
</script>

<style scoped>

</style>
