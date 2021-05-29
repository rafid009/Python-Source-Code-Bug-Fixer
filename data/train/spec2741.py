import numpy as np 

def function(x):

	t5 = x
	v3 = x
	paths = []
	try:
		if v3 > 3:
			t5 = 8-t5
			v3 = v3*t5
			paths.append(1)
		else:
			x = x-x
			v3 = v3+v3
			x = v3-x
			paths.append(2)
		if x >= 6:
			t5 = 6*t5
			x = x+x
			paths.append(3)
		else:
			v3 = t5+v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))