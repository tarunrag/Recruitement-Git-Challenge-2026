#include <stdio.h>

int main() {
    int n, i;
    int arr[100]; // We assume the array won't have more than 100 elements
    int min, max;

    // Step 1: Get the number of elements from the user
    scanf("%d", &n);

    // Step 2: Get the space-separated integers and store them in an array
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    // Step 3: Initialize min and max with the first element of the array
    min = arr[0];
    max = arr[0];

    // Step 4: Loop through the array to find the smallest and largest numbers
    for (i = 1; i < n; i++)
    {
        // If current element is smaller than our current min, update min
        if (arr[i] < min)
        {
            min = arr[i];
        }

        // If current element is larger than our current max, update max
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }

    // Step 5: Print the results in the required format
    printf("Minimum: %d\n", min);
    printf("Maximum: %d\n", max);

    return 0;
}
