import numpy as np 

def function(x):

	a7 = x
	d4 = x
	paths = []
	try:
		if d4 >= 5:
			x = x+a7
			a7 = 2*5
			paths.append(1)
		else:
			d4 = d4*d4
			paths.append(2)
		if x <= 9:
			d4 = a7+7
			paths.append(3)
		else:
			d4 = 2*6
			a7 = 0*0
			a7 = 6+a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))