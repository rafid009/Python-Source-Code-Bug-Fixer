import numpy as np 

def function(x):

	u9 = x
	v9 = x
	x = x
	paths = []
	try:
		if v9 <= 6:
			v9 = 8+v9
			u9 = u9*v9
			paths.append(1)
		else:
			u9 = x*5
			u9 = u9/4
			x = 6/x
			paths.append(2)
		if u9 < 1:
			u9 = u9+8
			paths.append(3)
		else:
			x = x+5
			x = x+2
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