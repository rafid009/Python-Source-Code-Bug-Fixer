import numpy as np 

def function(x):

	t2 = x
	a9 = 8
	paths = []
	try:
		if t2 < 9:
			t2 = t2/2
			a9 = 5*0
			a9 = a9*4
			paths.append(1)
		else:
			x = x*6
			a9 = 2+5
			paths.append(2)
		if a9 >= 0:
			a9 = a9+x
			paths.append(3)
		else:
			x = 7-x
			a9 = t2/a9
			a9 = 7-2
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		t2 = a9**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))