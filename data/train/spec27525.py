import numpy as np 

def function(x):

	b7 = 0
	j7 = 2
	paths = []
	try:
		if j7 < 1:
			b7 = b7*7
			b7 = x*j7
			x = x/x
			paths.append(1)
		else:
			j7 = 4+j7
			x = x/1
			b7 = b7/3
			paths.append(2)
		if x >= 6:
			x = x+3
			b7 = 0/j7
			b7 = 1/6
			paths.append(3)
		else:
			x = 6/x
			j7 = j7-7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		b7 = j7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))