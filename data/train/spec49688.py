import numpy as np 

def function(x):

	v3 = x
	r3 = x
	paths = []
	try:
		if r3 >= 2:
			v3 = 1*2
			paths.append(1)
		else:
			v3 = 4/x
			r3 = 5-r3
			paths.append(2)
		if v3 <= 6:
			x = x/8
			v3 = v3*x
			r3 = 1-v3
			paths.append(3)
		else:
			v3 = v3*4
			r3 = r3+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))