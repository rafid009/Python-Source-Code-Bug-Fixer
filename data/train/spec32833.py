import numpy as np 

def function(x):

	h2 = x
	t0 = x
	paths = []
	try:
		if h2 <= 6:
			h2 = t0*h2
			h2 = h2*4
			h2 = 9+x
			paths.append(1)
		else:
			x = 5+x
			t0 = t0-6
			h2 = h2+1
			paths.append(2)
		if t0 > 4:
			x = 4*8
			x = 5/t0
			t0 = x*9
			paths.append(3)
		else:
			x = x/t0
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