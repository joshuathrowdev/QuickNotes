<script setup>
// Vue Imports

// Vue Attributes
const emit = defineEmits(['formSubmitted'])

// methods
const handleClick = () => {
  emit('formSubmitted')
}
</script>

<script>
export default {
  name: 'SubmitButton',
}
</script>



<template>
  <button type="submit" class="Form-Submit-Button" @click="handleClick">Submit</button>
</template>



<style>

</style>