class Solution {
public:
    bool isPerfectSquare(int num) {
        long long l = 1;
        long long h = num/2;
        if(num == 1)
            return true;
        else{
            while(l<=h){
                long long mid = l+(h-l)/2;
                long long sqr = mid*mid;
                if(sqr == num)
                    return true;
                else if(sqr < num)
                    l = mid+1;
                else
                    h = mid-1;
            }
        }

        return false;
    }
};