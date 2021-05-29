import numpy as np 

def function(x):

	h3 = x
	k7 = 3
	paths = []
	try:
		if x <= 9:
			k7 = x*k7
			k7 = h3/k7
			paths.append(1)
		else:
			x = h3+0
			x = 0/k7
			paths.append(2)
		if x > 4:
			h3 = h3*9
			paths.append(3)
		else:
			h3 = h3+5
			h3 = h3+h3
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