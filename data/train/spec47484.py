import numpy as np 

def function(x):

	h1 = x
	b3 = x
	paths = []
	try:
		if x <= 3:
			b3 = b3/4
			h1 = 5+0
			paths.append(1)
		else:
			x = b3+x
			b3 = b3-8
			paths.append(2)
		if h1 <= 9:
			h1 = x-8
			x = 5/x
			paths.append(3)
		else:
			b3 = 3*b3
			h1 = 7/h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		b3 = h1**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))