import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from "../Header";
import Game from "../Game";

import { Toaster } from "../ui/toaster";
import PuzzleDataProvider from "../../providers/PuzzleDataProvider";
import GameStatusProvider from "../../providers/GameStatusProvider";

function App() {
  return (
    <Router>
      <PuzzleDataProvider>
        <GameStatusProvider>
          <div className="wrapper">
            <Header />
            <Toaster />
            <Game />
            <Routes>
              <Route path="/game/:gameId" element={<PuzzleDataProvider />} />
              {/* Other routes */}
            </Routes>
          </div>
        </GameStatusProvider>
      </PuzzleDataProvider>
    </Router>
  );
}


export default App;
