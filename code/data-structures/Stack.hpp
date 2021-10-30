#pragma once
#include <iostream>

class Stack{
public:
	Stack();
	void push(const int val);
	void pop();
	int peek();
	bool isEmpty();
private:
	struct Node{
		int data;
		Node* p_next;
	};
	Node* p_head;
	int height;
};

Stack::Stack(){
	p_head = nullptr;
	height = 0;
}

bool Stack::isEmpty(){
	return height==0;
}

void Stack::push(const int val){
	Node* p_newNode = new Node;
	p_newNode->data = val;
	p_newNode->p_next = p_head;
	p_head = p_newNode;
	height++;

}

void Stack::pop(){
	if (!isEmpty()){
		Node* p_pop;
		p_pop = p_head;
		p_head = p_head->p_next;
		delete p_pop;
		height--;
	}
}

int Stack::peek(){
	return p_head->data;
}