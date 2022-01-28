
#pragma once
#include <iostream>

// struct Node{
// 	int data;
// 	Node* p_next;
// };

class Queue {
public:
	Queue();
	int peek();
	void enqueue(int val);
	void dequeue();
	bool isEmpty();
private:
	Node* p_first;
	Node* p_last;
	int length;
};

Queue::Queue(){
	p_first = nullptr;
	p_last = nullptr;
	length = 0;
}

bool Queue::isEmpty(){
	return length == 0;
}

int Queue::peek(){
	return p_first->data;
}

void Queue::enqueue(int val) {
	Node* p_newNode = new Node;
	p_newNode->data = val;
	if (length == 0) {
		p_first = p_newNode;
		p_last = p_newNode;
	} else {
		p_last->p_next = p_newNode;
		p_last = p_newNode;
		
	}
	length++;
}

void Queue::dequeue() {
	if (!isEmpty()){
		Node* p_pop;
		p_pop = p_first;
		p_first = p_first->p_next;
		if (p_first == nullptr){
			p_last = nullptr;
		}
		delete p_pop;
		length--;
	}
}