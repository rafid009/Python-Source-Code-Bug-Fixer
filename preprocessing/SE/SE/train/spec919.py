import numpy as np 

def function(x):

	v4 = x
	q5 = 8
	paths = []
	try:
		if x > 9:
			v4 = v4+4
			q5 = q5*q5
			v4 = 1-4
			paths.append(1)
		else:
			v4 = 4+v4
			paths.append(2)
		if q5 > 4:
			x = x+2
			x = 4+x
			paths.append(3)
		else:
			q5 = q5/v4
			x = 8*4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))