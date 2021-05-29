import numpy as np 

def function(x):

	v9 = x
	b1 = x
	paths = []
	try:
		if v9 < 3:
			b1 = 1*b1
			b1 = v9+0
			v9 = 0*v9
			paths.append(1)
		else:
			b1 = b1+x
			paths.append(2)
		if x < 5:
			v9 = b1-5
			x = x-1
			paths.append(3)
		else:
			b1 = 8+b1
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