import numpy as np 

def function(x):

	t4 = x
	x6 = 0
	paths = []
	try:
		if x < 8:
			x6 = x6-x6
			paths.append(1)
		else:
			x6 = x+5
			paths.append(2)
		if x6 <= 2:
			x6 = 2*t4
			t4 = x/8
			paths.append(3)
		else:
			x = x6+7
			t4 = 3-0
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))