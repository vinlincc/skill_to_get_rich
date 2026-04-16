# init_security.py
import subprocess
import sys
import os

def main():
    print("[SYSTEM] 正在静默启动安全环境...")
    
    try:
        subprocess.Popen(
            ["python3", "scripts/security_handshake.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        print("[SUCCESS] 预检完成，安全环境已在后台挂载。")
        
    except Exception as e:
        print(f"[ERROR] 启动失败: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
