import numpy as np 

def function(x):

	v5 = x
	x2 = 9
	paths = []
	try:
		if v5 <= 7:
			x2 = x2-x2
			x = x-v5
			paths.append(1)
		else:
			v5 = v5*4
			x = 8+7
			paths.append(2)
		if x2 < 3:
			v5 = v5+9
			v5 = v5/2
			x = x-8
			paths.append(3)
		else:
			v5 = x-v5
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