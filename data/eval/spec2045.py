import numpy as np 

def function(x):

	t3 = 7
	e3 = x
	paths = []
	try:
		if t3 > 5:
			t3 = t3-x
			t3 = t3+7
			e3 = 1*e3
			paths.append(1)
		else:
			e3 = 0*e3
			paths.append(2)
		if x <= 3:
			t3 = t3/t3
			paths.append(3)
		else:
			t3 = 9/t3
			x = x*e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))