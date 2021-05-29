import numpy as np 

def function(x):

	v8 = 7
	a2 = x
	paths = []
	try:
		if v8 <= 8:
			a2 = a2+7
			x = x/2
			paths.append(1)
		else:
			v8 = v8*3
			a2 = a2*3
			a2 = 9/a2
			paths.append(2)
		if v8 < 1:
			x = a2/a2
			paths.append(3)
		else:
			x = x+2
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))