import numpy as np 

def function(x):

	t4 = x
	h1 = 1
	paths = []
	try:
		if h1 <= 7:
			t4 = 6/t4
			paths.append(1)
		else:
			x = x*3
			h1 = h1-6
			paths.append(2)
		if h1 < 5:
			x = t4*t4
			x = x*0
			t4 = 2*t4
			paths.append(3)
		else:
			h1 = 0*h1
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))