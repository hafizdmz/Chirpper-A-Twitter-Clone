<template>
  <div class="w-80 text-black">
    <div class="bg-chirpper-brown h-8 px-3 py-2 text-xs rounded-t-lg">
      {{ user }}
    </div>
    <div class="bg-stone-500 h-56"></div>
    <div class="bg-white p-4 h-52">
      <p>{{ tweet }}</p>
    </div>
    <div class="bg-chirpper-brown h-8 px-3 py-2 text-xs rounded-b-lg">
      <div class="flex justify-between">
        <p class="text-chirpper-brown-lite">Apr 16, 07.59pm</p>
        <div class="flex justify-end gap-5">
          <font-awesome-icon icon="fa-solid fa-thumbs-up" size="xl" />
          <font-awesome-icon icon="fa-solid fa-thumbs-down" size="xl" />
          <font-awesome-icon icon="fa-regular fa-comment" size="xl"/>
          <i class="fa-solid fa-thumbs-down"></i>
        </div>
      </div>
      <!-- <div class="flex gap-3">
                <button :isLiked="isLiked" class="mr-3" @click="buttonLiked">
                    <i v-if="!isLiked" class="fa-solid fa-thumbs-up mr-1"></i>
                    <i v-else class="fa-solid fa-thumbs-up mr-1" style="color: #1DA1F2;"></i>
                </button>
                <button :isDisliked="isDisliked" class="mr-3" @click="buttonDisliked">
                    <i v-if="!isDisliked" class="fa-solid fa-thumbs-down mr-1"></i>
                    <i v-else class="fa-solid fa-thumbs-down mr-1" style="color: #ca4444;"></i>
                </button>
            </div> -->
    </div>
  </div>
</template>
<script setup>
defineProps(["user", "tweet", "imgPath", "imgName", "isLiked", "isDisliked"]);
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faEnvelope } from "@fortawesome/free-solid-svg-icons";

import { ref } from "vue";

const isLiked = ref(false);
const buttonLiked = () => {
  isLiked.value = !isLiked.value;
  if (isDisliked.value) {
    isDisliked.value = false;
  }
};
const isDisliked = ref(false);
const buttonDisliked = () => {
  isDisliked.value = !isDisliked.value;
  if (isLiked.value) {
    isLiked.value = false;
  }
};
</script>
