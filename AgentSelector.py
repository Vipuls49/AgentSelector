import random as r
ans=['yes','no']
agents=[]
data=[]
av=[]
onrole=[]
given=[]
def is_empty(list1):
    if len(list1)==0:
        return True
    else:
        return False
        
        
def is_available(avail):
    if avail=='yes':
        return True
    else:
        return False
no_agent=int(input("enter no of agent's data to be filled="))
for i in range(no_agent):
    agentNo=input("enter agent no:")
    avail=r.choice(ans)
    avail_since=r.randint(1,12)
    role=input("enter role:")
    data.append(agentNo)
    data.append(avail)
    data.append(avail_since)
    data.append(role)
    print(data)
    agents.append(data)
    data=[]
    print(agents)
    
iss=int(input("Enter no of issues you want to resolved"))
for k in range(iss):
    issue=input("enter your issue=")
    issue_role=input("enter role of issue=")
    
    print("1.all available mode(Your issue visible to all agents)")
    print("2.random(randomly selected agent for your issue")
    mode=int(input("Select mode from above for your issue:"))
    if mode==1:
        for i in agents:
            i.append(issue)
            i.append(issue_role)
            print("This is the list of agents who have the info of your issue ")
            count=1
        for f in agents:
            print("-----",count,"-----")
            print("Agent_no=",f[0])
            print("Availability=",f[1])
            print("Hours since agent will work on your issue",f[2])
            print("Role of agent=",f[3])
            print("Your issue=",f[4])
            print("Your issue role=",f[5])
            print("-----------")
            count+=1
            
            
            
    elif mode==2:
        for i in agents:
            if is_available(str(i[1])):
                av.append(i)
                
        if(is_empty(av)):
            print("sorry for your inconvinience but any agent is not available this time try after some time")
                
            
                
        for j in av:
            if j[3].lower()==issue_role.lower():
                onrole.append(j)
        given=r.choice(onrole)
        given.append(issue)
        given.append(issue_role)
        print("this is the assigned agent for your issue")
        print("Agent_no=",given[0])
        print("Availability=",given[1])
        print("Hours since agent will work on your issue",given[2])
        print("Role of agent=",given[3])
        print("Your issue=",given[4])
        print("Your issue role=",given[5])
        
    else:
        print("Entered wrong choice pls enter again")
        
                        
                    
                        
                
            
        
        
        
  