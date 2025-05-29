<script setup>
// Component Imports
import SubmitButton from '../common/SubmitButton.vue';

// Vue Imports
import { reactive } from 'vue';

// Vue Attributes
const emit = defineEmits(['submission'])

// Data Attributes
const formInput = reactive({
  title: '',
  body: '',
})

// Methods
const handleFormSubmission = () => {
  console.log("Form Data: ")
  console.log("Title: " + formInput.title)
  console.log("Body: " + formInput.body)

  // Emitting Submission Event and Passing
  // Form Data along ot parent component
  emit('submission', {...formInput})
  // becuase the reactive is passed be reference, we need to pass a copy of
  // the data to parent so that when we reset, the parent does not see changes

  // Reseting Fomr Input Fields
  resetFormFields()
}

const resetFormFields = () => {
  formInput.title = ''
  formInput.body = ''
}

</script>



<template>
  <div class="Add-Note-From-Root-Container">
    <h2 class="Display-Heading-2">Add A Note</h2>
    
    <div class="Add-Note-Form-Static-Container">
      <form @submit.prevent="">
        <label>Title</label>
        <input type="text"  v-model="formInput.title">

        <label>Content</label>
        <input type="text" required v-model="formInput.body">

        <SubmitButton @formSubmitted="handleFormSubmission" />
      </form>
    </div>

    <!-- Debuggin And Displaying Form Data -->
    <div> 
      <p>Title: {{ formInput.title }}</p>
      <p>Body: {{ formInput.body }}</p>
      <p>Created_At {{ Date.now() }}</p>
    </div>

  </div>
</template>


<style>

</style>