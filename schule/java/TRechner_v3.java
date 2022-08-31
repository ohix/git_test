class TRechner_v3 {
  
  public static void main(String[] args)
         throws java.io.IOException  {
    int a=0, b=0, erg=0, rest=1;
    char z='+';
    System.out.println("Gib ganze Zahlen ein!");
    System.out.print("a="); a=readint();
    System.out.print("b="); b=readint();
    System.out.print("Rechenzeichen (+,-,*,/): ");
    z=readchar();
    if(z=='+') erg = a+b;
    else if(z=='-') erg = a-b;
         else if(z=='*') erg = a*b;
              else if(z=='/') {erg = a/b; rest = a%b;}
                   else System.out.println("Falsches Zeichen");
    System.out.println("Ergebnis: "+erg);
    if(z=='/') System.out.println("Rest: "+rest);
  }
    
 static String readString()
     throws java.io.IOException {
     byte zeile[]=new byte[25];
     System.in.read(zeile);
     String s = "";
     int i = 0;
     char z =' ';
     byte b = zeile[i];
     while ((b!=13) && (b!=10) && (i<25))
           {z=(char) zeile[i];s=s+z;i++;b=zeile[i];}
     return s;
 }    
    
 static double readdouble()
     throws java.io.IOException {
     String s=readString();
     double ergebnis=0.0;
     try {
           ergebnis = Double.valueOf(s).doubleValue();
         } catch (NumberFormatException e) {
           System.out.println(" Falsche Eingabe!\n");
         }
     return ergebnis;
 } 
 
 static int readint()
     throws java.io.IOException {
     String s=readString();
     int ergebnis=0;
     try {
           ergebnis = Integer.valueOf(s).intValue();
         } catch (NumberFormatException e) {
           System.out.println(" Falsche Eingabe!\n");
         }
     return ergebnis;
 }      
    
 static char readchar()
     throws java.io.IOException {
     String s=readString();
     char ergebnis=' ';
     try {
           ergebnis = s.charAt(0);
         } catch (StringIndexOutOfBoundsException e) {
           System.out.println(" Falsche Eingabe!\n");
         }
     return ergebnis;
  }   
}

