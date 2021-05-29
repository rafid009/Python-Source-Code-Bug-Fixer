import numpy as np 

def function(x):

	r6 = x
	d2 = x
	paths = []
	try:
		if x > 3:
			d2 = d2*0
			paths.append(1)
		else:
			r6 = 4+7
			paths.append(2)
		if d2 >= 5:
			d2 = 1/x
			d2 = d2-2
			r6 = r6-2
			paths.append(3)
		else:
			r6 = r6-6
			x = 9-8
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))