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

/** Diese Klasse stellt eine Klasse f&uuml;r die Realisierung von
 Maschinenintervallarithmetik unter Java zur Verfuegung */

public class Interval {
  
  
  // ================
  // I. DATENSTRUKTUR
  // ================
  private double inf=0,sup=0; // Intervallgrenzen
  private boolean empty=false;   // leeres Intervall?

  /** Sollen die Intervallgrenzen exakt (ohne Konvertierung) ausgegeben
   werden, mu&szlig; diese Variable auf true gesetzt werden. Die Ausgaben
   werden allerdings oftmals sehr lang und un&uuml;bersichtlich. */
  public static boolean PRINT_EXACT=false;
  
  // =================
  // II. KONSTRUKTOREN
  // =================
  private Interval(){}
  
  /** Erzeugt ein Intervall aus zwei <code>double</code>-Werten. Ist einer
   dieser Werte <code>NaN</code>, so wird das leere Intervall
   gew&auml;hlt.
   @param inf das Infimum des Intervalls
   @param sup das Supremum des Intervalls
   @exception NumberFormatException falls inf>sup
   */
  public Interval(double inf,double sup) throws NumberFormatException {
    if (Double.isNaN(inf) || Double.isNaN(sup)) {
      empty=true;
    }
    else {
      this.inf=inf;
      this.sup=sup;
      if (inf>sup)
        throw new NumberFormatException("inf>sup (inf="+inf+",sup="+sup+")");
    }
  }
  
  /** Erzeugt ein Punktintervall aus einem <code>double</code>-Wert
   @param val Ober- und Untergrenze des neuen Intervalls
   (<code>NaN</code> steht f&uuml;r das leere Intervall)
   */
  public Interval(double val) {
    if (Double.isNaN(val)) {
      empty=true;
    } else {
      this.inf=val;
      this.sup=val;
    }
  }
  
  /** Erzeugt ein Intervall aus einer Stringdarstellung. Es gibt mehrere
   Formen eines g&uuml;ltigen String:<ul>
   <li> Eine einzelne reelle Zahl, etwa <code>3.14</code>
   <li> ein Punktintervall der Form <code>[3.14]</code>
   <li> die Werte <code>+Infinity</code> und <code>-Infinity</code>
   <li> der Wert <code>NaN</code>, der auf das leere Intervall abgebildet
   wird
   <li> ein Intervall der Form <code>[3.14,3.15]</code>, wobei die
   Grenzen auch unendlich sein d&uuml;rfen. Es mu&szlig; jedoch auch hier
   inf&lt;sup gelten.
   <li> das leere Intervall <code>[empty]</code>
   </UL>
   <P>
   <b>Hinweis:</B> Im allgemeinen m&uuml;ssen die angegebenen Gleitkommazahlen
   gerundet werden. Um eine Einschlie&szlig;ung zu erhalten, findet hierbei
   eine Rundung nach au&szlig;en statt. Somit wird etwa das aus
   <code>0.1</code> gebildete Intervall kein Punktintervall sein.
   <P>
   @exception NumberFormatException falls der String ung&uuml;ltig war
   */
  public Interval(String s) throws NumberFormatException {
    s=s.toUpperCase();
    if (s.equals("[EMPTY]"))
      empty=true;
    else {
      int inf_from=s.indexOf("[");
      int inf_till=s.indexOf(",");
      int sup_from=inf_till+1;
      int sup_till=s.indexOf("]");
      if (inf_from==-1 && inf_till==-1 && sup_till==-1)
      {
        inf=DownOps.parse(s);
        sup=UpOps.parse(s);
        if (Double.isNaN(inf))
          empty=true;
      }
      else if (inf_from==0 && sup_till==s.length()-1 && inf_till!=-1) {
        inf=DownOps.parse(s.substring(inf_from+1,inf_till));
        sup=UpOps.parse(s.substring(sup_from,sup_till));
        if (Double.isNaN(inf) || Double.isNaN(sup))
          empty=true;
        else if (inf>sup)
          throw new NumberFormatException("inf>sup in "+s);
      }
      else if (inf_from==0 && sup_till==s.length()-1 && inf_till==-1) {
        inf=DownOps.parse(s.substring(inf_from+1,sup_till));
        sup=UpOps.parse((s.substring(inf_from+1,sup_till)));
        if (Double.isNaN(inf))
          empty=true;
      }
      else
        throw new NumberFormatException(s);
    }
  }
  
  
  // ===================================================
  // III. ELEMENTARE ZUGRIFFS- UND MANIPULATIONSMETHODEN
  // ===================================================
  /** Gibt eine Stringdarstellung des Intervalls zur&uuml;ck */
  public String toString() {
    if (empty) return "[empty]";
    if (PRINT_EXACT) {
      if (inf==sup)
        return IOTools.toString(inf);
      return "["+IOTools.toString(inf)+","+IOTools.toString(sup)+"]";
    }
      if (inf==sup)
        return ""+inf;
      return "["+inf+","+sup+"]";

  }
  
