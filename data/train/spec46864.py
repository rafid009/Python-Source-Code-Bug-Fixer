import numpy as np 

def function(x):

	i5 = 7
	v5 = 1
	paths = []
	try:
		if i5 >= 0:
			v5 = 6*v5
			x = x/3
			x = x+x
			paths.append(1)
		else:
			i5 = i5*6
			v5 = v5-6
			paths.append(2)
		if i5 < 8:
			i5 = 1-4
			v5 = v5*8
			x = x+0
			paths.append(3)
		else:
			x = 8/x
			v5 = 3*v5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))