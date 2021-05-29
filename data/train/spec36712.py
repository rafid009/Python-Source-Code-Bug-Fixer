import numpy as np 

def function(x):

	r0 = x
	d2 = 6
	paths = []
	try:
		if x < 1:
			d2 = d2+9
			paths.append(1)
		else:
			r0 = 0+r0
			paths.append(2)
		if d2 <= 8:
			r0 = 9/x
			d2 = d2-x
			r0 = 5-3
			paths.append(3)
		else:
			d2 = d2*9
			r0 = 3-9
			x = 7+6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		d2 = r0**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))