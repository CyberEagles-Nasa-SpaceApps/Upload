from pathlib import Path

import arcade

LARGURA, ALTURA = 800, 600
VELOCIDADE_CAMERA = 600  # pixels por segundo

PASTA = Path(__file__).resolve().parent
ARQUIVO_MAPA = PASTA / "Jogo Astronauta.tmx"


class Jogo(arcade.Window):
    
        def on_key_press(self, tecla, modificadores):
         self.teclas.add(tecla)

        if tecla == arcade.key.ESCAPE:
            self.close()

        def on_key_release(self, tecla, modificadores):
         self.teclas.discard(tecla)
        
        def __init__(self):
         super().__init__(LARGURA, ALTURA, "Jogo do Astronauta")

        self.mapa = arcade.load_tilemap(ARQUIVO_MAPA, scaling=1.0)
        self.cenario = arcade.Scene.from_tilemap(self.mapa)

        # Tamanho do mapa em pixels (105 x 105 tiles de 32 px)
        self.mapa_largura = self.mapa.width * self.mapa.tile_width
        self.mapa_altura = self.mapa.height * self.mapa.tile_height

        self.camera = arcade.Camera2D()
        self.camera.position = (LARGURA / 2, ALTURA / 2)

        self.teclas = set()
        self.personagem = arcade.Sprite(PASTA / "astronauta.png",scale=0.5)

        self.personagem.center_x = 400
        self.personagem.center_y = 300
        self.velocidade = 250
        self.lista_personagens = arcade.SpriteList()
        self.lista_personagens.append(self.personagem)

        def on_draw(self):
         self.clear()
         self.camera.use()
         self.cenario.draw()
         self.lista_personagens.draw()

    
        def on_update(self, delta_time):
         dx = 0
         dy = 0

        if arcade.key.W in self.teclas:
            dy += 1

        if arcade.key.S in self.teclas:
            dy -= 1

        if arcade.key.A in self.teclas:
            dx -= 1

        if arcade.key.D in self.teclas:
            dx += 1

        self.personagem.center_x += dx * self.velocidade * delta_time
        self.personagem.center_y += dy * self.velocidade * delta_time

        metade_largura = self.personagem.width / 2
        metade_altura = self.personagem.height / 2

        self.personagem.center_x = max(
            metade_largura,
            min(self.mapa_largura - metade_largura, self.personagem.center_x)
        )

        self.personagem.center_y = max(
            metade_altura,
            min(self.mapa_altura - metade_altura, self.personagem.center_y)
        )

        x = max(
            LARGURA / 2,
            min(self.mapa_largura - LARGURA / 2, self.personagem.center_x)
        )

        y = max(
            ALTURA / 2,
            min(self.mapa_altura - ALTURA / 2, self.personagem.center_y)
        )

        self.camera.position = (x, y)



def main():
    Jogo()
    arcade.run()


if __name__ == "__main__":
    main()
