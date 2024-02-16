## Python fundamentals
* List is mutable and Tuples are immutable (cannot be changed, so append no work)
* Lists are heterogeneous. That means that Python accepts different types in a list.

* range -> start, stop, step

* enumerate -> makes key/values

* Slice

       

## Advanced OOP in python        
https://medium.com/@aserdargun/advanced-oop-in-python-a5f6130da291


In Python lists are heterogeneous. That means that Python accepts different types in a list. Notice the list contains a NONE value.
Method overloading - you can use optional or keyword params

    class Device:
        def set_address(self, address, port=None):
            if port is None:
                self.address = address
            else:
                self.address = address + ":" + port

    device = Device()
    device.set_address("127.0.0.1", port="8000")
    print(device.address)


### Polymorphism


Open-closed principle - Open-Closed principle states that software entities should be open for extension but closed for modification. 


Coding pattern - Models, Data creation and Reporting

    Models -> Classes
    Data creation -> calling class methods
    Reporting -> printing / returns from the methods

