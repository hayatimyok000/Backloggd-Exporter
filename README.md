

## 🌟 Features

### ⚡ Core Functionality
- 📊 **Multiple Export Formats** - CSV, JSON, or TXT
- 🎯 **Complete Library Extraction** - Get all your games with ratings
- 🔄 **Smart Pagination** - Automatically handles multi-page libraries
- 💾 **Custom Save Location** - Choose where to save your data

### 🎨 Interface
- 🟢 **Matrix Digital Rain** - Animated background with falling characters
- ✨ **Glitch Effects** - Dynamic text animations during processing
- 📟 **Live Monitor** - Real-time game extraction display
- 🖥️ **Console Log** - Colored terminal-style output with timestamps
- 🎭 **Hover Animations** - Smooth transitions on all interactive elements

### 🛡️ Technical
- 🚀 **Multi-threaded** - Non-blocking UI during scraping
- 🔒 **Error Handling** - Robust exception management
- ⏱️ **Rate Limiting** - Respectful delays between requests
- 📝 **UTF-8 Support** - Proper encoding for international characters

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/hayatim_yok/matrix-backloggd-exporter.git
cd matrix-backloggd-exporter
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python matrix_extractor.py
```

---

## 🎯 Usage

### Quick Start

1. **Launch the Application**
   ```bash
   python matrix_extractor.py
   ```

2. **Enter Your Backloggd Username**
   - Type your username in the `TARGET_USER` field

3. **Choose Export Settings**
   - **OUTPUT_FILE**: Name for your export file (default: `matrix_dump`)
   - **EXPORT_FORMAT**: Select CSV, JSON, or TXT
   - **DESTINATION_PATH**: Click to browse and select save location

4. **Execute**
   - Click `[ ▶ EXECUTE_SEQUENCE ]`
   - Watch the real-time extraction in the monitor
   - Your file will be saved when complete!

### Export Format Examples

#### CSV Format
```csv
Game,Rating
The Legend of Zelda: Breath of the Wild,5/5
Hollow Knight,4.5/5
Celeste,5/5
```

#### JSON Format
```json
[
  {
    "name": "The Legend of Zelda: Breath of the Wild",
    "rating": "5/5"
  },
  {
    "name": "Hollow Knight",
    "rating": "4.5/5"
  }
]
```

#### TXT Format
```
The Legend of Zelda: Breath of the Wild - 5/5
Hollow Knight - 4.5/5
Celeste - 5/5
```

---

## 📸 Screenshots

### Main Interface
*Matrix-themed UI with digital rain background*

### Live Extraction
*Real-time monitor showing game extraction progress*

### Console Output
*Color-coded terminal logs with timestamps*

---

## 🛠️ Technical Details

### Built With
- **tkinter** - GUI framework
- **requests** - HTTP library for web scraping
- **BeautifulSoup4** - HTML parsing
- **Threading** - Asynchronous processing

### Architecture
```
matrix_extractor.py
├── DigitalRain (Canvas Animation)
├── GlitchLabel (Text Effect Component)
└── MatrixScraperApp (Main Application)
    ├── UI Setup
    ├── Event Handlers
    └── Scraping Logic
```

### How It Works
1. Sends GET requests to Backloggd user pages
2. Parses HTML using BeautifulSoup
3. Extracts game names and ratings from card elements
4. Handles pagination automatically
5. Exports to chosen format with proper encoding

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Project**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contributions
- 🌐 Add more export formats (XML, Excel)
- 🎨 Additional themes or color schemes
- 📊 Statistics and analytics features
- 🌍 Multi-language support
- 🔍 Search and filter capabilities

---

## 📋 Requirements

```txt
requests>=2.31.0
beautifulsoup4>=4.12.0
```

---

## ⚠️ Disclaimer

This tool is for personal use only. Please respect Backloggd's terms of service and don't abuse the scraping functionality. Always use reasonable delays between requests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by the Matrix movie series
- Built for the Backloggd gaming community
- Special thanks to all contributors

---

## 📞 Contact

**hayatim_yok** - [@hayatim_yok](https://github.com/hayatim_yok)

Project Link: [https://github.com/hayatim_yok/matrix-backloggd-exporter](https://github.com/hayatim_yok/matrix-backloggd-exporter)

---

<div align="center">

**⭐ Star this repository if you find it useful! ⭐**

Made with ❤️ and ☕ by hayatim_yok


</div>
