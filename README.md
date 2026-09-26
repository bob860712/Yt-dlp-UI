# 🌐 Multi-language Navigation / 多國語言導覽 / 多语言导航 / 多言語ナビゲーション / 다국어 네비게이션

[English](https://www.google.com/search?q=%2523english&utm_source=gemini) | [繁體中文](https://www.google.com/search?q=%2523%25E7%25B9%2581%25E9%25AB%2594%25E4%25B8%25AD%25E6%2596%2587&utm_source=gemini) | [简体中文](https://www.google.com/search?q=%2523%25E7%25AE%2580%25E4%25BD%2593%25E4%25B8%25AD%25E6%2596%2587&utm_source=gemini) | [日本語](https://www.google.com/search?q=%2523%25E6%2597%25A5%25E6%259C%25AC%25E8%25AA%259E&utm_source=gemini) | [한국어](https://www.google.com/search?q=%2523%25ED%2595%259C%25EA%25B5%25AD%25EC%2596%25B4&utm_source=gemini)

---

# yt-dlp Desktop Video Downloader

A lightweight, native Python desktop application (`tkinter`-based) for downloading videos and audio using `yt-dlp`. No web browser or server setup required!

## ✨ Features

* **Native Desktop UI**: Built with `tkinter`, runs instantly as a lightweight desktop app.
* **Multi-language Support**: Switch between English, Traditional Chinese, Simplified Chinese, Japanese, and Korean on the fly.
* **Custom Output Folder**: Select your destination folder before downloading; files save directly there.
* **Open Output Folder**: Easily open your target directory with a single click.
* **Subtitle Extraction**: Automatically detects and lets you choose official or auto-generated subtitles (`.srt`).
* **Core Auto-Update**: Check and update the `yt-dlp` core directly within the app.

## 🚀 Quick Start & Packaging

### For Regular Users

1. Download the pre-built `.exe` file directly from the **Releases** page.
2. Download `ffmpeg.exe` and place it in the same folder.

### For Developers (Source Code & Packaging)

1. Install dependencies:
```bash
pip install yt-dlp

```


2. Run the application:
```bash
python app_native.py

```


3. Package into a standalone `.exe`:
```bash
pyinstaller --noconsole --onefile app_native.py

```



---

# yt-dlp 桌面影音下載器

這是一個基於 Python 原生桌面介面 (`tkinter`) 開發的輕量級影音下載器，使用 `yt-dlp` 作為核心。不需啟動伺服器或開啟網頁瀏覽器，點擊即可秒開！

## ✨ 主要特色

* **純本地原生介面**：採用 `tkinter` 開發，輕量、穩定且執行快速。
* **多國語言切換**：支援繁體中文、簡體中文、英文、日文、韓文，隨選隨切。
* **自選儲存資料夾**：下載前自由指定目標資料夾，檔案完成後直接存入。
* **一鍵開啟資料夾**：提供專屬按鈕，下載完成後可直接打開檔案總管檢視。
* **字幕下載**：自動解析網頁並支援勾選官方或自動產生的原生字幕 (`.srt`)。
* **核心線上更新**：內建一鍵檢查並更新最新 `yt-dlp` 核心的功能。

## 🚀 快速開始與打包

### 一般使用者

1. 請至 **Release** 頁面下載打包好的 `.exe` 執行檔。
2. 請下載 `ffmpeg.exe` 至程式資料夾中。

### 開發者 / 源碼執行與打包

1. 安裝必要套件：
```bash
pip install yt-dlp

```


2. 執行程式：
```bash
python app_native.py

```


3. 打包成獨立執行檔 (`.exe`)：
```bash
pyinstaller --noconsole --onefile app_native.py

```



---

# yt-dlp 桌面影音下载器

这是一个基于 Python 原生桌面界面 (`tkinter`) 开发的轻量级影音下载器，使用 `yt-dlp` 作为核心。无需启动服务器或打开网页浏览器，点击即可秒开！

## ✨ 主要特色

* **纯本地原生界面**：采用 `tkinter` 开发，轻量、稳定且运行迅速。
* **多语言切换**：支持繁体中文、简体中文、英文、日文、韩文，随选随切。
* **自选保存文件夹**：下载前自由指定目标文件夹，文件完成后直接存入。
* **一键打开文件夹**：提供专属按钮，下载完成后可直接打开文件管理器查看。
* **字幕下载**：自动解析网页并支持勾选官方或自动生成的原生字幕 (`.srt`)。
* **核心在线更新**：内置一键检查并更新最新 `yt-dlp` 核心的功能。

## 🚀 快速开始与打包

### 普通用户

1. 请至 **Release** 页面下载打包好的 `.exe` 运行文件。
2. 请下载 `ffmpeg.exe` 至程序文件夹中。

### 开发者 / 源码运行与打包

1. 安装必要库：
```bash
pip install yt-dlp

```


2. 运行程序：
```bash
python app_native.py

```


3. 打包成独立可执行文件 (`.exe`)：
```bash
pyinstaller --noconsole --onefile app_native.py

```



---

# yt-dlp デスクトップ動画ダウンローダー

`yt-dlp` をコアに使用した、Python のネイティブデスクトップUI (`tkinter`) ベースの軽量な動画・音声ダウンローダーです。Webブラウザやサーバーの起動は不要で、すぐに起動して使用できます。

## ✨ 主な機能

* **ネイティブデスクトップUI**: `tkinter` を使用しており、軽量で高速に動作します。
* **多言語対応**: 英語、繁体字中国語、簡体字中国語、日本語、韓国語を簡単に切り替え可能です。
* **保存先フォルダの選択**: ダウンロード前に任意のフォルダを指定でき、完了後に直接保存されます。
* **出力フォルダを開く**: ボタン一つでエクスプローラー/Finderから保存先フォルダを開くことができます。
* **字幕のダウンロード**: 公式字幕や自動生成字幕 (`.srt`) を自動解析して選択・ダウンロードできます。
* **コアの自動アップデート**: アプリ内から直接 `yt-dlp` の最新コアを確認・更新できます。

## 🚀 クイックスタート & パッケージング

### 一般ユーザー向け

1. **Release** ページからビルド済みの `.exe` ファイルをダウンロードしてください。
2. `ffmpeg.exe` をダウンロードし、同じフォルダに配置してください。

### 開発者向け（ソースコード実行・パッケージング）

1. 依存関係のインストール:
```bash
pip install yt-dlp

```


2. アプリの実行:
```bash
python app_native.py

```


3. スタンドアロン実行ファイル (`.exe`) へのパッケージング:
```bash
pyinstaller --noconsole --onefile app_native.py

```



---

# yt-dlp 데스크톱 비디오 다운로더

`yt-dlp` 코어를 사용하는 Python 네이티브 데스크톱 인터페이스(`tkinter`) 기반의 경량 비디오 및 오디오 다운로더입니다. 웹 브라우저나 서버를 실행할 필요 없이 바로 실행할 수 있습니다.

## ✨ 주요 기능

* **네이티브 데스크톱 UI**: `tkinter`로 제작되어 가볍고 빠르게 실행됩니다.
* **다국어 지원**: 영어, 번체 중국어, 간체 중국어, 일본어, 한국어를 간편하게 전환할 수 있습니다.
* **저장 폴더 지정**: 다운로드 전 원하는 폴더를 지정하여 파일이 바로 저장되도록 합니다.
* **출력 폴더 열기**: 버튼 하나로 파일 탐색기/파인더에서 저장 폴더를 바로 열 수 있습니다.
* **자막 다운로드**: 공식 자막 또는 자동 생성 자막(`.srt`)을 자동으로 감지하고 선택하여 다운로드할 수 있습니다.
* **코어 온라인 업데이트**: 앱 내에서 직접 최신 `yt-dlp` 코어를 확인하고 업데이트할 수 있습니다.

## 🚀 빠른 시작 및 패키징

### 일반 사용자

1. **Release** 페이지에서 빌드된 `.exe` 파일을 다운로드하세요.
2. `ffmpeg.exe`를 다운로드하여 프로그램 폴더에 배치하세요.

### 개발자 / 소스 코드 실행 및 패키징

1. 필수 패키지 설치:
```bash
pip install yt-dlp

```


2. 프로그램 실행:
```bash
python app_native.py

```


3. 독립형 실행 파일(`.exe`)로 패키징:
```bash
pyinstaller --noconsole --onefile app_native.py

```