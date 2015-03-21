//import java.awt.Color;
//import java.awt.Dimension;
//import java.awt.Graphics;
//import java.awt.Image;
import java.awt.*;
import java.awt.event.*;
//import java.awt.event.KeyAdapter;
//import java.awt.event.MouseAdapter;
//import java.awt.event.MouseEvent;

import javax.swing.JPanel;

public class GamePanel extends JPanel implements Runnable{
	private static final int PWIDTH = 500;
	private static final int PHEIGHT = 400;
	
	private Thread animator;
	private volatile boolean running = false;
	
	private volatile boolean gameOver = false;
	
	// global variables for off-screen rendering
	private Graphics dbg;
	private Image dbImage = null;
	
	
	public GamePanel(){
		setBackground(Color.white);
		setPreferredSize( new Dimension(PWIDTH, PHEIGHT));
		
		setFocusable(true);
		requestFocus(); //JPanel now receives key events
		readyForTermination();
		
		//create game components
		// ...
		
		//listen for mouse
		addMouseListener( new MouseAdapter() {
			public void mousePressed(MouseEvent e){
				testPress(e.getX(), e.getY());
			}
		});
	}
	
	private void readyForTermination(){
		addKeyListener( new KeyAdapter() {
			//listen for esc, q, end, ctrl-q
			public void keyPressed(KeyEvent e){
				int keyCode = e.getKeyCode();
				if ((keyCode == KeyEvent.VK_ESCAPE) ||
					(keyCode == KeyEvent.VK_Q) ||
					(keyCode == KeyEvent.VK_END) ||
					((keyCode == KeyEvent.VK_Q) && e.isControlDown()) ) {
					running = false;
				}
			}
		});
	}
	
	private void testPress(int x, int y){
		System.out.println("you've just clicked at (" + x + ", " + y + ")");
	}
	
	public void addNotify(){
	/*Wait for the JPanel to be added to the JFrame/JApplet
	 *before starting */	
		super.addNotify(); //create the peer
		startGame(); //Start thread
	}
	
	private void startGame(){
		//initialise and start the thread
		if (animator == null || !running){
			animator = new Thread(this);
			animator.start();
		}
	}

	public void stopGame()
	// called by the user to stop the game.
	{ running = false;}
	
	@Override
	public void run() {
		/* Repeatedly update, render, sleep */
		running = true;
		while(running){
			gameUpdate(); // game state is updated
			gameRender(); // render to a buffer
			paintScreen(); // paint with the buffer
		
			try {
				Thread.sleep(20); // sleep a bit
			}
			catch(InterruptedException ex){}
		}
		System.exit(0); // so that closing JFrame works
	}

	private void paintScreen(){
		//actively render the buffer image to the screen
		Graphics g;
		try{
			g = this.getGraphics(); // get the panel's current content
			if ((g != null) && (dbImage != null))
				g.drawImage(dbImage, 0, 0, null);
			Toolkit.getDefaultToolkit().sync();
			g.dispose();
		}
		catch (Exception e){
			System.out.println("Graphics context error: " + e);
		}
	}
	
	private void gameUpdate() {
		if (!gameOver){}
			//update game state9
			
	}
	
	private void gameRender() {
		//draw current frame to an image buffer
		if (dbImage == null){
			dbImage = createImage(PWIDTH, PHEIGHT);
			if (dbImage == null){
				System.out.println("dbImage is null");
				return;
			}
			else
				dbg = dbImage.getGraphics();
		}
		
		//clear the background
		dbg.setColor(Color.white);
		dbg.fillRect(0, 0, PWIDTH, PHEIGHT);
		
		//draw game elements
		// ...
		
		if (gameOver)
			gameOverMessage(dbg);
	}
	
	private void gameOverMessage(Graphics g){
		// center the game over message
		g.drawString("Game over man... Game over", PWIDTH/2, PHEIGHT/2);
	}
}
