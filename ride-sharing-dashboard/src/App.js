import React from 'react';
import CreateRide from './pages/CreateRide'; 
import Layout from './components/Layout';
import 'bootstrap/dist/css/bootstrap.min.css';


const App = () => {
  return (
    <Layout>
      <CreateRide />
    </Layout>
  );
};

export default App;
