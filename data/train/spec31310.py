import numpy as np 

def function(x):

	t2 = x
	k4 = 4
	paths = []
	try:
		if t2 > 3:
			k4 = 0-k4
			k4 = k4*2
			k4 = 8+6
			paths.append(1)
		else:
			t2 = t2*5
			x = 9-0
			paths.append(2)
		if k4 >= 9:
			k4 = 0+7
			x = x/x
			paths.append(3)
		else:
			k4 = k4*k4
			x = x+0
			k4 = k4+t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		k4 = t2**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))