  /** Gibt das Infimum des Intervalles zur&uuml;ck */
  public double inf() {return (empty)?Double.NaN:inf;}
  
  /** Gibt das Supremum des Intervalles zur&uuml;ck */
  public double sup() {return (empty)?Double.NaN:sup;}
  
  /** Gibt <code>-this</code> zur&uuml;ck. */
  public Interval negate() {
    Interval erg=new Interval();
    if (empty)
      erg.empty=true;
    else {
      erg.inf=-sup;
      erg.sup=-inf;
    }
    return erg;
  }
  
  /** Liefert <code>true</code>, falls das Intervall leer ist. */
  public boolean isEmpty() {
    return empty;
  }
  
  // ======================
  // IV. SCHNITT UND HUELLE
  // ======================
  /** Gibt die H&uuml;lle zweier Intervalle zur&uuml;ck. */
  public Interval hull(Interval val) {
    if (empty) return val;
    if (val.empty) return this;
    Interval erg=new Interval();
    erg.inf=(inf<val.inf)?inf:val.inf;
    erg.sup=(sup>val.sup)?sup:val.sup;
    return erg;
  }
  
  /** Gibt den Schnitt zweier Intervalle zur&uuml;ck. */
  public Interval intersection(Interval val) {
    if (empty) return this;
    if (val.empty) return val;
    Interval erg=new Interval();
    erg.inf=(inf>=val.inf)?inf:val.inf;
    erg.sup=(sup<=val.sup)?sup:val.sup;
    erg.empty=(erg.inf>erg.sup);
    return erg;
  }
  
  
  // =============================================
  // V. ADDITION UND SUBTRAKTION ZWEIER INTERVALLE
  // =============================================
  /** Gibt die Intervallsumme <code>this+val</code> zur&uuml;ck. */
  public Interval add(Interval val) {
    Interval erg=new Interval();
    if (empty || val.empty) {
      erg.empty=true;
      return erg;
    }
    erg.inf=DownOps.summe(inf,val.inf);
    if (Double.isNaN(erg.inf))
      erg.inf=Double.NEGATIVE_INFINITY;
    erg.sup=UpOps.summe(sup,val.sup);
    if (Double.isNaN(erg.sup))
      erg.sup=Double.POSITIVE_INFINITY;
    return erg;
  }
  
  /** Gibt die Intervalldifferenz <code>this-val</code> zur&uuml;ck */
  public Interval subtract(Interval val) {
    return add(val.negate());
  }
  
  // =================
  // VI MULTIPLIKATION
  // =================
  // Abkuerzungen fuer die Multiplikation:
  private double mul_lo(double x,double y) {
    double res=DownOps.produkt(x,y);
    if (Double.isNaN(res))
      return Double.NEGATIVE_INFINITY;
    return res;
  }
  
  private double mul_hi(double x,double y) {
    double res=UpOps.produkt(x,y);
    if (Double.isNaN(res))
      return Double.POSITIVE_INFINITY;
    return res;
  }
  
