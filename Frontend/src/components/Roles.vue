<template>
  <v-row>
    <v-col cols="4">
      <!-- List of Applications -->
      <v-list dense>
        <v-list-item
          v-for="app in applications"
          :key="app.id"
          @click="selectApplication(app.id)"
          :class="{ 'selected': app.id === selectedApplicationId }"
        >
          <v-list-item-title>{{ app.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-col>
    
    <v-col cols="8">
      <!-- List of Roles for Selected Application -->
      <v-list dense>
        <v-list-item v-for="role in rolesForSelectedApplication" :key="role.id">
          <v-list-item-title>{{ role.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-col>
  </v-row>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useAppStore } from '@/store/app';

const applications = computed(() => {
  // Get the applications from the store
  return useAppStore().applications;
});

const selectedApplicationId = ref(null);

const roles = ref([
  // An array of role objects with applicationId property
  // indicating which application they belong to.
]);

const rolesForSelectedApplication = computed(() => {
  // Filter roles based on the selectedApplicationId
  return roles.value.filter(role => role.applicationId === selectedApplicationId.value);
});

const selectApplication = (applicationId) => {
  // Update the selected application
  selectedApplicationId.value = applicationId;
};
</script>
