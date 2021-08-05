# Menu Planner and Recipe Book

The program where you can organize your recipes, create menus, and print shopping lists all in one package.

## Requirements

### Must have features

- Ability to add a recipe
- Be able to create and manage different menus
- Print a shopping list based off the current day

### Stretch Goals

- Recommend Recipe's based off what is already in the menu/weekday for greater ingredient usage
- Be able to email shopping lists

## User Story

- Open up the application it shows a calendar view and when you click on a day it populates the side bar with that day. There we can add new meals and see more details of all the already created days
- When done populating the menu should be able to print it and a shopping list on paper for usage 

## Views

    • Top bar
        ◦ Tab to switch between Menu view and Recipe book view like tabs on a browser
    • Menu
        ◦ Calendar
            ▪ Filled in with days
        ◦ Day
            ▪ Next to the calendar where we can modify everything about that day
    • Recipe book
        ◦ Navigation tabs on the left for custom sorting based off tab
            ▪ A tree structure, like a file system with embedded folders
        ◦ Recipe edit page on the right
        ◦ Buttons on the top to create recipes 

## Objects 

    • Universal
        ◦ Singleton
        ◦ Day
            ▪ Meal
                • Course
    • Backend
        ◦ Database
            ▪ Wrapper for sqlite to facilitate reads, writes, and queries to the database
        ◦ Object Handler
            ▪ Makes queries to database and converts the responses to objects
            ▪ Takes objects and updates the database
    • Frontend
        ◦ Main window
            ▪ Menu
                • Calendar
                • Day Editor
            ▪ Recipe book
                • Organizer
                • Recipe Editor

## DataBase Scheme

### Recipe Book

| Recipes   |           |                   |                   |
| ---       | ---       | ---               | ---               |
| Name      | PrepTime  | hasIngredients    | hasInstructions   |

| Tree Nodes    |            |
| ---           | ---        |
| Name          | Parent     |

| Ingredients   |           |           |               |
| ---           | ---       | ---       | ---           |
| Name          | Recipe    | Quantity  | identifier    |

| Instructions  |           |       |
| ---           | ---       | ---   |
| Step          | Recipe    | Text  |

### Menu's

| Meals |       |       |           |
| ---   | ---   | ---   | ---       |
| Month | Day   | Menu  | Meal-ID   |

| Tree Nodes |          |
| ---        | ---      |
| Recipe     | Meal-ID  |
