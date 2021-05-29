import numpy as np 

def function(x):

	v2 = 1
	i6 = 3
	paths = []
	try:
		if i6 > 2:
			x = x*2
			x = x/8
			v2 = v2*7
			paths.append(1)
		else:
			x = 8+2
			i6 = x-v2
			v2 = v2-6
			paths.append(2)
		if v2 < 3:
			v2 = v2/x
			x = 1+v2
			v2 = 6-4
			paths.append(3)
		else:
			i6 = i6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))