import os
import re
import sys
import json
import shutil
import platform
import subprocess
import threading
import zipfile
import urllib.request
import importlib
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# 設定使用者目錄，用於存放自主更新的 yt-dlp 模組
UPDATE_DIR = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'YtDlpUI_Data')
LIB_DIR = os.path.join(UPDATE_DIR, 'lib')

if os.path.exists(LIB_DIR) and LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)

import yt_dlp

# 五國語言完整字典
LANGS = {
    "zh-TW": {
        "title": "yt-dlp 影音下載器",
        "version": "yt-dlp 版本",
        "update_core": "更新核心",
        "url_label": "影音網址 (多個網址請換行):",
        "dir_label": "儲存資料夾:",
        "select_dir": "選擇",
        "open_dir": "開啟",
        "no_dir": "尚未選擇 (預設為當前程式資料夾)",
        "analyze_btn": "解析網址",
        "type_label": "下載類型:",
        "opt_video": "影片 (Video)",
        "opt_audio": "純音檔 (Audio)",
        "res_label": "畫質:",
        "fmt_label": "格式:",
        "audio_fmt_label": "音檔格式:",
        "sub_label": "原生字幕 (.srt):",
        "sub_tip": "請先點擊「解析網址」",
        "download_btn": "開始下載",
        "status_ready": "就緒",
        "checking": "檢查更新中...",
        "analyzing": "解析中...",
        "downloading": "正在下載...",
        "processing": "正在轉檔/合併...",
        "success": "下載完成！",
        "error": "發生錯誤",
        "alert_no_url": "請先輸入網址！",
        "alert_no_dir": "請先選擇儲存資料夾！",
        "alert_success": "下載成功！檔案已儲存至："
    },
    "zh-CN": {
        "title": "yt-dlp 影音下载器",
        "version": "yt-dlp 版本",
        "update_core": "更新核心",
        "url_label": "影音网址 (多个网址请换行):",
        "dir_label": "保存文件夹:",
        "select_dir": "选择",
        "open_dir": "打开",
        "no_dir": "未选择 (默认当前程序文件夹)",
        "analyze_btn": "解析网址",
        "type_label": "下载类型:",
        "opt_video": "视频 (Video)",
        "opt_audio": "纯音频 (Audio)",
        "res_label": "画质:",
        "fmt_label": "格式:",
        "audio_fmt_label": "音频格式:",
        "sub_label": "原生字幕 (.srt):",
        "sub_tip": "请先点击“解析网址”",
        "download_btn": "开始下载",
        "status_ready": "就绪",
        "checking": "检查更新中...",
        "analyzing": "解析中...",
        "downloading": "正在下载...",
        "processing": "正在转码/合并...",
        "success": "下载完成！",
        "error": "发生错误",
        "alert_no_url": "请先输入网址！",
        "alert_no_dir": "请先选择保存文件夹！",
        "alert_success": "下载成功！文件已保存至："
    },
    "en": {
        "title": "yt-dlp Video Downloader",
        "version": "yt-dlp Version",
        "update_core": "Update Core",
        "url_label": "Video URLs (one per line):",
        "dir_label": "Save Folder:",
        "select_dir": "Browse",
        "open_dir": "Open",
        "no_dir": "Not selected (defaults to app folder)",
        "analyze_btn": "Analyze URL",
        "type_label": "Type:",
        "opt_video": "Video",
        "opt_audio": "Audio Only",
        "res_label": "Quality:",
        "fmt_label": "Format:",
        "audio_fmt_label": "Audio Format:",
        "sub_label": "Native Subtitles (.srt):",
        "sub_tip": "Click \"Analyze URL\" first",
        "download_btn": "Start Download",
        "status_ready": "Ready",
        "checking": "Checking for updates...",
        "analyzing": "Analyzing...",
        "downloading": "Downloading...",
        "processing": "Processing/Merging...",
        "success": "Download completed!",
        "error": "Error",
        "alert_no_url": "Please enter URL(s) first!",
        "alert_no_dir": "Please select a save folder first!",
        "alert_success": "Download successful! Saved to: "
    },
    "ja": {
        "title": "yt-dlp 動画ダウンローダー",
        "version": "yt-dlp バージョン",
        "update_core": "コア更新",
        "url_label": "動画URL (1行に1つ):",
        "dir_label": "保存先:",
        "select_dir": "選択",
        "open_dir": "開く",
        "no_dir": "未選択 (デフォルト:アプリフォルダ)",
        "analyze_btn": "URL解析",
        "type_label": "種類:",
        "opt_video": "動画",
        "opt_audio": "音声のみ",
        "res_label": "画質:",
        "fmt_label": "形式:",
        "audio_fmt_label": "音声形式:",
        "sub_label": "字幕 (.srt):",
        "sub_tip": "先に「URL解析」をクリックしてください",
        "download_btn": "ダウンロード開始",
        "status_ready": "準備完了",
        "checking": "アップデート確認中...",
        "analyzing": "解析中...",
        "downloading": "ダウンロード中...",
        "processing": "処理/結合中...",
        "success": "ダウンロード完了！",
        "error": "エラー",
        "alert_no_url": "URLを入力してください！",
        "alert_no_dir": "保存先フォルダを選択してください！",
        "alert_success": "ダウンロード成功！保存先: "
    },
    "ko": {
        "title": "yt-dlp 비디오 다운로더",
        "version": "yt-dlp 버전",
        "update_core": "코어 업데이트",
        "url_label": "동영상 URL (줄바꿈으로 구분):",
        "dir_label": "저장 폴더:",
        "select_dir": "선택",
        "open_dir": "열기",
        "no_dir": "선택되지 않음 (기본 폴더)",
        "analyze_btn": "URL 분석",
        "type_label": "유형:",
        "opt_video": "비디오",
        "opt_audio": "오디오 전용",
        "res_label": "화질:",
        "fmt_label": "포맷:",
        "audio_fmt_label": "오디오 포맷:",
        "sub_label": "자막 (.srt):",
        "sub_tip": "'URL 분석'을 먼저 클릭하세요",
        "download_btn": "다운로드 시작",
        "status_ready": "준비됨",
        "checking": "업데이트 확인 중...",
        "analyzing": "분석 중...",
        "downloading": "다운로드 중...",
        "processing": "처리/병합 중...",
        "success": "다운로드 완료!",
        "error": "오류",
        "alert_no_url": "URL을 먼저 입력해주세요!",
        "alert_no_dir": "저장 폴더를 먼저 선택해주세요!",
        "alert_success": "다운로드 성공! 저장 위치: "
    }
}

