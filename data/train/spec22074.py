import numpy as np 

def function(x):

	k4 = x
	v3 = x
	paths = []
	try:
		if v3 > 4:
			k4 = k4-k4
			k4 = k4+v3
			paths.append(1)
		else:
			k4 = k4-k4
			k4 = v3*v3
			paths.append(2)
		if x >= 4:
			x = k4*4
			paths.append(3)
		else:
			v3 = v3+7
			v3 = k4-v3
			x = 1+0
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		k4 = v3**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))