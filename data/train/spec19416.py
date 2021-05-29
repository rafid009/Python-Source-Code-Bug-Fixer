import numpy as np 

def function(x):

	v1 = 4
	j3 = x
	paths = []
	try:
		if v1 >= 1:
			x = x-j3
			paths.append(1)
		else:
			j3 = x*1
			v1 = 8+3
			paths.append(2)
		if j3 <= 4:
			x = x/4
			x = 8+9
			paths.append(3)
		else:
			x = 0-1
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		v1 = j3**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))