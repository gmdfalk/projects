/*
    Copyright (C) 1999  (Jens Scheffler)

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
*/


package grundkurs.tools;

import java.io.*;
import java.util.*;
import java.math.*;

/** Diese Klasse stellt einige einfache Methoden zum Einlesen von der Tastatur
 zur Verf&uuml;gung. Es werden diverse Werte von der Tastatur eingelesen, die
 jeweils durch ein Leerzeichen, einen Tabstop oder ein Zeilenendezeichen
 getrennt sein m&uuml;ssen.
 @author Jens Scheffler
 @version 1.01 Spezialfassung f&uuml;r <I>Programmieren 1 in Java</I>
 */
public class IOTools {

    private IOTools(){} // somit kann die Klasse nicht instanziiert werden!
    private static BufferedReader in=
               new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer eingabe;
    private static String zeichenkette;

/** L&ouml;scht alles, was sich in der momentanen Zeile befindet.
 Das hei&szlig;t es wird der Eingabe bis zum Zeilenende keine Beachtung mehr
 geschenkt
 */
    public static void flush(){
        eingabe=null;
    }

/* Private Methode, die den Tokenizer fuellt. Dies ist uebrigens eine von
 zwei Methoden, die die Klasse zum Absturz bringen kann...*/
    private static void init(){
      zeichenkette=null;
      if (eingabe!=null && eingabe.hasMoreTokens()) return;
        while (eingabe==null || !eingabe.hasMoreTokens())
          eingabe=new StringTokenizer(readLine());
    }

/* Private Methode, die eine Fehlermeldung ausgibt */
    private static void error(Exception e,String prompt) {
      System.out.println("Eingabefehler "+e);
      System.out.println("Bitte Eingabe wiederholen...");
      System.out.print(prompt);
    }

/** Liest eine ganze Textzeile von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zeile.
 */
/* Dies ist die zweite Methode, die die Klasse zum Absturz bringen kann.*/
    public static String readLine(String prompt){
        flush();
        String erg="";
        System.out.print(prompt);
        try{
            erg=in.readLine();
        } catch(IOException e){
            System.err.println(""+e+"\n Programm abgebrochen...\n");
            System.exit(1);
        }
        if (erg==null) {
          System.err.println("Dateiende erreicht.\nProgramm abgebrochen...\n");
          System.exit(1);
        }
        return erg;
    }

/** Liest eine <CODE>int</CODE>-Zahl von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zahl.
 */
    public static int readInteger(String prompt){
        int erg;
        System.out.print(prompt);
        init();
        while(true){
            try{
                erg=Integer.parseInt(eingabe.nextToken());
            } catch (NumberFormatException e) {
              error(e,prompt);init();continue;
            }
            return erg;
        }
    }

/** Liest eine <CODE>long</CODE>-Zahl von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zahl.
 */
    public static long readLong(String prompt){
        long erg;
        System.out.print(prompt);
        init();
        while(true){
            try{
                erg=Long.parseLong(eingabe.nextToken());
            } catch (NumberFormatException e) {error(e,prompt);init();continue;}
            return erg;
        }
    }

/** Liest eine <CODE>double</CODE>-Zahl von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zahl.
 */
    public static double readDouble(String prompt){
        double erg;
        System.out.print(prompt);
        init();
        while(true){
            try{
                erg=Double.valueOf(eingabe.nextToken()).doubleValue();
            } catch(NumberFormatException e) {error(e,prompt);init();continue;}
            return erg;
        }
    }

/** Liest eine <CODE>float</CODE>-Zahl von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zahl.
 */
    public static float readFloat(String prompt){
        float erg;
        System.out.print(prompt);
        init();
        while(true){
            try{
                erg=Float.valueOf(eingabe.nextToken()).floatValue();
            } catch(NumberFormatException e) {error(e,prompt);init();continue;}
            return erg;
        }
    }

/** Liest eine <CODE>short</CODE>-Zahl von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zahl.
 */
    public static short readShort(String prompt){
        short erg;
        System.out.print(prompt);
        init();
        while(true){
            try{
                erg=Short.valueOf(eingabe.nextToken()).shortValue();
            } catch(NumberFormatException e) {error(e,prompt);init();continue;}
            return erg;
        }
    }

/** Liest eine <CODE>byte</CODE>-Zahl von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zahl.
 */
    public static byte readByte(String prompt){
        byte erg;
        System.out.print(prompt);
        init();
        while(true){
            try{
                erg=Byte.valueOf(eingabe.nextToken()).byteValue();
            } catch(NumberFormatException e) {error(e,prompt);init();continue;}
            return erg;
        }
    }

/** Liest einen boolschen Wert von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return der eingelesene Wert.
 */
    public static boolean readBoolean(String prompt){
        String try_this=readString(prompt);
        while (!try_this.equals("true") && !try_this.equals("false")) {
            error(new NumberFormatException("For input string: \"" + try_this + "\""),prompt);
            try_this=readString();
        }
        return try_this.equals("true");
    }


/** Liest ein Textwort von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return das eingelesene Wort.
 */
    public static String readString(String prompt){
        System.out.print(prompt);
        init();
        return eingabe.nextToken();
    }

