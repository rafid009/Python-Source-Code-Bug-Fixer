import numpy as np 

def function(x):

	p8 = 0
	v1 = x
	x = x
	paths = []
	try:
		if p8 >= 0:
			p8 = p8+v1
			paths.append(1)
		else:
			x = x*v1
			v1 = v1+8
			v1 = 5-x
			paths.append(2)
		if p8 < 4:
			p8 = p8-5
			paths.append(3)
		else:
			p8 = p8/p8
			x = x*8
			v1 = 2+v1
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		v1 = p8**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))