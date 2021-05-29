import numpy as np 

def function(x):

	a4 = 9
	d8 = 0
	paths = []
	try:
		if x <= 8:
			a4 = a4*a4
			a4 = a4+d8
			paths.append(1)
		else:
			a4 = 3-x
			a4 = a4-x
			x = x*2
			paths.append(2)
		if d8 <= 1:
			x = x*4
			paths.append(3)
		else:
			d8 = 5/5
			x = x/6
			x = x-1
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		d8 = a4**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))