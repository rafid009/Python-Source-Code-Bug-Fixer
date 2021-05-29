import numpy as np 

def function(x):

	n4 = 9
	u4 = 7
	paths = []
	try:
		if u4 <= 8:
			n4 = n4-6
			paths.append(1)
		else:
			n4 = n4/9
			u4 = 2+x
			paths.append(2)
		if x <= 4:
			x = x*2
			x = x-x
			paths.append(3)
		else:
			x = 4-u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))