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
        float curDist;
        float[] heuristic = new float[8];
        int maxH = 0;

        for (int i = 0; i < 8; i++)
        {
            heuristic[i] = CalcH(mainScript, i);
            if(heuristic[i] > heuristic[maxH])
            {
                maxH = i;
            }
        }

        float myLoc = mainScript.getCharacterLocation();
        float[] buttonLocs = mainScript.getButtonLocations();
        if(myLoc > buttonLocs[maxH])
        {
            mainScript.moveUp();
            mainScript.push();
        }
        else
        {
            mainScript.moveDown();
            mainScript.push();
        }
        


    }

    private float CalcH(CharacterScript ms, int row)
    {
        float[] dist = ms.getBombDistances();
        float myLoc = ms.getCharacterLocation();
        float[] speeds = ms.getBombSpeeds();
        float[] buttonLocs = ms.getButtonLocations();

        float bombTime = dist[row] / speeds[row];
        float buttonTime = Math.Abs(myLoc - buttonLocs[row]) / ms.getPlayerSpeed();
        float timeLeft = bombTime - buttonTime;

        return timeLeft > 0 ? timeLeft : (timeLeft) * (-1);
        
       
    }


}
