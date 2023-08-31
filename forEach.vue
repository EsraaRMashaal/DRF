<script lang="ts">

 // Best way to wait for .forEach() to complete all APIs calls
  async loopOnData() {
        this.data.forEach(item => { // loop on all data then call api depend on each record
          console.log('Data :', item);
         var dataLength = 0;
          API.finally(() => {
           dataLength += 1;
            if (dataLength === this.data.length){ // last iteration 
               console.log('Done --------');
            }
          });
        });
    }
  
</script>
