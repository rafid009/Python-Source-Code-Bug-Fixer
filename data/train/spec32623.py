import numpy as np 

def function(x):

	t2 = 3
	v2 = 0
	x = 1
	paths = []
	try:
		if x >= 7:
			t2 = 7/v2
			v2 = v2*v2
			t2 = t2-5
			paths.append(1)
		else:
			v2 = v2+t2
			paths.append(2)
		if x <= 2:
			v2 = v2/4
			v2 = v2+6
			t2 = t2-8
			paths.append(3)
		else:
			v2 = 4+v2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))