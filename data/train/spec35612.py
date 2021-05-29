import numpy as np 

def function(x):

	b6 = 0
	v1 = 1
	paths = []
	try:
		if b6 <= 2:
			v1 = 9-7
			v1 = v1-b6
			b6 = b6+1
			paths.append(1)
		else:
			x = b6*0
			x = 1-x
			paths.append(2)
		if v1 >= 2:
			v1 = v1+x
			b6 = b6/x
			b6 = v1*v1
			paths.append(3)
		else:
			x = x*0
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))