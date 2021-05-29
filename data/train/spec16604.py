import numpy as np 

def function(x):

	j5 = 4
	t4 = x
	x = 6
	paths = []
	try:
		if x > 0:
			t4 = 0/t4
			t4 = j5*j5
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if j5 < 6:
			x = 8*x
			t4 = 3+7
			x = j5-x
			paths.append(3)
		else:
			t4 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))