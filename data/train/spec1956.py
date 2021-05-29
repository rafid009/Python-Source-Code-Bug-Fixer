import numpy as np 

def function(x):

	h1 = 5
	t6 = 4
	paths = []
	try:
		if x > 8:
			h1 = x/8
			paths.append(1)
		else:
			t6 = t6/8
			x = x/6
			paths.append(2)
		if h1 > 8:
			t6 = h1+x
			paths.append(3)
		else:
			h1 = h1-t6
			t6 = h1*3
			x = x+8
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))