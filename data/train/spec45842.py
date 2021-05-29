import numpy as np 

def function(x):

	r9 = x
	j6 = x
	paths = []
	try:
		if r9 >= 2:
			x = 0*x
			paths.append(1)
		else:
			x = x+r9
			r9 = 5-x
			r9 = 5*9
			paths.append(2)
		if j6 > 7:
			x = x-1
			j6 = j6-8
			paths.append(3)
		else:
			r9 = r9-6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		r9 = j6**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))