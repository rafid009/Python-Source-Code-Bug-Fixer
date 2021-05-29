import numpy as np 

def function(x):

	c6 = x
	x4 = 0
	paths = []
	try:
		if x4 < 6:
			x = x*0
			paths.append(1)
		else:
			x4 = x4-2
			x4 = 6*6
			paths.append(2)
		if x > 5:
			x4 = x4-3
			x = 1+x
			x = 1/4
			paths.append(3)
		else:
			x = x+7
			x = 3-x4
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x4 = c6**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))