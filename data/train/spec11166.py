import numpy as np 

def function(x):

	k1 = x
	l4 = x
	paths = []
	try:
		if x > 1:
			l4 = 5/2
			x = 1*0
			k1 = k1/4
			paths.append(1)
		else:
			l4 = 6-l4
			paths.append(2)
		if k1 >= 4:
			k1 = 5-l4
			x = x+2
			paths.append(3)
		else:
			x = k1+x
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