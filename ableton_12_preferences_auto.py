import shutil
import os
import subprocess

# Caminhos para diferentes arquivos de configuração
live_recording_prefs = "/Users/lucasvictorino/Library/Preferences/Ableton/Live 12.1/Preferences_Alternativas/Preferences_LiveRecording.cfg"
studio_production_prefs = "/Users/lucasvictorino/Library/Preferences/Ableton/Live 12.1/Preferences_Alternativas/Preferences_StudioProduction.cfg"
default_prefs = "/Users/lucasvictorino/Library/Preferences/Ableton/Live 12.1/Preferences_Alternativas/Preferences_Default.cfg"

# Caminho para a pasta de preferências ativa do Ableton
preferences_destination = "/Users/lucasvictorino/Library/Preferences/Ableton/Live 12.1/Preferences.cfg"

# Função para selecionar as preferências e copiar para o destino
def set_preferences(prefs_file):
    try:
        # Substitui as preferências atuais pelo arquivo selecionado
        shutil.copy(prefs_file, preferences_destination)
        print(f"Configurações carregadas de: {prefs_file}")
        
        # Abre o Ableton Live após restaurar as preferências
        subprocess.call(["open", "-a", "Ableton Live 12 Suite"])
    except Exception as e:
        print(f"Erro ao aplicar configurações: {e}")

# Menu para escolher qual configuração carregar
print("Selecione o setup de preferências para carregar:")
print("1. Gravação ao Vivo (Live Recording)")
print("2. Produção em Estúdio (Studio Production)")
print("3. Padrão (Default)")

choice = input("Digite o número da opção: ")

if choice == '1':
    set_preferences(live_recording_prefs)
elif choice == '2':
    set_preferences(studio_production_prefs)
elif choice == '3':
    set_preferences(default_prefs)
else:
    print("Opção inválida. Saindo...")
