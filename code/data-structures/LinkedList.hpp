#pragma once

template <class T>
class LinkedList{
public:
    LinkedList();
    ~LinkedList();
    void insert(const T& elem);
    bool first(T& elem);
    bool next(T& elem);
    int size();
    bool isEmpty();
private:
    struct Node{
        T data;
        Node* p_next;
    };
    Node* p_head;
    Node* p_current;
    int numElements;
};


//-- Constructor
template <class T>
LinkedList<T>::LinkedList(){
    p_head = 0;
        p_current = 0;
    numElements=0;
}

// ~Destructor
template<class T>
LinkedList<T>::~LinkedList(){
    Node* p_delete;
    while (!isEmpty()){
        p_delete = p_head;
        p_head = p_head->p_next;
        delete p_delete;
        numElements--;
    }
    std::cout << "Deleting Linked List" << std::endl;
}

template<class T>
void LinkedList<T>::insert(const T& elem){
    Node* p_newNode = new Node;
    p_newNode->data = elem;
    p_newNode->p_next = p_head;
    p_head = p_newNode;
    numElements++;
}

template<class T>
bool LinkedList<T>::first(T& elem){
    bool retVal = false;
    if (!isEmpty()){
        retVal = true;
        p_current = p_head;
        elem = p_current->data;
    }

    return retVal;
}

template<class T>
bool LinkedList<T>::next(T& elem){
    bool retVal = false;
    if (p_current && p_current->p_next !=0){
        p_current = p_current->p_next;
        elem = p_current->data;
        retVal = true;
    }

    return retVal;
}

//-- size() fucntions
template<class T>
int LinkedList<T>::size(){
    return numElements;
}

//-- isEmpty(): Check if linked list is empty
template<class T>
bool LinkedList<T>::isEmpty(){
    return size() == 0;
}