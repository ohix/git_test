class Lotto_6_aus_49_v3 {
    static int n=6; // 6 Zahlen werden gezogen
    static int[] x = new int[n];    // Lottozahlen
    static int[] tip = new int[n];  // Benutzereingabe
    
    public static void main(String[] args) throws java.io.IOException  {
      System.out.println("Lotto 6 aus 49\n");
      
      // Feld mit Lottozahlen
      System.out.println("Lottozahlen: ");
      int z=0; // aktuell gezogene Zahl
      boolean d = false;  // Detektorvariable
      for(int i=0;i<n;i++){
        do{z=(int)(Math.random()*49+1);   // 1 ... 49
           d = false;  // Annahme: z ist nicht doppelt
           // mit allen vorherigen Zahlen vergleichen
           for(int j=0;j<i;j++)
              if(z==x[j]) d=true;   // �bereinstimmung --> d=true
        }while(d==true);  // falls doppelt --> wiederholen   
        x[i]=z; 
      } 
      // Eingabe des Benutzers 
     for(int i=0;i<n;i++){
        do{System.out.print(i+". Zahl: ");
           z=readint(); // Eingabe einer Zahl
           d = false;   // Annahme: z ist nicht doppelt
           // mit allen vorherigen Zahlen vergleichen
           for(int j=0;j<i;j++)
              if(z==tip[j]) d=true;   // �bereinstimmung --> d=true
           if((z<1)||(z>49)) d=true;  // falls nicht 1 ... 49
        }while(d==true);  // falls doppelt --> wiederholen   
        tip[i]=z; 
      } 
      
      // Vergleich von Lottozahlen x und Eingabe tip
      int treffer=0;
      for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
          if(x[i]==tip[j]) treffer++;
      ausgabe();
      System.out.println("Du hast "+treffer+" Richtige.");
    }
    
    
    static void ausgabe(){
      for(int i=0;i<n;i++) 
      System.out.print(x[i]+" ");
      System.out.println("");
    }  
    
    static String readString() throws java.io.IOException {
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
    
    static double readdouble() throws java.io.IOException {
      String s=readString();
      double ergebnis=0.0;
      try {
        ergebnis = Double.valueOf(s).doubleValue();
      } catch (NumberFormatException e) {
        System.out.println(" Falsche Eingabe!\n");
      }
      return ergebnis;
    } 
    
    static int readint() throws java.io.IOException {
      String s=readString();
      int ergebnis=0;
      try {
        ergebnis = Integer.valueOf(s).intValue();
      } catch (NumberFormatException e) {
        System.out.println(" Falsche Eingabe!\n");
      }
      return ergebnis;
    }      
    
    static char readchar() throws java.io.IOException {
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
    
  