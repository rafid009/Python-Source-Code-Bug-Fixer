import numpy as np 

def function(x):

	i3 = x
	r6 = 8
	paths = []
	try:
		if x >= 3:
			r6 = 0-1
			x = 5*x
			paths.append(1)
		else:
			r6 = r6+5
			r6 = 6-0
			i3 = 3*6
			paths.append(2)
		if r6 > 0:
			i3 = i3*3
			paths.append(3)
		else:
			i3 = i3+4
			i3 = 3*1
			x = 2/r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))