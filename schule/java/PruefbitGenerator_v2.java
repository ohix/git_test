//Beispielinput: 001 | 010011

class PruefbitGenerator_v2 {
    public static void main(String[] args)
    throws java.io.IOException  {
        String eingabe="";  // z.B. "101"
        String s="";
        char e=' ', a=' ';  // Eingabezeichen, z.B. '1'
        int z=0;            // Zustände: 0,1,2,3,4
        // Eingabe
        System.out.print("Gib eine Ziffernfolge (0,1) ein! ");
        eingabe = readString(); // z.B. "101"
        
        // �berf�hrungs- und Ausgabefunktion
        int laenge = eingabe.length();
        for (int i=0;i<laenge;i++){
            e=eingabe.charAt(i);
            a=' ';      //Ausgabe
            s=s+e;  // s=s+0 s=0+0 s=0+0+1 neuer String, in den ggf. Ausgabezeichen eingefügt werden
            switch (z) {
                case 0:             //Aktueller Zustand
                if(e=='0'){z=2;}    //Eingabe , Folgezustand
                if(e=='1'){z=1;}
                break;
                case 1: 
                if(e=='0'){z=3;}
                if(e=='1'){z=4;}
                break;
                case 2: 
                if(e=='0'){z=4;}
                if(e=='1'){z=3;}
                break;
                case 3: 
                if(e=='0'){z=0; a='1'; s=s+a;}
                if(e=='1'){z=0; a='0'; s=s+a;}
                break;
                case 4: 
                if(e=='0'){z=0; a='0'; s=s+a;}
                if(e=='1'){z=0; a='1'; s=s+a;} //s=0+0+1+1
                break;
                default:break; 
            
            }
            System.out.println("Zustand:"+z+" Ausgabezeichen:"+a);
        }
        // Ausgabe
        System.out.println();
        System.out.println("String mit Pr�fbits: "+s);   
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