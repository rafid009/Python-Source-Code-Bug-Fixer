import numpy as np 

def function(x):

	b2 = x
	x9 = 7
	x = x
	paths = []
	try:
		if b2 < 2:
			b2 = b2+0
			x9 = 5/x9
			x9 = x9/x
			paths.append(1)
		else:
			b2 = b2+b2
			paths.append(2)
		if x >= 3:
			x9 = x9+x
			x9 = x9-6
			paths.append(3)
		else:
			x = x*2
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))