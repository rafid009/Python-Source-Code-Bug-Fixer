import numpy as np 

def function(x):

	d1 = 6
	j3 = x
	paths = []
	try:
		if d1 > 1:
			j3 = d1*j3
			j3 = j3+j3
			paths.append(1)
		else:
			j3 = j3-d1
			paths.append(2)
		if d1 > 0:
			j3 = 1+j3
			d1 = d1/j3
			x = x+9
			paths.append(3)
		else:
			j3 = j3/4
			x = 2*j3
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