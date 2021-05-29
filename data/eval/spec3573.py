import numpy as np 

def function(x):

	p9 = x
	r6 = 5
	x = x
	paths = []
	try:
		if x >= 1:
			r6 = 4*r6
			x = x/p9
			r6 = r6+5
			paths.append(1)
		else:
			r6 = r6/p9
			x = x/3
			x = x*1
			paths.append(2)
		if x <= 3:
			x = r6+5
			x = x-1
			paths.append(3)
		else:
			x = p9+r6
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