import numpy as np 

def function(x):

	w6 = 5
	b3 = 9
	paths = []
	try:
		if b3 < 7:
			w6 = b3+3
			x = x+6
			x = b3-x
			paths.append(1)
		else:
			w6 = x*8
			w6 = 7/9
			paths.append(2)
		if x >= 6:
			w6 = 6/w6
			w6 = w6+9
			b3 = 2/b3
			paths.append(3)
		else:
			x = x/7
			x = w6+x
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