# Google Sheets MD5 Hasher (Python)

This script reads values from **Column A and Column B** of a Google Sheet and writes their **MD5 hashes** into **Column C and Column D** respectively.

---

## 📌 Features

* Reads all rows from a Google Sheet
* Generates MD5 hash for:

  * Column A → Column C
  * Column B → Column D
* Skips empty cells safely
* Uses **Google Service Account** authentication

---

## 🛠 Requirements

* Python 3.8+
* Google Cloud Service Account
* Google Sheets API enabled

### Python Libraries

```bash
pip install gspread google-auth
```

---

## 🔐 Google Service Account Setup

1. Go to **Google Cloud Console**
2. Create a project
3. Enable **Google Sheets API**
4. Create a **Service Account**
5. Download `credentials.json`
6. Share your Google Sheet with the service account email
   *(Editor access)*

---

## 📂 Project Structure

```
project/
│── credentials.json
│── md5_sheet.py
│── README.md
```

---

## 🚀 Usage

Update the following values in the script:

```python
sheet_id="SheetID_here"
sheet_name="Sheet1"
```

Run the script:

```bash
python md5_sheet.py
```

---

## 📊 How It Works

| Input Column | Output Column |
| ------------ | ------------- |
| A            | C (MD5 Hash)  |
| B            | D (MD5 Hash)  |

Empty cells remain empty.

---

## 🧪 Example

**Input**

```
A: hello
B: world
```

**Output**

```
C: 5d41402abc4b2a76b9719d911017c592
D: 7d793037a0760186574b0282f2f435e7
```

---

## ⚠️ Notes

* MD5 is **not secure** for passwords
* Use only for **data comparison / deduplication**
* Do not commit `credentials.json` to GitHub

---

## 📄 License

Free to use for internal and educational purposes.
