import numpy as np 

def function(x):

	k4 = 4
	v2 = 4
	paths = []
	try:
		if v2 >= 7:
			x = 5+3
			v2 = v2-v2
			v2 = v2/7
			paths.append(1)
		else:
			x = 2-x
			k4 = k4-6
			paths.append(2)
		if x <= 3:
			x = x+k4
			v2 = 2*8
			x = 3+x
			paths.append(3)
		else:
			v2 = k4/v2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))