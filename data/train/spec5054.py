import numpy as np 

def function(x):

	j7 = 7
	g5 = x
	paths = []
	try:
		if x >= 4:
			j7 = 0/1
			paths.append(1)
		else:
			j7 = j7+1
			paths.append(2)
		if g5 <= 7:
			j7 = x+j7
			paths.append(3)
		else:
			x = 1/x
			j7 = j7-4
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))