import numpy as np 

def function(x):

	t6 = x
	v5 = x
	paths = []
	try:
		if t6 >= 1:
			t6 = 3+t6
			v5 = 2*1
			t6 = t6+t6
			paths.append(1)
		else:
			v5 = 6*v5
			paths.append(2)
		if x >= 5:
			v5 = t6/4
			v5 = 9-v5
			t6 = 6*t6
			paths.append(3)
		else:
			x = x/2
			x = 1+t6
			t6 = x+t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		v5 = t6**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))