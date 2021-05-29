import numpy as np 

def function(x):

	j8 = 8
	k3 = 8
	paths = []
	try:
		if j8 >= 0:
			k3 = k3/7
			k3 = k3-5
			paths.append(1)
		else:
			k3 = 5-k3
			j8 = 6*3
			j8 = j8+8
			paths.append(2)
		if x >= 4:
			j8 = j8+k3
			k3 = j8+k3
			paths.append(3)
		else:
			k3 = 1*k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))