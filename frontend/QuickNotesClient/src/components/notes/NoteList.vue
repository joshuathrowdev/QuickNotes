<script setup>
// Component Import
import Note from './Note.vue';

// Vue Imports
import { defineProps } from 'vue';

// Vue Attributes
const props = defineProps(['notes']) // Props Attribute

// Data Attributes
const notes = props.notes
</script>


<template>
  <div class="Note-List-Root-Container">
    <h2 class="Display-Heading-2">Available Notes</h2>
    <div class="Note-List-Static-Container">
      <div v-for="note in notes" :key="note.id">
        <Note :note="note" />
      </div>
    </div>
  </div>
  
</template>


<style>

</style>