import numpy as np 

def function(x):

	t8 = x
	v4 = 4
	x = x
	paths = []
	try:
		if x > 8:
			t8 = t8*t8
			v4 = v4/7
			v4 = t8+x
			paths.append(1)
		else:
			x = t8/v4
			x = t8-v4
			x = 2*x
			paths.append(2)
		if x > 5:
			v4 = x+4
			t8 = t8*6
			v4 = 6+t8
			paths.append(3)
		else:
			v4 = x/v4
			t8 = v4-4
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		v4 = t8**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))