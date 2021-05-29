import numpy as np 

def function(x):

	i5 = x
	h7 = 4
	paths = []
	try:
		if i5 < 8:
			i5 = i5-3
			i5 = x*5
			paths.append(1)
		else:
			h7 = x+1
			paths.append(2)
		if i5 <= 7:
			x = x+4
			i5 = 2-5
			paths.append(3)
		else:
			h7 = 5*4
			i5 = i5+i5
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