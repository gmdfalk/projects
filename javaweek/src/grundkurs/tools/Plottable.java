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

/** Klassen, die dieses Interface implementieren,
 k&ouml;nnen mit dem Funktionsplotter gezeichnet
 werden. Kurvenpunkte werden bez&uuml;glich
 der X- und Y-Koordinate eines bestimmten
 Parameterbereichs angegeben. */
public interface Plottable {

  /** Ab diesem Wert beginnt der Parameterbereich */
  public double inf();

  /** Bis zu diesem Wert geht der Parameterbereich */
  public double sup();

  /** X-Koordinate x(t) zum Parameter t aus [inf,sup] */
  public double x(double t);

  /** Y-Koordinate y(t) zum Parameter t aus [inf,sup] */
  public double y(double t);

}
