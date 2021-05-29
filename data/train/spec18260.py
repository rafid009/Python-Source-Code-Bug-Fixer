import numpy as np 

def function(x):

	r9 = 4
	d6 = 8
	x = 5
	paths = []
	try:
		if x >= 6:
			r9 = 2*d6
			d6 = d6/d6
			paths.append(1)
		else:
			r9 = r9-6
			d6 = 6-x
			d6 = 1+x
			paths.append(2)
		if r9 >= 7:
			r9 = 4-r9
			d6 = d6*9
			paths.append(3)
		else:
			d6 = d6*r9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))