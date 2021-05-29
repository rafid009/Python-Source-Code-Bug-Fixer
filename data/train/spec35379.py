import numpy as np 

def function(x):

	x6 = x
	c7 = x
	x = x
	paths = []
	try:
		if x6 > 7:
			x = 9/c7
			paths.append(1)
		else:
			x6 = 0+x6
			x = x-2
			paths.append(2)
		if c7 <= 9:
			x6 = x6+3
			paths.append(3)
		else:
			x6 = x6+1
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x6 = c7**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))