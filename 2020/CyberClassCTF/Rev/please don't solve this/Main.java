import java.util.Scanner;
public class Main
{
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      String password = sc.nextLine();
      password=encrypt(password);
      if (password.equals("aavhyp1x1t]e2pp_]e/x1]w2s]sr{")) {
          System.out.println("Correct. Your input is the flag.");
      }
      else {
          System.out.println("Your input is incorrect.");
      }
  }
  
  public static String encrypt(String input) {
      String ret = "";
      int len = input.length();
      for (int i = 0; i<len; i++) {
    	int a = input.charAt(i);
        if ((int)(a)%2 == 0) {
        	ret+=(char)(a+2);
        }
        else {
        	ret+=(char)(a-2);
        }
      }
      return ret;
  }
}
