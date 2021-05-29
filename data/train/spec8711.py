import numpy as np 

def function(x):

	a8 = x
	t4 = 9
	paths = []
	try:
		if t4 > 7:
			t4 = a8-t4
			t4 = 7*8
			t4 = 8+9
			paths.append(1)
		else:
			x = t4*3
			paths.append(2)
		if x <= 9:
			a8 = a8+a8
			paths.append(3)
		else:
			a8 = a8+x
			a8 = a8*4
			x = x*4
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))