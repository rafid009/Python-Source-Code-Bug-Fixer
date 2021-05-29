import numpy as np 

def function(x):

	v2 = x
	k6 = x
	x = x
	paths = []
	try:
		if x > 6:
			k6 = 8/2
			x = 7+x
			paths.append(1)
		else:
			v2 = 3-9
			paths.append(2)
		if x <= 2:
			v2 = v2*2
			v2 = 8+v2
			k6 = k6*v2
			paths.append(3)
		else:
			x = 8+5
			v2 = k6*2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		v2 = k6**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))