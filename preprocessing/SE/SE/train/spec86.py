import numpy as np 

def function(x):

	a9 = x
	t5 = x
	paths = []
	try:
		if t5 < 8:
			t5 = t5/7
			x = x-5
			x = x/2
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if t5 >= 2:
			x = x-7
			x = 1+x
			paths.append(3)
		else:
			x = 6+x
			a9 = a9+t5
			x = t5-8
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		a9 = t5**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))