
# Version Control (Git + GitHub)

This file summarizes essential Git operations used in this project:  
👉 [GitHub Repo Link](https://github.com/asimkarki/Portfolio)

---

## 🛠 Initial Setup
1. **Install Git**: https://git-scm.com  
2. **Clone Repo**:  
   ```bash
   git clone https://github.com/asimkarki/Portfolio.git
   cd Portfolio
   ```

3. **Set Git Config** *(one-time)*:  
   ```bash
   git config --global user.name "Asim Karki"
   git config --global user.email "email"
   ```

---

## 🔁 Common Git Commands

### ✅ Check Status
```bash
git status
```

### ➕ Stage Changes
```bash
git add filename        # single file
git add .               # all changes
```

### 💬 Commit Changes
```bash
git commit -m "Initial Commit"
```

### ⬆️ Push to GitHub
```bash
git push origin main   
```

### ⬇️ Pull Updates
```bash
git pull origin main
```

---

## 🌿 Branching & Merging

### Create a New Branch
```bash
git checkout -b feature-branch
```

### Switch Branch
```bash
git checkout main
```

### Merge Branch into Main
```bash
git checkout main
git merge feature-branch
```

---

## ⚠️ Handle Merge Conflicts

1. Git shows conflict in files:
   ```
   <<<<<<< HEAD
   Your changes
   =======
   Incoming changes
   >>>>>>> feature-branch
   ```
2. Manually edit & resolve.
3. Mark as resolved:
   ```bash
   git add conflicted-file
   git commit
   ```

---

## 🧹 Clean Up Branch (after merge)
```bash
git branch -d feature-branch
```
