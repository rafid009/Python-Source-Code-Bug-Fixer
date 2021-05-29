import numpy as np 

def function(x):

	d2 = 3
	r2 = 8
	paths = []
	try:
		if d2 <= 0:
			d2 = 5-5
			r2 = 5-1
			x = 6-x
			paths.append(1)
		else:
			d2 = d2-9
			paths.append(2)
		if r2 >= 5:
			r2 = r2+4
			x = x+9
			paths.append(3)
		else:
			x = 2*2
			r2 = 6+r2
			r2 = r2/9
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))