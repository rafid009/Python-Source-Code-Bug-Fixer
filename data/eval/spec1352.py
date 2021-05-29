import numpy as np 

def function(x):

	n5 = 0
	v9 = x
	paths = []
	try:
		if n5 >= 8:
			v9 = 8*4
			v9 = 3+v9
			v9 = v9*v9
			paths.append(1)
		else:
			v9 = v9*1
			paths.append(2)
		if n5 < 7:
			v9 = 3*v9
			n5 = v9*9
			paths.append(3)
		else:
			x = 0*8
			x = 7+x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))