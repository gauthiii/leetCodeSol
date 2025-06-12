class Solution {
    public int reverse(int x) {

        int sign=1;

        if (x<0)
        sign=-1;

     String str = String.valueOf(Math.abs(x));

     try{
     String sb = new StringBuilder(str).reverse().toString();

     int r = Integer.parseInt(sb)*sign;

        return r;
     } catch (NumberFormatException e) {
            return 0;
        }
        
    }
}