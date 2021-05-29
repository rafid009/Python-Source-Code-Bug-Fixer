import numpy as np 

def function(x):

	a1 = x
	d1 = x
	paths = []
	try:
		if x < 4:
			x = a1*3
			a1 = 1+1
			paths.append(1)
		else:
			d1 = 5+d1
			a1 = a1+7
			paths.append(2)
		if a1 <= 5:
			d1 = d1+9
			d1 = a1*9
			paths.append(3)
		else:
			a1 = 4*a1
			d1 = x+8
			d1 = a1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))