import { createRouter, createWebHistory } from "vue-router";

// View Imports
import ListNoteView from '../views/ListNotesView.vue'
import NoteDetailsView from '../views/NoteDetailsView.vue'

import InvalidPageView from "../views/InvalidPageView.vue";

const routes = [
  {
    path: '/notes',
    name: 'NotesURL',
    component: ListNoteView
  },
  {
    path: '/notes/:id',
    name: 'NoteDetails',
    component: NoteDetailsView,
    props: true
  },

  // Catch All Path
  {
    path: '/:pathMatch(.*)',
    name: 'InvalidURL',
    component: InvalidPageView
  }
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router