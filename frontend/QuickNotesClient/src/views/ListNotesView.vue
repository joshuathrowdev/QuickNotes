<template>
  <div class="ListNotesViewContainer">
    <div v-if="notes.length">
      <NoteList :notes="notes"/>
    </div>
    <div v-else>
      <h1>No Notes were returned (Eventually will be the error message)</h1>
    </div>
  </div>
</template>

<script>
// Child Component Imports
import NoteList from '../components/notes/NoteList.vue';

export default {
  name: 'ListNotesView',
  components: {NoteList},

  setup() {
    let notes = [
      {
        id: 1,
        title: 'Finish The Composite Note Project',
        body: "Finish by today",
        created: Date.now()
      },
      {
        id: 2,
        title: 'Go To the Gym',
        body: "D interaval workout and eat less today",
        created: Date.now()
      }
    ]
  
    

    return {notes}
  }

}
</script>

<style>

</style>