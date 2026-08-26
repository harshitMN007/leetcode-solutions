void rotate(int* nums, int numsSize, int k) {

    int arr[numsSize];
    if(k>numsSize){
        k=k % numsSize;
    }
    if(numsSize==k || k==0){
        return;
    }
    for(int i=0;i<numsSize;i++){
        arr[i]=nums[i];
    }
    for(int i=0;i<(numsSize-k);i++){
        nums[i+k]=arr[i];
    }

    for(int i=0;i<k;i++){
        nums[i]=arr[i+numsSize-k];
    }

   
    
}

#problem with above is time complexity is O(n)

void rotate(int* nums, int numsSize, int k) {

    k = k % numsSize;

    if(k == 0)
        return;

    int temp;

    // Reverse entire array
    int left = 0;
    int right = numsSize - 1;

    while(left < right) {
        temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;

        left++;
        right--;
    }

    // Reverse first k elements
    left = 0;
    right = k - 1;

    while(left < right) {
        temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;

        left++;
        right--;
    }

    // Reverse remaining elements
    left = k;
    right = numsSize - 1;

    while(left < right) {
        temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;

        left++;
        right--;
    }
}
#this has a time complexity of O(1)