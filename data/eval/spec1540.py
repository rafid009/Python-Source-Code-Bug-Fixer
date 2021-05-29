import numpy as np 

def function(x):

	b3 = 9
	n4 = 1
	paths = []
	try:
		if b3 <= 6:
			n4 = 6+x
			n4 = 9/5
			n4 = x+6
			paths.append(1)
		else:
			n4 = 5-n4
			paths.append(2)
		if x < 7:
			x = x*x
			b3 = n4-b3
			b3 = b3*6
			paths.append(3)
		else:
			x = x-9
			n4 = x*8
			n4 = n4-6
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))