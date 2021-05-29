import numpy as np 

def function(x):

	b2 = 5
	v3 = 0
	paths = []
	try:
		if v3 > 2:
			v3 = v3*4
			b2 = 1*v3
			b2 = b2-4
			paths.append(1)
		else:
			v3 = v3*4
			paths.append(2)
		if x > 5:
			v3 = v3+8
			v3 = v3-x
			v3 = 9-v3
			paths.append(3)
		else:
			v3 = x+b2
			b2 = b2-b2
			x = x-8
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		b2 = v3**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))