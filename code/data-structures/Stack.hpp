#pragma once
#include <iostream>
#include <vector>

struct Node{
	int data;
	Node* p_next;
};
class Stack{
public:
	Stack();
	void push(const int val);
	void pop();
	int peek();
	bool isEmpty();
private:
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



class StackArray {
public:
	StackArray();
	void push(const int val);
	void pop();
	int peek();
	bool isEmpty();

private:
	std::vector<int> data;
	int height;
};


StackArray::StackArray(){
	height = 0;
}

void StackArray::push(const int val) {
	data.push_back(val);
	height++;
}

void StackArray::pop() {
	data.pop_back();
	height--;
}

int StackArray::peek() {
	return data[height-1];
}

bool StackArray::isEmpty() {
	return data.size() == 0;
}

