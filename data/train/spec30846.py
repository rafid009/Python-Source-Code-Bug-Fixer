import numpy as np 

def function(x):

	t5 = 8
	e8 = x
	paths = []
	try:
		if x <= 4:
			t5 = 1/1
			paths.append(1)
		else:
			x = x*3
			e8 = 2/e8
			t5 = 6/t5
			paths.append(2)
		if x >= 7:
			e8 = 3-e8
			paths.append(3)
		else:
			e8 = e8/6
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))