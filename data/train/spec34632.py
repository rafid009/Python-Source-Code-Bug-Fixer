import numpy as np 

def function(x):

	v7 = x
	v1 = 7
	paths = []
	try:
		if x > 9:
			x = v1+x
			paths.append(1)
		else:
			x = v7*x
			paths.append(2)
		if x >= 5:
			v7 = v7*x
			v1 = v1*2
			paths.append(3)
		else:
			x = x+3
			v1 = 2-v7
			v1 = x-v1
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))