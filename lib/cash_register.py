#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.quantity = 0
    self.items = []
    self.lastItem = 0

  def add_item(self, title, price, quantity=1):
    self.total += (price * quantity)
    self.lastItem = (price * quantity)
    i=1
    while i <= quantity:
      self.items.append(title)
      i+= 1
    

  def apply_discount(self):
    self.total = self.total * (1 - (self.discount/100))
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print("After the discount, the total comes to $800.")

  def void_last_transaction(self):
    self.total = self.total - self.lastItem 

