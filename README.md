# 🚍 API EMT Madrid

A **Flask** web application that interacts with the **EMT Madrid API** to provide real-time bus arrival estimations.

## 📑 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## 📖 Introduction

**Buses 2.0** is a web application that allows users to check **bus arrival times** at specific stops in **Madrid**. The app communicates with the **EMT Madrid Open API** to fetch real-time estimations and displays them on a simple web interface.

## ✨ Features

- 🚏 **Check real-time bus arrival times** at any EMT Madrid bus stop.
- 🔗 **Integration with the EMT Madrid API** for accurate data.
- 🖥️ **Web-based interface** using Flask and Jinja templates.
- 📝 **Easy to deploy and configure**.

## ⚙️ Installation

### 1️⃣ Clone this repository

```sh
git clone https://github.com/jdelafarauna/API_EMT_Mad.git
cd API_EMT_Mad
```

### 2️⃣ Create a virtual environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Run the application

```sh
python app.py
```

The application will be available at **http://127.0.0.1:5000/**.

## 🚀 Usage

1. Open your browser and go to **http://127.0.0.1:5000/**.
2. Enter a **bus stop ID** and a **bus line number**.
3. Click **Submit** to get the estimated arrival time.

## ⚙️ Configuration

- The API requires an **Access Token** from EMT Madrid.
- Replace the `accessToken` inside the `consultar_emt` function with your actual **EMT API Key**:

  ```python
  headers = {
      'Accept': 'application/json',
      'accessToken': 'your-api-key-here'
  }
  ```

- If you don't have an API Key, register at the [EMT Madrid Developer Portal](https://opendata.emtmadrid.es/).

## 📦 Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/)

To install dependencies manually:

```sh
pip install flask requests
```

## 🛠 Troubleshooting

- If you get a **403 Forbidden** error, check if your **API Key** is valid.
- Ensure that the **bus stop ID** and **bus line number** are correct.
- If running in a virtual environment, make sure it's activated before running the app.
- Check the EMT Madrid API status on their [official website](https://opendata.emtmadrid.es/).

## 👨‍💻 Contributors

- **[@jdelafarauna](https://github.com/jdelafarauna)** - Original Creator

Want to contribute? Feel free to open an **issue** or submit a **pull request**!

## 📜 License

This project is licensed under the **MIT License**.
