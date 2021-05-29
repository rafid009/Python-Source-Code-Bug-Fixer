import numpy as np 

def function(x):

	x3 = x
	t8 = x
	paths = []
	try:
		if x > 6:
			t8 = t8+6
			x = x3+x3
			x = x/5
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if x3 <= 7:
			x = 7-t8
			x3 = x3-x3
			paths.append(3)
		else:
			x3 = 6+9
			t8 = 9+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))