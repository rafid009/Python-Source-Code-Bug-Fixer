import numpy as np 

def function(x):

	a5 = x
	t5 = 9
	paths = []
	try:
		if x > 3:
			x = 8*9
			a5 = 0/4
			paths.append(1)
		else:
			x = x/t5
			a5 = a5*1
			paths.append(2)
		if x < 8:
			x = x+6
			t5 = t5-4
			t5 = t5+t5
			paths.append(3)
		else:
			t5 = x-2
			a5 = 4-t5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))