import numpy as np 

def function(x):

	h1 = 3
	t0 = x
	paths = []
	try:
		if h1 > 3:
			h1 = 5-x
			h1 = h1*5
			h1 = 6+x
			paths.append(1)
		else:
			h1 = h1+0
			x = x*x
			h1 = 3/4
			paths.append(2)
		if t0 <= 0:
			t0 = t0*3
			x = x-0
			paths.append(3)
		else:
			x = x+7
			x = 5-6
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))