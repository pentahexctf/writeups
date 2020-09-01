import java.util.Scanner;
public class Main
{
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      System.out.println("hello! can you help me find the password to my ol' CJ7?");
      String password = sc.nextLine();
      password=encrypt(password);
      if (password.equals("c}tn{bLyp11pyLf_07ppt1_f0fkc")) {
          System.out.println("ya got the flag my dude");
      }
      else {
          System.out.println("that's not the right flag ??? try again >:(");
      }
  }
  
  public static String encrypt(String input) {
      int len = input.length();
      char[] ret = new char[len];
      for (int i = 0; i<len; i++) {
        if (i % 2 == 0) {
        	ret[i] = input.charAt(i);
        }
        else {
        	ret[i] = input.charAt(len-i);
        }
      }
      String retstr = new String (ret);
      return retstr;
  }
}