def get_resource_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def parse_version(v_str):
    if not v_str:
        return (0,)
    clean_v = re.sub(r'[^0-9.]', '', v_str)
    try:
        return tuple(int(p) for p in clean_v.split('.') if p)
    except ValueError:
        return (0,)

class DownloaderApp:
    def __init__(self, root):
        self.root = root
        self.current_lang = "zh-TW"
        
        version_str = getattr(getattr(yt_dlp, 'version', None), '__version__', '未知')
        self.version_var = tk.StringVar(value=version_str)
        self.save_dir = ""
        self.sub_vars = {}

        self.setup_ui()
        self.update_texts()

    def t(self, key):
        return LANGS[self.current_lang].get(key, key)

    def setup_ui(self):
        self.root.title("yt-dlp Downloader")
        self.root.geometry("540x720")
        self.root.minsize(500, 680)
        
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 頂部：標題與語言切換
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))

        self.title_label = ttk.Label(top_frame, font=("Arial", 14, "bold"))
        self.title_label.pack(side=tk.LEFT)

        lang_frame = ttk.Frame(top_frame)
        lang_frame.pack(side=tk.RIGHT)
        
        ttk.Label(lang_frame, text="Lang:").pack(side=tk.LEFT, padx=2)
        self.lang_cb = ttk.Combobox(lang_frame, values=["zh-TW", "zh-CN", "en", "ja", "ko"], width=7, state="readonly")
        self.lang_cb.set("zh-TW")
        self.lang_cb.pack(side=tk.LEFT, padx=2)
        self.lang_cb.bind("<<ComboboxSelected>>", self.change_language)

        self.update_btn = ttk.Button(lang_frame, command=self.check_update)
        self.update_btn.pack(side=tk.LEFT, padx=5)

        # 核心版本顯示
        self.ver_label_widget = ttk.Label(main_frame, font=("Arial", 9), foreground="gray")
        self.ver_label_widget.pack(anchor=tk.W, pady=(0, 5))

        # 網址輸入區
        self.url_label = ttk.Label(main_frame, font=("Arial", 10, "bold"))
        self.url_label.pack(anchor=tk.W)
        
        self.url_text = tk.Text(main_frame, height=4, font=("Arial", 10))
        self.url_text.pack(fill=tk.X, pady=5)

        # 資料夾選擇與開啟區
        dir_frame = ttk.Frame(main_frame)
        dir_frame.pack(fill=tk.X, pady=5)
        
        self.dir_label = ttk.Label(dir_frame, font=("Arial", 10, "bold"))
        self.dir_label.pack(side=tk.LEFT)
        
        self.open_dir_btn = ttk.Button(dir_frame, command=self.open_output_directory)
        self.open_dir_btn.pack(side=tk.RIGHT, padx=2)

        self.select_dir_btn = ttk.Button(dir_frame, command=self.select_directory)
        self.select_dir_btn.pack(side=tk.RIGHT, padx=2)

        self.dir_path_label = ttk.Label(main_frame, font=("Arial", 9), foreground="blue")
        self.dir_path_label.pack(anchor=tk.W, pady=(0, 5))
        self.update_dir_label_text()

        # 解析按鈕
        self.analyze_btn = ttk.Button(main_frame, command=self.analyze_url)
        self.analyze_btn.pack(fill=tk.X, pady=5)

        # 設定選項區
        options_frame = ttk.LabelFrame(main_frame, padding=10)
        options_frame.pack(fill=tk.X, pady=5)

        # 類型
        type_frame = ttk.Frame(options_frame)
        type_frame.pack(fill=tk.X, pady=2)
        self.type_label = ttk.Label(type_frame)
        self.type_label.pack(side=tk.LEFT)
        
        self.type_var_combo = ttk.Combobox(type_frame, values=["video", "audio"], state="readonly", width=15)
        self.type_var_combo.pack(side=tk.RIGHT)
        self.type_var_combo.set("video")
        self.type_var_combo.bind("<<ComboboxSelected>>", self.toggle_type_event)

        # 畫質與格式
        self.res_frame = ttk.Frame(options_frame)
        self.res_frame.pack(fill=tk.X, pady=2)
        self.res_label = ttk.Label(self.res_frame, width=8)
        self.res_label.pack(side=tk.LEFT)
        self.res_cb = ttk.Combobox(self.res_frame, values=["best", "4320", "2160", "1440", "1080", "720", "480", "360"], width=12, state="readonly")
        self.res_cb.set("best")
        self.res_cb.pack(side=tk.LEFT, padx=5)

        self.fmt_label = ttk.Label(self.res_frame, width=6)
        self.fmt_label.pack(side=tk.LEFT)
        self.fmt_cb = ttk.Combobox(self.res_frame, values=["mp4", "mkv", "webm", "avi"], width=8, state="readonly")
        self.fmt_cb.set("mp4")
        self.fmt_cb.pack(side=tk.LEFT)

        # 音檔格式框架
        self.audio_frame = ttk.Frame(options_frame)
        self.audio_label = ttk.Label(self.audio_frame, width=10)
        self.audio_label.pack(side=tk.LEFT)
        self.audio_cb = ttk.Combobox(self.audio_frame, values=["mp3", "flac", "m4a", "wav", "aac", "ogg", "opus"], width=15, state="readonly")
        self.audio_cb.set("mp3")
        self.audio_cb.pack(side=tk.LEFT, padx=5)

        # 字幕區
        sub_frame = ttk.LabelFrame(main_frame, padding=10)
        sub_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.sub_label = ttk.Label(sub_frame)
        self.sub_label.pack(anchor=tk.W)

        self.sub_canvas = tk.Canvas(sub_frame, height=70)
        self.sub_scrollbar = ttk.Scrollbar(sub_frame, orient="vertical", command=self.sub_canvas.yview)
        self.sub_scrollable_frame = ttk.Frame(self.sub_canvas)

        self.sub_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.sub_canvas.configure(scrollregion=self.sub_canvas.bbox("all"))
        )
        self.sub_canvas.create_window((0, 0), window=self.sub_scrollable_frame, anchor="nw")
        self.sub_canvas.configure(yscrollcommand=self.sub_scrollbar.set)

        self.sub_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.sub_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.sub_tip_label = ttk.Label(self.sub_scrollable_frame, foreground="gray")
        self.sub_tip_label.pack(anchor=tk.W, pady=5)

        # 下載按鈕與進度條
        self.download_btn = ttk.Button(main_frame, command=self.start_download)
        self.download_btn.pack(fill=tk.X, pady=5)

        self.progress_bar = ttk.Progressbar(main_frame, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill=tk.X, pady=2)

        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.pack(anchor=tk.W)

    def change_language(self, event):
        self.current_lang = self.lang_cb.get()
        self.update_texts()

    def update_texts(self):
        t = self.t
        self.root.title(t("title"))
        self.title_label.config(text=t("title"))
        self.update_btn.config(text=t("update_core"))
        self.ver_label_widget.config(text=f"{t('version')}: {self.version_var.get()}")
        self.url_label.config(text=t("url_label"))
        self.dir_label.config(text=t("dir_label"))
        self.select_dir_btn.config(text=t("select_dir"))
        self.open_dir_btn.config(text=t("open_dir"))
        self.analyze_btn.config(text=t("analyze_btn"))
        self.type_label.config(text=t("type_label"))
        self.res_label.config(text=t("res_label"))
        self.fmt_label.config(text=t("fmt_label"))
        self.audio_label.config(text=t("audio_fmt_label"))
        self.sub_label.config(text=t("sub_label"))
        self.sub_tip_label.config(text=t("sub_tip"))
        self.download_btn.config(text=t("download_btn"))
        if not self.status_label.cget("text"):
            self.status_label.config(text=t("status_ready"))

    def update_dir_label_text(self):
        t = self.t
        if self.save_dir:
            self.dir_path_label.config(text=self.save_dir)
        else:
            self.dir_path_label.config(text=t("no_dir"))

    def select_directory(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.save_dir = dir_path
            self.update_dir_label_text()

    def open_output_directory(self):
        target = self.save_dir if self.save_dir and os.path.exists(self.save_dir) else os.getcwd()
        try:
            if platform.system() == "Windows":
                os.startfile(target)
            elif platform.system() == "Darwin":
                subprocess.run(["open", target])
            else:
                subprocess.run(["xdg-open", target])
        except Exception as e:
            messagebox.showerror("Error", f"無法開啟資料夾: {str(e)}")

    def toggle_type_event(self, event):
        val = self.type_var_combo.get()
        if val == "audio":
            self.res_frame.pack_forget()
            self.audio_frame.pack(fill=tk.X, pady=2)
        else:
            self.audio_frame.pack_forget()
            self.res_frame.pack(fill=tk.X, pady=2)

    def get_parsed_urls(self):
        raw = self.url_text.get("1.0", tk.END)
        lines = raw.split("\n")
        return [l.strip() for l in lines if l.strip()]

    def analyze_url(self):
        urls = self.get_parsed_urls()
        if not urls:
            messagebox.showwarning("Warning", self.t("alert_no_url"))
            return

        self.status_label.config(text=self.t("analyzing"))
        
        def task():
            ydl_opts = {'skip_download': True, 'quiet': True, 'no_warnings': True}
            manual_subs_map = {}
            auto_subs_map = {}
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    for url in urls:
                        info = ydl.extract_info(url, download=False)
                        for k, v in info.get('subtitles', {}).items():
                            if v: manual_subs_map[k] = f"Official: {v[0].get('name', k)} ({k})"
                        for k, v in info.get('automatic_captions', {}).items():
                            if v and not ('tlang=' in v[0].get('url', '')):
                                auto_subs_map[k] = f"Auto: {v[0].get('name', k)} ({k})"
                
                self.root.after(0, lambda: self.update_subtitles_ui(manual_subs_map, auto_subs_map))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", str(e)))

        threading.Thread(target=task, daemon=True).start()

    def update_subtitles_ui(self, manual, auto):
        for widget in self.sub_scrollable_frame.winfo_children():
            widget.destroy()

        self.sub_vars.clear()
        combined = {**manual, **auto}
        
        if not combined:
            lbl = ttk.Label(self.sub_scrollable_frame, text="No subtitles available")
            lbl.pack(anchor=tk.W)
            self.status_label.config(text=self.t("status_ready"))
            return

        for code, name in combined.items():
            var = tk.BooleanVar(value=False)
            self.sub_vars[code] = var
            chk = ttk.Checkbutton(self.sub_scrollable_frame, text=name, variable=var)
            chk.pack(anchor=tk.W)

        self.status_label.config(text=self.t("status_ready"))

    def check_update(self):
        self.status_label.config(text=self.t("checking"))
        def task():
            global yt_dlp
            try:
                req = urllib.request.Request("https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest", headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    data = json.loads(response.read().decode())
                latest_version = data.get('tag_name')
                current_version = getattr(getattr(yt_dlp, 'version', None), '__version__', '0')

                if parse_version(current_version) >= parse_version(latest_version):
                    self.root.after(0, lambda: messagebox.showinfo("Info", f"Already latest version ({current_version})"))
                    return

                whl_url = next(a['browser_download_url'] for a in data.get('assets', []) if a.get('name', '').endswith('.whl'))
                os.makedirs(LIB_DIR, exist_ok=True)
                whl_path = os.path.join(UPDATE_DIR, "latest.whl")
                urllib.request.urlretrieve(whl_url, whl_path)

                with zipfile.ZipFile(whl_path, 'r') as zip_ref:
                    zip_ref.extractall(LIB_DIR)
                if os.path.exists(whl_path): os.remove(whl_path)

                if LIB_DIR not in sys.path: sys.path.insert(0, LIB_DIR)
                for mod_name in list(sys.modules.keys()):
                    if mod_name == 'yt_dlp' or mod_name.startswith('yt_dlp.'):
                        del sys.modules[mod_name]
                yt_dlp = importlib.import_module('yt_dlp')
                new_ver = getattr(getattr(yt_dlp, 'version', None), '__version__', '未知')
                self.version_var.set(new_ver)
                self.root.after(0, lambda: messagebox.showinfo("Info", f"Updated successfully to {new_ver}"))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
            finally:
                self.root.after(0, lambda: self.status_label.config(text=self.t("status_ready")))

        threading.Thread(target=task, daemon=True).start()

    def start_download(self):
        urls = self.get_parsed_urls()
        if not urls:
            messagebox.showwarning("Warning", self.t("alert_no_url"))
            return
        if not self.save_dir:
            messagebox.showwarning("Warning", self.t("alert_no_dir"))
            return

        selected_subs = [code for code, var in self.sub_vars.items() if var.get()]
        dl_type = self.type_var_combo.get()
        resolution = self.res_cb.get()
        video_format = self.fmt_cb.get()
        audio_format = self.audio_cb.get()

        payload = {
            "urls": urls,
            "type": dl_type,
            "resolution": resolution,
            "videoFormat": video_format,
            "audioFormat": audio_format,
            "selectedSubs": selected_subs,
            "saveDir": self.save_dir
        }

        self.download_btn.config(state=tk.DISABLED)
        self.progress_bar['value'] = 0

        threading.Thread(target=self.run_download_task, args=(payload,), daemon=True).start()

    def run_download_task(self, payload):
        urls = payload["urls"]
        dl_type = payload["type"]
        resolution = payload["resolution"]
        video_format = payload["videoFormat"]
        audio_format = payload["audioFormat"]
        selected_subs = payload["selectedSubs"]
        save_dir = payload["saveDir"]
        resource_dir = get_resource_path()

        total_urls = len(urls)
        failed_count = 0

        for idx, single_url in enumerate(urls, 1):
            def progress_hook(d):
                if d['status'] == 'downloading':
                    downloaded = d.get('downloaded_bytes', 0)
                    total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                    sub_percent = (downloaded / total) if total > 0 else 0
                    overall_percent = ((idx - 1 + sub_percent) / total_urls) * 100
                    self.root.after(0, lambda: self.update_progress(overall_percent, f"{self.t('downloading')} ({idx}/{total_urls})"))
                elif d['status'] == 'finished':
                    self.root.after(0, lambda: self.update_progress((idx / total_urls) * 100, f"{self.t('processing')}"))

            ydl_opts = {
                'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_hook],
                'ffmpeg_location': resource_dir,
                'quiet': True,
                'no_warnings': True
            }

            if selected_subs:
                ydl_opts.update({
                    'writesubtitles': True,
                    'writeautomaticsub': True,
                    'subtitleslangs': selected_subs,
                    'convertsubtitles': 'srt'
                })

            if dl_type == 'audio':
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': audio_format, 'preferredquality': '192'}],
                })
            else:
                ydl_opts['merge_output_format'] = video_format
                if resolution == 'best':
                    ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best'
                else:
                    ydl_opts['format'] = f"bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]/best"

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([single_url])
            except Exception:
                failed_count += 1

        self.root.after(0, lambda: self.download_finished(save_dir))

    def update_progress(self, percent, msg):
        self.progress_bar['value'] = percent
        self.status_label.config(text=msg)

    def download_finished(self, save_dir):
        self.download_btn.config(state=tk.NORMAL)
        self.progress_bar['value'] = 100
        self.status_label.config(text=self.t("success"))
        messagebox.showinfo("Success", f"{self.t('alert_success')}\n{save_dir}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DownloaderApp(root)
    root.mainloop()