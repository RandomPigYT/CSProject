import pygame
import json


class SpriteSheet:
    def __init__(self, fileName: str):
        self.spriteSheet = pygame.image.load(fileName).convert()

        self.metaData = fileName.replace("png", "json").replace(
            "assets/", "json_files/"
        )

        with open(self.metaData) as f:
            self.data = json.load(f)
        f.close()

    def GetSprite(self, name, w, h):

        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))

        spriteFrame = self.data["frames"][name]["frame"]

        sprite.blit(
            self.spriteSheet, (0, 0), (spriteFrame["x"], spriteFrame["y"], w, h)
        )

        return sprite
