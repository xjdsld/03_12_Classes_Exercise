Hero RPG Prototype

Project Structure
project/
│
├── main.py              
├── characters.py       
├── items_shop.py        
└── README.md

This project is a simple Python-based RPG prototype where a player creates a hero, assigns a class, and interacts with a basic item and shop system. A bot hero is also generated randomly to simulate an opponent or companion.

Features
Hero Creation

Player selects one of three hero classes:

Strength

Dexterity

Magic Skills

Player assigns a name.

Hero stats are generated randomly.

Bot Hero

A bot hero is created with a randomly chosen class.

Bot stats are generated automatically.

Items and Shop

Players can buy items that affect their stats:

Sword: +10 Strength (10 coins)

Mushroom: +15 Magic Skills (15 coins)

Flower: –20 Dexterity (30 coins)

Object-Oriented Structure

Abstract base class HERO

Subclasses: Strengh, Dextrexity, Magic_skills

Item logic handled through Items and Shop classes

