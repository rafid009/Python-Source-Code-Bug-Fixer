import numpy as np 

def function(x):

	v9 = x
	t7 = 7
	paths = []
	try:
		if t7 >= 6:
			x = x*x
			paths.append(1)
		else:
			x = t7/7
			paths.append(2)
		if v9 >= 2:
			t7 = x*v9
			x = x+6
			v9 = 1/v9
			paths.append(3)
		else:
			t7 = 3+v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		t7 = v9**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))