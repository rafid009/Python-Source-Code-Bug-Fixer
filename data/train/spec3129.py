import numpy as np 

def function(x):

	v5 = x
	l0 = 7
	paths = []
	try:
		if l0 <= 2:
			x = 5+v5
			paths.append(1)
		else:
			v5 = v5/7
			l0 = 1+l0
			v5 = x*v5
			paths.append(2)
		if v5 > 9:
			v5 = v5/5
			l0 = l0*4
			x = 9/l0
			paths.append(3)
		else:
			v5 = v5-7
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