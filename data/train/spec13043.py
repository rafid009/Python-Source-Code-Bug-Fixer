import numpy as np 

def function(x):

	h1 = 0
	i5 = x
	paths = []
	try:
		if i5 < 2:
			h1 = i5+h1
			paths.append(1)
		else:
			x = 6*0
			h1 = i5+h1
			paths.append(2)
		if i5 < 6:
			i5 = 9+i5
			x = x*8
			i5 = 9-i5
			paths.append(3)
		else:
			x = 1+5
			h1 = 7/h1
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