import numpy as np 

def function(x):

	e1 = 2
	v4 = 7
	paths = []
	try:
		if e1 < 9:
			e1 = x/3
			v4 = v4*e1
			x = x+v4
			paths.append(1)
		else:
			x = x*3
			x = e1-x
			paths.append(2)
		if v4 < 3:
			e1 = e1*1
			e1 = e1+e1
			paths.append(3)
		else:
			v4 = 8*v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))