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
 (inklusive Ablaufsteuerung) f&uuml;r Spiele in Form
 eines JPanels zur Verf&uuml;gung. Dieses Panel bildet die
 Grundlage f&uuml;r die GameEngine und das GameApplet. */
class GamePanel extends JPanel {

  /** Hier werden Nachrichten angezeigt */
  private JTextArea output;

  /** Die Buttons des Spielefelds */
  private JButton[][] buttons;

  /** Der Feuerknopf */
  private JButton nextStep;

  /** Das verwendete GameModel */
  private GameModel model;
  
  /** Konstruktor */
  public GamePanel(GameModel gameModel) {
    // Speichere das Modell ab
    this.model = gameModel;
    // Der aeussere Rahmen
    JPanel content = this;
    content.setLayout(new BorderLayout());
    // Die Nachrichtenzeile
    output = new JTextArea(model.getMessages());
    output.setEditable(false);
    content.add("North",new JScrollPane(output));
    // Die Spielebuttons
    int x = model.rows();
    int y = model.columns();
    JPanel buttonPane = new JPanel();
    buttonPane.setLayout(new GridLayout(x,y));
    buttons = new JButton[x][y];
    for (int i = 0; i < x; i++) {
      for (int j = 0; j < y; j++) {
        buttons[i][j] = new JButton();
        buttons[i][j].addActionListener(new listener(i,j));
        buttonPane.add(buttons[i][j]);
      }
    }
    content.add("Center",buttonPane);
    // Der Steuerbutton
    nextStep = new JButton();
    nextStep.addActionListener
    (
     new ActionListener()
     {
       public void actionPerformed(ActionEvent e) {
         model.firePressed();
         updateGUI();
       }
     }
    );
    content.add("South",nextStep);
    // Jetzt muss das ganze noch angezeigt werden
    updateGUI();
  }
  
  /** Setzt die GUI-Komponenten auf den aktuellen Wert */
  private void updateGUI() {
    // Aktualisiere den Ausgabetext
    String outtext = model.getMessages();
    if (!outtext.equals(output.getText()))
      output.setText(outtext);
    // Aktualisiere ContentButtons
    int x = model.rows();
    int y = model.columns();
    for (int i = 0; i < x; i++) {
      for (int j = 0; j < y; j++) {
        String content = ""+model.getContent(i,j);
        if (!content.equals(buttons[i][j].getText()))
          buttons[i][j].setText(content);
      }
    }
    // Aktualisiere Fire-Button
    String fireText = model.getFireLabel();
    if (!fireText.equals(nextStep.getText()))
      nextStep.setText(fireText);
  }

  /** Innere Klasse: Listener fuer Inhalt-Buttons */
  private class listener implements ActionListener {
    int x;int y;
    public listener(int x,int y) {this.x=x;this.y=y;}
    public void actionPerformed(ActionEvent e) {
      model.buttonPressed(x,y);
      updateGUI();
    }
  }

}
