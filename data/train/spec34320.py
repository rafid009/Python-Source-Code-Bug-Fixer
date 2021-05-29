import numpy as np 

def function(x):

	v1 = 6
	v7 = x
	paths = []
	try:
		if v1 >= 4:
			x = v7-x
			v1 = v1+1
			paths.append(1)
		else:
			v1 = v1-3
			x = 9/x
			x = 9*x
			paths.append(2)
		if x >= 8:
			v1 = v1*v7
			paths.append(3)
		else:
			x = v1*4
			v7 = 0+v7
			v1 = x+x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v1 = v7**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))