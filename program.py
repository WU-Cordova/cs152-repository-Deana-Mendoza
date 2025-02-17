

from datastructures.bag import Bag

#testing stuff for bag during class lecture 1/27/25
def main(): 
    
    bag=Bag()
    bag.add("apple")
    bag.add("pear")
    bag.add("banana")

    items=bag.distinct_items()

    print(f"Distinct Items:{items}")



if __name__ == '__main__':
    main()
