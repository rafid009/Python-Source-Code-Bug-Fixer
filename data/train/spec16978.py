import numpy as np 

def function(x):

	v0 = x
	j3 = 6
	paths = []
	try:
		if j3 <= 4:
			x = x-5
			v0 = j3+5
			j3 = j3-0
			paths.append(1)
		else:
			j3 = j3/v0
			paths.append(2)
		if v0 >= 6:
			x = x*j3
			x = x+3
			paths.append(3)
		else:
			j3 = j3/2
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))