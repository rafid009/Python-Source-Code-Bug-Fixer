import numpy as np 

def function(x):

	v9 = 7
	h3 = x
	paths = []
	try:
		if h3 <= 9:
			x = x+v9
			x = 0/x
			x = h3/h3
			paths.append(1)
		else:
			v9 = h3+v9
			h3 = h3*x
			x = 3-9
			paths.append(2)
		if v9 <= 8:
			v9 = h3*3
			paths.append(3)
		else:
			x = h3/3
			x = x+x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))