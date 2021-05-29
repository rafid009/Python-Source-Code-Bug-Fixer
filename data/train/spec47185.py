import numpy as np 

def function(x):

	r0 = x
	d6 = 2
	paths = []
	try:
		if r0 >= 9:
			r0 = r0*4
			r0 = d6+7
			x = x/2
			paths.append(1)
		else:
			x = d6-d6
			d6 = d6/9
			paths.append(2)
		if x > 1:
			r0 = r0-3
			x = d6/4
			x = 8*9
			paths.append(3)
		else:
			x = x+7
			d6 = d6/1
			d6 = 6*d6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))