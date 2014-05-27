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

import java.math.*;

/** F&uuml;r die numerische Arbeit mit IEEE-Gleitkommazahlen werden
 oftmals neben dem Rundungsmodus round-to-nearest auch nach oben oder
 nach unten gerichtete Operationen ben&ouml;tigt. Diese sind jedoch
 weder im Sprachstandard von Java noch in der Virtual Machine vorgesehen.
 Die folgende Klasse stellt deshalb eine Software-Erweiterung von Java
 um einige nach oben gerichtete Operationen dar. */

public class UpOps {

  /** Die Zahl 0 als Konstante */
  private static BigInteger zero=BigInteger.valueOf(0);

  /** Die Zahl 10 als Konstante */
  private static BigInteger ten=BigInteger.valueOf(10);

  /** Die Zahl 1 als Konstante */
  private static BigInteger one=BigInteger.valueOf(1);

  /** Nicht instanziierbare Klasse */
  private UpOps(){}

  /** Nach oben gerichtete Addition */
  public static double summe(double a,double b) {
    return -DownOps.summe(-a,-b);
  }

  /** Nach oben gerichtete Subtraktion */
  public static double differenz(double a,double b) {
    return summe(a,-b);
  }

  /** Nach oben gerichtete Multiplikation */
  public static double produkt(double a,double b) {
    return -DownOps.produkt(-a,b);
  }

  /** Nach oben gerichtete Division. Bei Division durch 0 wird <code>NaN</code>
   zur&uuml;ckgegeben. */
  public static double quotient(double a,double b) {
    return -DownOps.quotient(-a,b);
  }

  /** Liefert die naechstgroessere Maschinenzahl zurueck. */
  public static double inc(double d) {
    return summe(d,Double.MIN_VALUE);
  }

    /** Berechnet die n-te Potenz einer Maschinenzahl. Hierbei mu&szlig;
   n eine nichtnegative Integerzahl sein
   @param d die zu potenzierende Zahl
   @param n die Potenz
   @exception NumberFormatException falls n<0
   */
  public static double pow(double d,int n) {
    // Zuerst einmal die Sonderfaelle: n<0, 0 hoch 0 und d= +/- oo
    if (n<0)
      throw new NumberFormatException("n<0");
    if (Double.isNaN(d) || (d==0 && n==0))
      return Double.NaN;
    if (d==Double.POSITIVE_INFINITY) {
      if (n==0)
        return Double.NaN;
      else
        return Double.POSITIVE_INFINITY;
    }
    if (d==Double.NEGATIVE_INFINITY) {
      if (n==0)
        return Double.NaN;
      else if (n%2==0)
        return Double.POSITIVE_INFINITY;
      else
        return Double.NEGATIVE_INFINITY;
    }
    if (n==0)
      return 1;
    // Jetzt wandle d in eine IEEEZahl um
    IEEEZahl D=new IEEEZahl(d);
    // Betrachte das Vorzeichen (vertauscht)
    D.vorzeichen=(D.vorzeichen!=0 && n%2!=0)?0:1;
    // Betrachte Exponenten
    D.exponent=D.exponent*n;
    // Betrachte Mantisse
    D.mantisse=D.mantisse.pow(n);
    // Runde nach oben und liefere Ergebnis zurueck
    return -D.toDouble();
  }


  
  /** Wandelt einen String in eine <code>double</code>-Zahl um und rundet
   hierbei gerichtet nach oben.
   Da f&uuml;r die Umwandlung nur Gleitkommaoperationen verwendet werden,
   k&ouml;nnte die Schranke in einigen F&auml;llen noch verbessert werden. */
  public static double parse(String s) throws NumberFormatException{
    s=s.toUpperCase(); // Achte nicht auf Gross- oder Kleinschreibung
    if (s.equals("NAN"))
      return Double.NaN;
    if (s.equals("INFINITY"))
      return Double.POSITIVE_INFINITY;
    if (s.equals("+INFINITY"))
      return Double.POSITIVE_INFINITY;
    if (s.equals("-INFINITY"))
      return Double.NEGATIVE_INFINITY;
    int exp=0;                          // *10E(exp)
    BigInteger val=zero;
    int sign=1;
    char C[]=s.toCharArray();
    char c=' ';
    int i=0; // Laufvariable
    if (C[0]=='-') {
      sign=-1;
      i++;
    }
    if (C[0]=='+') {
      sign=+1;
      i++;
    }
    for (;i<C.length;i++) { // Bestimme den Teil vor dem Komma
      c=C[i];
      if (c=='E' || c=='.') break;
      if (c<'0' || c>'9')
        throw new NumberFormatException("Illegal character: "+c);
      val=val.multiply(ten).add(BigInteger.valueOf(c-'0'));
    }
    if (c=='.') // Bestimme den Nachkommaanteil
      for (++i;i<C.length;i++) {
        c=C[i];
        if (c=='E') break;
        if (c<'0' || c>'9')
          throw new NumberFormatException("Illegal character: "+c);
        val=val.multiply(ten).add(BigInteger.valueOf(c-'0'));
        exp--;
      }
    if (c=='E') {
      i++;
      if (i>=C.length)
        throw new NumberFormatException("Exponent missing");
      exp+=Integer.parseInt(s.substring(i));
    }
    // Beruecksichtige nun den Exponenten
    if (exp>=0) {
      BigInteger faktor=ten.pow(exp);
      IEEEZahl res=new IEEEZahl(1);
      res.mantisse=res.mantisse.multiply(val.multiply(faktor));
      res.vorzeichen=(sign==1)?1:0;
      return -res.toDouble();
    }
    else { // exp<0
      IEEEZahl res=new IEEEZahl(1);
      res.mantisse=res.mantisse.multiply(val);
      res.vorzeichen=(sign==1)?1:0;
      IEEEZahl quot=new IEEEZahl(1);
      quot.mantisse=quot.mantisse.multiply(ten.pow(-exp));
      // Speichere das neue Vorzeichen und den neuen Exponenten im Objekt A
      res.exponent=res.exponent-quot.exponent; // =0
      // Berechne die neue Mantisse
      int differenz=54+quot.mantisse.bitLength()-res.mantisse.bitLength();
      if (differenz>0) { // Schiebe die Mantisse nach links
        res.mantisse=res.mantisse.shiftLeft(differenz);
        res.exponent=res.exponent-differenz;
      }
      BigInteger[] quotient=res.mantisse.divideAndRemainder(quot.mantisse);
      res.mantisse=quotient[0];
      BigInteger rest=quotient[1];
      // Betrachte den Rest wegen der Rundung
      if (res.vorzeichen==1 && !rest.equals(zero))
        res.mantisse=res.mantisse.add(one);
      // Ergebnisrueckgabe
      return -res.toDouble();
    }

  }
  
}
