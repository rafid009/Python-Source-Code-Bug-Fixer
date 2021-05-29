import numpy as np 

def function(x):

	v1 = x
	e6 = x
	paths = []
	try:
		if e6 > 1:
			x = x*e6
			v1 = v1+9
			e6 = e6*3
			paths.append(1)
		else:
			e6 = e6*8
			v1 = v1/2
			v1 = v1-9
			paths.append(2)
		if x < 7:
			x = x-1
			v1 = x/v1
			v1 = v1+6
			paths.append(3)
		else:
			v1 = v1/e6
			v1 = e6+9
			v1 = v1-x
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		e6 = v1**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))