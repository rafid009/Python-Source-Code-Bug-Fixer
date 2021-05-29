import numpy as np 

def function(x):

	b6 = 1
	n5 = x
	paths = []
	try:
		if b6 > 9:
			x = b6+x
			paths.append(1)
		else:
			b6 = n5-n5
			n5 = n5-7
			n5 = n5*6
			paths.append(2)
		if x <= 6:
			b6 = 3*1
			paths.append(3)
		else:
			b6 = b6+x
			x = 1/x
			n5 = n5/7
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))