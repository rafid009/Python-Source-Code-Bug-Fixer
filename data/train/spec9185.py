import numpy as np 

def function(x):

	r9 = 7
	p6 = x
	paths = []
	try:
		if x < 4:
			x = x-5
			x = x/7
			p6 = p6*1
			paths.append(1)
		else:
			p6 = 9/p6
			p6 = x/2
			r9 = r9-0
			paths.append(2)
		if r9 >= 0:
			r9 = 0/r9
			x = 1*x
			r9 = 2*3
			paths.append(3)
		else:
			r9 = 8+r9
			p6 = 8-r9
			x = x/7
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		r9 = p6**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))