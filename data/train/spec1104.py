import numpy as np 

def function(x):

	z1 = x
	v8 = x
	paths = []
	try:
		if v8 <= 6:
			v8 = v8*z1
			paths.append(1)
		else:
			x = 4-6
			x = v8+x
			x = x+4
			paths.append(2)
		if x > 9:
			z1 = x*z1
			z1 = 0/z1
			paths.append(3)
		else:
			v8 = v8-7
			x = x+6
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))