import numpy as np 

def function(x):

	a4 = 9
	t4 = x
	paths = []
	try:
		if a4 < 8:
			t4 = t4/a4
			t4 = t4+x
			paths.append(1)
		else:
			t4 = 6+t4
			t4 = t4-9
			t4 = a4+t4
			paths.append(2)
		if t4 > 7:
			x = 8+0
			t4 = t4*t4
			x = x*4
			paths.append(3)
		else:
			t4 = t4-1
			a4 = x*a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))