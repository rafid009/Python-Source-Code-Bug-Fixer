import numpy as np 

def function(x):

	d9 = 7
	r2 = 3
	x = x
	paths = []
	try:
		if d9 < 0:
			x = x*1
			x = 6-x
			x = x+3
			paths.append(1)
		else:
			r2 = r2*1
			paths.append(2)
		if r2 >= 3:
			d9 = x*r2
			d9 = x/8
			paths.append(3)
		else:
			d9 = 9/5
			d9 = d9*r2
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))