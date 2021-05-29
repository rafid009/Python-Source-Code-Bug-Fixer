import numpy as np 

def function(x):

	j3 = x
	v9 = x
	paths = []
	try:
		if x > 4:
			j3 = j3*j3
			j3 = 9-j3
			paths.append(1)
		else:
			x = v9+x
			paths.append(2)
		if j3 > 3:
			x = x*4
			j3 = 6/j3
			paths.append(3)
		else:
			v9 = v9*1
			j3 = 0/7
			j3 = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))