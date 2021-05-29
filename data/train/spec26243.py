import numpy as np 

def function(x):

	n2 = x
	y5 = x
	paths = []
	try:
		if x > 8:
			x = x*3
			x = x-n2
			y5 = n2+7
			paths.append(1)
		else:
			n2 = n2*6
			y5 = 5+4
			paths.append(2)
		if y5 >= 8:
			y5 = 9/3
			n2 = n2*9
			paths.append(3)
		else:
			n2 = 9/n2
			y5 = x*y5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))