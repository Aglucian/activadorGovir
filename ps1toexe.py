import subprocess

def run_ps1_script():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "activar_windows.ps1"])

if __name__ == "__main__":
    run_ps1_script()
