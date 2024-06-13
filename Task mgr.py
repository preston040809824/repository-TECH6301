#Read tasks
file=open("Tasks.txt", "r")
chunk_out= file.read()
print("Task list:", chunk_out)
file.close()

#Write tasks and append to the end of the doc
file=open("Tasks.txt", "a")
file.write("New Task:\nEnter new task")
file.close
 
#to remove a line from the task list
with open('months.txt', 'r') as fr:

        lines = fr.readlines()
         
        
        ptr = 1
with open("Tasks.txt", "w") as fw
    for line in lines:
        if ptr !=n: #to remove the n'th line (i.e. the last task)
            fw.write(line)
            ptr += 1
print("Task Deleted")