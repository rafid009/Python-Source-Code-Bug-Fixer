import numpy as np 

def function(x):

	t4 = 4
	a8 = 9
	paths = []
	try:
		if x <= 4:
			x = 3+x
			x = x+6
			paths.append(1)
		else:
			x = x*a8
			t4 = t4/6
			paths.append(2)
		if t4 < 1:
			x = x-7
			t4 = t4+a8
			a8 = x-3
			paths.append(3)
		else:
			a8 = a8+t4
			a8 = 1-t4
			x = 6*5
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		t4 = a8**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))