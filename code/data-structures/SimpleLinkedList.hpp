#pragma once
#include <iostream>

class SimpleLinkedList{
public:
    SimpleLinkedList();
    SimpleLinkedList(const int val);
    ~SimpleLinkedList();
    int size();
    bool isEmpty();
    void append(const int val);
    void prepend(const int val);
    void insert(const int index, const int val);
    void remove(const int index);
private:
    struct Node{
        int data;
        Node* p_next;
    };
    Node* p_head;
    Node* p_current;
    Node* p_tail;
    int numNodes;
};

//-- Default Constructor
SimpleLinkedList::SimpleLinkedList(){
    p_head = nullptr;
    p_tail = nullptr;
    p_current = nullptr;
    numNodes = 0;
}
// Constructor and initialize anode
SimpleLinkedList::SimpleLinkedList(const int val){
    Node* p_newNode = new Node;
    p_newNode->data = val;
    p_newNode->p_next = nullptr;
    p_head = p_newNode;
    p_tail = p_head;
    p_current = nullptr;
    numNodes = 1;
}
// Destructor
SimpleLinkedList::~SimpleLinkedList(){

    Node* p_delete;
    while (!isEmpty()){
        p_delete = p_head;
        p_head = p_head->p_next;

        // std::cout << "Node = " << p_delete->data << std::endl;
        delete p_delete;
        numNodes--;
    }
    // std::cout << "Deleting Linked List" << std::endl;
}

// Return size of linked list
int SimpleLinkedList::size(){
    return numNodes;
}

bool SimpleLinkedList::isEmpty(){
    return size() == 0;
}

// Append an element
void SimpleLinkedList::append(const int val){
    if (isEmpty()){
        Node* p_newNode = new Node;
        p_newNode->data = val;
        p_newNode->p_next = nullptr;
        p_head = p_newNode;
        p_tail = p_newNode;
        numNodes++;
    }
    else{
        Node* p_newNode = new Node;
        p_newNode->data = val;
        p_newNode->p_next = nullptr;
        p_tail->p_next = p_newNode;
        p_tail = p_newNode;
        numNodes++;
    }
}

// inser element at the beginning of linked list
void SimpleLinkedList::prepend(const int val){
    if (isEmpty()){
        Node *p_newNode = new Node;
        p_newNode->data = val;
        p_newNode->p_next = nullptr;
        p_head = p_newNode;
        p_tail = p_newNode;
        numNodes++;
    } 
    else {
        Node *p_newNode = new Node;
        p_newNode->data = val;
        p_newNode->p_next = p_head;
        p_head = p_newNode;
        numNodes++;
    }
}

void SimpleLinkedList::insert(const int index, const int val){
    if (isEmpty() || index == 0){
        prepend(val);
    }
    else if (index >= size()){
        std::cout << "Index exceeds length of List. Appending value to the end of list." << std::endl;
        append(val);
    }
    else {
        p_current = p_head;
        int idx = 1;
        while (p_current != nullptr){
            // std::cout << "idx = " << idx << "\t Current Node Value = " << p_current->data << std::endl;
            if (idx == index){
                Node *p_newNode = new Node;
                p_newNode->data = val;
                p_newNode->p_next = p_current->p_next;
                p_current->p_next = p_newNode;
                numNodes++;
                break;
            }
            p_current = p_head->p_next;
            idx++;
        }
    }
}

void SimpleLinkedList::remove(const int index){
    Node *p_remove = new Node;
    if (index == 0){
        p_remove = p_head;
        p_head = p_head->p_next;
        delete p_remove;
        numNodes--;
    }
    else if (index >= size()){
        std::cout << "Index exceeds length of list. No item was removed." << std::endl;
    }
    else {
        p_current = p_head;
        Node *p_prev;
        int idx = 0;
        while (p_current != nullptr){
            if (idx == index){
                // remove node
                p_remove = p_current;
                p_prev->p_next = p_current->p_next;
                delete p_remove;
                numNodes--;
                break;
            }
            p_prev = p_current;
            p_current = p_current->p_next;
            idx++;
        }
    }

}
