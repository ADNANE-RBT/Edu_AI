<template lang="">
    <div>
        <div class="row">
      <div class="col-md-7">
        <billing-card />
      </div>
      <div class="col-md-5">
        <invoice-card class="mt-4" />
      </div>
    </div>
    </div>
</template>
<script setup>
// import MasterCard from "@/examples/Cards/MasterCard.vue";
// import DefaultInfoCard from "@/examples/Cards/DefaultInfoCard.vue";
// import PaymentCard from "./components/PaymentCard.vue";
import InvoiceCard from "./components/InvoiceCard.vue";
import BillingCard from "./components/BillingCard.vue";
// import TransactionCard from "./components/TransactionCard.vue";
</script>
<style lang="">
    
</style>