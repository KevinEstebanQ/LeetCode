from random import randint

class Solution:
    def insersionSort(self,  Ulist: list)->list:
        #first loop through the whole array starting at index 1 since
        # index 0 is the sorted part

        #I just works to copy the value to sort
        for i in range(len(Ulist)):
            #copy the current value at i
            copy = Ulist[i]
            #walk back to the beggining of the array
            #will always reference the num behind i
            prevIndex = i - 1
            #loop while we havent got the beggining
            #loop until we hit a value behind key that is smaller than it
            while prevIndex >=0 and Ulist[prevIndex] > copy:
            #shift value once to the right
                Ulist[prevIndex + 1] =  Ulist[prevIndex]
            #keep looking back
                prevIndex-=1
            # we either hit the end or found a number less than key
            Ulist[prevIndex + 1] = copy

        return Ulist
            #MAIN IDEA: 
            #copy the value behing you to the front if the value is value is greater
            #than the key, once you find the position we can stop
            # keep copying the value forward, as the key is saved in a variable, no value
            #is lost
        
    

    def selectionSort(self, uList: list):
        for currentIndex in range(len(uList)):
            currentMin = currentIndex #asume num at i is the smallest 
            for j in range(currentIndex + 1, len(uList)):
                if uList[currentIndex] > uList[j]: # update if a new smallest is found
                    currentMin = currentIndex
            #use the saved variables to update the list
            uList[currentMin], uList[currentIndex] = uList[currentIndex], uList[currentMin]


        ## MAIN idea: go through the list checking for the current minimun index
        #asume the current min is index at i

        #if a smaller value is found the update, in the end swap the value at the assumed
        #min with the actual min
        return uList

        

    



def main():
    unsorted = []
    for i in range(0,100):
        unsorted.append(randint(0,100))

    print(unsorted)
    sl1 = Solution()
    print(sl1.insersionSort(unsorted))
    print("selection: " + str(sl1.selectionSort(unsorted)))
    print(sl1.insersionSort(unsorted) == sl1.selectionSort(unsorted))
    
main()