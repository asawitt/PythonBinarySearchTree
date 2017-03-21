# PythonBinarySearchTree
Python3 BST developed for HackerRank Challenges

## Installation
-Fastest would be to copy-paste the contents of DisjointSet.py into your code. As this was made for HR challenges that's what I do. 

-Or you could download BinarySearchTree.py and throw it in your project directory. Use "from BinarySearchTree import *" to use it in your code

-You could clone https://github.com/asawitt/PythonBinarySearchTree/ , move BinarySearchTree.py to your project directory, then use the above import statement if you really want to. Don't. 

## Information
Insert, Delete, Find run in O(log(n)) average, O(n) worst case. Operations on unbalanced trees will take longer, considering this, if your data is highly sequential it's recommended you use a self-balancing tree such as AVL or Red-Black trees


## Usage
### Create a new BST
tree = BST()
### Insert a value into the BST
tree.insert(value)
### Delete a value from the BST 
tree.delete(value)
### Find
-Returns True if the value is in the Tree, False otherwise
tree.find(value) 
### Printing
-Prints the tree, layer-by-layer
tree.printTree()
### Flatten
-Returns a list of the values in the BST from least to greatest
tree.flatten()

## License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

