import numpy as np 

def function(x):

	l3 = x
	r9 = x
	paths = []
	try:
		if r9 >= 6:
			x = 9-8
			x = x*3
			paths.append(1)
		else:
			l3 = 2/x
			paths.append(2)
		if l3 > 1:
			l3 = l3*1
			r9 = r9*r9
			paths.append(3)
		else:
			l3 = l3+5
			r9 = r9/3
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