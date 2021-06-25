class Solution:
     def countbinarysubstring(self,s):
          prev,cur=0,1
          output=0
          n=len(s)
          for i in range(1,n):
               if s[i]!=s[i-1]:
                    output+=min(cur,prev)
                    prev=cur
                    cur=1
               else:
                    cur+=1
          print(output)          
          return output+min(prev,cur)
s='010100011101'
s1=Solution()
output=s1.countbinarysubstring(s)
print(output)





   
       
         









