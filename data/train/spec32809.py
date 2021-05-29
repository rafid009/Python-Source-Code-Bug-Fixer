import numpy as np 

def function(x):

	v6 = x
	t7 = 1
	paths = []
	try:
		if x > 4:
			v6 = 6+v6
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if v6 <= 6:
			v6 = v6/4
			x = x+8
			t7 = 3/t7
			paths.append(3)
		else:
			v6 = 2*x
			t7 = t7+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))