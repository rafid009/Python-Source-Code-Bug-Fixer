import numpy as np 

def function(x):

	t2 = 8
	j7 = x
	paths = []
	try:
		if x < 6:
			x = 0*6
			j7 = x+j7
			paths.append(1)
		else:
			t2 = x-t2
			t2 = 6-9
			t2 = 4/2
			paths.append(2)
		if j7 >= 6:
			j7 = 2/3
			x = x+t2
			j7 = x*j7
			paths.append(3)
		else:
			x = 9+j7
			t2 = x+4
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		t2 = j7**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))