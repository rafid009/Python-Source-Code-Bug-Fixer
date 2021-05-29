import numpy as np 

def function(x):

	d1 = 8
	a4 = x
	paths = []
	try:
		if d1 >= 4:
			d1 = d1+0
			a4 = a4/7
			a4 = a4*4
			paths.append(1)
		else:
			d1 = d1/9
			paths.append(2)
		if a4 <= 7:
			d1 = 2/2
			d1 = 3+6
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))