import numpy as np 

def function(x):

	v0 = x
	i7 = 2
	paths = []
	try:
		if i7 >= 3:
			i7 = 7/8
			i7 = x+6
			i7 = x/i7
			paths.append(1)
		else:
			v0 = x*v0
			i7 = 4+9
			paths.append(2)
		if i7 < 9:
			v0 = 7*v0
			v0 = 1/v0
			i7 = 5-0
			paths.append(3)
		else:
			i7 = i7+6
			v0 = 9+v0
			i7 = i7*v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))