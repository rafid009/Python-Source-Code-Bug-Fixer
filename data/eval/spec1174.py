import numpy as np 

def function(x):

	v7 = x
	u2 = x
	paths = []
	try:
		if u2 > 5:
			u2 = 1/6
			x = x*v7
			paths.append(1)
		else:
			u2 = 1/u2
			v7 = v7*2
			v7 = 0+v7
			paths.append(2)
		if v7 < 2:
			u2 = 3*u2
			paths.append(3)
		else:
			u2 = u2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))