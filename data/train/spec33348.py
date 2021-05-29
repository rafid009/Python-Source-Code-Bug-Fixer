import numpy as np 

def function(x):

	v8 = x
	b3 = 8
	paths = []
	try:
		if b3 <= 3:
			x = x/9
			paths.append(1)
		else:
			x = x/7
			x = x*7
			paths.append(2)
		if b3 <= 6:
			v8 = 2*v8
			b3 = b3*4
			x = x-7
			paths.append(3)
		else:
			x = 1-6
			b3 = b3+4
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