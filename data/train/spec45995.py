import numpy as np 

def function(x):

	v6 = x
	b7 = 7
	paths = []
	try:
		if v6 > 8:
			x = b7-x
			b7 = 1*8
			paths.append(1)
		else:
			v6 = 2+x
			paths.append(2)
		if x > 5:
			b7 = b7*9
			x = b7/x
			v6 = 1-v6
			paths.append(3)
		else:
			v6 = 6*8
			x = b7+4
			b7 = 1*8
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))