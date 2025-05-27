<template>
  <div class="Note-Root-Container">
    <h2>{{ note.title }} | {{ note.id }}</h2>
    <p>{{ note.body }}</p>
  </div>
  

</template>

<script>
export default {
  name: 'Note',
  props: ['note'],

  setup(props) {
    let note = props.note

    return {note}
  }
}
</script>




<style>

</style>