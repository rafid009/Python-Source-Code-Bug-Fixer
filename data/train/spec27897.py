import numpy as np 

def function(x):

	j4 = 0
	v9 = 3
	paths = []
	try:
		if x >= 9:
			v9 = v9/9
			paths.append(1)
		else:
			j4 = j4*0
			j4 = 5+8
			v9 = v9+4
			paths.append(2)
		if j4 >= 0:
			x = 3*x
			v9 = 7+2
			paths.append(3)
		else:
			x = x*v9
			j4 = j4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))