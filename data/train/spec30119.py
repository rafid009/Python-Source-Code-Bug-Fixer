import numpy as np 

def function(x):

	j4 = 6
	k3 = x
	paths = []
	try:
		if x < 2:
			j4 = 9+x
			x = k3*x
			paths.append(1)
		else:
			x = 3+x
			x = x-5
			x = 7-8
			paths.append(2)
		if k3 >= 7:
			x = x/x
			k3 = k3+5
			j4 = j4/1
			paths.append(3)
		else:
			x = x-0
			x = x*x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))