  /** Liefert das Produkt <code>this*val</code> */
  public Interval multiply(Interval val) {
    // -1 fuer nach aussen, 1 fuer nach innen und 0 fuer to nearest
    Interval erg=new Interval();
    if (empty || val.empty) {
      erg.empty=true;
      return erg;
    }
    if (inf>0) {
      if (val.inf>0) {
        erg.inf=mul_lo(inf,val.inf);
        erg.sup=mul_hi(sup,val.sup);
      }
      else if (val.sup<0) {
        erg.inf=mul_lo(sup,val.inf);
        erg.sup=mul_hi(inf,val.sup);
      }
      else {
        erg.inf=mul_lo(sup,val.inf);
        erg.sup=mul_hi(sup,val.sup);
      }
    }
    else if (sup<0) {
      if (val.inf>0) {
        erg.inf=mul_lo(inf,val.sup);
        erg.sup=mul_hi(sup,val.inf);
      }
      else if (val.sup<0) {
        erg.inf=mul_lo(sup,val.sup);
        erg.sup=mul_hi(inf,val.inf);
      }
      else {
        erg.inf=mul_lo(inf,val.sup);
        erg.sup=mul_hi(inf,val.inf);
      }
    }
    else {
      if (val.inf>0) {
        erg.inf=mul_lo(inf,val.sup);
        erg.sup=mul_hi(sup,val.sup);
      }
      else if (val.sup<0) {
        erg.inf=mul_lo(sup,val.inf);
        erg.sup=mul_hi(inf,val.inf);
      }
      else {
        double inf1=mul_lo(inf,val.sup);
        double sup1=mul_hi(sup,val.sup);
        double inf2=mul_lo(sup,val.inf);
        double sup2=mul_hi(inf,val.inf);
        erg.inf=(inf1<inf2)?inf1:inf2;
        erg.sup=(sup1>sup2)?sup1:sup2;
      }
    }
    return erg;
  }
  
  
  // ===========
  // VI DIVISION
  // ===========
  // Abkuerzungen fuer die Division
  private double div_lo(double x,double y) {
    double res=DownOps.quotient(x,y);
    if (Double.isNaN(res))
      return Double.NEGATIVE_INFINITY;
    return res;
  }
  
  private double div_hi(double x,double y) {
    double res=UpOps.quotient(x,y);
    if (Double.isNaN(res))
      return Double.POSITIVE_INFINITY;
    return res;
  }
  
