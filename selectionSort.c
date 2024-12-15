#include <stdio.h>

void printArray(int arr[], int n) {
    for (int i =0; i < n; i++){
    printf("%d",arr[i]);
    }
}


int main(){
    int arr[] = {7,8,3,1,2};
    int n = 5;

    for (int i = 0; i <n-1; i++) {
    int smallest = i;
        for (int j = i+1; j<n; j++) {
        if (arr[smallest]> arr[j]) {
            int temp = arr[smallest];
            arr[smallest] = arr[i];
            arr[i] = temp;
        }
       }
    }
    
    printArray(arr,n);
    
    }

