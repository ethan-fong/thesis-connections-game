import React from "react";

import InfoModal from "../modals/InfoModal";
import STATIC_GAME_HEADER from "../../../public/static/sample_game_1.json";

function Header() {
  const header_name = STATIC_GAME_HEADER.title;
  const header_author = STATIC_GAME_HEADER.header_author;
  console.log("header name", header_name)
  return (
    <header>
      <h1 className="font-space-mono">{header_name}</h1>
      <InfoModal />
    </header>
  );
}

export default Header;
