#include <iostream>
// #include "LinkedList.hpp"
#include "SimpleLinkedList.hpp"
#include "Stack.hpp"
#include "Queue.hpp"

int main(){
    
    std::cout << "Simple Linked List Example" << std::endl;

    SimpleLinkedList list(10);
    list.append(5);
    list.append(16);
    list.append(3);
    list.insert(2,7);
    list.remove(9);
    std::cout << "Length = " << list.size() << std::endl;

    std::cout << "---------------- Stack ---------------" << std::endl;
    Stack s;
    s.push(10);
    s.push(5);
    int top = s.peek();
    s.pop();
    top = s.peek();
    std::cout << top << std::endl;

    std::cout << "---------------- Stack Array ---------------" << std::endl;
    StackArray sa;
    sa.push(10);
    sa.push(5);

    top = sa.peek();
    sa.pop();
    top = sa.peek();
    std::cout << top << std::endl;

    std::cout << "---------------- Queue ---------------" << std::endl;
    Queue Q;
    Q.enqueue(10);
    Q.enqueue(5);
    Q.enqueue(4);
    int first = Q.peek();
    std::cout << "First = " << first << std::endl;
    Q.dequeue();
    std::cout << "Dequeue..." << std::endl;
    first = Q.peek();
    std::cout << first << std::endl;

    // LinkedList<double> nums;
    // nums.insert(10.0);
    // nums.insert(100.0);
    // nums.insert(1.0);

    // double aNum;
    // if (nums.first(aNum)){
    //     std::cout << aNum << std::endl;
    //     while (nums.next(aNum)){
    //         std::cout << aNum << std::endl;
    //     }
    //     std::cout << std::endl;
    // }
    // std::cout << "The size of the list is " << nums.size() << std::endl;
    // if (nums.isEmpty()){
    //     std::cout << "The list is empty" << std::endl;
    // }
    // else{
    //     std::cout << "The lsit is NOT empty" << std::endl;
    // }

    return 0;
}