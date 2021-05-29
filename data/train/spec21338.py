import numpy as np 

def function(x):

	v2 = 1
	e7 = x
	paths = []
	try:
		if x > 1:
			e7 = 5+e7
			x = x*7
			e7 = 2/e7
			paths.append(1)
		else:
			v2 = v2*v2
			paths.append(2)
		if x < 7:
			x = v2*x
			paths.append(3)
		else:
			v2 = v2*2
			v2 = 1+v2
			v2 = v2-x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))