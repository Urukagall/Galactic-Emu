import pygame
pygame.init
pygame.font.init()
main_font = pygame.font.Font(None, 36)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input, isShopping, price, function, newImg, infoText=None):
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
		self.infoText = main_font.render(infoText, True, (175, 187, 242))
		self.infoTextRect = self.infoText.get_rect(center=(self.x_pos, self.y_pos - 70))
		self.priceText = main_font.render("Price:" + str(self.price), True, (175, 187, 242))
		self.priceTextRect = self.priceText.get_rect(center=(self.x_pos, self.y_pos - 50))
  
		self.isLevelMax = False

	def update(self, screen):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
		if self.price != None:
			if self.priceText == "Level MAX" or self.price == -1:
				self.isLevelMax = True
				self.priceText = main_font.render("Level Max", True, (175, 187, 242))
			elif not(self.isLevelMax):
				self.priceText = main_font.render("Price:" + str(self.price), True, (175, 187, 242))
			self.priceTextRect = self.priceText.get_rect(center=(self.x_pos, self.y_pos - 50))
			screen.blit(self.priceText, self.priceTextRect)


	def checkForInput(self, position, player):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			# If you have the money to buy return True
			if self.isShopping and (self.price <= player.money or self.price == None) and self.price != -1:
				player.updateMoney(-self.price)
				# self.function(player, self.newImg)
				return True
			# If the Button don't need money return True
			elif not(self.isShopping):
				return True

	def changeColor(self, position, screen):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, (16,37,161))
			if self.infoText != None:
				screen.blit(self.infoText, self.infoTextRect)
		else:
			self.text = main_font.render(self.text_input, True, "white")

	def ChangeWeapon (player, img):
		player.bulletHandler.img = img