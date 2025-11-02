import pyautogui
import time
import sys

print('** Rastreador de Coordenadas (X, Y) **')
print('Mova o mouse para a posição desejada.')
print('Pressione CTRL+C para sair.')
print('-' * 40)

try:
    # Loop principal para rastrear a posição do mouse continuamente
    while True:
        # Pega a posição atual do mouse
        x, y = pyautogui.position()
        
        # Cria a string de posição
        posicao_str = f'X: {str(x).rjust(4)} | Y: {str(y).rjust(4)}'
        
        # Imprime no terminal, sobrescrevendo a linha anterior (para manter o visual limpo)
        print(posicao_str, end='\r', flush=True) 
        
        # Pausa um pouco para evitar sobrecarregar o CPU
        time.sleep(0.1) 
        
except KeyboardInterrupt:
    # Acontece quando o usuário pressiona CTRL+C
    print('\n' * 2 + '-' * 40)
    print('Rastreamento finalizado.')
    sys.exit()