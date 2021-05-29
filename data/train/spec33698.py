import numpy as np 

def function(x):

	r3 = 3
	v3 = x
	paths = []
	try:
		if x < 9:
			v3 = x-4
			v3 = 4-9
			x = x-2
			paths.append(1)
		else:
			r3 = 6/r3
			r3 = r3+v3
			paths.append(2)
		if r3 <= 6:
			r3 = 7*r3
			r3 = r3*v3
			paths.append(3)
		else:
			v3 = 5-v3
			r3 = 3*r3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))