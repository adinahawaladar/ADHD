const express = require("express");
const multer = require("multer");
const cors = require("cors");
const fs = require("fs");
const path = require("path");
const axios = require("axios");

const app = express();
const upload = multer({ dest: "uploads/" });

app.use(cors());
app.use(express.json());

const GEMINI_API_KEY = "AIzaSyDMLDnw4Q4EjGip5EFoveTqfZkZK5a8P80"; // Replace with your Gemini API key
const GEMINI_API_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${GEMINI_API_KEY}`;

// Endpoint to upload file
app.post("/upload", upload.single("file"), (req, res) => {
    const filePath = req.file.path;
    const fileContent = fs.readFileSync(filePath, "utf8");

    // Parse user info
    const userInfo = {};
    fileContent.split("\n").forEach(line => {
        const [key, value] = line.split(":");
        if (key && value) userInfo[key.trim().toLowerCase()] = value.trim();
    });

    // Delete the file after reading
    fs.unlinkSync(filePath);

    res.json({ success: true, userInfo });
});

// Endpoint to chat with Gemini API
app.post("/chat", async (req, res) => {
    const { userInfo, message } = req.body;

    const prompt = `You are an ADHD Focus Helper. The user is a ${userInfo.age}-year-old ${userInfo.gender} with ${userInfo.stage} ADHD. They said: "${message}". Provide a helpful response.`;

    try {
        const response = await axios.post(GEMINI_API_URL, {
            contents: [{ parts: [{ text: prompt }] }],
        });

        const botMessage = response.data.candidates[0].content.parts[0].text;
        res.json({ success: true, botMessage });
    } catch (error) {
        console.error("Error calling Gemini API:", error);
        res.status(500).json({ success: false, error: "Failed to generate response" });
    }
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});