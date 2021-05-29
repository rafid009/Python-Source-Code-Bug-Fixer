import numpy as np 

def function(x):

	h1 = x
	l5 = 4
	paths = []
	try:
		if x > 6:
			l5 = l5-l5
			paths.append(1)
		else:
			h1 = h1+1
			x = 8+l5
			paths.append(2)
		if h1 > 4:
			h1 = 6/1
			paths.append(3)
		else:
			h1 = h1/2
			x = 1+x
			x = x-8
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		l5 = h1**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))