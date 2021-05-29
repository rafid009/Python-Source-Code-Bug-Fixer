import numpy as np 

def function(x):

	v4 = 3
	b4 = x
	paths = []
	try:
		if v4 <= 7:
			x = 6-9
			paths.append(1)
		else:
			x = x-b4
			paths.append(2)
		if b4 < 4:
			x = b4-x
			v4 = 4/7
			b4 = b4/1
			paths.append(3)
		else:
			x = x+b4
			v4 = 9*v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))