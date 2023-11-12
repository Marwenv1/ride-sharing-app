import React from 'react';
import Header from './Header';
import Footer from './Footer';
import '../styles/Layout.css'; 

const Layout = ({ children }) => {
  return (
    <>
      <Header />
      <main className="main-layout">{children}</main>
      <Footer />
    </>
  );
};

export default Layout;
