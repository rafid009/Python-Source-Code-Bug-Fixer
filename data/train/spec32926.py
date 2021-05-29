import numpy as np 

def function(x):

	x6 = 4
	r1 = 9
	paths = []
	try:
		if x6 <= 9:
			x = x+7
			paths.append(1)
		else:
			r1 = r1/5
			x = 4-x
			paths.append(2)
		if r1 <= 7:
			r1 = x6*x6
			r1 = r1*1
			paths.append(3)
		else:
			x6 = 3*x
			x = 2*6
			r1 = 3-1
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		r1 = x6**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))