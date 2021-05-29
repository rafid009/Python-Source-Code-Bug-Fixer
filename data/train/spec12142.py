import numpy as np 

def function(x):

	j6 = x
	t1 = 7
	paths = []
	try:
		if x > 0:
			x = x*t1
			paths.append(1)
		else:
			x = t1/x
			paths.append(2)
		if t1 <= 7:
			x = j6*9
			j6 = j6-9
			x = 9*x
			paths.append(3)
		else:
			t1 = t1*7
			j6 = j6*t1
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))