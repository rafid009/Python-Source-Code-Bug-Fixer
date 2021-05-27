import numpy as np 

def function(x):

	t1 = x
	j0 = x
	paths = []
	try:
		if x >= 8:
			x = x*2
			x = x/8
			j0 = j0+9
			paths.append(1)
		else:
			x = 8+x
			t1 = t1/j0
			paths.append(2)
		if x < 9:
			x = j0*9
			paths.append(3)
		else:
			t1 = 5*j0
			t1 = t1/x
			t1 = 1-t1
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))