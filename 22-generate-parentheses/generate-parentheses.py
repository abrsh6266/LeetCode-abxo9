class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = ['']
        n1 = [0]
        n2 = [0]

        j = 0;
        while j < 2*n :
            rest = []
            n1t = []
            n2t = []
            for i in range(0,len(res)):
                if( n1[i] > n2[i] ):
                    rest.append( res[i]+')' );
                    n1t.append(n1[i])
                    n2t.append(n2[i]+1 )
                rest.append( res[i]+'(' );
                n1t.append(n1[i]+1)
                n2t.append(n2[i] )
            res = rest
            n1 = n1t
            n2 = n2t 
            j += 1

        ans = []
        for i in range(0,len(res)):
            if( n1[i] == n2[i] ):
                ans.append(res[i]);

        return ans ;    
                
                