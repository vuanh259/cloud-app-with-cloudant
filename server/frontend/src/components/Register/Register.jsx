import React, { useState } from 'react';
import './Register.css'; 

const Register = () => {
    // Đủ 5 trường thông tin cấu trúc đúng chuẩn đề bài
    const [formData, setFormData] = useState({
        username: '',
        firstName: '',
        lastName: '',
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleRegister = async (e) => {
        e.preventDefault();
        // Logic gọi API Django Đăng ký ở đây...
        console.log("Submitting Register Form: ", formData);
    };

    return (
        <div class="register-container">
            <h2>Sign-up</h2>
            <form onSubmit={handleRegister}>
                <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
                <input type="text" name="firstName" placeholder="First Name" onChange={handleChange} required />
                <input type="text" name="lastName" placeholder="Last Name" onChange={handleChange} required />
                <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
                <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
                <button type="submit" className="btn-register">Register</button>
            </form>
        </div>
    );
};

export default Register;
