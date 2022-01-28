#include <iostream>
#include <vector>

void SelectionSort(std::vector<int> &v){
    std::vector<int> copy(v.size());

    // Sort through array
    for (int i = 0; i < v.size()-1; ++i){
        // Find minimum value
       int minIdx = i;
       for (int j = i+1; j < v.size(); ++j){
           if (v[j] < v[minIdx]){
               minIdx = j;
           }
       } 
       // Swap current min value to top of array
       int tmp = v[minIdx];
       v[minIdx] = v[i];
       v[i] = tmp;
    }

}

void Print(const std::vector<int> &v){
    for (int i = 0; i < v.size(); i++){
        std::cout << v[i] << std::endl;
    }  
}

int main(){

    std::vector<int> v{64, 25, 12, 22, 11};
    std::cout << "----- Unsorted Array ----" << std::endl;
    Print(v);
    SelectionSort(v);
    std::cout << "----- Sorted Array ----" << std::endl;
    Print(v);

    return 0;
}