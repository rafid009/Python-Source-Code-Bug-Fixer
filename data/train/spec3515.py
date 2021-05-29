import numpy as np 

def function(x):

	k3 = 2
	r4 = x
	paths = []
	try:
		if x >= 0:
			x = x*4
			paths.append(1)
		else:
			x = x+6
			r4 = r4*r4
			r4 = r4-9
			paths.append(2)
		if k3 < 7:
			x = 9*5
			x = 4/9
			x = r4-0
			paths.append(3)
		else:
			x = 8*k3
			k3 = 1-k3
			r4 = r4*0
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