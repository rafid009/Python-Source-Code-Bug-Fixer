import numpy as np 

def function(x):

	i9 = x
	v6 = 2
	paths = []
	try:
		if x < 7:
			v6 = v6/v6
			paths.append(1)
		else:
			x = 9*x
			i9 = x+i9
			x = 4+9
			paths.append(2)
		if v6 >= 3:
			x = 1/x
			x = 9-x
			x = x*7
			paths.append(3)
		else:
			x = 8+x
			i9 = i9/2
			x = 1-8
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		v6 = i9**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))