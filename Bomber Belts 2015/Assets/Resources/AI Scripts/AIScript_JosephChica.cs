using UnityEngine;
using System.Collections;
using System;

public class AIScript_JosephChica : MonoBehaviour {

    public CharacterScript mainScript;

    public float[] bombSpeeds;
    public float[] buttonCooldowns;
    public float playerSpeed;
    public int[] beltDirections;
    public float[] buttonLocations;

	// Use this for initialization
	void Start () {
        mainScript = GetComponent<CharacterScript>();

        if (mainScript == null)
        {
            print("No CharacterScript found on " + gameObject.name);
            this.enabled = false;
        }

        buttonLocations = mainScript.getButtonLocations();

        playerSpeed = mainScript.getPlayerSpeed();
	}

	// Update is called once per frame
	void Update () {

        buttonCooldowns = mainScript.getButtonCooldowns();
        beltDirections = mainScript.getBeltDirections();


        //Your AI code goes here
        float minDist = 1000;
        float[] heuristic = new float[8];
        int minH = 0;
        mainScript.moveUp();
        mainScript.push();

        for (int i = 0; i < 8; i++)
        {
            heuristic[i] = CalcH(mainScript, i);
            if(heuristic[i] < 0 && heuristic[i] < heuristic[minH])
            {
                minH = i;
            }
        }
        float myLoc = mainScript.getCharacterLocation();
        float[] buttonLocs = mainScript.getButtonLocations();
        print("My location: " + myLoc);
        print("Button location with min H " + buttonLocations[minH]);
        if(mainScript.getCharacterLocation() < buttonLocs[minH])
        {
            print("going down");
            mainScript.moveDown();
            mainScript.push();
        }
        else
        {
            print("going up");
            mainScript.moveUp();
            mainScript.push();
        }
    }

    private float CalcH(CharacterScript ms, int row)
    {
        float[] dist = ms.getBombDistances();
        float myLoc = ms.getCharacterLocation();
        float[] speeds = ms.getBombSpeeds();
        float[] buttonLocs = ms.getButtonLocations();
        beltDirections = ms.getBeltDirections();
        float opsLoc = ms.getOpponentLocation();
        float bombTime;
        float buttonTime;
        float timeLeft;

        if(beltDirections[row] == -1 || beltDirections[row] == 0)
        {
            bombTime = dist[row] / speeds[row];
            return bombTime;
            //print("speed: " + speeds[row]);
            //buttonTime = Math.Abs(myLoc - buttonLocs[row]) / ms.getPlayerSpeed();
            //timeLeft = bombTime - buttonTime;
            //return timeLeft;
        }

        else
        {
            return -1;
        }

        
        
    }
}
