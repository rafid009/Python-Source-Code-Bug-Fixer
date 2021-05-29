import numpy as np 

def function(x):

	v6 = 2
	x2 = 9
	paths = []
	try:
		if v6 < 2:
			x2 = x2+v6
			x2 = x2+x
			x = x+2
			paths.append(1)
		else:
			x = x/2
			v6 = v6+3
			paths.append(2)
		if x > 4:
			x2 = 2*x2
			paths.append(3)
		else:
			x = x*x
			x2 = 3-x2
			x = v6/x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))