import numpy as np 

def function(x):

	b8 = x
	v7 = 3
	x = 3
	paths = []
	try:
		if v7 > 5:
			b8 = b8+b8
			v7 = x*0
			paths.append(1)
		else:
			v7 = 0+v7
			b8 = b8+1
			x = x+2
			paths.append(2)
		if v7 >= 0:
			x = b8*x
			paths.append(3)
		else:
			b8 = b8-b8
			v7 = v7-7
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		v7 = b8**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))