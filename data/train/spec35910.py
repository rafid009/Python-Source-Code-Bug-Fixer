import numpy as np 

def function(x):

	n2 = x
	y5 = 8
	paths = []
	try:
		if n2 > 8:
			y5 = 0-y5
			x = x*2
			n2 = n2*n2
			paths.append(1)
		else:
			n2 = 5-n2
			paths.append(2)
		if x < 9:
			x = n2*y5
			y5 = 6-x
			x = y5-1
			paths.append(3)
		else:
			n2 = y5/n2
			y5 = y5*n2
			n2 = n2+1
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		n2 = y5**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))