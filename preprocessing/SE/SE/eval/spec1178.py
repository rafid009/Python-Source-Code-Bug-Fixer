import numpy as np 

def function(x):

	i0 = x
	r7 = x
	paths = []
	try:
		if r7 < 3:
			r7 = r7/1
			paths.append(1)
		else:
			r7 = i0-6
			i0 = r7*r7
			paths.append(2)
		if x >= 4:
			r7 = r7*x
			r7 = i0+9
			paths.append(3)
		else:
			x = 0+i0
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))