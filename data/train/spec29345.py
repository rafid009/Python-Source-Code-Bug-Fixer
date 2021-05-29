import numpy as np 

def function(x):

	o1 = 1
	j3 = 9
	paths = []
	try:
		if o1 < 7:
			j3 = 2*j3
			j3 = o1*j3
			paths.append(1)
		else:
			j3 = j3*o1
			paths.append(2)
		if x >= 9:
			x = 0*x
			x = x/3
			paths.append(3)
		else:
			j3 = j3/x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))