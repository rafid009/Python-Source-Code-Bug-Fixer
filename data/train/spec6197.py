import numpy as np 

def function(x):

	b4 = x
	v9 = x
	paths = []
	try:
		if x >= 5:
			x = x*b4
			b4 = b4-b4
			paths.append(1)
		else:
			v9 = 6*v9
			paths.append(2)
		if b4 > 9:
			x = 4*v9
			x = 2*x
			b4 = 2+4
			paths.append(3)
		else:
			x = 2*6
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