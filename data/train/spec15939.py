import numpy as np 

def function(x):

	t8 = 6
	v7 = x
	paths = []
	try:
		if t8 <= 1:
			v7 = v7*2
			t8 = t8-6
			paths.append(1)
		else:
			t8 = t8-5
			paths.append(2)
		if v7 > 2:
			v7 = 5-1
			x = t8+x
			x = v7/x
			paths.append(3)
		else:
			t8 = t8+t8
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))