  /** Liefert das Ergebnis der erweiterten Intervalldivision
   <code>this/val</code>. Das Array besteht immer aus genau zwei Elementen.
   */
  public Interval[] xDivide(Interval val) {
    Interval res[]=new Interval[2];
    res[0]=new Interval();
    res[1]=new Interval();
    if (empty || val.empty) { // Ist eines der Intervalle leer?
      res[0].empty=true;
      res[1].empty=true;
      return res;
    }
    double infa=inf,supa=sup,infb=val.inf,supb=val.sup; // zur besseren
    double pINF=Double.POSITIVE_INFINITY;       // Lesbarkeit ein paar
    double mINF=Double.NEGATIVE_INFINITY;       // Abkuerzungen
    if (((Double.isInfinite(infa) || Double.isInfinite(supa)) &&
         (Double.isInfinite(infb) || Double.isInfinite(supb))) ||
        (infa<=0 && 0<=supa && infb<=0 && 0<=supb) ||
        (infa==mINF && supa==pINF) ||
        (infb==mINF && supb==pINF)) { // das ganze Intervall zum Ergebnis
      res[0].inf=mINF;
      res[0].sup=pINF;
      res[1].empty=true;
      return res;
    }
    if (infa>0 && infb>0 && supb<pINF) {
      res[0].inf=div_lo(infa,supb);
      res[0].sup=div_hi(supa,infb);
      res[1].empty=true;
    }
    else if(supa<0 && infb>0 && supb<pINF) {
      res[0].inf=div_lo(infa,infb);
      res[0].sup=div_hi(supa,supb);
      res[1].empty=true;
    }
    else if (infa<=0 && 0<=supa && infb>0) {
      res[0].inf=div_lo(infa,infb);
      res[0].sup=div_hi(supa,infb);
      res[1].empty=true;
    }
    else if ((infa>0 && supb<0 && infb==mINF)||(infa>0 && infb>0 && supb==pINF)) {
      res[0].inf=div_lo(supa,supb);
      res[0].sup=div_hi(supa,infb);
      res[1].empty=true;
    }
    else if ((supa<0 && supb<0 && infb==mINF)||(supa<0 && infb>0 && supb==pINF)) {
      res[0].inf=div_lo(infa,infb);
      res[0].sup=div_hi(infa,supb);
      res[1].empty=true;
    }
    else if (infa>0 && supb<0 && infb>mINF) {
      res[0].inf=div_lo(supa,supb);
      res[0].sup=div_hi(infa,infb);
      res[1].empty=true;
    }
    else if (supa<0 && supb<0 && infb>mINF) {
      res[0].inf=div_lo(supa,infb);
      res[0].sup=div_hi(infa,supb);
      res[1].empty=true;
    }
    else if (infa<=0 && 0<=supa && supb<0) {
      res[0].inf=div_lo(supa,supb);
      res[0].sup=div_hi(infa,supb);
      res[1].empty=true;
    }
    else if ((infa>0 || supa<0) && infb==0 && supb==0) {
      res[0].inf=res[0].sup=mINF;
      res[1].inf=res[1].sup=pINF;
    }
    else if (infa>0 && infb<0 && supb==0) {
      res[0].inf=mINF;
      res[0].sup=div_hi(infa,infb);
      res[1].inf=pINF;;
      res[1].sup=pINF;
    }
    else if (supa<0 && infb<0 && supb==0) {
      res[0].inf=mINF;
      res[0].sup=mINF;
      res[1].inf=div_lo(supa,infb);;
      res[1].sup=pINF;
    }
    else if (infa>0 && infb==0 && 0<supb) {
      res[0].inf=mINF;
      res[0].sup=mINF;
      res[1].inf=div_lo(infa,supb);;
      res[1].sup=pINF;
    }
    else if (supa<0 && infb==0 && 0<supb) {
      res[0].inf=mINF;
      res[0].sup=div_hi(supa,supb);
      res[1].inf=pINF;
      res[1].sup=pINF;
    }
    else if (infa>0 && infb<0 && 0<supb) {
      res[0].inf=mINF;
      res[0].sup=div_hi(infa,infb);
      res[1].inf=div_lo(infa,supb);;
      res[1].sup=pINF;
    }
    else if (supa<0 && infb<0 && 0<supb) {
      res[0].inf=mINF;
      res[0].sup=div_hi(supa,supb);
      res[1].inf=div_lo(supa,infb);;
      res[1].sup=pINF;
    }
    return res;
  }
  
  /** Liefert das Ergebnis der einfachen Intervalldivision
   <code>this/val</code>. */
  public Interval divide(Interval val) {
    Interval erg[]=xDivide(val);
    return erg[0].hull(erg[1]);
  }
  
  
  
  // ========================
  // VII. INTERVALLVERGLEICHE
  // ========================
  /** Testet zwei Intervalle auf Mengengleichheit. */
  public boolean equals(Interval val) {
    if (empty || val.empty) return (empty && val.empty);
    return (inf==val.inf && sup==val.sup);
  }
  
  /** Testet, ob <code>this</code> Teilmenge von <code>val</code> ist. */
  public boolean subset(Interval val) {
    if (empty)
      return true;
    else
      if (val.empty)
        return false;
      else
        return (inf>=val.inf && sup<=val.sup);
  }
  
  /** Testet, ob <code>this</code> echte Teilmenge von <code>val</code> ist */
  public boolean properSubset(Interval val) {
    return subset(val) && !equals(val);
  }

  /** Testet, ob <code>this</code> im Inneren von <code>val</code> liegt */
  public boolean isIn(Interval val) {
    if (empty)
      return true;
    if (val.empty)
      return false;
    return inf>val.inf && sup<val.sup;
  }
  
