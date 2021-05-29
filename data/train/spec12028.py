import numpy as np 

def function(x):

	t2 = x
	d6 = 9
	paths = []
	try:
		if x >= 4:
			t2 = d6-d6
			x = 9-7
			paths.append(1)
		else:
			d6 = d6*3
			t2 = t2-8
			paths.append(2)
		if x > 6:
			d6 = 7/d6
			paths.append(3)
		else:
			t2 = x*1
			d6 = 2+d6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))