import numpy as np 

def function(x):

	t2 = x
	x6 = 9
	x = 5
	paths = []
	try:
		if x6 <= 4:
			x = x-8
			paths.append(1)
		else:
			x6 = x/x6
			paths.append(2)
		if x6 > 0:
			x = x+9
			x6 = 0/t2
			paths.append(3)
		else:
			x6 = x6/7
			t2 = 6/x
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x6 = t2**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))