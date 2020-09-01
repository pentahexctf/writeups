//the first t should be an h
import java.util.*;
import java.lang.Math;
public class Main
{
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      String password = sc.nextLine();
      String encrypted =never(gonna(give(you(up(password)))));
      if (encrypted.equals("lYWJlYWJlcLFwcLFwcLFwcLFwcG^m^m^5e\\FwcLFwcLFwcLFsfG|sfLJ|Ono:Oi4xP\\FwcLFwcLFwcGxva6xva6xufm5ufrx7h3h3h3h3crNoaGloPi8uPmJlYWJlYWJxfW1xfy1~c3R~cLFwcLFgYGFgYHIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMnIyMrNycmhmj39/j39/j3<=YWJ")) {
          System.out.println("Correct. Your input is the flag.");
      }
      else {
          System.out.println("Your input is incorrect.");
      }
  }
  public static String never(String input) {
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
  public static String gonna(String input) {
	  String ret = "";
	  for (int i = 0; i<input.length();i++) {
		  ret+=(char)(2+input.charAt((i+3)%input.length()));
	  }
	  return ret;
  }
  public static String give(String input) {
	  return Base64.getEncoder().encodeToString(input.getBytes());
  }
  public static String you(String input) {
	  String ret = "";
	  for (int i = 0; i<input.length(); i++) {
		  ret+= (char)(input.charAt(i)^3 );
	  }
	  return ret;
  }
  public static String up(String input) {
	  String ret = "";
	  for (int i = 0; i<input.length(); i++) {
		  for (int j = 0; j<function(i); j++) {
			  ret += (char)(input.charAt(i)-1);
		  }
	  }
	  return ret;
  }
  public static int function(int input) {
	  return Math.abs((int)(3 + 2.3*Math.sin(input)+0.8*Math.tan(2.3*input)+1));
  }
}
