import numpy as np 

def function(x):

	a2 = 3
	t8 = 6
	paths = []
	try:
		if x < 4:
			t8 = t8*5
			x = x+a2
			paths.append(1)
		else:
			t8 = x-t8
			x = 8/x
			x = 7*2
			paths.append(2)
		if x > 4:
			x = x+0
			paths.append(3)
		else:
			t8 = 7/2
			x = x*a2
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		a2 = t8**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))