  /**Testet, ob <code>this</code> und <code>val</code> disjunkt sind */
  public boolean disjoint(Interval val) {
    if (empty || val.empty)
      return true;
    else
      return !(inf<=val.sup && sup>=val.inf);
  }
  
  /**Testet, ob <code>this</code> einen bestimmte Zahl <code>val</code>
   enth&auml;lt */
  public boolean contains(double val) {
    if (empty)
      return false;
    else
      return (inf<=val && val<=sup);
  }
  


  // ========================
  // VIII. STANDARDFUNKTIONEN
  // ========================
  /** Liefert den Mittelpunkt eines endlichen Intervalls. Ist
   <code>this</code> nicht endlich oder leer, liefert die Funktion
   <code>NaN</code> zur&uuml;ck.*/
  public double mid() {
    if (empty || Double.isInfinite(inf) || Double.isInfinite(sup))
      return Double.NaN;
    if (Double.isInfinite(DownOps.summe(inf,sup)) ||
        Double.isInfinite(UpOps.summe(inf,sup)))
      return (inf/2)+(sup/2);
    return (inf+sup)/2;
  }

  /** Liefert eine Obergrenze f&uuml;r den Radius eines endlichen Intervalls.
   Ist <code>this</code> nicht endlich oder leer, liefert die Funktion
   <code>NaN</code> zur&uuml;ck.*/   
  public double rad() {
    if (empty || Double.isInfinite(inf) || Double.isInfinite(sup))
      return Double.NaN;
    double rad2=UpOps.differenz(sup,inf);
    if (Double.isInfinite(rad2))
      return UpOps.differenz(UpOps.quotient(sup,2),UpOps.quotient(inf,2));
    return UpOps.quotient(rad2,2);
  }

  /** Liefert eine Obergrenze f&uuml;r den Durchmesser eines endlichen
   Intervalls.
   Ist <code>this</code> nicht endlich oder leer, liefert die Funktion
   <code>NaN</code> zur&uuml;ck.*/   
  public double diam() {
    if (empty || Double.isInfinite(inf) || Double.isInfinite(sup))
      return Double.NaN;
    return UpOps.differenz(sup,inf);
  }

  /** Berechnet den Betrag des Intervalls <code>this</code>. Ist
   <code>this</code> das leere Intervall, so wird das leere Intervall
   zur&uuml;ckgegeben. */
  public Interval abs() {
    if (empty)
      return this;
    if (inf<=0 && 0<=sup)
      return new Interval(0,Math.max(-inf,sup));
    if (sup<=0)
      return new Interval(-sup,-inf);
    return this;
  }
  
  /** Liefert eine Obergrenze f&uuml;r den relativen Durchmesser eines
   endlichen Intervalls.
   Ist <code>this</code> nicht endlich oder leer, liefert die Funktion
   <code>NaN</code> zur&uuml;ck.*/   
  public double relDiam() {
    if (empty || Double.isInfinite(inf) || Double.isInfinite(sup))
      return Double.NaN;
    double minabs=abs().inf();
    double diam=UpOps.differenz(sup,inf);
    if (minabs==0)
      return diam;
    else
      return UpOps.quotient(diam,minabs);
  }

  // ========================
  // IX. POTENZFUNKTION
  // ========================
  /** Berechnet die n-te Potenz des Intervalls. Hierbei mu&szlig; n
   gr&ouml;&szlig;er als 0 sein -- andernfalls wird <code>null</code>
   zur&uuml;ckgegeben. */
  public Interval pow(int n) {
    if (empty)
      return this;
    if (n<1)
      return null;
    if (inf>0)
      return new Interval(DownOps.pow(inf,n),UpOps.pow(sup,n));
    else if (sup<0) {
      if (n%2==0)
        return new Interval(DownOps.pow(sup,n),UpOps.pow(inf,n));
      else
        return new Interval(DownOps.pow(inf,n),UpOps.pow(sup,n));
    }
    else {
      if (n%2==0)
        return new Interval(0,Math.max(UpOps.pow(inf,n),UpOps.pow(sup,n)));
      else
        return new Interval(DownOps.pow(inf,n),UpOps.pow(sup,n));
    }
  }

}
