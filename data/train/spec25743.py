import numpy as np 

def function(x):

	a0 = 5
	v8 = x
	paths = []
	try:
		if a0 > 1:
			a0 = a0/3
			x = x*1
			paths.append(1)
		else:
			a0 = a0/6
			a0 = 0/a0
			v8 = 9+v8
			paths.append(2)
		if v8 < 9:
			a0 = 1+2
			v8 = v8-2
			v8 = v8+5
			paths.append(3)
		else:
			a0 = a0*1
			a0 = a0/7
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))