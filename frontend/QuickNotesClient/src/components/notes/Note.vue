<script setup>
// Component Import

// Vue Imports
import { defineProps } from 'vue';

// Vue Attributes
const props = defineProps(['note']) 

// Data Attributes
const note = props.note


</script>


<template>
  <div class="Note-Root-Container">
    <h2>{{ note.title }} | {{ note.id }}</h2>
    <p>{{ note.body }}</p>
  </div>
</template>


<styl