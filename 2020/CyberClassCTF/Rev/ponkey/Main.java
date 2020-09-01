import java.util.Scanner;
public class Main
{
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      String password = sc.nextLine();
      password=encrypt(password);
      if (password.equals("ba`_ba`_srqpedcbzyxwonmlnmlkmlkjjihg210/xwvuLKJI3210MLKJ|{zy")) {
          System.out.println("Correct. Your input is the flag.");
      }
      else {
          System.out.println("Your input is incorrect.");
      }
  }
  
  public static String encrypt(String input) {
      String ret = "";
      for (int i = 0; i<input.length(); i++) {
        for (int h = 1; h < 5; h++) {
          ret+=(char)(input.charAt(i)-(h%5));
        }
      }
      return ret;
  }
}
