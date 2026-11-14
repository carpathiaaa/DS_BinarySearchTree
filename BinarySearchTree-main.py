#
#  main.py
#  getNext_search_tree
#
#  Created by Jim Bailey on 4/25/20.
#  Licensed under a Creative Commons Attribution 4.0 International License.
#  Modifications by Tina Majchrzak
#
import sys
import os
from Tree import Tree


def readInBstValues():
  if os.path.exists("input"):
    data = open("input").read().split()
  else:
    data = sys.stdin.read().split()
  idx = 0
  def read_n():
    nonlocal idx
    n = int(data[idx]); idx += 1
    vals = [int(x) for x in data[idx:idx + n]]; idx += n
    return vals

  insertVals = read_n()
  findVals = read_n()
  findQueries = read_n()
  removeVals = read_n()
  removeTarget = int(data[idx]); idx += 1
  flVals = read_n()
  flQueries = read_n()
  rlVals = read_n()
  rlQueries = read_n()
  return insertVals, findVals, findQueries, removeVals, removeTarget, flVals, flQueries, rlVals, rlQueries



def testInsertInOrder(insertVals):
  fir = Tree()
  for v in insertVals:
    fir.insertValue(v)

  print("\nTesting insertValue and inOrder traversal ")
  print(" Insert and display " + str(len(insertVals)) + " integers ")

  print(" InOrder Expected: " + '-27 -2 2 17 18 20 24 27 32 34 59 60 75 81 89 93 99 ')
  print(" InOrder Actually: " + fir.inOrder())
  print("\n PreOrder Expected: " + '32 18 2 -27 -2 17 24 20 27 60 59 34 89 75 81 93 99 ')
  print(" PreOrder Actually: " + fir.preOrder())
  print("\n PostOrder Expected: " + '-2 -27 17 2 20 27 24 18 34 59 81 75 99 93 89 60 32 ')
  print(" PostOrder Actually: " + fir.postOrder())

  print("\nEnd test insertValue and displayTree\n")


def testFind(findVals, findQueries):
  oak = Tree()
  for v in findVals:
    oak.insertValue(v)

  print("\nTesting findValue ")
  print(" Insert and display " + str(len(findVals)) + " integers ")
  print("  " + oak.inOrder())

  print("\n Checking find results: ")
  print("  Looking for " + str(findQueries[0]) + " " + ("found" if oak.findValue(findQueries[0]) else "not found"))
  print("  Looking for " + str(findQueries[1]) + " " + ("found" if oak.findValue(findQueries[1]) else "not found"))
  print("  Looking for " + str(findQueries[2]) + " " + ("found" if oak.findValue(findQueries[2]) else "not found"))
  print("  Looking for " + str(findQueries[3]) + " " + ("found" if oak.findValue(findQueries[3]) else "not found"))

  print("\nEnd of test findValue\n")


def testRemove(removeVals, removeTarget):
  plum = Tree()
  for v in removeVals:
    plum.insertValue(v)

  print("\nTesting removeValue ")
  print(" Insert and display " + str(len(removeVals)) + " integers")
  print("  " + plum.inOrder())

  print("\n Now testing remove, " + str(removeTarget) + " should be there and then gone")
  print("  Looking for " + str(removeTarget) + " " + ("found" if plum.findValue(removeTarget) else "not found"))
  plum.removeValue(removeTarget)
  print("  Looking for " + str(removeTarget) + " " + ("found" if plum.findValue(removeTarget) else "not found") + "\n")

  print(" Displaying tree after removing " + str(removeTarget))
  print("  InOrder is  " + plum.inOrder())

  print("\n Now seeing if adding " + str(removeTarget) + " back works")
  plum.insertValue(removeTarget)
  print("  Looking for " + str(removeTarget) + " " + ("found" if plum.findValue(removeTarget) else "not found"))

  print(" Displaying tree after adding " + str(removeTarget) + " back")
  print("  InOrder is  " + plum.inOrder())

  print("\nEnd of test removeValue \n")


def testFindLarger(flVals, flQueries):
  apple = Tree()
  for v in flVals:
    apple.insertValue(v)

  print("\nTesting findLarger ")
  print(" Insert and display " + str(len(flVals)) + " integers ")
  print("  " + apple.inOrder())
  print("\n Now testing findLarger")
  print("  " + str(flQueries[0]) + " should return " + '51' + " and returns " + str(apple.findLarger(flQueries[0])))
  print("  " + str(flQueries[1]) + " should return " + '34' + " and returns " + str(apple.findLarger(flQueries[1])))
  print("  " + str(flQueries[2]) + " should return " + '136' + " and returns " + str(apple.findLarger(flQueries[2])))
  print("  " + str(flQueries[3]) + " should return " + '-1' + " and returns " + str(apple.findLarger(flQueries[3])))
  print("  " + str(flQueries[4]) + " should return " + '10' + " and returns " + str(apple.findLarger(flQueries[4])))
  print("  " + str(flQueries[5]) + " should return " + '110' + " and returns " + str(apple.findLarger(flQueries[5])))
  print("  " + str(flQueries[6]) + " should return " + '51' + " and returns " + str(apple.findLarger(flQueries[6])))
  print("  " + str(flQueries[7]) + " should return " + '82' + " and returns " + str(apple.findLarger(flQueries[7])))

  print("\nEnd of testing findLarger\n")


def testRemoveLarger(rlVals, rlQueries):
  pear = Tree()
  for v in rlVals:
    pear.insertValue(v)

  print("\nTesting removeLarger ")
  print(" Insert and display " + str(len(rlVals)) + " integers ")
  print("  " + pear.inOrder())
  print("\n Now testing removeLarger")
  result = pear.removeLarger(rlQueries[0])
  print("  " + str(rlQueries[0]) + " should return " + '143' + " and returns " + str(result))
  print("  " + '143' + " should be gone and is " + ("found" if pear.findValue(143) else "not found") + "\n")
  result = pear.removeLarger(rlQueries[1])
  print("  " + str(rlQueries[1]) + " should return " + '6' + " and returns " + str(result))
  print("  " + '6' + " should be gone and is " + ("found" if pear.findValue(6) else "not found") + "\n")
  result = pear.removeLarger(rlQueries[2])
  print("  " + str(rlQueries[2]) + " should return " + '96' + " and returns " + str(result))
  print("  " + '96' + " should be gone and is " + ("found" if pear.findValue(96) else "not found") + "\n")
  result = pear.removeLarger(rlQueries[3])
  print("  " + str(rlQueries[3]) + " should return " + '110' + " and returns " + str(result))
  print("  " + '110' + " should be gone and is " + ("found" if pear.findValue(110) else "not found") + "\n")

  print("\n After removals ")
  print("  Expected " + '1 6D 7 26 28 33 54 72 78 96D 110D 137 140 143D 146 ')
  print("  Actually " + pear.inOrder())

  print("End of testing removeLarger\n")

def main():
  insertVals, findVals, findQueries, removeVals, removeTarget, flVals, flQueries, rlVals, rlQueries = readInBstValues()
  testInsertInOrder(insertVals)
  testFind(findVals, findQueries)
  testRemove(removeVals, removeTarget)


if __name__ == "__main__":
  main()
