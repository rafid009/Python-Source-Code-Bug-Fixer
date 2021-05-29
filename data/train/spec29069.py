import numpy as np 

def function(x):

	b9 = x
	v5 = x
	paths = []
	try:
		if v5 >= 7:
			b9 = v5+v5
			paths.append(1)
		else:
			x = v5-x
			paths.append(2)
		if v5 < 7:
			x = 6/7
			paths.append(3)
		else:
			v5 = 5-v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))