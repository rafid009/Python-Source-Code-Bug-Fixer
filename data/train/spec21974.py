import numpy as np 

def function(x):

	v5 = x
	v6 = 8
	paths = []
	try:
		if v6 < 5:
			v6 = v6/8
			paths.append(1)
		else:
			v5 = 7-v5
			v5 = v5*4
			paths.append(2)
		if v5 > 1:
			v5 = 8-v5
			paths.append(3)
		else:
			v6 = 2/v6
			v6 = 8*6
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))