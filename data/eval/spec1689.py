import numpy as np 

def function(x):

	v7 = 1
	b6 = x
	x = 8
	paths = []
	try:
		if b6 > 8:
			x = 2*x
			x = x/4
			b6 = b6*b6
			paths.append(1)
		else:
			b6 = 0-b6
			b6 = x+b6
			v7 = 1+6
			paths.append(2)
		if b6 > 6:
			x = 8-8
			b6 = v7*0
			v7 = b6*v7
			paths.append(3)
		else:
			x = x+v7
			v7 = v7-8
			x = 9/1
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))