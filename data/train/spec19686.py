import numpy as np 

def function(x):

	v8 = x
	a9 = x
	x = 4
	paths = []
	try:
		if v8 <= 8:
			v8 = v8/a9
			v8 = v8+v8
			v8 = v8+v8
			paths.append(1)
		else:
			x = x/1
			x = x+9
			v8 = v8+v8
			paths.append(2)
		if v8 < 5:
			x = v8+a9
			paths.append(3)
		else:
			x = x*9
			a9 = x/a9
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))