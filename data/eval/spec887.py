import numpy as np 

def function(x):

	e6 = 2
	v1 = 3
	paths = []
	try:
		if v1 >= 0:
			v1 = 9+7
			v1 = 9/v1
			paths.append(1)
		else:
			x = 2+x
			x = 7*4
			paths.append(2)
		if e6 > 2:
			x = v1*1
			e6 = e6+e6
			paths.append(3)
		else:
			v1 = x+e6
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