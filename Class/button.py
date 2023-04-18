import pygame
pygame.init
pygame.font.init()
main_font = pygame.font.Font(None, 36)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input, isShopping, price, function, newImg):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.isShopping = isShopping
		self.price = price
		self.function = function
		self.newImg = newImg

	# def update(self):
		# screen.blit(self.image, self.rect)
		# screen.blit(self.text, self.text_rect)

	def checkForInput(self, position, player):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			if self.isShopping and self.price <= player.money:
				player.money -= self.price
				self.function(player, self.newImg)
			# img = pygame.image.load("img/emeu.jpg")
			# img = pygame.transform.scale(img, (50, 50))
			# player.bulletHandler.img = img

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

	def ChangeWeapon (player, img):
		player.bulletHandler.img = img