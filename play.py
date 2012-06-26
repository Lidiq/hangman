﻿#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, random
import pygame
from pygame.locals import *


class Play:
    def __init__(self, screen, chosen_category):
        """Initialize the game field: 
        generates random word from a file, display the alphabet"""
        
        self.background = pygame.image.load('images\hangman_empty.png')
        screen.blit(self.background, (0, 0))
        self.screen = screen
        self.letters = list()
        self.random_word_lenght = len(self.load_word(chosen_category))
        self.display_underlines(self.random_word_lenght)
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 30)
        self.display_alphabet()
        self.chosen_letters = list()
    
    def display_underlines(self, random_word_lenght):
        """Display the underlines, each line for each letter in the must-guess word"""
        i_line = 0
        while i_line < random_word_lenght:
            underline_image = pygame.image.load('images/underline_word.png')
            self.screen.blit(underline_image, (400 + i_line * 35, 200))
            i_line = i_line + 1
    
    
    def alphabet_list(self):
        """Return list with bulgarian letters"""
        with open('dict_files/bulgarian_alphabet.txt') as source_file:
            alphabet = source_file.readlines()
        alphabet = [(letter.strip()) for letter in alphabet]
        return alphabet
    
    
    def display_alphabet(self):
        """Show the letters in bulgarian alphabet in 6x5 rectangle"""
        self.alphabet = self.alphabet_list()
        letter_space = 0
        slice = 0
        while slice < 30:
            for character in self.alphabet[slice : slice + 6]:
                letter = Letter((400 + letter_space, 300 + slice * 6), self.my_font, character, self.screen)
                self.letters.append(letter)
                letter_space += 30
            slice += 6
            letter_space = 0
        
    
    def load_word(self, category_name):
        """Load a random word from a file"""
        filename = 'dict_files/' + category_name + '.txt'
        with open(filename) as source_file:
            buffer = source_file.readlines()
        self.word = random.choice(buffer).strip()
        return self.word
        
    def handle_events(self):
        """Handle keyboard events"""
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            print("letter a is pressed")
        #pygame.display.flip()
    
    def handle_mouse_events(self, pos, i):
        """Handle mouse events"""
        (x, y) = pos
        for letter in self.letters:
            if letter.mouse_over(pos):
                self.screen.blit(self.background, letter.pos, pygame.Rect(x, y, 25, 25))
                self.chosen_letters.append(letter)
                print(self.chosen_letters)
                if letter.character not in self.word:
                    self.load_part_i(i)
                    return False
                else:
                    indices = [n for n in range(len(self.word)) if self.word.find(letter.character, n) == n]
                    self.display_guessed_letters(indices, letter.character)
                    return True 
        return True
    
    #save the loaded words
    #save the guessed letters to not be clicked again
    
    def display_guessed_letters(self, indices, letter):
        """Display the right guessed letters"""
        for index in indices:
            show_letter = self.my_font.render(letter, True, (48, 79, 157))
            self.screen.blit(show_letter, (400 + index * 35, 170))
     
    def load_part_i(self, i):
        """Load a part of the hangman"""
        image = pygame.image.load('images\hangman_' + str(i) + '.png')
        if i == 1:
            self.screen.blit(image, (8, 450))
        elif i == 2:
            self.screen.blit(image, (95, 45))
        elif i == 3:
            self.screen.blit(image, (110, 36))
        elif i == 4:
            self.screen.blit(image, (260, 47))
        elif i == 5:
            self.screen.blit(image, (202, 110))
        elif i == 6: 
            self.screen.blit(image, (260, 220))
        elif i == 7: 
            self.screen.blit(image, (180, 230))
        elif i == 8: 
            self.screen.blit(image, (270, 230))
        elif i == 9: 
            self.screen.blit(image, (270, 350))
        elif i == 10: 
            self.screen.blit(image, (210, 350))
 
 
class Letter:
    def __init__(self, pos, my_font, letter, screen):
        self.my_font = my_font
        self.pos = pos
        self.normal = self.my_font.render(letter, True, (181, 76, 90))
        self.highlight = self.my_font.render('i', True, (181, 76, 90))
        self.image = self.normal
        self.show = screen.blit(self.image, self.pos)
        self.character = letter
        
        
    def mouse_over(self, pos):
        if self.show.collidepoint(pos):
            self.image = self.highlight
            return True
        else:
            self.image = self.normal
            return False
        
    def draw(self, screen):
        self.show = screen.blit(self.image, self.pos)
    
       
       
       
       
       