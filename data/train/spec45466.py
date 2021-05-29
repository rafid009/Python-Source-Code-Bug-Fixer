import numpy as np 

def function(x):

	j5 = x
	k3 = 9
	paths = []
	try:
		if k3 > 4:
			j5 = j5/3
			k3 = 8*k3
			paths.append(1)
		else:
			j5 = k3*j5
			paths.append(2)
		if k3 <= 2:
			j5 = k3-0
			k3 = 9*j5
			j5 = j5-5
			paths.append(3)
		else:
			k3 = k3+6
			j5 = x/j5
			j5 = x*k3
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))