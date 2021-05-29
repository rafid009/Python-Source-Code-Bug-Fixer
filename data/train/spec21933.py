import numpy as np 

def function(x):

	v1 = 8
	k6 = 9
	paths = []
	try:
		if x <= 8:
			x = x*8
			x = 6+x
			x = x+3
			paths.append(1)
		else:
			k6 = k6*v1
			k6 = k6+5
			paths.append(2)
		if k6 > 7:
			v1 = v1-9
			paths.append(3)
		else:
			v1 = v1/9
			k6 = 4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))