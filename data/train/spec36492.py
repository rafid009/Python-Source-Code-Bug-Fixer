import numpy as np 

def function(x):

	k5 = x
	v6 = 7
	paths = []
	try:
		if k5 > 2:
			x = x*2
			x = 2-v6
			k5 = 9-x
			paths.append(1)
		else:
			v6 = v6+k5
			k5 = x+k5
			k5 = k5-v6
			paths.append(2)
		if x > 6:
			k5 = k5*v6
			paths.append(3)
		else:
			k5 = 0-k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		v6 = k5**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))