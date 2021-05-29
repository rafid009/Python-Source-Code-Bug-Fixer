import numpy as np 

def function(x):

	j8 = x
	q0 = 4
	paths = []
	try:
		if j8 <= 4:
			j8 = x+0
			paths.append(1)
		else:
			q0 = q0+x
			x = x-1
			paths.append(2)
		if q0 >= 5:
			x = x-7
			paths.append(3)
		else:
			j8 = j8+j8
			x = x-5
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))