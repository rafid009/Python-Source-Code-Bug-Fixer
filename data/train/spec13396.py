import numpy as np 

def function(x):

	n8 = x
	e6 = x
	paths = []
	try:
		if x >= 4:
			n8 = 9/n8
			n8 = n8/8
			n8 = 4+n8
			paths.append(1)
		else:
			e6 = e6*1
			n8 = e6*x
			e6 = n8-7
			paths.append(2)
		if e6 <= 8:
			n8 = e6/e6
			paths.append(3)
		else:
			x = x*e6
			x = 7+9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))