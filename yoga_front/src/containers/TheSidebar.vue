<template>
    <div class="sidebar">
        <ul class="sidebar__list">
            <div class="sidebar__item">
                <span class="sidebar__icon">
                    <img src="@/assets/img/icons/main.png" alt="">
                </span>
                <b-link class="sidebar__link" :to="{name: 'home'}">Главная</b-link>
            </div>
            <div class="sidebar__item">
                <span class="sidebar__icon">
                    <img src="@/assets/img/icons/gear.png" alt="">
                </span>
                <b-link class="sidebar__link" :to="{name: 'workouts'}">Тренировки</b-link>
            </div>
            <div class="sidebar__item">
                <span class="sidebar__icon">
                    <img src="@/assets/img/icons/gear.png" alt="">
                </span>
                <b-link class="sidebar__link" :to="{name: 'troubles'}">Проблемы</b-link>
            </div>
            <div class="sidebar__item">
                <span class="sidebar__icon">
                    <img src="@/assets/img/icons/tested.png" alt="">
                </span>
                <b-link class="sidebar__link" :to="{name: 'students'}">Пользователи</b-link>
            </div>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'TheSidebar',
}
</script>

<style lang="scss">
.sidebar {

}

.sidebar__list {
    list-style: none;
    margin: 0;
    padding: 0;
    // padding: 40px 10px 40px 25px;
}

.sidebar__item {
    // display: flex;
    position: relative;
    padding-left: 24px;
    margin-bottom: 20px;
    
    .b-icon {
        position: absolute;
        top: 4px;
        left: 0;
    }
}



.sidebar__link {
    color: #007bff;
    border-bottom: 1px solid#cee6ff;
    &:hover {
        text-decoration: none;
        border-bottom: 1px solid rgba(243, 55, 57, 0.23);
        color: #f33435;
    }
    &.active {
        color: #000000;
        border: none;
    }
}

.sidebar__icon {
    position: absolute;
    top: 3px;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 16px;
    height: 16px;
    object-fit: contain;
}
</style>