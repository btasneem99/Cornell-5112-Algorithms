# Problem 1a

def maxsum_list(xs) -> int:
    maxLen = len(xs)

    dp = [0 for i in range(maxLen)]
    v = [0 for i in range(maxLen)]

    def _maxsum(arr, i, n):
        if (i >= maxLen):
            return 0
    
        if (v[i]):
            return dp[i]
        v[i] = 1

        dp[i] = max(_maxsum(arr,i+1,n), arr[i] + _maxsum(arr,i+2,n))
        return dp[i]
    
    return _maxsum(xs,0,len(xs))
