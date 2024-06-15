import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QComboBox, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Definição das cartas de cada cor
amarelo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 'coringa', 'coringa+4']
azul = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 'coringa', 'coringa+4']
verde = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 'coringa', 'coringa+4']
vermelho = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'negar', 'voltar', 'mais 2', 'coringa', 'coringa+4']

mao = []

# Função de compra
def comprar(amarelo, azul, verde, vermelho):
    randcor = random.randint(1, 4)
    if randcor == 1:
        cor = 'amarelo'
        randcor = amarelo
    elif randcor == 2:
        cor = 'azul'
        randcor = azul
    elif randcor == 3:
        cor = 'verde'
        randcor = verde
    else:
        cor = 'vermelho'
        randcor = vermelho

    randnum = random.randint(0, len(randcor) - 1)
    carta = randcor.pop(randnum)
    return (cor, carta)

# Mão inicial
for i in range(7):
    mao.append(comprar(amarelo, azul, verde, vermelho))

class UnoGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('UNO Game')
        self.setStyleSheet("background-color: #f0f0f0;")

        self.top_card_label = QLabel('Carta do topo:', self)
        self.top_card_label.setFont(QFont('Arial', 14))
        self.top_card_label.setStyleSheet("color: #333333;")

        self.color_combo = QComboBox(self)
        self.color_combo.addItems(['amarelo', 'azul', 'verde', 'vermelho'])
        self.color_combo.setFont(QFont('Arial', 12))
        self.color_combo.setStyleSheet("background-color: white; color: #333333;")

        self.card_combo = QComboBox(self)
        self.card_combo.addItems([str(i) for i in range(10)] + ['negar', 'voltar', 'mais 2', 'coringa', 'coringa+4'])
        self.card_combo.setFont(QFont('Arial', 12))
        self.card_combo.setStyleSheet("background-color: white; color: #333333;")

        self.submit_button = QPushButton('Jogar Carta', self)
        self.submit_button.setFont(QFont('Arial', 12))
        self.submit_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px;")

        self.submit_button.clicked.connect(self.submit_top_card)

        self.current_hand_label = QLabel(f'Mão atual: {len(mao)} cartas', self)
        self.current_hand_label.setFont(QFont('Arial', 12))
        self.current_hand_label.setStyleSheet("color: #333333; padding: 10px; border: 1px solid #cccccc; background-color: white; border-radius: 5px;")

        vbox = QVBoxLayout()
        vbox.addWidget(self.top_card_label, alignment=Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.color_combo)
        hbox.addWidget(self.card_combo)
        
        vbox.addLayout(hbox)
        vbox.addWidget(self.submit_button, alignment=Qt.AlignCenter)
        vbox.addWidget(self.current_hand_label, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

    def submit_top_card(self):
        cortopo = self.color_combo.currentText()
        numtopo = self.card_combo.currentText()

        # Converte numtopo para o tipo correto
        if numtopo.isdigit():
            numtopo = int(numtopo)
        else:
            numtopo = str(numtopo)

        # Remover a carta do topo do baralho correspondente
        if cortopo == 'amarelo' and numtopo in amarelo:
            amarelo.remove(numtopo)
        elif cortopo == 'azul' and numtopo in azul:
            azul.remove(numtopo)
        elif cortopo == 'verde' and numtopo in verde:
            verde.remove(numtopo)
        elif cortopo == 'vermelho' and numtopo in vermelho:
            vermelho.remove(numtopo)
        else:
            QMessageBox.warning(self, "Carta Inválida", "Carta não encontrada no baralho correspondente.")
            return

        self.top_card_label.setText(f'Carta do topo: {cortopo} {numtopo}')

        # Cartas especiais
        if numtopo == 'mais 2':
            for _ in range(2):
                mao.append(comprar(amarelo, azul, verde, vermelho))
            mensagensdois = [
                "Carta 'mais 2' comprei 2 cartas e criei ódio por voce!",
                "Carta 'mais 2' eu compro 2 cartas e reduzo sua espectativa de vida em 2 anos!",
                "Carta 'mais 2'??? é assim que vc me trata??? ",
                "Carta 'mais 2'? tem certeza? olha que vou contar pra todo mundo que você esta roubando heim!"
            ]
            QMessageBox.information(self, "Mais 2", random.choice(mensagensdois))
            self.update_hand()
            return

        if numtopo == 'coringa+4':
            for _ in range(4):
                mao.append(comprar(amarelo, azul, verde, vermelho))
            mensagensquatro = [
                "Carta 'coringa+4' assim acaba com a amizade!",
                "Carta 'coringa+4' VAI PRA PQP!",
                "Carta 'coringa+4??? é assim que vc me trata??? ",
                "Carta 'coringa+4'? NAO QUERO MAIS JOGAR!!!!"
            ]
            mensagem_escolhida = random.choice(mensagensquatro)
            QMessageBox.information(self, "Coringa +4", mensagem_escolhida)
            if mensagem_escolhida == mensagensquatro[3]:
                QMessageBox.information(self, "Jogo Terminado", "Jogo encerrado!")
                self.close()
            self.update_hand()
            return

        if numtopo == 'negar':
            QMessageBox.information(self, "Negar", "Carta 'negar', passando a vez e a mão na perna da sua namorada...")
            return

        # Tenta jogar uma carta da mão
        carta_jogada = None
        for carta in mao:
            cor, numero = carta
            if cor == cortopo or str(numero) == str(numtopo):
                carta_jogada = carta
                break

        if carta_jogada:
            mao.remove(carta_jogada)
            QMessageBox.information(self, "Carta Jogada", f"Carta jogada: {carta_jogada}")
        else:
            nova_carta = comprar(amarelo, azul, verde, vermelho)
            mao.append(nova_carta)
            QMessageBox.information(self, "Compra de Carta", f"Não tinha carta correspondente na mão, comprou nova carta: {nova_carta}")

        self.update_hand()

        if len(mao) == 1:
            QMessageBox.information(self, "UNO!", "UNO!")
        elif len(mao) == 0:
            QMessageBox.information(self, "Vitória", "GANHEI!")
            self.close()

    def update_hand(self):
        self.current_hand_label.setText(f'Mão atual: {len(mao)} cartas')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UnoGame()
    ex.show()
    sys.exit(app.exec_())
