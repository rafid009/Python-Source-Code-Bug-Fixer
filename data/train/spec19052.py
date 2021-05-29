import numpy as np 

def function(x):

	r2 = x
	d8 = x
	paths = []
	try:
		if d8 <= 3:
			r2 = r2+x
			r2 = x+r2
			paths.append(1)
		else:
			d8 = d8*4
			x = x-6
			d8 = 2-d8
			paths.append(2)
		if d8 >= 7:
			r2 = r2+x
			r2 = r2+5
			r2 = 7*3
			paths.append(3)
		else:
			d8 = d8+3
			r2 = 4/x
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		d8 = r2**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))