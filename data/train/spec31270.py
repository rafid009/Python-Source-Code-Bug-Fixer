import numpy as np 

def function(x):

	d2 = x
	r6 = 7
	x = x
	paths = []
	try:
		if r6 < 3:
			r6 = 3-r6
			x = 3*d2
			x = 5/x
			paths.append(1)
		else:
			r6 = 4/4
			paths.append(2)
		if d2 > 4:
			x = 1*x
			x = r6/x
			x = 9-x
			paths.append(3)
		else:
			d2 = d2/6
			r6 = d2*0
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		r6 = d2**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))