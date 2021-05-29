import numpy as np 

def function(x):

	v1 = x
	j3 = x
	paths = []
	try:
		if v1 > 6:
			j3 = 9/5
			v1 = v1/4
			paths.append(1)
		else:
			v1 = v1-1
			paths.append(2)
		if v1 < 9:
			j3 = v1+7
			x = 1-9
			j3 = 5*j3
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))