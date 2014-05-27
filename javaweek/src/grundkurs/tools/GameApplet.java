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
import javax.swing.border.*;

/** Diese Klasse stellt eine grafische Oberfl&auml;che
 (inklusive Ablaufsteuerung) f&uuml;r Spiele dar. Das Spiel
 wird in einem Applet dargestellt, welches in einem Web-Browser
 dargestellt wird. Der Benutzer kann das Applet nicht beenden; er
 kann es jedoch re-initialisieren, indem er den Reset-Knopf drueckt. **/
public abstract class GameApplet extends JApplet {

  /** In dieser Methode wird das darzustellende GameModel erzeugt. */
  public abstract GameModel createModel();

  /** Diese Methode gibt die Beschriftung des Reset-Knopfes zur&uuml;ck.
   Der Standard-Name ist <CODE>Neues Spiel</CODE>. */
  public String getLabelOfResetButton() {return "Neues Spiel";}

  /** In diesem Panel wird die GUI gezeichnet */
  private JPanel content;

  /** Dies ist das aktuelle GamePanel */
  private GamePanel panel;

  /** Diese Methode startet das Applet */
  public final void start() {}
  
  /** Diese Methode initialisiert das Applet. Sie darf nicht
   &uuml;berschrieben werden. */
  public final void init() {
    // Initialisiere das allumfassende Panel
    content = new JPanel();
    content.setLayout(new BorderLayout());
    // Besorge ein Spielmodell
    GameModel model = createModel();
    // Setze den Spielnamen
    content.add("North",new JLabel(model.getGameName(),JLabel.CENTER));
    // Erzeuge den Reset-Knopf
    JButton reset = new JButton(getLabelOfResetButton());
    content.add("South", reset);
    // Erzeuge einen Listener fuer den Reset-Knopf
    reset.addActionListener
    (
     new ActionListener()
     {
       public void actionPerformed(ActionEvent e) {
         setGui(createModel());
         validate();
       }
     }
    );
    // Initialisiere das Spiel
    setGui(model);
    // Setze das ContentPane
    content.setBorder(new BevelBorder(BevelBorder.RAISED));
    getContentPane().add(content);
  }

  /** Initialisiert die grafische Oberfl&auml;che des Spiels */
  private void setGui(GameModel model) {
    if (panel != null) {
      content.remove(panel);
    }
    content.add("Center", panel = new GamePanel(model));
    panel.setBorder(new BevelBorder(BevelBorder.LOWERED));
  }

}
