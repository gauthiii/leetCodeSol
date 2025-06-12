public class Solution {
    public boolean isValid(String s) {
        Stack<Character> myStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '(' || ch == '{' || ch == '[') {
                myStack.push(ch);
            } else {
                if (myStack.isEmpty()) return false;

                char top = myStack.peek();
                if ((ch == ')' && top == '(') ||
                    (ch == ']' && top == '[') ||
                    (ch == '}' && top == '{')) {
                    myStack.pop();
                } else {
                    return false;
                }
            }
        }

        return myStack.isEmpty();
    }
}
