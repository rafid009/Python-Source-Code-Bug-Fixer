import numpy as np 

def function(x):

	v3 = 3
	b2 = 5
	paths = []
	try:
		if b2 <= 8:
			b2 = b2/9
			v3 = v3/4
			x = x+9
			paths.append(1)
		else:
			x = 4*b2
			paths.append(2)
		if x > 9:
			v3 = 2+v3
			x = x+5
			paths.append(3)
		else:
			v3 = v3+0
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