<!-- 
<script setup>
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonButton from "@/components/ArgonButton.vue";


</script> -->

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonButton from "@/components/ArgonButton.vue";

const formData = ref({
  name: '',
  university_name: '',
  description: '',
  modules_sem1: Array(6).fill(''),
  modules_sem2: Array(6).fill(''),
  modules_sem3: Array(6).fill(''),
  modules_sem4: Array(6).fill('')
});

const submitForm = async () => {
  try {
    console.log(formData.value)
    const response = await axios.post('http://localhost:5000/predict', formData.value);
    console.log('Response:', response.data);
    
  } catch (error) {
    console.error('Error submitting form:', error);
  }
};
</script>
<template>
  <div class="w-full">
    <div class="col-md-8 mx-auto">
      <div class="card">
        <div class="card-header pb-0">
          <div class="d-flex align-items-center">
            <p class="mb-0">Insert Degree</p>
            <argon-button color="success" size="sm" class="ms-auto" @click="submitForm">Submit</argon-button>
          </div>
        </div>
        <div class="card-body">
          <p class="text-uppercase text-sm">Master Information</p>
          <div class="row">
            <div class="col-md-6">
              <label for="name" class="form-control-label">Name</label>
              <argon-input type="text" v-model="formData.name" />
            </div>
            <div class="col-md-6">
              <label for="university_name" class="form-control-label">University Name</label>
              <argon-input type="text" v-model="formData.university_name" />
            </div>
          </div>
          <div class="row">
            <div class="col-md-10">
              <label for="description" class="form-control-label">Description</label>
              <argon-input type="text" v-model="formData.description" />
            </div>
          </div>
          <hr class="horizontal dark" />
          <p class="text-uppercase text-sm">Semester 1 modules</p>
          <div class="row">
            <div class="col-md-6" v-for="(module, index) in formData.modules_sem1" :key="index">
              <label :for="'module_11' + index+1" class="form-control-label">Module 11{{ index+1 }}</label>
              <argon-input type="text" v-model="formData.modules_sem1[index]" />
            </div>
          </div>

          <hr class="horizontal dark" />
          <p class="text-uppercase text-sm">Semester 2 modules</p>
          <div class="row">
            <div class="col-md-6" v-for="(module, index) in formData.modules_sem2" :key="index">
              <label :for="'module_12' + index+1" class="form-control-label">Module 12{{ index+1 }}</label>
              <argon-input type="text" v-model="formData.modules_sem2[index]" />
            </div>
          </div>
          
          <hr class="horizontal dark" />
          <p class="text-uppercase text-sm">Semester 3 modules</p>
          <div class="row">
            <div class="col-md-6" v-for="(module, index) in formData.modules_sem3" :key="index">
              <label :for="'module_21' + index+1" class="form-control-label">Module 21{{ index+1 }}</label>
              <argon-input type="text" v-model="formData.modules_sem3[index]" />
            </div>
          </div>

          <hr class="horizontal dark" />
          <p class="text-uppercase text-sm">Semester 4 modules</p>
          <div class="row">
            <div class="col-md-6" v-for="(module, index) in formData.modules_sem4" :key="index">
              <label :for="'module_22' + index+1" class="form-control-label">Module 22{{ index+1 }}</label>
              <argon-input type="text" v-model="formData.modules_sem4[index]" />
            </div>
          </div>



        </div>
      </div>
    </div>
  </div>
</template>


<!-- 
<template lang="">
    <div class="w-full">
        <div class="col-md-8 mx-auto">
          <div class="card">
            <div class="card-header pb-0">
              <div class="d-flex align-items-center">
                <p class="mb-0">Insert Degree</p>
                <argon-button color="success" size="sm" class="ms-auto"
                  >Submit</argon-button
                >
              </div>
            </div>
            <div class="card-body">
              <p class="text-uppercase text-sm">Master Information</p>
              <div class="row">
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >name</label
                  >
                  <argon-input type="text" value="lucky.jesse" />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >University name</label
                  >
                  <argon-input type="text" value="lucky.jesse" />
                </div>
        
              </div>
              <div class="row">
                <div class="col-md-10">
                  <label for="example-text-input" class="form-control-label"
                    >Description</label
                  >
                  <argon-input type="text" value="lucky.jesse" />
                </div>
           
        
              </div>


              <hr class="horizontal dark" />
              <p class="text-uppercase text-sm">Semester 1 modules </p>
              <div class="row">
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 111</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 112</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 113</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 114</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 115</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 116</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
               
              </div>
              <hr class="horizontal dark" />
              <p class="text-uppercase text-sm">Semester 2 </p>
              <div class="row">
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 121</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 122</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 123</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 124</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 125</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 126</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
               
              </div>
              <hr class="horizontal dark" />
              <p class="text-uppercase text-sm">Semester 3 </p>
              <div class="row">
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 211</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 212</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 213</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 214</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 215</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 216</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
               
              </div>


              <hr class="horizontal dark" />
              <p class="text-uppercase text-sm">Semester 4 </p>
              <div class="row">
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 221</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 222</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 223</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 224</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 225</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label"
                    >module 226</label
                  >
                  <argon-input
                    type="text"
                    value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                  />
                </div>
               
              </div>
            </div>
          </div>
        </div>
    </div>
</template> -->

<style lang="">
    
</style>