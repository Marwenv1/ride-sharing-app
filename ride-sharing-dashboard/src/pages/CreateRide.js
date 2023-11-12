import React, { useState } from 'react';
import axios from 'axios';
import TabNavigation from '../components/TabNavigation';

const CreateRide = () => {
  const apiURL = process.env.REACT_APP_API_URL;
  const [activeTab, setActiveTab] = useState('initial-info');
  const [formData, setFormData] = useState({
    client_name: '',
    phone_number: '',
    pickup_address: '',
    destination_address: '',
    pickup_time: '',
  });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await axios.post(`${apiURL}rides`, formData);
      alert('Ride registered successfully!');
      console.log(response.data);
    } catch (error) {
      setError('Failed to register the ride. Please try again.');
      console.error('Error registering ride:', error.response?.data || error.message);
    }
  };

  const renderTabContent = () => {
    switch (activeTab) {
      case 'initial-info':
        return (
          <form onSubmit={handleSubmit} className="needs-validation" noValidate>
            <div className="form-group">
              <label htmlFor="client_name">Client Name</label>
              <input
                type="text"
                className="form-control"
                id="client_name"
                name="client_name"
                value={formData.client_name}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="phone_number">Phone Number</label>
              <input
                type="tel"
                className="form-control"
                id="phone_number"
                name="phone_number"
                value={formData.phone_number}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="pickup_address">Pickup Address</label>
              <input
                type="text"
                className="form-control"
                id="pickup_address"
                name="pickup_address"
                value={formData.pickup_address}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="destination_address">Destination Address</label>
              <input
                type="text"
                className="form-control"
                id="destination_address"
                name="destination_address"
                value={formData.destination_address}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="pickup_time">Pickup Time</label>
              <input
                type="datetime-local"
                className="form-control"
                id="pickup_time"
                name="pickup_time"
                value={formData.pickup_time}
                onChange={handleChange}
                required
              />
            </div>
            <button type="submit" className="btn btn-primary">Register Ride</button>
            {error && <div className="alert alert-danger mt-3">{error}</div>}
          </form>
        );
      case 'ride-info':
        return <div>Ride Info Content</div>;
      case 'costs':
        return <div>Costs Content</div>;
      default:
        return null;
    }
  };

  return (
    <div className="container mt-5">
      <h2>Register a Ride</h2>
      <TabNavigation activeTab={activeTab} setActiveTab={setActiveTab} />
      {renderTabContent()}
    </div>
  );
};

export default CreateRide;