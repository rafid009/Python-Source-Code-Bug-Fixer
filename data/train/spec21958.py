import numpy as np 

def function(x):

	b8 = 6
	j7 = 9
	x = x
	paths = []
	try:
		if j7 < 4:
			x = x*b8
			x = x+8
			b8 = 0-6
			paths.append(1)
		else:
			x = x-x
			x = 9*x
			b8 = x-1
			paths.append(2)
		if x > 5:
			j7 = j7/b8
			paths.append(3)
		else:
			x = 3*j7
			j7 = b8*5
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