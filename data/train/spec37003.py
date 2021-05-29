import numpy as np 

def function(x):

	b4 = x
	n7 = 6
	x = 8
	paths = []
	try:
		if x < 5:
			x = 3-6
			x = x-5
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if x <= 8:
			b4 = b4/4
			n7 = n7/b4
			n7 = n7+b4
			paths.append(3)
		else:
			x = 3+5
			n7 = 6+4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		n7 = b4**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))