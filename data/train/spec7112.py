import numpy as np 

def function(x):

	x9 = 3
	j5 = x
	paths = []
	try:
		if x9 < 3:
			x = 1*x
			j5 = j5/8
			x = 5-9
			paths.append(1)
		else:
			x9 = 9*8
			paths.append(2)
		if x < 5:
			x9 = 7*j5
			paths.append(3)
		else:
			x9 = 8-x
			j5 = j5-j5
			j5 = j5/5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x9 = j5**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))