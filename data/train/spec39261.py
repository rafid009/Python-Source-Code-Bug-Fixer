import numpy as np 

def function(x):

	p0 = x
	v9 = x
	x = x
	paths = []
	try:
		if x >= 2:
			v9 = p0-4
			paths.append(1)
		else:
			p0 = p0-6
			p0 = v9/p0
			p0 = p0*0
			paths.append(2)
		if x < 8:
			v9 = 4-9
			paths.append(3)
		else:
			p0 = 9*p0
			v9 = 8+v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))