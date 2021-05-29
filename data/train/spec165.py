import numpy as np 

def function(x):

	v5 = x
	e2 = 2
	paths = []
	try:
		if v5 > 6:
			e2 = 5*6
			v5 = v5-2
			v5 = v5*1
			paths.append(1)
		else:
			v5 = 6-x
			paths.append(2)
		if e2 < 0:
			e2 = 5+3
			e2 = e2+v5
			e2 = 1/3
			paths.append(3)
		else:
			e2 = e2/x
			v5 = 2/9
			v5 = v5+e2
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))