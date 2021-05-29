import numpy as np 

def function(x):

	h3 = x
	h1 = 3
	paths = []
	try:
		if h1 <= 9:
			h1 = h1/5
			h3 = h3*2
			h1 = 2-5
			paths.append(1)
		else:
			x = 9+9
			h1 = x*h1
			h1 = 3+8
			paths.append(2)
		if h3 >= 5:
			h3 = h3*0
			h1 = h1+1
			h1 = h1*h1
			paths.append(3)
		else:
			h1 = 0-8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))