<script setup>
// Component Imports
import NoteList from '../components/notes/NoteList.vue';
import AddNoteForm from '../components/forms/AddNoteForm.vue';

// Vue Imports
import { ref } from 'vue';

// Vue Attributes
const emit = defineEmits(['resetForm'])


// Data Attributes
const notes = ref([
  {
    id: 1,
    title: 'Go Get a Haircut',
    body: 'Go to the barbershop and get a haircut around 10 am',
    created_at: Date.now()  
  },
  {
    id: 2,
    title: 'Finish This Learning Project',
    body: 'Finish this notes app using the knowledge we learned by tonight',
    created_at: Date.now()
  }
])


// Methods
const handleFormSubmission = (formData) => {
  // Adding Meta Data to Form Data
  formData.id = notes.value[notes.value.length - 1].id + 1
  formData.created_at = Date.now()

  notes.value.push(formData)

}

</script>


<script>
export default {
  name: 'ListNotesView'
}
</script>


<template>
  <div class="List-Notes-View-Root-Container">
    <div v-if="notes.length">
      <!-- Notes List Child Component -->
       <NoteList :notes="notes" />
    </div>

    <div v-else>
      <!-- Error Message -->
       <p>There was an error in obtaining the notes... Please Try Again Later</p>
    </div>



    <!-- Add Note Form -->
    <div>
      <AddNoteForm @submission="handleFormSubmission"/>
    </div>
  </div>
</template>


<style>

</style>

<!-- List Notes Page -->
 
<!-- Logical Responsibilites -->
  <!-- 1) Add overall page layout -->
  <!-- 2) Access api throughout endpoints and follow CRUD properties -->