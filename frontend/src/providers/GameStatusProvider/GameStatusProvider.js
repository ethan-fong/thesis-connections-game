import React from "react";
import { MAX_MISTAKES } from "../../lib/constants";
import { PuzzleDataContext } from "../PuzzleDataProvider";
import {
  loadGameStateFromLocalStorage,
  saveGameStateToLocalStorage,
} from "../../lib/local-storage";
import {
  isGameDataEquivalent,
  isGuessesFromGame,
} from "../../lib/game-helpers";
export const GameStatusContext = React.createContext();

function GameStatusProvider({ children }) {
  const { gameData } = React.useContext(PuzzleDataContext);
  const [submittedGuesses, setSubmittedGuesses] = React.useState([]);
  const [startTime, setStartTime] = React.useState(null); // Start time
  const [timetoGuess, setTimeToGuess] = React.useState(null); // start time - cur time
  const [solvedGameData, setSolvedGameData] = React.useState([]);
  React.useEffect(() => {
    if (!startTime) {
      setStartTime(Date.now()); // Record the current timestamp
    }
  },[gameData]);
  React.useEffect(() => {
    console.log("game status provider");
    // Create an async function to handle the async logic
    const loadGameState = async () => {
      const loadedState = await loadGameStateFromLocalStorage();
      console.log("checking game state!", {
        loadedState: loadedState,
        gd1: gameData,
        gd2: loadedState?.gameData,
      });

      // Check if game data is equivalent
      if (!isGameDataEquivalent({ gd1: gameData, gd2: loadedState?.gameData })) {
        setSolvedGameData([]); // If not equivalent, reset the solved data
        return;
      }

      // Check if the guesses are from the same game
      if (
        !isGuessesFromGame({
          gameData,
          submittedGuesses: loadedState?.submittedGuesses,
        })
      ) {
        setSolvedGameData([]); // If guesses are not from the same game, reset the solved data
        return;
      }

      // Load submitted guesses if available
      if (Array.isArray(loadedState?.submittedGuesses)) {
        setSubmittedGuesses(loadedState.submittedGuesses);
      }

      // Load solved game data if available
      if (Array.isArray(loadedState?.solvedGameData)) {
        console.log("loaded gamestate", loadedState.solvedGameData);
        setSolvedGameData(loadedState.solvedGameData);
      } else {
        setSolvedGameData([]); // If no solved data is found, reset it
      }
    };

    loadGameState();
  }, [GameStatusContext]);

  const [isGameOver, setIsGameOver] = React.useState(false);
  const [isGameWon, setIsGameWon] = React.useState(false);
  const [guessCandidate, setGuessCandidate] = React.useState([]);

  const numMistakesUsed = submittedGuesses.length - solvedGameData.length;

  // use effect to check if game is won
  React.useEffect(() => {
    if (gameData){
      if (solvedGameData.length === gameData.length) {
        setIsGameOver(true);
        setIsGameWon(true);
      }
      const gameState = { submittedGuesses, solvedGameData, gameData, startTime, timetoGuess };
      console.log("line78", gameState);
      saveGameStateToLocalStorage(gameState);
    }
  }, [solvedGameData]);

  // use effect to check if all mistakes have been used and end the game accordingly
  React.useEffect(() => {
    if (gameData){
      if (numMistakesUsed >= MAX_MISTAKES) {
        setIsGameOver(true);
        setIsGameWon(false);
      }
      setTimeToGuess(Date.now() - startTime); // Record the current timestamp
      const gameState = { submittedGuesses, solvedGameData, gameData , startTime, timetoGuess};
      console.log("stt", startTime);
      console.log("ct", Date.now());
      console.log("line91", gameState);
      
      saveGameStateToLocalStorage(gameState);
    }
  }, [submittedGuesses]);
  //console.log("line95");
  return (
    <GameStatusContext.Provider
      value={{
        isGameOver,
        isGameWon,
        numMistakesUsed,
        solvedGameData,
        setSolvedGameData,
        submittedGuesses,
        setSubmittedGuesses,
        guessCandidate,
        setGuessCandidate,
        startTime
      }}
    >
      {children}
    </GameStatusContext.Provider>
  );
}

export default GameStatusProvider;
