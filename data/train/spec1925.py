import numpy as np 

def function(x):

	r6 = 0
	j4 = x
	paths = []
	try:
		if x <= 6:
			r6 = r6*r6
			x = 2*j4
			paths.append(1)
		else:
			r6 = 0-7
			paths.append(2)
		if x >= 8:
			r6 = r6-5
			j4 = j4+4
			paths.append(3)
		else:
			r6 = 5*0
			x = x-4
			r6 = r6-8
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))