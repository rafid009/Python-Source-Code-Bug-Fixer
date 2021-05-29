import numpy as np 

def function(x):

	r5 = 2
	d6 = 5
	paths = []
	try:
		if d6 >= 7:
			d6 = x*x
			x = x*5
			paths.append(1)
		else:
			d6 = d6+3
			d6 = d6+x
			paths.append(2)
		if r5 > 1:
			r5 = 3+r5
			paths.append(3)
		else:
			x = 5/8
			r5 = 3+d6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))