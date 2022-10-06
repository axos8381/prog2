#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fibHelp();
	private:
		int age;
		int fib();
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}

int Person::fib(int n){
	if(n <= 1) {
      returnn;
   }
      return fib(n-1) + fib(n-2);
   
}

int Person::fibHelp(){
	return fib(age);
}
 
void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_fibHelp(Person* person) {return person->fibHelp();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}