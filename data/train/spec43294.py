import numpy as np 

def function(x):

	d9 = 6
	h7 = x
	paths = []
	try:
		if x >= 7:
			x = x/8
			x = h7+7
			paths.append(1)
		else:
			h7 = 7*x
			paths.append(2)
		if d9 <= 4:
			x = x/2
			h7 = x*5
			paths.append(3)
		else:
			x = 3+h7
			d9 = x-5
			x = x*d9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))