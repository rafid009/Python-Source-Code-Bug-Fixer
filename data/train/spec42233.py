import numpy as np 

def function(x):

	b2 = x
	v8 = 3
	paths = []
	try:
		if b2 < 0:
			x = 7+x
			v8 = 8-5
			v8 = v8+4
			paths.append(1)
		else:
			v8 = v8-4
			paths.append(2)
		if b2 < 4:
			b2 = b2*4
			paths.append(3)
		else:
			x = x/2
			v8 = 8*v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))