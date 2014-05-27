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

import java.awt.*;

/** Diese Klasse bettet ein Canvas-Objekt in ein Fenster ein. */
class Chalkboard{

  private Frame f;
  private Canvas c;

  /** Erzeuge ein neues Fenster mit dem angegebenen Titel */
  public Chalkboard(Canvas c,String title) {
    f=new Frame(title);
    f.add(c);
    f.setSize(300,300);
    this.c=c;
  }

  /** Zeige das Fenster */
  public void show() {
    f.setVisible(true);
  }
    
  /** Blende das Fenster aus */
  public void hide() {
    f.setVisible(false);
  }

  /** Gib das gezeichnete Fenster als Objekt zur&uuml;ck */
  public Frame getFrame() {
    return f;
  }

  /** Gibt saemtliche verwendeten Resourcen frei. Sollte aufgerufen werden,
   wenn das Fenster nicht mehr gebraucht wird.*/
  public void dispose() {
    f.removeAll();
    f.setVisible(false);
    f.setEnabled(false);
    f.dispose();
    System.gc();
  }
}
