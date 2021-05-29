import numpy as np 

def function(x):

	j2 = 6
	i2 = 6
	paths = []
	try:
		if i2 >= 3:
			j2 = x-j2
			paths.append(1)
		else:
			j2 = 5-5
			paths.append(2)
		if j2 < 1:
			x = 3/i2
			paths.append(3)
		else:
			j2 = j2*j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))