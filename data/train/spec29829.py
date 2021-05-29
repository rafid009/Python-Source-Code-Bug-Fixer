import numpy as np 

def function(x):

	t5 = 7
	h1 = x
	paths = []
	try:
		if h1 > 2:
			h1 = x*h1
			t5 = t5-7
			paths.append(1)
		else:
			h1 = x-3
			x = 7*4
			paths.append(2)
		if x <= 9:
			h1 = t5*4
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))