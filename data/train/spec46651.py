import numpy as np 

def function(x):

	v5 = x
	o0 = 9
	paths = []
	try:
		if v5 >= 6:
			x = 8*x
			v5 = v5+v5
			v5 = v5/o0
			paths.append(1)
		else:
			v5 = 5/o0
			x = 2-x
			v5 = 5+v5
			paths.append(2)
		if v5 <= 4:
			o0 = o0+7
			paths.append(3)
		else:
			v5 = v5*o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))