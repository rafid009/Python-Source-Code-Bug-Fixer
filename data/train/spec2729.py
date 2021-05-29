import numpy as np 

def function(x):

	v5 = 8
	i0 = x
	paths = []
	try:
		if i0 >= 2:
			x = 2*7
			i0 = 9/8
			x = x*4
			paths.append(1)
		else:
			v5 = 5*x
			i0 = 3*i0
			paths.append(2)
		if x > 3:
			i0 = i0*i0
			v5 = v5+i0
			i0 = 6/i0
			paths.append(3)
		else:
			i0 = i0*0
			v5 = v5+v5
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