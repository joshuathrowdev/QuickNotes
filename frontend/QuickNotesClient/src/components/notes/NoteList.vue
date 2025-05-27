<template>
  <div class="Note-List-Root-Container">
    <h1 class="text-4xl font-bold italic tracking-wide text-mainPurple mb-4">Available Notes</h1>
    <div class="Note-List-Static-Container">
      <div v-for="note in notes" :key="note.id">
      <Note :note="note" />
    </div>
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