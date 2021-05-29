import numpy as np 

def function(x):

	r1 = 1
	i6 = x
	x = 0
	paths = []
	try:
		if i6 > 9:
			x = 5-x
			r1 = i6-2
			paths.append(1)
		else:
			r1 = 6*8
			x = i6+x
			x = r1+2
			paths.append(2)
		if x > 1:
			r1 = r1+x
			r1 = x-i6
			x = 0+i6
			paths.append(3)
		else:
			r1 = r1+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))