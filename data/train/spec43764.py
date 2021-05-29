import numpy as np 

def function(x):

	v9 = x
	b4 = x
	paths = []
	try:
		if v9 >= 9:
			v9 = v9/x
			v9 = x/v9
			x = x/8
			paths.append(1)
		else:
			x = 9/v9
			paths.append(2)
		if b4 < 6:
			x = 5-5
			b4 = x*b4
			x = x+8
			paths.append(3)
		else:
			b4 = b4+9
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		b4 = v9**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))