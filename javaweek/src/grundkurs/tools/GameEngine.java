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

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

/** Diese Klasse stellt eine grafische Oberfl&auml;che
 (inklusive Ablaufsteuerung) f&uuml;r Spiele dar. Das Spiel
 wird in einem eigenen Fenster dargestellt. Schlie&szlig;t der
 Benutzer das Fenster, wird die Ausf&uuml;hrung des Programmes
 beendet. **/
public class GameEngine {

  /** Konstruktor */
  public GameEngine(GameModel gameModel) {
    // Der aeussere Rahmen
    JFrame theGame = new JFrame(gameModel.getGameName());
    theGame.setContentPane(new GamePanel(gameModel));
    theGame.addWindowListener
    (
     new WindowAdapter()
     {
       public void windowClosing(WindowEvent e){System.exit(0);}
     }
    );
    // Jetzt muss das ganze noch angezeigt werden
    theGame.pack();
    theGame.setVisible(true);
  }

}
