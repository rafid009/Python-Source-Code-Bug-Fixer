import numpy as np 

def function(x):

	r1 = 7
	v3 = 4
	x = x
	paths = []
	try:
		if v3 > 5:
			x = 4*v3
			paths.append(1)
		else:
			r1 = r1/v3
			x = v3/3
			paths.append(2)
		if v3 < 6:
			r1 = 6+r1
			v3 = v3-9
			paths.append(3)
		else:
			x = 9+v3
			v3 = v3*8
			v3 = r1/8
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		r1 = v3**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))