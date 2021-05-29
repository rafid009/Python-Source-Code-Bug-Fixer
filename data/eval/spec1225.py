import numpy as np 

def function(x):

	e6 = 8
	d7 = 6
	paths = []
	try:
		if x > 3:
			x = x/1
			d7 = 2-x
			e6 = 7-e6
			paths.append(1)
		else:
			e6 = e6/5
			paths.append(2)
		if e6 >= 5:
			e6 = e6+x
			e6 = 8*e6
			e6 = 8*e6
			paths.append(3)
		else:
			d7 = d7-x
			d7 = d7*x
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