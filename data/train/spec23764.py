import numpy as np 

def function(x):

	m5 = x
	r9 = 9
	paths = []
	try:
		if x >= 6:
			x = x-9
			r9 = 4*r9
			paths.append(1)
		else:
			r9 = 8+1
			paths.append(2)
		if r9 > 4:
			x = x-8
			r9 = x*r9
			r9 = 1*r9
			paths.append(3)
		else:
			r9 = 5/9
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))