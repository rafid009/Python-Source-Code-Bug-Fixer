import numpy as np 

def function(x):

	i4 = x
	r1 = 3
	paths = []
	try:
		if x < 8:
			i4 = i4+r1
			i4 = 2+i4
			r1 = r1*i4
			paths.append(1)
		else:
			x = 5+6
			i4 = i4+6
			paths.append(2)
		if i4 > 3:
			i4 = 0+x
			paths.append(3)
		else:
			x = 7-4
			x = i4/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))