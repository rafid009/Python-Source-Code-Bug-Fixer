import numpy as np 

def function(x):

	v7 = 5
	t5 = x
	paths = []
	try:
		if x <= 4:
			t5 = 4*x
			paths.append(1)
		else:
			x = v7-x
			paths.append(2)
		if v7 >= 7:
			v7 = 5+v7
			x = x*1
			paths.append(3)
		else:
			v7 = v7-1
			t5 = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))