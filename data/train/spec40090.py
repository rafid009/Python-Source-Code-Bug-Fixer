import numpy as np 

def function(x):

	r6 = 1
	b3 = x
	paths = []
	try:
		if x <= 4:
			r6 = r6+0
			paths.append(1)
		else:
			b3 = b3-8
			paths.append(2)
		if b3 >= 1:
			r6 = 6/r6
			b3 = b3/2
			paths.append(3)
		else:
			x = 0/x
			x = x+2
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))