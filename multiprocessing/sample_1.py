from datetime import datetime
import cursor
import multiprocessing

i = 1
per_query = 10
offset = 1
offset_limit = 100

# Function which handel Image Part.
def DataFromMysql(start,end):
    print("==========================================================================================")
    print(" START TIME For Start Offset "+ str(start) +" : "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    x = range(start, end)
    for n in x:
      print(n)

    print("END TIME For End Offset "+ str(end) +" : "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  
    print("==========================================================================================")


# Main Function Start       
if __name__ == '__main__':
    while offset < offset_limit:
        conn = "conn"+str(i)
        cursor = "cursor"+str(i)
        m = "m"+str(i)
        end = (offset+per_query)
        m = multiprocessing.Process(target=DataFromMysql, args=(offset,end))
        m.start() 
        offset += per_query
        i += 1  