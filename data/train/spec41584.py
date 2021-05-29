import numpy as np 

def function(x):

	t6 = 6
	d0 = 3
	paths = []
	try:
		if t6 > 6:
			x = x*7
			t6 = 9/t6
			paths.append(1)
		else:
			x = t6-x
			x = x-6
			d0 = d0+t6
			paths.append(2)
		if x > 4:
			x = t6-x
			paths.append(3)
		else:
			x = 1*0
			x = x*5
			t6 = 6-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))