import React from 'react';
import '../styles/TabNavigation.css';

const TabNavigation = ({ activeTab, setActiveTab }) => {
  return (
    <div className="tab-navigation">
      <button 
        onClick={() => setActiveTab('initial-info')} 
        className={`tab ${activeTab === 'initial-info' ? 'active' : ''}`}
      >
        Initial info
      </button>
      <button 
        onClick={() => setActiveTab('ride-info')} 
        className={`tab ${activeTab === 'ride-info' ? 'active' : ''}`}
      >
        Ride info
      </button>
      <button 
        onClick={() => setActiveTab('costs')} 
        className={`tab ${activeTab === 'costs' ? 'active' : ''}`}
      >
        Costs
      </button>
    </div>
  );
};

export default TabNavigation;
