#include <iostream>
#include <string>
#include "factory.h"


int main(){
    factory* eva = new factory("001","001",10); 
   
    drone** d = new drone*[4];
    d[0] = new drone("Mega Tank Drone","Tank",300,1000);
    d[1] = new drone("Unit - 01","Tank",626,10000);
    d[2] = new drone("Shinji","Air",500,1000);
    d[3] = new drone("Asuka","Tank",300,10000);
    factory* donda = new factory("111","123",d,6,4);
    
donda ->levelUp();
donda ->levelUp();
//eva ->printDrones("m"); //segmentation fault whenever this is run
//cout <<"\n";
donda ->printDrones("hp");
cout << "\n";
//donda ->printDrones("m");
cout << "\n";
//d[0] ->print();


   cout << "\n";

   
    for(int q = 0; q < 4; q++)
    {
        delete d[q];
        d[q] = nullptr;
    }
    delete [] d;
    delete eva;
     
   delete donda;

    return 0;
}