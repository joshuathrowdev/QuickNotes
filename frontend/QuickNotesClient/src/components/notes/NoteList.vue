<template>
  <div class="NoteListContainer">
    <h1>Available Notes</h1>
    <div v-for="note in notes" :key="note.id">
      <Note :note="note" />
    </div>
  </div>
  
</template>

<script>
import Note from './Note.vue';

export default {
  name: 'NoteList',
  components: {Note},
  props: ['notes'], // accepting passed props from parent view component

  setup(props) {
    let notes = props.notes

    return {notes}
  }

}
</script>

<style>

</style>