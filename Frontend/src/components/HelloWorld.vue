<template>
  <v-container>
    <!-- Overview Cards Row -->
    <v-row>
      <!-- Loop through each card in the cards array -->
      <v-col cols="12" md="6" lg="4" v-for="(card, index) in cards" :key="index">
        <v-card class="pa-4" elevation="2">
          <v-card-title class="d-flex justify-space-between align-center">
            <span>{{ card.title }}</span>
            <v-icon size="32">{{ card.icon }}</v-icon>
          </v-card-title>
          <v-card-text class="display-1 text-center">{{ card.text }}</v-card-text>
          <v-card-actions class="justify-center">
            <v-btn text :color="card.btnColor" @click="card.action">{{ card.btnText }}</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAppStore } from '@/store/app';

const router = useRouter();
const store = useAppStore();

const userCount = computed(() => store.users.length);
const roleCount = computed(() => store.roles.length);
const applicationCount = computed(() => store.applications.length);

const cards = ref([
  { 
    title: 'Users', 
    text: userCount, 
    icon: 'mdi-account-group', 
    btnText: 'View Details', 
    btnColor: 'primary', 
    action: () => { router.push('/users'); }
  },
  { 
    title: 'Roles', 
    text: roleCount, 
    icon: 'mdi-account-key', 
    btnText: 'Manage Roles', 
    btnColor: 'success', 
    action: () => { router.push('/roles'); }
  },
  { 
    title: 'Applications', 
    text: applicationCount, 
    icon: 'mdi-application', 
    btnText: 'View Apps', 
    btnColor: 'info', 
    action: () => { router.push('/applications'); }
  },
  // Add more cards as needed
]);
</script>


<style>
/* Custom Styles */
</style>
