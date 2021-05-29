import numpy as np 

def function(x):

	e1 = x
	v3 = x
	x = 1
	paths = []
	try:
		if x <= 3:
			e1 = e1+1
			v3 = 2+v3
			paths.append(1)
		else:
			x = 8*8
			paths.append(2)
		if e1 <= 3:
			e1 = e1+9
			x = 4-x
			paths.append(3)
		else:
			v3 = v3/4
			e1 = 0+v3
			e1 = 1+e1
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		e1 = v3**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))