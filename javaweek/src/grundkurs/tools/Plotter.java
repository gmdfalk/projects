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
import java.awt.event.*;

/** Ein zweidimensionaler Funktionsplotter. Zu plottende Objekte
 m&uuml;ssen das Plottable-Interface implementieren */
public class Plotter {

  /** Anzahl der zu plottenden Zwischenpunkte */
  private final static int num=500;

  /** Dieses Canvas zeichnet die Funktion */
  private plot p;

  /** Einbettung in ein Fenster */
  private Chalkboard f;

  /** Erzeugt einen neuen Plot. */
  public Plotter(Plottable p,String title) {
    f=new Chalkboard(this.p=new plot(p,num),title);
    f.getFrame().addWindowListener(new WindowAdapter(){
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
  }

  /** Diese Methode ist aufzurufen, wenn der Plotter nicht mehr
   gebraucht wird. */
  public void dispose() {
    f.dispose();
    f=null;
  }

  /** Macht den Plot sichtbar oder unsichtbar.
   @param flag sichtbar=true, unsichtbar=false */
  public void setVisible(boolean flag) {
    if (flag) f.show(); else f.hide();
  }

  /** Macht das Koordinatensystem sichtbar oder unsichtbar.
   @param flag sichtbar=true, unsichtbar=false */
  public void showGrid(boolean flag) {
    p.showGrid=flag;
    p.repaint();
  }

  /** Legt fest, in welchen Zwischenabst&auml;nden Markierungen in das
   Gitter eingef&uuml;gt werden sollen.
   @param x Zwischenabst&auml;nde in x-Richtung
   @param y Zwischenabst&auml;nde in y-Richtung
   */
  public void adjustGrid(double x,double y) {
    p.bx=x;
    p.by=y;
  }

  /** Liefert die Zeichenfl&auml;che der Klasse. */
  public Canvas getCanvas() {
    return p;
  }

  /** Setzt die Anzahl der Zwischenpunkte, mit denen die Kurve gezeichnet
   werden soll. Je h&ouml;her die Anzahl der Zwischenpunkte, desto genauer
   die Zeichnung. Standardwert ist 500. */
  public void setNumOfPoints(int num) {
    p.num=num;
    p.repaint();
  }
  
  /** Zeichnet die Funktion neu. Diese Methode muss aufgerufen werden, falls
   Aenderungen am &uuml;bergebenen Plottable-Objekt vorgenommen wurden. */
  public void repaint() {
    p.repaint();
  }

  /** Diese innere Klasse erweitert die Canvas-Klasse. Mit ihr werden die
   Funktionen gezeichnet. */
  private class plot extends Canvas{

    public int num; // Anzahl der zu plottenden Zwischenpunkte
    public Plottable p; // zu plottende Funktion
    public boolean showGrid=false; // Gitter zeichnen?
    public double bx=1; // Breite des Rasters in x-Richtung
    public double by=1; // Breite des Rasters in y-Richtung

    public plot(Plottable p,int num) {
      this.p=p;
      this.num=num;
      setBackground(Color.black);
      setForeground(Color.white);
    }

    /** Hilfsmethode: Berechnet eine x-Koordinate im
      * relativen Koordinaten-System.
      **/
    private int getX(double xValue,double lx,double ux)
    {
      double dx=(ux-lx)/getSize().width;
      return (int)((xValue - lx) / dx);
    }

    /** Hilfsmethode: Berechnet eine y-Koordinate im
      * relativen Koordinaten-System.
      **/
    private int getY(double yValue,double ly,double uy)
    {
      double dy=(uy-ly)/getSize().height;
      return (int) ((uy - yValue) / dy);
    }    
    
    public void paint(Graphics g) {
      // Vorbereitende Massnahmen
      double[] x=new double[num];
      double[] y=new double[num];
      double lx,ly,ux,uy;
      ux=uy=-Double.MAX_VALUE;
      lx=ly=+Double.MAX_VALUE;
      double dt=(p.sup()-p.inf())/(num-1);
      double t=p.inf();
      for (int i=0;i<num;i++) {
        x[i]=p.x(t);
        y[i]=p.y(t);
        t+=dt;
        lx=Math.min(lx,x[i]);
        ly=Math.min(ly,y[i]);
        ux=Math.max(ux,x[i]);
        uy=Math.max(uy,y[i]);
      }
      // Sollen die Achsen gezeichnet werden?
      g.setColor(Color.gray);
      if (showGrid) {
        // Zeichne X-Linie
        g.drawLine(0,getY(0,ly,uy),getSize().width,getY(0,ly,uy));
        // Zeichne Y-Linie
        g.drawLine(getX(0,lx,ux),0,getX(0,lx,ux),getSize().height);
        // Zeichne das X-Gitter (links)
        for (double xG = 0; xG >= lx; xG-= bx)
          g.drawLine(getX(xG,lx,ux),getY(0,ly,uy)-5,getX(xG,lx,ux),getY(0,ly,uy)+5);
        // Zeichne das X-Gitter (rechts)
        for (double xG = 0; xG <= ux; xG+= bx)
          g.drawLine(getX(xG,lx,ux),getY(0,ly,uy)-5,getX(xG,lx,ux),getY(0,ly,uy)+5);        
        // Zeichne das Y-Gitter (unten)
        for (double yG = 0; yG >= ly; yG-= by)
          g.drawLine(getX(0,lx,ux)-5,getY(yG,ly,uy),getX(0,lx,ux)+5,getY(yG,ly,uy));
        // Zeichne das Y-Gitter (oben)
        for (double yG = 0; yG <= uy; yG+= by)
          g.drawLine(getX(0,lx,ux)-5,getY(yG,ly,uy),getX(0,lx,ux)+5,getY(yG,ly,uy));
      }
      // Zeichne den Graphen der Funktion
      g.setColor(Color.white);
      for (int i=1;i<num;i++) {
        g.drawLine(getX(x[i-1],lx,ux),
                   getY(y[i-1],ly,uy),
                   getX(x[i],lx,ux),
                   getY(y[i],ly,uy));
      }
    }
  }
}
