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

import java.math.BigInteger;

/** Diese Klasse unterteilt eine double-Zahl in Mantisse, Vorzeichen
 und Exponent. Auf die einzelnen Komponenten soll ein direkter
 Zugriff moeglich sein. */
class IEEEZahl {

  /** Vorzeichenbit. ==0 heisst positiv, !=0 heisst negativ */
  public long vorzeichen;

  /** Mantisse inklusive fuehrender 1 */
  public BigInteger mantisse;

  /** Exponent */
  public long exponent;

  /** Die Zahl 0 als Konstante */
  public final static BigInteger zero=BigInteger.valueOf(0);

  /** Die Zahl 1 als Konstante */
  public final static BigInteger one=BigInteger.valueOf(1);

  /** Konstruktor */
  public IEEEZahl(double d) {
    // Wandle die Zahl um und speichere sie vorlaeufig in vorzeichen
    vorzeichen=Double.doubleToLongBits(d);
    // Charakteristik - es muessen das erste und die letzten 52 Zeichen weg
    exponent=vorzeichen & 0x7ff0000000000000L;   // Maske: 01111111111100000..
    // Mantisse - hier brauchen wir nur die letzten 52 Zeichen
    long mant=vorzeichen & 0x000fffffffffffffL;  // Maske: 00000000000011111..
    // Vorzeichen - nur das erste Bit zaehlt
    vorzeichen=vorzeichen & 0x8000000000000000L; // Maske: 10000000000000000..
    // Schiebe die Charakteristik zurecht
    exponent=exponent>>>52;
    // Schiebe das Vorzeichen zurecht
    vorzeichen=vorzeichen>>>63;
    // Fuege die fuehrende 1 in die Mantisse ein
    if (exponent>0)
      mant=mant | 0x0010000000000000L; // 00000000000100000000000...
    // Speichere die Mantisse als BigInteger ab
    mantisse=BigInteger.valueOf(mant);
    // Wandle die Charakteristik in den Exponenten um
    if (exponent==0)
      exponent=-1022-52;
    else
      exponent=exponent-1023-52;
  }

  /** Wandelt das Objekt in eine double-Zahl um und rundet dabei nach unten.
   Die Instanzvariablen werden hierbei veraendert. */
  public double toDouble() {
    // Einfachster Fall: mantisse==0
    if (mantisse.equals(zero))
      return 0;
    // alle anderen Faelle bedeuten Arbeit...
    long dummy; // Speicher fuer diverse Zwischenergebnisse
    // Sorge dafuer, dass es maximal 53 Ziffern !=1 gibt
    while (mantisse.bitLength()>53) {
      int diff=mantisse.bitLength()-53;   // So viele Bits sind zuviel
      BigInteger backup=mantisse;         // Sichere die alte Mantisse
      mantisse=mantisse.shiftRight(diff); // Schiebe die Mantisse zurecht
      exponent=exponent+diff;             // Korrigiere den Exponenten
      // Bei negativen Zahlen muessen wir noch die herausgeschobenen Bits
      // untersuchen:
      if (vorzeichen!=0) {
        // Betrachte herausgeschobene Bits
        backup=backup.xor(mantisse.shiftLeft(diff));
        // Sind diese ungleich 0, erhoehe die Mantisse um 1
        if (!backup.equals(zero)) {
          mantisse=mantisse.add(one);
        }
      }
    }
    // Sorge dafuer, dass die 53. Ziffer von links ==1 ist
    if (mantisse.bitLength()<53) {
      int diff=53-mantisse.bitLength();   // So viele Bits fehlen in der Mantisse
      mantisse=mantisse.shiftLeft(diff); // Schiebe die Mantisse zurecht
      exponent=exponent-diff;             // Korrigiere den Exponenten
    }
    // Fall: exponent-52<-1022-52
    if (exponent<-1126) {
      return (vorzeichen==0)?0:-Double.MIN_VALUE;
    }
    // Fall: -1022>exponent-52>=-1022-52
    if (exponent<-1074) {
      int diff=-1074-(int)exponent; // Um so viele Stellen muss geschoben werden
      BigInteger backup=mantisse; // Sichere die Mantisse
      mantisse=mantisse.shiftRight(diff); // Schiebe die Mantisse zurecht
      exponent=-1074;          // Korrigiere den Exponenten
      // Bei negativen Zahlen muessen wir noch die herausgeschobenen Bits
      // untersuchen:
      if (vorzeichen!=0) {
        // Betrachte herausgeschobene Bits
        backup=backup.xor(mantisse.shiftLeft(diff));
        // Sind diese ungleich 0, erhoehe die Mantisse um 1
        if (!backup.equals(zero))
          mantisse=mantisse.add(one);
      }
      // Besitzt die Ziffer nun weniger als 53 Stellen, gib das Ergebnis aus
      if (mantisse.bitLength()<53)
        return Double.
          longBitsToDouble((vorzeichen<<63) | mantisse.longValue());
    }
    // Fall: 1023>=exponent-52
    if (exponent<=971) {
      long mant=mantisse.longValue();
      // Schneide die fuehrende 1 ab
      mant=mant & 0x000fffffffffffffL;
      // Gib Ergebnis zurueck
      return Double.
        longBitsToDouble((vorzeichen<<63) | (exponent+1023+52<<52) | mant);
    }
    // Fall: exponent-52>1023
    return (vorzeichen==0)?Double.MAX_VALUE:Double.NEGATIVE_INFINITY;
  }

}
