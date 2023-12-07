<template>
  <v-app id="inspire">
    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-app-bar-title>User Access Management</v-app-bar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" temporary>
      <v-list>
        <v-list-item v-for="(item, index) in navigationItems" :key="index" link @click="navigateTo(item.route)">
          <v-list-item-title>{{ item.label }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="bg-grey-lighten-2">
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const drawer = ref(null);
const router = useRouter();

const navigationItems = [
  { label: 'Home', route: '/'},
  { label: 'Users', route: '/users' },
  { label: 'Applications', route: '/applications' },
];

const navigateTo = (route) => {
  router.push(route);
  drawer.value = false; // Optionally close the drawer on navigation
};

</script>
