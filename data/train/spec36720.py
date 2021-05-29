import numpy as np 

def function(x):

	v4 = 7
	j3 = x
	paths = []
	try:
		if v4 <= 5:
			x = 0-v4
			paths.append(1)
		else:
			x = x*j3
			x = 3+x
			paths.append(2)
		if j3 > 5:
			x = j3/x
			v4 = 4/v4
			v4 = v4/5
			paths.append(3)
		else:
			v4 = v4+7
			v4 = v4*5
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))