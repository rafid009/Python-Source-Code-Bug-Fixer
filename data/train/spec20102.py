import numpy as np 

def function(x):

	e2 = 4
	v8 = x
	paths = []
	try:
		if v8 <= 1:
			x = 7+x
			paths.append(1)
		else:
			v8 = v8/8
			e2 = 6/x
			paths.append(2)
		if x <= 4:
			x = x+9
			paths.append(3)
		else:
			v8 = 5+v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		e2 = v8**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))