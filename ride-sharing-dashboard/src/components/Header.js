import React from 'react';
import '../styles/Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-top">
        <button className="menu-button">
          <span className="menu-icon">&#9776;</span> 
        </button>
        <span className="header-title">PDS</span>
        <div className="spacer"></div> 
      </div>
      <div className="header-search-signout">
        <div className="search-container">
          <input type="text" placeholder="Search" className="search-input"/>
        </div>
        <button className="sign-out-button">Sign out</button>
      </div>
    </header>
  );
};

export default Header;
