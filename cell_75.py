#!/usr/bin/env python
# coding: utf-8

# In[ ]:


accounts =  open("accounts_file.txt","w")
accounts.close()
branch = "|_"
print("please enter branch: ")
while True:
  aft = False
  code = input("code: ")
  name = input("name: ")
  parent = input("Parent: ")
  if parent.lower() == "null":
    accounts = open("accounts_file.txt",'a')
    accounts.write(branch+code + "--" + name + '\n')
    accounts.close()
  else:
    accounts = open("accounts_file.txt",'r')
    lines_B = []
    lines_A =[]
    for line in accounts:
      if aft == False:
        for i in range(0,len(line),1):
          if line[i] == '_':
            N = i + 1
          if line[i] == '-':
            M = i
            break
        if line[N:M] == parent:
          lines_B.append(line)
          aft = True
        else:
          lines_B.append(line)
      else:
        lines_A.append(line)
    accounts.close()
    parent = lines_B[len(lines_B)-1]
    branch_level = (parent.count('     ') * 5) + 5
    with open("accounts_file.txt",'w') as accounts:
      for i in range(0,len(lines_B),1):
        accounts.write(lines_B[i])
      line_to_write =(" "*branch_level)+branch+code+'--'+name
      line_to_write = line_to_write.rjust(branch_level,' ')
      accounts.write(line_to_write+'\n')
      for i in range(0,len(lines_A),1):
        accounts.write(lines_A[i])
  x = input("Anymore Branches? (y or n) ")
  if x.lower() == "n":
    #need to output
    break
print("\nAccounts hierarchy: ")
with open("accounts_file.txt",'r') as accounts:
  for line in accounts:
    print(line)

