import numpy as np 

def function(x):

	d0 = 7
	r5 = x
	x = 9
	paths = []
	try:
		if x <= 1:
			r5 = r5-r5
			r5 = r5+9
			x = x*6
			paths.append(1)
		else:
			x = x+x
			x = 6-5
			paths.append(2)
		if x > 0:
			x = x+6
			x = x+x
			r5 = r5*5
			paths.append(3)
		else:
			d0 = r5/d0
			r5 = r5+d0
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		d0 = r5**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))