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
 k&ouml;nnen von der GameEngine als Spiel dargestellt
 und gesteuert werden.
 */
public interface GameModel {

  /** Gibt die Anzahl der Zeilen des Spielbretts
   zur&uuml;ck. Die Anzahl darf sich im Laufe des
   Spieles nicht mehr ver&auml;ndern.
   */
  public int rows();

  /** Gibt die Anzahl der Spalten des Spielbretts
   zur&uuml;ck. Die Anzahl darf sich im Laufe des
   Spieles nicht mehr ver&auml;ndern.
   */
  public int columns();

  /** Gibt den Text zur&uuml;ck, der aktuell auf dem
   Feuer-Button stehen soll.
   */
  public String getFireLabel();

  /** Gibt den Text zur&uuml;ck, der in der aktuellen
   Runde im Meldefenster stehen soll.
   */
  public String getMessages();

  /** Gibt den Namen des Spieles als String zur&uuml;ck */
  public String getGameName();

  /** Gibt den aktuellen Inhalt eines bestimmten Feldes zur&uuml;ck
   @param row die Zeile, von 0 an gez&auml;hlt
   @param col die Zeile, von 0 an gez&auml;hlt
   */
  public char getContent(int row, int col);

  /** Signalisiert, dass ein bestimmter Button gedr&uuml;ckt wurde
   @param row die Zeile, von 0 an gez&auml;hlt
   @param col die Zeile, von 0 an gez&auml;hlt
   */
  public void buttonPressed(int row,int col);
  
  /** Signalisert, da&szlig; der Feuer-Button gedr&uuml;ckt wurde */
  public void firePressed();
  
}
