import numpy as np 

def function(x):

	n7 = 9
	t6 = x
	paths = []
	try:
		if n7 > 3:
			x = x*x
			n7 = n7*0
			paths.append(1)
		else:
			n7 = t6+n7
			x = n7/x
			t6 = 6*t6
			paths.append(2)
		if x <= 4:
			x = 5-6
			n7 = x/1
			paths.append(3)
		else:
			x = x-4
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))