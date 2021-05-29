import numpy as np 

def function(x):

	h1 = x
	l5 = x
	paths = []
	try:
		if l5 <= 0:
			l5 = l5*x
			h1 = h1*h1
			h1 = x*h1
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if l5 > 4:
			l5 = x/h1
			h1 = h1-l5
			x = x-4
			paths.append(3)
		else:
			x = x*5
			x = x*x
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))