    /** Liest ein Zeichen von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return das eingelesene Zeichen.
 */
    public static char readChar(String prompt){
        String try_this=readString(prompt);
        while (!(try_this.length() == 1)) {
            error(new NumberFormatException("For input string: \"" + try_this + "\""),prompt);
            try_this=readString();
        }
        return try_this.charAt(0);


    }

/** Liest eine ganze Textzeile von der Tastatur ein.
@return die eingelesene Zeile.
 */
    public static String readLine(){
        return readLine("");
    }

/** Liest eine <CODE>int</CODE>-Zahl von der Tastqtur ein.
@return die eingelesene Zahl.
 */
    public static int readInteger(){
            return readInteger("");
    }

/** Liest eine <CODE>int</CODE>-Zahl von der Tastqtur ein.
@return die eingelesene Zahl.
 */
    public static int readInt(){
            return readInteger("");
    }

/** Liest eine <CODE>int</CODE>-Zahl von der Tastatur ein. Soll vorher eine
 Eingabeaufforderung gemacht werden, geschieht dies durch den Parameter.
 Dieser kann jedoch auch wegfallen.
@param prompt eine eventuelle Eingabeaufforderung
@return die eingelesene Zahl.
 */
    public static int readInt(String prompt){
            return readInteger(prompt);
    }

/** Liest eine <CODE>long</CODE>-Zahl von der Tastatur ein.
@return die eingelesene Zahl.
 */
    public static long readLong(){
            return readLong("");
    }

/** Liest eine <CODE>double</CODE>-Zahl von der Tastatur ein.
@return die eingelesene Zahl.
 */
    public static double readDouble(){
        return readDouble("");
    }

/** Liest eine <CODE>short</CODE>-Zahl von der Tastatur ein.
@return die eingelesene Zahl.
 */
    public static short readShort(){
        return readShort("");
    }

/** Liest eine <CODE>byte</CODE>-Zahl von der Tastatur ein.
@return die eingelesene Zahl.
 */
    public static byte readByte(){
        return readByte("");
    }

/** Liest eine <CODE>float</CODE>-Zahl von der Tastatur ein.
@return die eingelesene Zahl.
 */
    public static float readFloat(){
        return readFloat("");
    }

/** Liest ein Zeichen von der Tastatur ein.
@return das eingelesene Zeichen
 */
    public static char readChar(){
      return readChar("");
    }
    
/** Liest ein Textwort von der Tastatur ein.
@return das eingelesene Wort.
 */
    public static String readString(){
        return readString("");
    }

    /** Liest einen boolschen Wert von der Tastatur ein.
@return das eingelesene Wort.
 */
    public static boolean readBoolean(){
        return readBoolean("");
    }

    /** Wandelt eine double-Zahl in einen String um.
     Bei der &uuml;blichen Umwandlung von double-Werten in einen String
     findet eine Rundung statt. So wird etwa die Zahl 0.1, obwohl intern
     nicht darstellbar, dennoch auf dem Bildschirm ausgegeben. Diese
     Methode umgeht die Rundung */
    public static String toString(double d) {
      if (Double.isInfinite(d) || Double.isNaN(d))
        return ""+d;
      return (new BigDecimal(d)).toString();
    }
}
