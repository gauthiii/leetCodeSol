class Solution {
    public boolean isPalindrome(int x) {

        if (x<0)
        return false;

        if (x==0)
        return true;

        int o=x;
        int r=0;

        while (x>0){
            int d = x%10;
            r=(r*10)+d;
            x/=10;
        }

        return (o==r);
    }
}