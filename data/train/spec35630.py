import numpy as np 

def function(x):

	b4 = x
	j7 = 4
	paths = []
	try:
		if j7 < 3:
			j7 = j7/8
			j7 = j7-b4
			x = x-4
			paths.append(1)
		else:
			b4 = 9+b4
			paths.append(2)
		if x < 4:
			b4 = b4/x
			b4 = 8-b4
			j7 = j7+x
			paths.append(3)
		else:
			j7 = j7-3
			x = x+5
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