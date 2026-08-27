import subprocess
import json
import os
import sys

DRIVE_FOLDER_ID = "13VNtFHx_y-_jPkb130O7Yw-OCcYONeQF"
TARGET_DIR = "/home/ubuntu/skills/brunoairsoft-style/templates/drive_references"

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {e.stderr}")
        return None

def main():
    print(f"Iniciando sincronização da pasta do Drive: {DRIVE_FOLDER_ID}")
    
    abs_target_dir = os.path.abspath(TARGET_DIR)
    if not os.path.exists(abs_target_dir):
        os.makedirs(abs_target_dir)

    query = f"'{DRIVE_FOLDER_ID}' in parents and trashed = false"
    params = json.dumps({"q": query})
    list_cmd = ["gws", "drive", "files", "list", "--params", params, "--format", "json"]
    
    output = run_command(list_cmd)
    if not output:
        sys.exit(1)

    try:
        data = json.loads(output)
        files = data.get('files', [])
        
        if not files:
            print("Nenhum arquivo encontrado.")
            return

        print(f"Encontrados {len(files)} arquivos.")

        for file in files:
            file_id = file['id']
            file_name = file['name']
            if file['mimeType'] == 'application/vnd.google-apps.folder':
                continue
                
            dest_path = os.path.join(abs_target_dir, file_name)
            print(f"Baixando: {file_name}")
            
            # Método que funcionou: get com alt=media
            download_params = json.dumps({"fileId": file_id, "alt": "media"})
            download_cmd = ["gws", "drive", "files", "get", "--params", download_params, "--output", dest_path]
            run_command(download_cmd)
            
            if os.path.exists(dest_path):
                print(f"Sucesso: {file_name} ({os.path.getsize(dest_path)} bytes)")
            else:
                print(f"Falha: {file_name}")

        print("Sincronização concluída.")

    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
