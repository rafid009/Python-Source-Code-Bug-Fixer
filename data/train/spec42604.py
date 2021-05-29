import numpy as np 

def function(x):

	j3 = 4
	v1 = x
	paths = []
	try:
		if j3 <= 7:
			v1 = v1-5
			paths.append(1)
		else:
			j3 = 0-5
			paths.append(2)
		if x < 9:
			j3 = x+x
			paths.append(3)
		else:
			j3 = j3*6
			j3 = x+1
			j3 = v1*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))