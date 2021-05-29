import numpy as np 

def function(x):

	r5 = 3
	j3 = x
	paths = []
	try:
		if r5 <= 4:
			x = x+7
			paths.append(1)
		else:
			j3 = j3-x
			paths.append(2)
		if r5 >= 9:
			r5 = r5-r5
			paths.append(3)
		else:
			r5 = x*r5
			j3 = j3+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))