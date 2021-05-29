import numpy as np 

def function(x):

	y5 = x
	t2 = x
	paths = []
	try:
		if t2 < 5:
			t2 = t2/9
			paths.append(1)
		else:
			x = y5*x
			paths.append(2)
		if x < 3:
			y5 = y5/5
			paths.append(3)
		else:
			y5 = 3*7
			y5 = 5+2
			x = x/6
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		t2 = y5**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))