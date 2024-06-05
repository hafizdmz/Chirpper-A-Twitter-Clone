<template>
  <main class="grid grid-cols-3 gap-4">
    <div class="flex flex-col items-center ml-48 mt-5">
      <div class="my-4">
        <p class="text-4xl">Welcome,</p>
        <p class="text-4xl">@User</p>
        <Button @handle-click="toggleModal">
          <font-awesome-icon icon="fa-solid fa-feather" />
          Start Chirpping!
        </Button>
      </div>
    </div>
    <div
      class="flex flex-col items-center mt-10 border-l border-r border-gray-200"
    >
      <div class="flex flex-row gap-x-3">
        <!-- define better data for every items -->
        <Card
          v-for="item in data"
          :key="item.id"
          :tweet="item.content"
          :user="item.user"
        />
      </div>
      <div class="my-4">
        <Button>
          <i class="fa-solid fa-spinner"></i>
          Load More Chirpper!
        </Button>
      </div>
      <div>
        <ModalUpload @toggle-modal="toggleModal" :show-modal="showModal">
          <Form>
            <div class="flex flex-col items-center">
              <TextArea id="textarea-input" label="" v-model="tweet" row="5" />
              <label for="uploadFile" class="mt-5">
                <InputFile
                  button-text="Upload Image"
                  id="uploadBtn"
                  v-model="uploadedFile"
                />
              </label>
            </div>
            <div class="flex flex-row space-x-2 mt-10">
              <Button
                type="submit"
                class="p-2 mt-3 rounded-md"
                @click="handleUploadFile"
              >
                Submit
              </Button>
              <Button
                type="button"
                class="p-2 mt-3 rounded-md"
                @click="toggleModal"
              >
                Close
              </Button>
            </div>
          </Form>
        </ModalUpload>
      </div>
    </div>
    <div class="mt-9">
      <p class="text-4xl mb-3">Latest Notification:</p>
      <li class="text-lg">@user12 just chirpping 2min ago</li>
      <li class="text-lg">@user4 commented on your post 5min ago</li>
      <li class="text-lg">@user28 just chirpping 12min ago</li>
      <li class="text-lg">@user7 liked your post 15min ago</li>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Card from "../components/Card.vue";
import Button from "../components/Button.vue";
import ModalUpload from "../components/ModalUpload.vue";
import InputFile from "../components/InputFile.vue";
import TextArea from "../components/TextAreaLabel.vue";
import Form from "../components/Form.vue";
// import { useFetch } from '../composable/useAxios';

const data = [
  {
    user: "user 1",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque venenatis ex gravida luctus mattis. Curabitur feugiat erat ex, sit amet gravida ligula pretium sit amet. In molestie tortor ut quam venenatis, id mattis purus eleifend.",
    id: 1,
  },
];

const uploadedFile = ref(null);
let tweet = ref("");

const handleUploadFile = () => {
  console.log(tweet);
  console.log(uploadedFile.value);
};

// const {tryFetching} = useFetch()

// const access_token = localStorage.getItem("accessToken")
// const data = ref([])

// const handleFetching = async() =>{
//   const result = await tryFetching(import.meta.env.VITE_API_BASEURL + "/api/tweets", access_token)
//   // console.log(result.data)
//   data.value = result
// }

//like dislike toggle button
// const toggleLike = (data) => {
//   if (!data.liked) {
//     data.like++;
//   } else {
//     data.like--;
//   }
//   data.liked = !data.liked;

//   if (data.disliked) {
//     data.dislike--;
//     data.disliked = false;
//   }
// };

// const toggleDislike = (data) => {
//   if (!data.disliked) {
//     data.dislike++;
//   } else {
//     data.dislike--;
//   }
//   data.disliked = !data.disliked;

//   if (data.liked) {
//     data.like--;
//     data.liked = false;
//   }
// };

// onMounted(() =>{
//   handleFetching()
// })

const showModal = ref(false);
const toggleModal = () => {
  showModal.value = !showModal.value;
};
</script>
